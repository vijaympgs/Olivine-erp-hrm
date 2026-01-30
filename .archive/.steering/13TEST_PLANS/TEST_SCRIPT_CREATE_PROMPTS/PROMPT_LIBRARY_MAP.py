# Prompt Library Mapping
# Maps component menu_id to their test script prompt files

PROMPT_LIBRARY = {
    # Core Procurement Transactions (BBP 4.x)
    "requisitions": "Procurement/4.1_Purchase_Requisition_test_script_prompt.md",
    "rfqs": "Procurement/4.2_Request_for_Quotation_test_script_prompt.md",
    "purchase-orders": "Procurement/4.3_Purchase_Order_test_script_prompt.md",
    "asns": "Procurement/4.5_Advance_Shipment_Notice_test_script_prompt.md",
    "receipts": "Procurement/4.6_Goods_Receipts_test_script_prompt.md",
    "bills": "Procurement/4.7_Invoice_Matching_test_script_prompt.md",
    "purchase-returns": "Procurement/4.8_Purchase_Returns_test_script_prompt.md",
    
    # Supporting Components
    "suppliers": "Vendors_Master_Data_test_script_prompt.md",
    "payments": "Payments_Processing_test_script_prompt.md",
    "compliance": "Compliance_Management_test_script_prompt.md",
    "procurement-config": "Configuration_Management_test_script_prompt.md",

    # Inventory Management (BBP 5.x)
    "inventory-dashboard": "Inventory/5.1_Inventory_Dashboard_test_script_prompt.md",
    "stock-management": "Inventory/5.2_Stock_Management_test_script_prompt.md",
    "stock-movements": "Inventory/5.3_Stock_Movements_test_script_prompt.md",
    "stock-adjustments": "Inventory/5.4_Stock_Adjustments_test_script_prompt.md",
    "stock-take": "Inventory/5.5_Physical_Inventory_test_script_prompt.md",
    "inventory-valuation": "Inventory/5.6_Inventory_Valuation_test_script_prompt.md",
    
    # Inventory Advanced (5.7 - 5.10)
    "reorder-points": "Inventory/5.7_Replenishment_test_script_prompt.md",
    "batch-mgmt": "Inventory/5.8_Item_Tracking_test_script_prompt.md",
    "stock-summary-report": "Inventory/5.9_Inventory_Reports_test_script_prompt.md",
    "inventory-setup": "Inventory/5.10_Inventory_Setup_test_script_prompt.md",
}

# Base path for all prompt files
PROMPT_BASE_PATH = ".steering/13TEST_PLANS/TEST_SCRIPT_CREATE_PROMPTS/"

# Usage Instructions:
# 1. When "GEN PROMPT" is clicked, look up component menu_id in PROMPT_LIBRARY
# 2. If found, load the corresponding .md file from PROMPT_BASE_PATH
# 3. If not found, generate generic prompt (fallback)
# 4. Display in modal for copy/paste

# Benefits:
# - No AI memory required
# - Works across sessions and model switches
# - Easy to maintain (just update .md files)
# - Version controlled with git



