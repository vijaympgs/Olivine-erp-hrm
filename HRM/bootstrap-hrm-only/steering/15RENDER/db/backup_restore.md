# PostgreSQL Backup & Restore Strategy

## Backup (Daily)
Use pg_dump via cron or Render job:

pg_dump $DATABASE_URL > backup_$(date +%F).sql

## Restore
psql $DATABASE_URL < backup_YYYY-MM-DD.sql

Store backups in:
- AWS S3
- GCP Cloud Storage
