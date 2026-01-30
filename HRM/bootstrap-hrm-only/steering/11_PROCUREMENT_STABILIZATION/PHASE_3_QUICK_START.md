# Procurement Stabilization - Quick Start Guide

## 📍 Current State
✅ **Backend**: Workflow actions + nested serializers complete  
✅ **Frontend**: Types + API service complete  
⏳ **Next**: Wire PurchaseOrderFormPage to real API

---

## 🚀 Phase 3 Execution Plan

### Task 1: Replace Mock Data with API Calls
**File**: `frontend/src/modules/procurement/pages/PurchaseOrderFormPage.tsx`

1. Import the service:
   ```typescript
   import procurementService from '../procurement.service';
   ```

2. Replace `handleToolbarAction` save logic:
   ```typescript
   case 'save':
     if (isNew) {
       await procurementService.createPurchaseOrder({ ...header, lines });
     } else {
       await procurementService.updatePurchaseOrder(id, { ...header, lines });
     }
     break;
   ```

3. Add submit action:
   ```typescript
   case 'submit':
     await procurementService.submitPurchaseOrder(id);
     break;
   ```

### Task 2: Add Loading & Error States
```typescript
const [loading, setLoading] = useState(false);
const [error, setError] = useState<string | null>(null);

// Wrap API calls
try {
  setLoading(true);
  setError(null);
  await procurementService.createPurchaseOrder(data);
  navigate('/procurement/orders');
} catch (err) {
  setError(err.message);
} finally {
  setLoading(false);
}
```

### Task 3: Fetch Initial Data (Edit Mode)
```typescript
useEffect(() => {
  if (!isNew && id) {
    procurementService.getPurchaseOrder(id)
      .then(po => {
        setHeader({ ...po });
        setLines(po.lines || []);
      });
  }
}, [id, isNew]);
```

### Task 4: Add Form Validation
```typescript
const validateForm = () => {
  if (!header.supplier) return 'Supplier is required';
  if (!header.delivery_location) return 'Delivery location is required';
  if (lines.length === 0) return 'At least one line item is required';
  return null;
};
```

---

## 🧪 Testing Checklist

- [ ] Create new PO with lines → Verify saved to backend
- [ ] Edit existing PO → Verify updates persist
- [ ] Submit PO → Verify status changes to CONFIRMED
- [ ] Try to submit without supplier → Verify error message
- [ ] Add item via lookup → Verify line created with correct data
- [ ] Delete line → Verify totals recalculate

---

## 📚 Key Files Reference

| File | Purpose |
|------|---------|
| `procurement.types.ts` | TypeScript interfaces |
| `procurement.service.ts` | API calls |
| `PurchaseOrderFormPage.tsx` | Main form component |
| `backend/domain/procurement/views.py` | Workflow actions |
| `backend/domain/procurement/serializers.py` | Nested CRUD |

---

## 🔗 API Endpoints

```
GET    /procurement/orders/              # List POs
GET    /procurement/orders/{id}/         # Get single PO
POST   /procurement/orders/              # Create PO
PUT    /procurement/orders/{id}/         # Update PO
DELETE /procurement/orders/{id}/         # Delete PO

POST   /procurement/orders/{id}/submit/  # Submit for approval
POST   /procurement/orders/{id}/approve/ # Approve PO
POST   /procurement/orders/{id}/cancel/  # Cancel PO
```

---

**Ready to proceed with Phase 3!** 🚀
