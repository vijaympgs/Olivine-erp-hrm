# Product Lookup Pattern - Implementation Guide

**Created**: 2025-12-21  
**Purpose**: Standardized product lookup component for all backoffice modules  
**Inspired by**: POS Product Lookup

---

## 📋 **Overview**

The Product Lookup Pattern provides a consistent, reusable way to select products across all backoffice modules. It's inspired by the POS product lookup but adapted for backoffice use with additional features like recent items, grid/list views, and keyboard shortcuts.

---

## 🎯 **Key Features**

1. **Search Functionality**
   - Search by Item Code, Name, SKU, or Barcode
   - Real-time search with debouncing (300ms)
   - Filters for active items only

2. **View Modes**
   - List View (default) - Detailed information
   - Grid View - Visual browsing

3. **Recent Items**
   - Tracks last 10 selected products
   - Displays when search is empty
   - Stored in localStorage

4. **Keyboard Support**
   - Enter key on empty item code field → Opens lookup
   - Escape key → Closes lookup
   - Auto-focus on search input

5. **Visual Feedback**
   - Hover states
   - Loading indicators
   - Empty states

---

## 🔧 **Components**

### **1. ProductLookupModal**
Location: `frontend/src/ui/components/ProductLookupModal.tsx`

**Props:**
```typescript
interface ProductLookupModalProps {
  isOpen: boolean;                    // Control visibility
  onClose: () => void;                // Close handler
  onSelect: (product: ProductLookupResult) => void;  // Selection handler
  allowMultiple?: boolean;            // Allow multiple selections (default: false)
  title?: string;                     // Modal title (default: 'Product Lookup')
}
```

**Return Type:**
```typescript
interface ProductLookupResult {
  id: string;              // Item ID
  item_code: string;       // Item Code
  item_name: string;       // Item Name
  sku_code?: string;       // SKU (if variant)
  variant_name?: string;   // Variant name (if applicable)
  stock_uom: string;       // Stock UOM
  retail_price?: number;   // Price (if available)
  is_variant: boolean;     // Is this a variant?
  variant_id?: string;     // Variant ID (if applicable)
}
```

### **2. useProductLookup Hook**
Location: `frontend/src/hooks/useProductLookup.ts`

**Usage:**
```typescript
const {
  isLookupOpen,
  selectedProduct,
  openLookup,
  closeLookup,
  handleProductSelect,
  clearSelection
} = useProductLookup();
```

---

## 📝 **Implementation Steps**

### **Step 1: Import Components**
```typescript
import { ProductLookupModal, ProductLookupResult } from '../../ui/components/ProductLookupModal';
```

### **Step 2: Add State**
```typescript
const [isLookupOpen, setIsLookupOpen] = useState(false);
const [activeLineId, setActiveLineId] = useState<string | null>(null);
```

### **Step 3: Create Handlers**
```typescript
// Handle Enter key on Item Code field
const handleItemCodeKeyDown = (lineId: string, e: React.KeyboardEvent<HTMLInputElement>) => {
  if (e.key === 'Enter') {
    e.preventDefault();
    const line = lines.find(l => l.id === lineId);
    if (line && line.item_code.trim() === '') {
      setActiveLineId(lineId);
      setIsLookupOpen(true);
    }
  }
};

// Handle Product Selection
const handleProductSelect = (product: ProductLookupResult) => {
  if (activeLineId) {
    updateLine(activeLineId, 'item_code', product.item_code);
    updateLine(activeLineId, 'item_name', product.item_name);
    updateLine(activeLineId, 'uom', product.stock_uom);
  }
  setIsLookupOpen(false);
  setActiveLineId(null);
};
```

### **Step 4: Update Input Field**
```typescript
<input 
  type="text" 
  value={line.item_code} 
  onChange={e => updateLine(line.id, 'item_code', e.target.value)} 
  onKeyDown={(e) => handleItemCodeKeyDown(line.id, e)}
  placeholder="Enter code or press Enter"
  className="..." 
/>
```

### **Step 5: Add Modal**
```typescript
<ProductLookupModal
  isOpen={isLookupOpen}
  onClose={() => {
    setIsLookupOpen(false);
    setActiveLineId(null);
  }}
  onSelect={handleProductSelect}
  title="Select Product for [Module Name]"
/>
```

---

## 🎨 **Usage Examples**

### **Example 1: Purchase Requisition** ✅ Implemented
File: `frontend/src/pages/procurement/RequisitionFormPage.tsx`

Features:
- Enter key on empty item code opens lookup
- Auto-fills item name and UOM
- Tracks active line for selection

### **Example 2: Sales Order** (To Implement)
```typescript
// Similar pattern for Sales Order line items
const handleProductSelect = (product: ProductLookupResult) => {
  if (activeLineId) {
    updateLine(activeLineId, 'item_code', product.item_code);
    updateLine(activeLineId, 'item_name', product.item_name);
    updateLine(activeLineId, 'uom', product.stock_uom);
    updateLine(activeLineId, 'price', product.retail_price || 0);
  }
  setIsLookupOpen(false);
  setActiveLineId(null);
};
```

### **Example 3: Stock Transfer** (To Implement)
```typescript
// Stock transfer with availability check
const handleProductSelect = (product: ProductLookupResult) => {
  if (activeLineId) {
    updateLine(activeLineId, 'item_code', product.item_code);
    updateLine(activeLineId, 'item_name', product.item_name);
    updateLine(activeLineId, 'uom', product.stock_uom);
    // TODO: Fetch available quantity from source location
  }
  setIsLookupOpen(false);
  setActiveLineId(null);
};
```

---

## 🔑 **Key Behaviors**

### **Trigger Conditions:**
1. **Enter key** on empty item code field → Opens lookup
2. **Manual button** (optional) → Opens lookup
3. **F2 key** (optional, like POS) → Opens lookup

### **Auto-Fill Behavior:**
When a product is selected:
1. Item Code → Auto-filled
2. Item Name → Auto-filled (read-only)
3. UOM → Auto-filled from stock_uom
4. Price → Auto-filled if available (for sales)
5. Focus → Moves to next field (quantity)

### **Recent Items:**
- Stored in `localStorage` key: `recent_product_lookups`
- Maximum 10 items
- Newest first
- Persists across sessions

---

## 📊 **Data Flow**

```
User Action (Enter on empty field)
    ↓
Open Modal (isLookupOpen = true)
    ↓
User Searches/Selects
    ↓
handleProductSelect(product)
    ↓
Update Line Items (item_code, item_name, uom)
    ↓
Save to Recent Items (localStorage)
    ↓
Close Modal (isLookupOpen = false)
```

---

## 🎯 **Modules to Implement**

### **High Priority:**
- [x] Purchase Requisition
- [ ] Purchase Order
- [ ] Sales Order
- [ ] Stock Transfer
- [ ] Stock Adjustment

### **Medium Priority:**
- [ ] RFQ (Request for Quotation)
- [ ] GRN (Goods Receipt Note)
- [ ] Stock Take
- [ ] Sales Quote

### **Low Priority:**
- [ ] Purchase Return
- [ ] Sales Return
- [ ] Bill of Materials
- [ ] Production Order

---

## 🐛 **Troubleshooting**

### **Issue: Modal doesn't open**
- Check `isLookupOpen` state
- Verify `onKeyDown` handler is attached
- Check console for errors

### **Issue: Search not working**
- Verify `itemService.getItems()` API call
- Check network tab for API response
- Ensure backend is running

### **Issue: Selection doesn't update line**
- Verify `activeLineId` is set correctly
- Check `handleProductSelect` logic
- Ensure `updateLine` function works

---

## 📚 **Related Documentation**

- [Item Master Service](../../services/itemService.ts)
- [POS Product Lookup](../../modules/pos/billing/PosRightPanel.tsx)
- [Refer This Before New UI Module](./Refer_this_before_new_UI_module.md)

---

## ✅ **Checklist for New Implementation**

When implementing in a new module:

- [ ] Import `ProductLookupModal` and `ProductLookupResult`
- [ ] Add state: `isLookupOpen`, `activeLineId`
- [ ] Create `handleItemCodeKeyDown` handler
- [ ] Create `handleProductSelect` handler
- [ ] Add `onKeyDown` to item code input
- [ ] Add `ProductLookupModal` component
- [ ] Test Enter key trigger
- [ ] Test product selection
- [ ] Test auto-fill behavior
- [ ] Verify recent items work
- [ ] Update this documentation with example

---

**Last Updated**: 2025-12-21  
**Status**: ✅ Active - Ready for use  
**Maintainer**: Development Team
