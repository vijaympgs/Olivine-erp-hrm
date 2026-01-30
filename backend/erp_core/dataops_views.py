import json
from django.apps import apps
from django.db import connection
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from django.conf import settings


@method_decorator(csrf_exempt, name='dispatch')
class DataOpsSchemaView(View):
    """
    Introspects the Django ORM to return a list of all models (tables)
    exposed in the system, mirroring the Django Admin structure.
    """
    def get(self, request):
        try:
            tables = []
            models = apps.get_models()
            
            for model in models:
                app_config = apps.get_app_config(model._meta.app_label)
                module_name = app_config.verbose_name.upper() if app_config.verbose_name else model._meta.app_label.upper()
                table_name = model._meta.db_table
                
                # Count rows safely
                try:
                    row_count = model.objects.count()
                except:
                    row_count = 0
                
                # Count columns
                column_count = len(model._meta.fields)
                    
                tables.append({
                    "name": table_name,
                    "rowCount": row_count,
                    "columnCount": column_count,
                    "module": module_name
                })
                
            return JsonResponse({"success": True, "tables": tables})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)


@method_decorator(csrf_exempt, name='dispatch')
class DataOpsContentView(View):
    """
    Returns schema columns and first N rows for a given table.
    Enhanced with nullable, default, and FK information.
    """
    def post(self, request):
        try:
            body = json.loads(request.body)
            table_name = body.get('table')
            limit = body.get('limit', 50)
            offset = body.get('offset', 0)
            
            # Find model by table name
            target_model = None
            for model in apps.get_models():
                if model._meta.db_table == table_name:
                    target_model = model
                    break
            
            if not target_model:
                return JsonResponse({
                    "success": False, 
                    "error": f"Table {table_name} not found in ORM"
                }, status=404)
            
            # Total count for pagination
            total_count = target_model.objects.count()
            
            # Fetch rows with pagination
            qs = target_model.objects.all()[offset:offset + limit].values()
            data = list(qs)
            
            # Get enhanced columns info
            columns = []
            for field in target_model._meta.fields:
                # Determine default value
                default_val = '-'
                if field.has_default():
                    default = field.get_default()
                    if callable(default):
                        default_val = '<callable>'
                    elif default is not None:
                        default_val = str(default)
                
                columns.append({
                    "name": field.name,
                    "type": field.get_internal_type(),
                    "primaryKey": field.primary_key,
                    "nullable": field.null,
                    "default": default_val
                })

            return JsonResponse({
                "success": True, 
                "columns": columns,
                "columnCount": len(columns),
                "rows": data,
                "totalCount": total_count,
                "limit": limit,
                "offset": offset
            }, encoder=DjangoJSONEncoder)

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)


@method_decorator(csrf_exempt, name='dispatch')
class DataOpsRelationshipsView(View):
    """
    Returns all foreign key relationships for a given table.
    Introspects Django ORM ForeignKey fields.
    """
    def post(self, request):
        try:
            body = json.loads(request.body)
            table_name = body.get('table')
            
            # Find model by table name
            target_model = None
            for model in apps.get_models():
                if model._meta.db_table == table_name:
                    target_model = model
                    break
            
            if not target_model:
                return JsonResponse({
                    "success": False, 
                    "error": f"Table {table_name} not found"
                }, status=404)
            
            relationships = []
            
            # Outgoing FKs (this table references other tables)
            for field in target_model._meta.fields:
                if field.is_relation and hasattr(field, 'related_model') and field.related_model:
                    relationships.append({
                        "direction": "outgoing",
                        "fromTable": table_name,
                        "fromCol": field.column,  # actual DB column name
                        "toTable": field.related_model._meta.db_table,
                        "toCol": field.related_model._meta.pk.column,
                        "fieldName": field.name,
                        "relationType": field.get_internal_type()
                    })
            
            # Incoming FKs (other tables reference this table)
            for rel in target_model._meta.related_objects:
                related_model = rel.related_model
                field = rel.field
                relationships.append({
                    "direction": "incoming",
                    "fromTable": related_model._meta.db_table,
                    "fromCol": field.column,
                    "toTable": table_name,
                    "toCol": target_model._meta.pk.column,
                    "fieldName": field.name,
                    "relationType": "ForeignKey"
                })
            
            return JsonResponse({
                "success": True,
                "table": table_name,
                "relationships": relationships,
                "outgoingCount": len([r for r in relationships if r['direction'] == 'outgoing']),
                "incomingCount": len([r for r in relationships if r['direction'] == 'incoming'])
            })
            
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)


@method_decorator(csrf_exempt, name='dispatch')
class DataOpsQueryView(View):
    """
    Execute raw SELECT queries against the database.
    Only SELECT statements are allowed for safety.
    """
    def post(self, request):
        try:
            body = json.loads(request.body)
            query = body.get('query', '').strip()
            
            # Security: Only allow SELECT
            if not query.lower().startswith('select'):
                return JsonResponse({
                    "success": False, 
                    "error": "Only SELECT queries are allowed for safety"
                }, status=400)
            
            with connection.cursor() as cursor:
                cursor.execute(query)
                columns = [col[0] for col in cursor.description]
                rows = cursor.fetchall()
            
            # Format as list of dicts
            results = [dict(zip(columns, row)) for row in rows]
                
            return JsonResponse({
                "success": True,
                "columns": columns,
                "rows": results,
                "rowCount": len(results)
            })
            
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)


@method_decorator(csrf_exempt, name='dispatch')
class DataOpsDatabaseInfoView(View):
    """
    Returns database connection and metadata information.
    """
    def get(self, request):
        try:
            db_settings = settings.DATABASES.get('default', {})
            engine = db_settings.get('ENGINE', 'unknown')
            
            # Determine database type
            if 'sqlite' in engine:
                db_type = 'SQLite'
                db_name = db_settings.get('NAME', 'unknown')
                
                # Get SQLite version
                with connection.cursor() as cursor:
                    cursor.execute("SELECT sqlite_version();")
                    version = cursor.fetchone()[0]
            elif 'postgresql' in engine:
                db_type = 'PostgreSQL'
                db_name = db_settings.get('NAME', 'unknown')
                with connection.cursor() as cursor:
                    cursor.execute("SELECT version();")
                    version = cursor.fetchone()[0].split()[1] if cursor.fetchone() else 'unknown'
            else:
                db_type = engine.split('.')[-1]
                db_name = db_settings.get('NAME', 'unknown')
                version = 'unknown'
            
            # Count tables
            table_count = len(apps.get_models())
            
            return JsonResponse({
                "success": True,
                "database": {
                    "type": db_type,
                    "name": db_name,
                    "version": version,
                    "tableCount": table_count,
                    "host": db_settings.get('HOST', 'localhost') or 'localhost',
                    "port": db_settings.get('PORT', '') or 'default'
                }
            })
            
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)
