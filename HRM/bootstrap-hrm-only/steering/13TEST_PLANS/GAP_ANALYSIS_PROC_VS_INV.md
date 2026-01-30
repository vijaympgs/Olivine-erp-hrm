# 📊 Gap Analysis: Procurement vs. Inventory Test Prompts

**Objective:** Compare the structural and granular differences between Procurement (Phase 0 Complete) and Inventory (Phase 0 Complete) test script prompts.

---

## 1. Structural Difference: "Document" vs. "Domain"

| Feature | **Procurement (4.x)** | **Inventory (5.x)** |
| :--- | :--- | :--- |
| **Granularity** | **Component-Approached** | **Functional/Module-Approached** |
| **Mapping Rule** | 1 Prompt = 1 Transaction Document (e.g., PO, RFQ) | 1 Prompt = 1 Functional Domain (e.g., Movements, Replenishment) |
| **Logic** | Linear Workflow (Req -> PO -> GRN) | State-Based Logic (Stock Levels, Valuation, Tracking) |
| **File Count** | 7 Core Transaction Files + 4 Support | 10 Functional Domain Files |

### 🔍 Key Observation
**Procurement** follows a traditional "Document Flow" where each screen corresponds to a specific business document (Requisition, PO).
**Inventory** follows a "Domain Logic" approach, where **Stock Movements (5.3)** handles *multiple* transaction types (Transfers, Receipts, Issues) because they all share the same underlying ledger logic.

---

## 2. Coverage Analysis

### ✅ Procurement Coverage (Document Centric)
| Prompt File | Scope | Granularity |
| :--- | :--- | :--- |
| `4.1_Purchase_Requisition...` | Requisitions ONLY | High (Specific fields/logic) |
| `4.2_Request_for_Quotation...` | RFQs ONLY | High |
| `4.3_Purchase_Order...` | Purchase Orders ONLY | High |
| `...` | ... | ... |

### ✅ Inventory Coverage (Domain Centric)
| Prompt File | Scope | Aggregation Details |
| :--- | :--- | :--- |
| `5.3_Stock_Movements...` | **Aggregated**: Internal Transfers, Intercompany Transfers, Goods Issues, Goods Receipts (View). | **High Efficiency**: Tests the *movement engine*, not just screens. |
| `5.7_Replenishment...` | **Aggregated**: Reorder Points, Safety Stock, Min-Max, Suggestions. | Tests the *planning engine*. |
| `5.8_Item_Tracking...` | **Aggregated**: Batches, Serials, Expiry, Recall. | Tests the *tracking attributes*. |
| `5.9_Inventory_Reports...` | **Aggregated**: Stock Summary, Valuation Report, Aging, Movement History. | Tests the *query engine*. |

---

## 3. Identified Gaps & Risks

### ⚠️ Gap 1: "Granular Screen Validation"
**Risk**: In Procurement, `test_4_3_purchase_order.py` specifically tests the PO screen's unique validation.
In Inventory, `test_5_3_stock_movements.py` tests the *backend movement*, but might miss specific UI/UX constraints of the "Internal Transfer" screen vs the "Intercompany Transfer" screen if not explicitly called out in the prompt.

**Mitigation**: Ensure `5.3_Stock_Movements` prompt explicitly lists test cases for *each subtype* (Internal vs Intercompany) to ensure screen-specific logic isn't lost.

### ⚠️ Gap 2: "Master Data Dependency"
**Risk**: Procurement prompts (like Vendors) are separated.
Inventory relies heavily on `Item Master` setup potentially covered in `5.8_Item_Tracking` or `5.2_Stock_Management`. If `Item Master` tests are missing, Inventory tests might fail on setup.

**Mitigation**: Confirmed `5.2` and `5.10` cover the necessary parameter setups.

---

## 4. Recommendation

The **Inventory Strategy (Domain/Module Level)** is superior for this specific module because:
1.  Inventory is less about "creating documents" and more about "managing state" (stock levels).
2.  Testing `StockMovement` as a single unit ensures the *ledger integrity* is consistent across all transaction types.
3.  Aggregation reduces file sprawl (avoids having `test_safety_stock.py`, `test_min_max.py`, `test_reorder_point.py` which all test the same `ReorderPolicy` model).

**Verdict**: No action required. The difference is architectural and appropriate for the different nature of the modules.
