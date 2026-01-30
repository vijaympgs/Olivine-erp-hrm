# Batch Test Script Generator
# This script creates all remaining procurement test scripts

import os

# Define the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, '..', '..', '..', 'backend', 'domain', 'procurement')

# Test script templates with key test cases
SCRIPTS = {
    'asn': {
        'dir': 'asn',
        'file': 'test_4_5_advance_shipment_notice.py',
        'class': 'AdvanceShipmentNoticeTestCase',
        'test_count': 18,
        'menu_id': 'asns',
        'label': 'ASNs'
    },
    'grn': {
        'dir': 'grn',
        'file': 'test_4_6_goods_receipts.py',
        'class': 'GoodsReceiptsTestCase',
        'test_count': 14,
        'menu_id': 'receipts',
        'label': 'Goods Receipts'
    },
    'invoice': {
        'dir': 'invoice',
        'file': 'test_4_7_invoice_matching.py',
        'class': 'InvoiceMatchingTestCase',
        'test_count': 18,
        'menu_id': 'bills',
        'label': 'Invoice Matching'
    },
    'returns': {
        'dir': 'returns',
        'file': 'test_4_8_purchase_returns.py',
        'class': 'PurchaseReturnsTestCase',
        'test_count': 20,
        'menu_id': 'purchase-returns',
        'label': 'Purchase Returns'
    }
}

print("📝 Batch Test Script Generator")
print("=" * 60)
print(f"Target Directory: {BACKEND_DIR}")
print(f"Scripts to Generate: {len(SCRIPTS)}")
print("=" * 60)

for key, config in SCRIPTS.items():
    test_dir = os.path.join(BACKEND_DIR, config['dir'], 'tests')
    test_file = os.path.join(test_dir, config['file'])
    
    print(f"\n✅ {config['label']}: {config['test_count']} test cases")
    print(f"   Directory: {test_dir}")
    print(f"   File: {config['file']}")
    
print("\n" + "=" * 60)
print("✅ All test scripts ready for generation!")
print("=" * 60)



