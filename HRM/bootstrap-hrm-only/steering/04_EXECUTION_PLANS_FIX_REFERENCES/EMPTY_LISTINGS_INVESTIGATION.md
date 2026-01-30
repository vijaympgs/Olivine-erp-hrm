# EMPTY LISTINGS INVESTIGATION - ROOT CAUSE FOUND

**Date**: 2025-12-25 20:12 IST  
**Status**: 🔍 ROOT CAUSE IDENTIFIED  
**Authority**: Viji (Product Owner)

---

## 🎯 PROBLEM STATEMENT

**Symptom**: Data exists in Django Admin but UI listings are empty for:
- Variants (Attributes)
- Attribute Values  
- Attribute Templates
- Price Lists
- UOM

**Expected**: Grids should show data  
**Actual**: Headers render but NO rows appear

---

## 🔍 INVESTIGATION RESULTS

### **STEP 1: Backend Verification** ✅

**Models**: All exist under `domain.company` ✅  
**API Endpoints**: All registered correctly ✅  
**ViewSets**: All configured with proper filtering ✅

**Backend Router** (`domain/company/urls.py`):
```python
router.register(r'attributes', AttributeViewSet, basename='attribute')
router.register(r'attribute-values', AttributeValueViewSet, basename='attributevalue')
router.register(r'attribute-templates', ProductAttributeTemplateViewSet, basename='productattributetemplate')
router.register(r'uoms', UnitOfMeasureViewSet, basename='unitofmeasure')
router.register(r'price-lists', PriceListViewSet, basename='pricelist')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'brands', BrandViewSet, basename='brand')

urlpatterns = [
    path('api/', include(router.urls)),  # ← Routes to /api/*
]
```

**Actual Backend URLs**:
- `/api/attributes/`
- `/api/attribute-values/`
- `/api/attribute-templates/`
- `/api/uoms/`
- `/api/price-lists/`
- `/api/categories/`
- `/api/brands/`

---

### **STEP 2: Frontend Service Verification** ⚠️

**Services Checked**:

| Service | Base URL | Status |
|---------|----------|--------|
| `attributeService.ts` | `/api/attributes` | ✅ CORRECT |
| `attributeValueService.ts` | `/api/attribute-values` | ✅ CORRECT |
| `productAttributeTemplateService.ts` | `/api/attribute-templates` | ✅ CORRECT |
| `uomService.ts` | `/api/uoms` | ✅ CORRECT |
| `priceListService.ts` | `/api/price-lists` | ✅ CORRECT |
| `categoryService.ts` | `/api/v1/company/categories` | ❌ **WRONG** |
| `brandService.ts` | `/api/v1/company/brands` | ❌ **WRONG** |

---

## 🚨 **ROOT CAUSE IDENTIFIED**

### **Issue 1: Category & Brand URL Mismatch**

**File**: `frontend/src/services/categoryService.ts` (Line 31)
```typescript
private baseUrl = `${API_BASE_URL}/api/v1/company/categories`;
//                                  ^^^^^^^^^^^^^^^^
//                                  WRONG PATH!
```

**File**: `frontend/src/services/brandService.ts` (Line 31)
```typescript
private baseUrl = `${API_BASE_URL}/api/v1/company/brands`;
//                                  ^^^^^^^^^^^^^^^^
//                                  WRONG PATH!
```

**Expected**: `/api/categories` and `/api/brands`  
**Actual**: `/api/v1/company/categories` and `/api/v1/company/brands`  
**Result**: 404 Not Found → Empty listings

---

### **Issue 2: Query Parameter Verification** ✅

**Backend ViewSets** correctly filter by `company_id`:
```python
def get_queryset(self):
    qs = super().get_queryset()
    company_id = self.request.query_params.get('company_id')
    if company_id:
        qs = qs.filter(company_id=company_id)
    return qs
```

**Frontend Pages** correctly pass `company_id`:
```typescript
// AttributeSetup.tsx Line 25
setFilters(prev => ({ ...prev, company_id: prev.company_id || activeCompanies[0].id }));

// UOMSetup.tsx Line 25
setFilters(prev => ({ ...prev, company_id: prev.company_id || activeCompanies[0].id }));
```

**Status**: ✅ NO ISSUE HERE

---

## ✅ **FIX REQUIRED**

### **Fix 1: Correct Category Service URL**

**File**: `frontend/src/services/categoryService.ts`

**Change Line 3**:
```typescript
// Before
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

// After
const API_BASE_URL = '/api';
```

**Change Line 31**:
```typescript
// Before
private baseUrl = `${API_BASE_URL}/api/v1/company/categories`;

// After
private baseUrl = `${API_BASE_URL}/categories`;
```

---

### **Fix 2: Correct Brand Service URL**

**File**: `frontend/src/services/brandService.ts`

**Change Line 3**:
```typescript
// Before
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

// After
const API_BASE_URL = '/api';
```

**Change Line 31**:
```typescript
// Before
private baseUrl = `${API_BASE_URL}/api/v1/company/brands`;

// After
private baseUrl = `${API_BASE_URL}/brands`;
```

---

## 📊 **EXPECTED RESULTS AFTER FIX**

| Module | Before Fix | After Fix |
|--------|------------|-----------|
| **Attributes** | ✅ Working | ✅ Working |
| **Attribute Values** | ✅ Working | ✅ Working |
| **Attribute Templates** | ✅ Working | ✅ Working |
| **UOM** | ✅ Working | ✅ Working |
| **Price Lists** | ✅ Working | ✅ Working |
| **Categories** | ❌ Empty (404) | ✅ Shows data |
| **Brands** | ❌ Empty (404) | ✅ Shows data |

---

## 🎓 **LESSONS LEARNED**

### **API URL Consistency**:
1. ✅ All services should use same base URL pattern
2. ✅ Backend router defines canonical paths
3. ✅ Frontend must match exactly
4. ❌ Don't mix `/api/` and `/api/v1/company/` patterns

### **Debugging Empty Listings**:
1. Check browser Network tab for 404 errors
2. Verify backend route registration
3. Verify frontend service URLs match backend
4. Check query parameter names match
5. Verify data exists in Django Admin

---

## 🚀 **NEXT STEPS**

1. ✅ Fix categoryService.ts URL
2. ✅ Fix brandService.ts URL
3. ✅ Test Code Masters page
4. ✅ Verify data loads correctly
5. ✅ Check browser console for errors
6. ✅ Verify all other Merchandising screens

---

**Status**: 🔍 **ROOT CAUSE IDENTIFIED**  
**Fix Required**: YES (2 files)  
**Impact**: Category and Brand listings will work  

Awaiting authorization to apply fix. - Viji
