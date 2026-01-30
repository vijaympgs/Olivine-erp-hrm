/**
 * Purchase Order E2E Tests
 * Generated from: tests/retail/procurement/purchase_order_scenarios.md
 * Screen: /procurement/orders
 * Component: PurchaseOrderFormPage.tsx
 */

import { test, expect, Page } from '@playwright/test';

const BASE_URL = process.env.BASE_URL || 'http://localhost:3001';
const PO_URL = `${BASE_URL}/procurement/orders`;

// Test data
const TEST_SUPPLIER = {
    code: 'SUP-001',
    name: 'Test Supplier',
};

const TEST_ITEM = {
    code: 'SKU-001',
    rate: 50,
    qty: 100,
};

// Helper functions
async function login(page: Page) {
    await page.goto(`${BASE_URL}/login`);
    await page.fill('[data-testid="username"]', 'purchaser');
    await page.fill('[data-testid="password"]', 'purchaser123');
    await page.click('[data-testid="btn-login"]');
    await page.waitForURL('**/dashboard');
}

async function navigateToPO(page: Page) {
    await page.goto(PO_URL);
    await page.waitForLoadState('networkidle');
}

test.describe('Purchase Order - SC-PO', () => {
    test.beforeEach(async ({ page }) => {
        await login(page);
        await navigateToPO(page);
    });

    test('SC-PO-001: Create PO (Direct - Happy Path)', async ({ page }) => {
        // Step 2: Click New
        await page.click('[data-testid="btn-new"]');

        // Step 3: Verify PO Number auto-generated
        const poNumber = await page.inputValue('[data-testid="po-number"]');
        expect(poNumber).toMatch(/PO-\d{4}-\d+/);

        // Step 4: Select Supplier
        await page.click('[data-testid="supplier-lookup"]');
        await page.fill('[data-testid="supplier-search"]', TEST_SUPPLIER.code);
        await page.click(`text=${TEST_SUPPLIER.name}`);

        // Step 5: Set Delivery Date
        await page.fill('[data-testid="delivery-date"]', '2026-02-15');

        // Step 6: Select Ship To
        await page.click('[data-testid="location-select"]');
        await page.click('[data-testid="location-option"]:first-child');

        // Step 7: Add Line
        await page.click('[data-testid="btn-add-line"]');

        // Step 8: Select Item
        await page.click('[data-testid="item-lookup-0"]');
        await page.fill('[data-testid="item-search"]', TEST_ITEM.code);
        await page.click(`text=${TEST_ITEM.code}`);

        // Step 9: Enter Quantity
        await page.fill('[data-testid="line-qty-0"]', String(TEST_ITEM.qty));

        // Step 10: Verify Rate
        const rate = await page.inputValue('[data-testid="line-rate-0"]');
        expect(parseFloat(rate)).toBeGreaterThan(0);

        // Step 12: Click Save
        await page.click('[data-testid="btn-save"]');
        await expect(page.locator('.toast-success')).toBeVisible();

        // Step 13: Click Submit
        await page.click('[data-testid="btn-submit"]');
        await expect(page.locator('[data-testid="status-badge"]')).toContainText(/pending|approval/i);
    });

    test('SC-PO-003: Approve PO', async ({ page }) => {
        // Find a pending PO
        await page.click('[data-testid="filter-status"]');
        await page.click('text=Pending Approval');

        // Open first pending PO
        await page.click('[data-testid="grid-row"]:first-child');

        // Step 3: Click Approve
        await page.click('[data-testid="btn-approve"]');

        // Step 4: Confirm
        await page.click('[data-testid="btn-confirm"]');

        // Step 5: Verify status
        await expect(page.locator('[data-testid="status-badge"]')).toContainText(/approved/i);
    });

    test('SC-PO-004: Reject PO', async ({ page }) => {
        // Find pending PO
        await page.click('[data-testid="filter-status"]');
        await page.click('text=Pending Approval');
        await page.click('[data-testid="grid-row"]:first-child');

        // Click Reject
        await page.click('[data-testid="btn-reject"]');

        // Enter reason
        await page.fill('[data-testid="rejection-reason"]', 'Budget constraints');
        await page.click('[data-testid="btn-confirm-reject"]');

        // Verify
        await expect(page.locator('[data-testid="status-badge"]')).toContainText(/rejected/i);
    });

    test('SC-PO-005: Edit Draft PO', async ({ page }) => {
        // Find draft PO
        await page.click('[data-testid="filter-status"]');
        await page.click('text=Draft');
        await page.click('[data-testid="grid-row"]:first-child');

        // Edit
        await page.click('[data-testid="btn-edit"]');

        // Add line
        await page.click('[data-testid="btn-add-line"]');

        // Save
        await page.click('[data-testid="btn-save"]');
        await expect(page.locator('.toast-success')).toBeVisible();
    });

    test('SC-PO-006: Cannot Edit Approved PO', async ({ page }) => {
        // Find approved PO
        await page.click('[data-testid="filter-status"]');
        await page.click('text=Approved');
        await page.click('[data-testid="grid-row"]:first-child');

        // Verify Edit is disabled
        const editBtn = page.locator('[data-testid="btn-edit"]');
        await expect(editBtn).toBeDisabled().catch(async () => {
            // Or not visible
            await expect(editBtn).toHaveCount(0);
        });
    });

    test('SC-PO-008: Validation - No Lines', async ({ page }) => {
        // Create PO without lines
        await page.click('[data-testid="btn-new"]');

        // Fill header only
        await page.click('[data-testid="supplier-lookup"]');
        await page.fill('[data-testid="supplier-search"]', TEST_SUPPLIER.code);
        await page.click(`text=${TEST_SUPPLIER.name}`);

        // Try to save
        await page.click('[data-testid="btn-save"]');

        // Verify error
        await expect(page.locator('.validation-error, .toast-error')).toContainText(/line|item/i);
    });
});
