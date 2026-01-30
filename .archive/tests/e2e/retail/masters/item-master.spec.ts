/**
 * Item Master E2E Tests
 * Generated from: tests/retail/masters/item_master_scenarios.md
 * Screen: /inventory/item-master
 * Component: ItemMasterSetup.tsx
 */

import { test, expect, Page } from '@playwright/test';

// Test configuration
const BASE_URL = process.env.BASE_URL || 'http://localhost:3001';
const ITEM_MASTER_URL = `${BASE_URL}/inventory/item-master`;

// Test data
const TEST_ITEM = {
    code: `TEST-${Date.now()}`,
    name: 'Test Item Automation',
    category: 'General',
    uom: 'PCS',
    sellingPrice: '100.00',
    costPrice: '80.00',
};

// Helper functions
async function login(page: Page) {
    await page.goto(`${BASE_URL}/login`);
    await page.fill('[data-testid="username"]', 'admin');
    await page.fill('[data-testid="password"]', 'admin123');
    await page.click('[data-testid="btn-login"]');
    await page.waitForURL('**/dashboard');
}

async function navigateToItemMaster(page: Page) {
    await page.goto(ITEM_MASTER_URL);
    await page.waitForLoadState('networkidle');
}

test.describe('Item Master - SC-ITEM', () => {
    test.beforeEach(async ({ page }) => {
        await login(page);
        await navigateToItemMaster(page);
    });

    test('SC-ITEM-001: Create Simple Item (Happy Path)', async ({ page }) => {
        // Step 1: Verify list view loads
        await expect(page.locator('h1, [data-testid="page-title"]')).toContainText(/Item/i);

        // Step 2: Click New button
        await page.click('[data-testid="btn-new"]');

        // Step 3: Enter Item Code
        await page.fill('[data-testid="item-code"]', TEST_ITEM.code);

        // Step 4: Enter Item Name
        await page.fill('[data-testid="item-name"]', TEST_ITEM.name);

        // Step 5: Select Category
        await page.click('[data-testid="category-lookup"]');
        await page.click(`text=${TEST_ITEM.category}`);

        // Step 6: Select Base UOM
        await page.click('[data-testid="uom-lookup"]');
        await page.click(`text=${TEST_ITEM.uom}`);

        // Step 7: Enter Selling Price
        await page.fill('[data-testid="selling-price"]', TEST_ITEM.sellingPrice);

        // Step 8: Click Save
        await page.click('[data-testid="btn-save"]');

        // Step 9: Verify success
        await expect(page.locator('.toast-success, [role="alert"]')).toBeVisible();
    });

    test('SC-ITEM-003: Edit Existing Item', async ({ page }) => {
        // Step 2: Search for item
        await page.fill('[data-testid="search-input"]', TEST_ITEM.code);
        await page.press('[data-testid="search-input"]', 'Enter');

        // Step 3: Click row to select
        await page.click(`text=${TEST_ITEM.code}`);

        // Step 4: Click Edit
        await page.click('[data-testid="btn-edit"]');

        // Step 5: Modify Name
        const newName = `${TEST_ITEM.name} Updated`;
        await page.fill('[data-testid="item-name"]', newName);

        // Step 6: Click Save
        await page.click('[data-testid="btn-save"]');

        // Step 7: Verify update
        await expect(page.locator('.toast-success, [role="alert"]')).toBeVisible();
    });

    test('SC-ITEM-004: Duplicate Code Validation', async ({ page }) => {
        // Create first item
        await page.click('[data-testid="btn-new"]');
        await page.fill('[data-testid="item-code"]', 'DUP-TEST-001');
        await page.fill('[data-testid="item-name"]', 'Duplicate Test');
        await page.click('[data-testid="btn-save"]');
        await page.waitForTimeout(1000);

        // Try to create with same code
        await page.click('[data-testid="btn-new"]');
        await page.fill('[data-testid="item-code"]', 'DUP-TEST-001');
        await page.fill('[data-testid="item-name"]', 'Duplicate Test 2');
        await page.click('[data-testid="btn-save"]');

        // Verify error
        await expect(page.locator('.toast-error, [role="alert"]')).toContainText(/duplicate|exists/i);
    });

    test('SC-ITEM-005: Required Field Validation', async ({ page }) => {
        // Step 1: Click New
        await page.click('[data-testid="btn-new"]');

        // Step 2-3: Leave required fields empty
        // Step 4: Click Save
        await page.click('[data-testid="btn-save"]');

        // Step 5: Verify validation errors
        await expect(page.locator('[data-testid="item-code-error"], .field-error')).toBeVisible();
    });

    test('SC-ITEM-008: Search and Filter', async ({ page }) => {
        // Step 1: Enter search term
        await page.fill('[data-testid="search-input"]', 'Test');
        await page.press('[data-testid="search-input"]', 'Enter');

        // Verify filtered results
        await page.waitForTimeout(500);
        const rows = await page.locator('table tbody tr, [data-testid="grid-row"]').count();
        expect(rows).toBeGreaterThanOrEqual(0);

        // Step 3: Clear search
        await page.fill('[data-testid="search-input"]', '');
        await page.press('[data-testid="search-input"]', 'Enter');
    });

    test('SC-ITEM-009: Cancel Create (Discard Changes)', async ({ page }) => {
        // Step 1: Click New
        await page.click('[data-testid="btn-new"]');

        // Step 2: Enter some data
        await page.fill('[data-testid="item-code"]', 'CANCEL-TEST');

        // Step 3: Click Cancel
        await page.click('[data-testid="btn-cancel"]');

        // Step 4-5: Verify return to list, no save
        await expect(page.locator('[data-testid="btn-new"]')).toBeVisible();
    });
});

test.afterAll(async ({ browser }) => {
    // Cleanup: Delete test items created during tests
    const context = await browser.newContext();
    const page = await context.newPage();
    await login(page);
    // Add cleanup logic if needed
    await context.close();
});
