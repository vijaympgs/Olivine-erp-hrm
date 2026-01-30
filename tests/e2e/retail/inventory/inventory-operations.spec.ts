/**
 * Inventory Operations E2E Tests
 * Generated from: tests/retail/inventory/*_scenarios.md
 * Screens: Internal Transfer, Stock Adjustment
 */

import { test, expect, Page } from '@playwright/test';

const BASE_URL = process.env.BASE_URL || 'http://localhost:3001';

async function login(page: Page) {
    await page.goto(`${BASE_URL}/login`);
    await page.fill('[data-testid="username"]', 'warehouse');
    await page.fill('[data-testid="password"]', 'warehouse123');
    await page.click('[data-testid="btn-login"]');
    await page.waitForURL('**/dashboard');
}

test.describe('Inventory Operations', () => {
    test.beforeEach(async ({ page }) => {
        await login(page);
    });

    test.describe('Internal Transfers - SC-TRANS', () => {
        test('SC-TRANS-001: Create Transfer (Happy Path)', async ({ page }) => {
            await page.goto(`${BASE_URL}/inventory/transfers`);

            await page.click('[data-testid="btn-new"]');

            // From location
            await page.click('[data-testid="from-location"]');
            await page.click('[data-testid="location-option"]:first-child');

            // To location
            await page.click('[data-testid="to-location"]');
            await page.click('[data-testid="location-option"]:last-child');

            // Add item
            await page.click('[data-testid="btn-add-line"]');
            await page.click('[data-testid="item-lookup-0"]');
            await page.click('[data-testid="item-option"]:first-child');

            // Enter qty
            await page.fill('[data-testid="transfer-qty-0"]', '50');

            // Save
            await page.click('[data-testid="btn-save"]');
            await expect(page.locator('.toast-success')).toBeVisible();

            // Submit
            await page.click('[data-testid="btn-submit"]');
            await expect(page.locator('[data-testid="status-badge"]')).toContainText(/transit/i);
        });

        test('SC-TRANS-002: Receive Transfer', async ({ page }) => {
            await page.goto(`${BASE_URL}/inventory/transfers`);

            // Filter to In Transit
            await page.click('[data-testid="filter-status"]');
            await page.click('text=In Transit');

            // Open first
            await page.click('[data-testid="grid-row"]:first-child');

            // Enter received qty
            const transferQty = await page.inputValue('[data-testid="transfer-qty-0"]');
            await page.fill('[data-testid="received-qty-0"]', transferQty);

            // Receive
            await page.click('[data-testid="btn-receive"]');
            await page.click('[data-testid="btn-confirm"]');

            await expect(page.locator('[data-testid="status-badge"]')).toContainText(/received|complete/i);
        });

        test('SC-TRANS-004: Cannot Transfer More Than Available', async ({ page }) => {
            await page.goto(`${BASE_URL}/inventory/transfers`);

            await page.click('[data-testid="btn-new"]');

            await page.click('[data-testid="from-location"]');
            await page.click('[data-testid="location-option"]:first-child');

            await page.click('[data-testid="to-location"]');
            await page.click('[data-testid="location-option"]:last-child');

            await page.click('[data-testid="btn-add-line"]');
            await page.click('[data-testid="item-lookup-0"]');
            await page.click('[data-testid="item-option"]:first-child');

            // Enter qty higher than available
            await page.fill('[data-testid="transfer-qty-0"]', '999999');

            await page.click('[data-testid="btn-submit"]');

            await expect(page.locator('.toast-error, .validation-error')).toContainText(/insufficient|stock/i);
        });
    });

    test.describe('Stock Adjustments - SC-ADJ', () => {
        test('SC-ADJ-001: Positive Adjustment (Happy Path)', async ({ page }) => {
            await page.goto(`${BASE_URL}/inventory/adjustments/new`);

            // Select location
            await page.click('[data-testid="location-select"]');
            await page.click('[data-testid="location-option"]:first-child');

            // Select reason
            await page.click('[data-testid="reason-select"]');
            await page.click('text=Found Stock');

            // Add item
            await page.click('[data-testid="btn-add-line"]');
            await page.click('[data-testid="item-lookup-0"]');
            await page.click('[data-testid="item-option"]:first-child');

            // Positive qty
            await page.fill('[data-testid="adjust-qty-0"]', '10');

            // Save
            await page.click('[data-testid="btn-save"]');
            await expect(page.locator('.toast-success')).toBeVisible();

            // Post
            await page.click('[data-testid="btn-post"]');
            await page.click('[data-testid="btn-confirm"]');

            await expect(page.locator('[data-testid="status-badge"]')).toContainText(/posted/i);
        });

        test('SC-ADJ-002: Negative Adjustment', async ({ page }) => {
            await page.goto(`${BASE_URL}/inventory/adjustments/new`);

            await page.click('[data-testid="location-select"]');
            await page.click('[data-testid="location-option"]:first-child');

            await page.click('[data-testid="reason-select"]');
            await page.click('text=Damage');

            await page.click('[data-testid="btn-add-line"]');
            await page.click('[data-testid="item-lookup-0"]');
            await page.click('[data-testid="item-option"]:first-child');

            // Negative qty
            await page.fill('[data-testid="adjust-qty-0"]', '-5');

            await page.click('[data-testid="btn-save"]');
            await page.click('[data-testid="btn-post"]');
            await page.click('[data-testid="btn-confirm"]');

            await expect(page.locator('.toast-success')).toBeVisible();
        });

        test('SC-ADJ-004: Cannot Exceed Stock', async ({ page }) => {
            await page.goto(`${BASE_URL}/inventory/adjustments/new`);

            await page.click('[data-testid="location-select"]');
            await page.click('[data-testid="location-option"]:first-child');

            await page.click('[data-testid="reason-select"]');
            await page.click('text=Damage');

            await page.click('[data-testid="btn-add-line"]');
            await page.click('[data-testid="item-lookup-0"]');
            await page.click('[data-testid="item-option"]:first-child');

            // Try to remove more than available
            await page.fill('[data-testid="adjust-qty-0"]', '-999999');

            await page.click('[data-testid="btn-post"]');

            await expect(page.locator('.toast-error, .validation-error')).toContainText(/negative|insufficient/i);
        });

        test('SC-ADJ-005: Reason Code Required', async ({ page }) => {
            await page.goto(`${BASE_URL}/inventory/adjustments/new`);

            await page.click('[data-testid="location-select"]');
            await page.click('[data-testid="location-option"]:first-child');

            // Skip reason
            await page.click('[data-testid="btn-add-line"]');
            await page.click('[data-testid="item-lookup-0"]');
            await page.click('[data-testid="item-option"]:first-child');
            await page.fill('[data-testid="adjust-qty-0"]', '10');

            await page.click('[data-testid="btn-save"]');

            await expect(page.locator('.validation-error, .field-error')).toBeVisible();
        });
    });
});
