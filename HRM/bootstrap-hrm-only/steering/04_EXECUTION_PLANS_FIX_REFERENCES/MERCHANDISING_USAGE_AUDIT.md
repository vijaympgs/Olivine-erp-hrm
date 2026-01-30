# MERCHANDISING ENTITIES - USAGE AUDIT REPORT

**Date**: 2025-12-25 19:40 IST  
**Scope**: retail-erp-platform ONLY  
**Method**: Code search analysis (backend + frontend)  
**Status**: ANALYSIS COMPLETE

---

## ENTITY 1: CATEGORY / HIERARCHY

**Used**: YES  
**Usage Level**: CORE DEPENDENCY

### Backend Usage:
- **Model**: `backend/domain/company/models.py` (Line 777)
  - Table: `be_category`
  - Fields: id, name, created_at, updated_at
- **Foreign Key**: `ItemMaster.category` (Line 842)
  - Relationship: ItemMaster → Category (SET_NULL)
- **API Endpoint**: `/api/v1/company/categories/`
  - ViewSet: `CategoryViewSet` (views.py Line 593)
  - Serializers: `CategorySerializer`, `CategoryListSerializer`
- **Migrations**: `0001_initial.py` (Line 32)
- **Seed Data**: `seed_masters.py` (Line 91-104)
- **Admin**: Registered in Django Admin

### Frontend Usage:
- **Lookup Modal**: `CategoryLookupModal.tsx` (CREATED THIS SESSION)
- **Item Service**: `itemService.ts` (Line 54) - `category_id` field
- **Product Module**: `ProductPage.tsx`, `ProductForm.tsx`
  - Display in tables
  - Search/filter by category
  - Form input field

### Nature of Usage:
CORE ITEM MASTER DEPENDENCY - Categories organize products hierarchically

**Safe to Remove**: NO

---

## ENTITY 2: BRAND

**Used**: YES  
**Usage Level**: CORE DEPENDENCY

### Backend Usage:
- **Model**: `backend/domain/company/models.py` (Line 794)
  - Table: `be_brand`
  - Fields: id, name
- **Foreign Key**: `ItemMaster.brand` (Line 843)
  - Relationship: ItemMaster → Brand (SET_NULL)
- **API Endpoint**: `/api/v1/company/brands/`
  - ViewSet: `BrandViewSet` (views.py Line 610)
  - Serializers: `BrandSerializer`, `BrandListSerializer`
- **Migrations**: `0001_initial.py` (Line 19)
- **Seed Data**: `seed_masters.py` (Line 111-113)
- **Admin**: Registered in Django Admin (Line 24)

### Frontend Usage:
- **Lookup Modal**: `BrandLookupModal.tsx` (CREATED THIS SESSION)
- **Item Service**: `itemService.ts` (Line 54) - `brand_id` field
- **Admin Display**: ItemMaster admin shows brand column

### Nature of Usage:
CORE ITEM MASTER DEPENDENCY - Brands classify products by manufacturer

**Safe to Remove**: NO

---

## ENTITY 3: PRICING

**Used**: PARTIAL  
**Usage Level**: PLACEHOLDER ONLY

### Backend Usage:
- **No dedicated Pricing model found**
- **No API endpoint for pricing rules**
- **No serializers for pricing**

### Frontend Usage:
- **Menu Item**: `/master/pricing` (menuConfig.ts Line 101)
- **Route**: Placeholder page (router.tsx Line 164)
  - Shows "Pricing Management - Coming Soon"

### Nature of Usage:
PLACEHOLDER - No actual implementation exists

**Safe to Remove**: YES (menu item + placeholder route only)

---

## ENTITY 4: PRICE LIST

**Used**: YES  
**Usage Level**: CORE DEPENDENCY

### Backend Usage:
- **Model**: `backend/domain/company/models.py` (Line 570)
  - Table: `be_pricelist`
  - Related Model: `PriceListLine` (Line 620)
- **Foreign Key**: `ItemMaster.price_list` (Line 845)
  - Relationship: ItemMaster → PriceList (SET_NULL)
- **Foreign Key**: `Company.default_price_list` (business_entities)
  - Relationship: Company → PriceList (PROTECT)
- **API Endpoint**: `/api/v1/company/price-lists/`
  - ViewSet: `PriceListViewSet` (views.py Line 440)
  - Serializers: `PriceListSerializer`, `PriceListListSerializer`, `PriceListLineSerializer`
- **Migrations**: `0001_initial.py` (Line 284, 403)
- **Seed Data**: `seed_data.py` (Line 417-464)
- **Admin**: Commented out due to admin.E108 error (admin.py Line 158)

### Frontend Usage:
- **Page**: `PriceListSetup.tsx` (exists)
- **Route**: `/inventory/price-lists` (router.tsx Line 155)
- **Menu**: "Price Lists" (menuConfig.ts Line 102)

### Nature of Usage:
CORE PRICING DEPENDENCY - Price lists define item pricing by company/customer

**Safe to Remove**: NO

---

## ENTITY 5: VARIANTS (ATTRIBUTES)

**Used**: YES  
**Usage Level**: CORE DEPENDENCY

### Backend Usage:
- **Model**: `backend/domain/company/models.py`
  - `Attribute` model (extensive usage)
  - `AttributeValue` model
  - `ProductAttributeTemplate` model
  - `VariantAttribute` model
- **API Endpoints**:
  - `/api/v1/company/attributes/` (AttributeViewSet Line 244)
  - `/api/v1/company/attribute-values/` (AttributeValueViewSet)
  - `/api/v1/company/attribute-templates/` (ProductAttributeTemplateViewSet Line 183)
- **Serializers**: Multiple (AttributeSerializer, AttributeListSerializer, etc.)
- **Migrations**: Extensive (0001_initial.py)
- **Seed Data**: `seed_data.py` (Line 139-249)
- **Admin**: Registered (AttributeAdmin Line 134, AttributeValueAdmin Line 142)

### Frontend Usage:
- **Pages**: 
  - `AttributeSetup.tsx` (exists)
  - `AttributeValueSetup.tsx` (exists)
  - `ProductAttributeTemplateSetup.tsx` (exists)
- **Routes**: 
  - `/inventory/attributes` (router.tsx Line 150)
  - `/inventory/attribute-values` (Line 151)
  - `/inventory/attribute-templates` (Line 152)
- **Services**: `productAttributeTemplateService.ts`

### Nature of Usage:
CORE VARIANT SYSTEM - Attributes define product variations (Color, Size, etc.)

**Safe to Remove**: NO

---

## ENTITY 6: ATTRIBUTE VALUES

**Used**: YES  
**Usage Level**: CORE DEPENDENCY

### Backend Usage:
- **Model**: `backend/domain/company/models.py`
  - `AttributeValue` model
- **API Endpoint**: `/api/v1/company/attribute-values/`
  - ViewSet: `AttributeValueViewSet`
  - Serializers: `AttributeValueSerializer`, `AttributeValueListSerializer`
- **Foreign Key**: Multiple relationships to Attribute
- **Migrations**: `0001_initial.py`
- **Seed Data**: `seed_data.py`
- **Admin**: Registered (AttributeValueAdmin Line 142)

### Frontend Usage:
- **Page**: `AttributeValueSetup.tsx` (exists)
- **Route**: `/inventory/attribute-values` (router.tsx Line 151)
- **Menu**: "Attribute Values" (menuConfig.ts Line 99)

### Nature of Usage:
CORE VARIANT SYSTEM - Attribute values are the actual values for attributes (Red, Blue, Large, Small)

**Safe to Remove**: NO

---

## ENTITY 7: ATTRIBUTE TEMPLATES

**Used**: YES  
**Usage Level**: CORE DEPENDENCY

### Backend Usage:
- **Model**: `backend/domain/company/models.py`
  - `ProductAttributeTemplate` model
  - `ProductAttributeTemplateLine` model
- **Foreign Key**: `ItemMaster.attribute_template` (Line 844)
  - Relationship: ItemMaster → ProductAttributeTemplate (SET_NULL)
- **API Endpoint**: `/api/v1/company/attribute-templates/`
  - ViewSet: `ProductAttributeTemplateViewSet` (views.py Line 183)
  - Serializers: `ProductAttributeTemplateSerializer`, `ProductAttributeTemplateListSerializer`
- **Migrations**: `0001_initial.py`
- **Seed Data**: `seed_data.py` (Line 228-263)
- **Admin**: Registered

### Frontend Usage:
- **Page**: `ProductAttributeTemplateSetup.tsx` (exists)
- **Route**: `/inventory/attribute-templates` (router.tsx Line 152)
- **Menu**: "Attribute Templates" (menuConfig.ts Line 100)
- **Service**: `productAttributeTemplateService.ts`

### Nature of Usage:
CORE VARIANT SYSTEM - Templates group attributes for product types (e.g., "Apparel Template" with Color, Size, Material)

**Safe to Remove**: NO

---

## ENTITY 8: UOM (UNIT OF MEASURE)

**Used**: YES  
**Usage Level**: CORE DEPENDENCY

### Backend Usage:
- **Model**: `backend/domain/company/models.py`
  - `UnitOfMeasure` model
  - `UOMConversion` model
  - `VariantUOM` model
- **Foreign Keys**: EXTENSIVE
  - `ItemMaster.stock_uom` (Line 844)
  - `ItemVariant.sales_uom`, `stock_uom`, `purchase_uom` (Line 524)
  - Multiple other references
- **API Endpoints**:
  - `/api/v1/company/uoms/` (UnitOfMeasureViewSet)
  - `/api/v1/company/uom-conversions/` (UOMConversionViewSet Line 367)
- **Serializers**: `UnitOfMeasureSerializer`, `UOMConversionSerializer`, etc.
- **Migrations**: Extensive (0001_initial.py)
- **Seed Data**: `seed_data.py`
- **Admin**: Registered

### Frontend Usage:
- **Lookup Modal**: `UOMLookupModal.tsx` (CREATED THIS SESSION)
- **Page**: `UOMSetup.tsx` (exists)
- **Route**: `/inventory/uoms` (router.tsx Line 153)
- **Menu**: "UOM" (menuConfig.ts Line 103)
- **POS**: Used in billing (PosDesktop.tsx)

### Nature of Usage:
CRITICAL INVENTORY DEPENDENCY - UOMs define measurement units for all items (EA, KG, LTR, etc.)

**Safe to Remove**: NO

---

## SUMMARY TABLE

| Entity | Used | Level | Backend Model | API Endpoint | Frontend Page | Safe to Remove |
|--------|------|-------|---------------|--------------|---------------|----------------|
| **Category** | YES | CORE | ✅ | ✅ | ✅ | **NO** |
| **Brand** | YES | CORE | ✅ | ✅ | ✅ | **NO** |
| **Pricing** | PARTIAL | PLACEHOLDER | ❌ | ❌ | Placeholder | **YES** |
| **Price List** | YES | CORE | ✅ | ✅ | ✅ | **NO** |
| **Variants (Attributes)** | YES | CORE | ✅ | ✅ | ✅ | **NO** |
| **Attribute Values** | YES | CORE | ✅ | ✅ | ✅ | **NO** |
| **Attribute Templates** | YES | CORE | ✅ | ✅ | ✅ | **NO** |
| **UOM** | YES | CRITICAL | ✅ | ✅ | ✅ | **NO** |

---

## CROSS-MODULE DEPENDENCIES

### POS Module:
- **UOM**: Used in billing (PosDesktop.tsx Line 172-175)
- **Category**: Used in product display
- **Price List**: Implicit (pricing logic)

### Procurement Module:
- **UOM**: Purchase UOM for items
- **Price List**: Vendor pricing

### Inventory Module:
- **UOM**: Stock UOM, conversions
- **Attributes**: Variant tracking
- **Category**: Stock organization

### Sales Module:
- **Price List**: Customer pricing
- **UOM**: Sales UOM
- **Category**: Product filtering

---

## RECOMMENDATIONS

### SAFE TO REMOVE:
1. **Pricing** (menu item + placeholder route)
   - No backend implementation
   - No actual usage
   - Only placeholder page exists

### MUST NOT REMOVE:
1. **Category** - Core item organization
2. **Brand** - Core item classification
3. **Price List** - Core pricing system
4. **Variants/Attributes** - Core variant system
5. **Attribute Values** - Core variant system
6. **Attribute Templates** - Core variant system
7. **UOM** - Critical inventory dependency

---

## NOTES

1. **Category & Brand**: Both have foreign keys in ItemMaster (SET_NULL), meaning items can exist without them, but they are widely used
2. **Price List**: Has PROTECT relationship from Company.default_price_list, meaning companies MUST have a default price list
3. **UOM**: Has multiple PROTECT/CASCADE relationships, making it critical infrastructure
4. **Attributes**: Entire variant system depends on this - removing would break product variants
5. **Pricing**: Only placeholder exists - can be safely removed from menu until implemented

---

**Analysis Complete**  
**Report Generated**: 2025-12-25 19:40 IST  
**Analyst**: Antigravity Agent  
**Authority**: Viji (Product Owner)
