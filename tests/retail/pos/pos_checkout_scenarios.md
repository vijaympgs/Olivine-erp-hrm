# Screen: POS Checkout

**Sidebar Path**: Retail > Store Ops > Billing > Checkout  
**URL**: `/pos/ui`  
**Component**: `PosPage.tsx` → `PosDesktop.tsx`  
**Status**: Core Transaction Screen - Multi-Vertical Support

---

## Purpose

The POS Checkout is the primary transaction screen for retail sales. It supports:
- 8 verticals (General, Grocery, Fashion, Restaurant, Pharmacy, Electronics, Services, Fuel)
- Product search and barcode scanning
- Cart management with quantity adjustments
- Multi-tender payments (Cash, Card, UPI, Split)
- Customer selection with loyalty integration
- Vertical-specific features (Batch, Serial, Modifiers, Prescription, etc.)

Per BBP evidence: `/pos/business-rules` controls feature flags per vertical.

---

## Preconditions

| Prerequisite | Dependency Chain | Required |
|--------------|------------------|----------|
| Day Open | `/operations/pos/day-open` | Yes |
| Session Open | `/operations/pos/session-open` | Yes |
| Terminal Configured | `/pos/terminal` | Yes |
| Business Rules Set | `/pos/business-rules` | Yes |
| At least 1 Item with price | `/inventory/item-master` | Yes |
| User Permission | `pos.checkout.access`, `pos.checkout.discount` | Yes |

---

## Scenarios

### SC-POS-001: Simple Cash Sale (Happy Path)

**Type**: Happy Path  
**Priority**: Critical  
**Preconditions**: Day open, Session open, Item "SKU-001" exists with price ₹100

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Verify session active | Check header | Session ID displayed, operator name |
| 2 | Search for item | Search box = "SKU-001" or scan | Item lookup opens |
| 3 | Select item | Click item in results | Item added to cart, Qty = 1 |
| 4 | Verify cart line | Cart area | SKU-001, Qty: 1, Price: ₹100.00 |
| 5 | Click Pay | `[data-testid="btn-pay"]` or Enter | Tender screen opens |
| 6 | Verify total | Tender header | Total: ₹100.00 |
| 7 | Click Cash | `[data-tender="CASH"]` | Cash input field |
| 8 | Enter exact amount | Amount = "100.00" | Change: ₹0.00 |
| 9 | Click Complete | `[data-testid="btn-complete"]` | Transaction saved |
| 10 | Verify receipt | Receipt display/print | Receipt shows transaction details |
| 11 | Verify cart cleared | Main screen | Empty cart, ready for next |

**Postconditions**: 
- Sale record created in `pos_transactions`
- Inventory decremented by 1
- Cash drawer balance increased by ₹100

---

### SC-POS-002: Multiple Items Sale

**Type**: Happy Path  
**Priority**: Critical  
**Preconditions**: Items SKU-001 (₹100) and SKU-002 (₹50) exist

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Add Item 1 | Search "SKU-001" | Cart: 1 item, Total: ₹100 |
| 2 | Add Item 2 | Search "SKU-002" | Cart: 2 items, Total: ₹150 |
| 3 | Increase qty of Item 1 | Click +/enter qty = 3 | Cart: SKU-001 x3 = ₹300 |
| 4 | Verify total | Cart footer | Total: ₹350 (300 + 50) |
| 5 | Complete payment | Cash ₹350 | Transaction complete |

**Postconditions**: 2 line items saved, inventory: SKU-001 -3, SKU-002 -1

---

### SC-POS-003: Sale with Customer Selection

**Type**: Happy Path  
**Priority**: High  
**Preconditions**: Customer "CUST-001" exists in Customer Master

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Click Customer button | `[data-testid="btn-customer"]` | Customer lookup sidebar opens |
| 2 | Search customer | Search = "CUST-001" | Customer found in results |
| 3 | Select customer | Click customer row | Customer attached to transaction |
| 4 | Verify header | POS header | Customer name displayed |
| 5 | Add items | Normal flow | Items in cart |
| 6 | Complete sale | Payment flow | Transaction with customer_id |

**Postconditions**: Transaction linked to customer, visible in customer history

---

### SC-POS-004: Apply Line Discount (Percentage)

**Type**: Happy Path  
**Priority**: High  
**Preconditions**: Item SKU-001 (₹100), user has discount permission

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Add item | SKU-001 | Line total: ₹100 |
| 2 | Click line | Select cart line | Line selected |
| 3 | Click Discount | `[data-testid="btn-line-discount"]` | Discount dialog opens |
| 4 | Select % type | Toggle "Percentage" | Percentage input active |
| 5 | Enter 10% | Value = "10" | Preview: -₹10 |
| 6 | Apply | Click Apply | Line total: ₹90 |
| 7 | Complete sale | Payment ₹90 | Discount recorded |

**Postconditions**: Line discount saved in transaction details

---

### SC-POS-005: Apply Transaction Discount

**Type**: Happy Path  
**Priority**: High  
**Preconditions**: Multiple items, total ₹200

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Add items | Total = ₹200 | Cart populated |
| 2 | Click Bill Discount | `[data-testid="btn-bill-discount"]` | Discount dialog |
| 3 | Enter ₹20 flat | Amount = "20" | Preview |
| 4 | Apply | Save | Total: ₹180 |
| 5 | Pay | Cash ₹180 | Success |

**Postconditions**: Transaction-level discount recorded

---

### SC-POS-006: Hold and Recall

**Type**: Happy Path  
**Priority**: Medium  
**Preconditions**: Session open

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Add items to cart | 2 items, ₹150 | Cart populated |
| 2 | Click Hold | `[data-testid="btn-hold"]` | Hold reference input |
| 3 | Enter reference | "Customer Phone Call" | Optional note |
| 4 | Confirm | Save Hold | Transaction held, cart cleared |
| 5 | Serve another customer | New sale | Complete and finish |
| 6 | Click Recall | `[data-testid="btn-recall"]` | Held transactions list |
| 7 | Select held transaction | Click row | Cart restored with original items |
| 8 | Complete sale | Pay ₹150 | Held transaction completed |

**Postconditions**: Held transaction converted to completed sale

---

### SC-POS-007: Void Line Item

**Type**: Happy Path  
**Priority**: Medium  
**Preconditions**: Cart has 2 items

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Add 2 items | A: ₹100, B: ₹50, Total: ₹150 | Cart populated |
| 2 | Select Item A | Click row | Row selected |
| 3 | Click Remove | `[data-testid="btn-remove-line"]` | Confirmation |
| 4 | Confirm | Yes | Item A removed |
| 5 | Verify cart | Single item | Total: ₹50 |

**Postconditions**: Only Item B in cart, Item A not charged

---

### SC-POS-008: Void Entire Transaction

**Type**: Edge Case  
**Priority**: Medium  
**Preconditions**: Cart has items

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Add items | ₹200 total | Cart populated |
| 2 | Click Cancel Sale | `[data-testid="btn-cancel-sale"]` | Confirmation dialog |
| 3 | Enter reason | Required field | Reason captured |
| 4 | Confirm | "Yes, void" | Cart cleared |
| 5 | Verify | Check list | No transaction saved |

**Postconditions**: No sale record created, inventory unchanged

---

### SC-POS-009: Split Payment (Cash + Card)

**Type**: Happy Path  
**Priority**: Medium  
**Preconditions**: Total ₹200, card terminal configured

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Total | ₹200 | Tender screen |
| 2 | Click Cash | `[data-tender="CASH"]` | Cash input |
| 3 | Enter partial | ₹100 | Balance: ₹100 |
| 4 | Apply | Cash applied | Remaining shown |
| 5 | Click Card | `[data-tender="CARD"]` | Card input |
| 6 | Enter ₹100 | Balance: ₹0 | Fully settled |
| 7 | Complete | Confirm | Split payment recorded |

**Postconditions**: Transaction with 2 tender lines (CASH ₹100, CARD ₹100)

---

### SC-POS-010: Over-payment with Change

**Type**: Happy Path  
**Priority**: Medium  
**Preconditions**: Total ₹85

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Total | ₹85 | Tender screen |
| 2 | Cash ₹100 | Enter 100 | Change displayed: ₹15 |
| 3 | Complete | Confirm | Change calculated |
| 4 | Receipt | Check | "Tendered: ₹100, Change: ₹15" |

**Postconditions**: Change amount logged, cash drawer accurate

---

### SC-POS-011: Return/Refund (Same Day)

**Type**: Happy Path  
**Priority**: Medium  
**Preconditions**: Completed sale exists with receipt #

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Click Return | `[data-testid="btn-return"]` | Return mode |
| 2 | Enter receipt # | Original receipt number | Transaction loaded |
| 3 | Select items to return | Check items | Return qty input |
| 4 | Enter return qty | Qty = 1 | Return amount calculated |
| 5 | Process refund | Confirm | Refund dialog |
| 6 | Select refund method | Cash out | Cash returned |
| 7 | Complete | Confirm | Return recorded |

**Postconditions**: Return transaction created, inventory restored, cash decremented

---

### SC-POS-012: Item Not Found

**Type**: Edge Case  
**Priority**: Low  
**Preconditions**: None

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Search invalid | "INVALID-SKU-XYZ" | Search executed |
| 2 | Verify results | Empty results | "No items found" message |
| 3 | Cart unchanged | Check cart | Still empty or previous items |

**Postconditions**: No crash, graceful handling

---

### SC-POS-013: Session Not Open (Blocked)

**Type**: Edge Case  
**Priority**: High  
**Preconditions**: Day open but session NOT open

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Navigate to POS | `/pos/ui` | Access blocked |
| 2 | Verify message | Screen | "Please open a session first" |
| 3 | Redirect offered | Button | Link to Session Open |

**Postconditions**: Cannot transact without active session

---

### SC-POS-014: Day Not Open (Blocked)

**Type**: Edge Case  
**Priority**: High  
**Preconditions**: No day open

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Navigate to POS | `/pos/ui` | Access blocked |
| 2 | Verify message | Screen | "Please open the day first" |

**Postconditions**: POS inaccessible until day opened

---

### SC-POS-015: Batch Capture (Pharmacy Vertical)

**Type**: Vertical-Specific  
**Priority**: High  
**Preconditions**: Pharmacy vertical active, Item has `is_batch_tracked = true`

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Add batch item | Scan/search | Batch selector modal opens |
| 2 | View batches | List | Available batches with expiry |
| 3 | Select batch | Choose nearest expiry (FEFO) | Batch assigned |
| 4 | Confirm | Add to cart | Item with batch # in cart |
| 5 | Complete sale | Payment | Batch inventory decremented |

**Postconditions**: Specific batch stock reduced, traceability maintained

---

## Data Cleanup

After test execution:
- Void any test transactions
- Restore inventory levels
- Clear held transactions

---

**Scenario Count**: 15  
**Automation Ready**: Yes  
**Last Updated**: 2026-01-25
