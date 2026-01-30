/**
 * Masters Setup E2E Tests
 * Generated from: tests/retail/masters/*_scenarios.md
 * Screens: UOM, Category, Price List
 */

import { test, expect, Page } from '@playwright/test';

const BASE_URL = process.env.BASE_URL || 'http://localhost:3001';

async function login(page: Page) {
    await page.goto(`${BASE_URL}/login`);
    await page.fill('[data-testid="username"]', 'admin');
    await page.fill('[data-testid="password"]', 'admin123');
    await page.click('[data-testid="btn-login"]');
    await page.waitForURL('**/dashboard');
}

test.describe('Masters Setup', () => {
    test.beforeEach(async ({ page }) => {
        await login(page);
    });

    test.describe('UOM Setup - SC-UOM', () => {
        test('SC-UOM-001: Create UOM (Happy Path)', async ({ page }) => {
            await page.goto(`${BASE_URL}/inventory/uoms`);

            await page.click('[data-testid="btn-new"]');

            await page.fill('[data-testid="uom-code"]', `UOM-${Date.now()}`);
            await page.fill('[data-testid="uom-name"]', 'Test UOM');

            await page.click('[data-testid="btn-save"]');
            await expect(page.locator('.toast-success')).toBeVisible();
        });

        test('SC-UOM-002: Create UOM with Base', async ({ page }) => {
            await page.goto(`${BASE_URL}/inventory/uoms`);

            await page.click('[data-testid="btn-new"]');

            await page.fill('[data-testid="uom-code"]', `BOX-${Date.now()}`);
            await page.fill('[data-testid="uom-name"]', 'Box');

            await page.click('[data-testid="base-uom"]');
            await page.click('text=PCS');

            await page.fill('[data-testid="conversion-factor"]', '12');

            await page.click('[data-testid="btn-save"]');
            await expect(page.locator('.toast-success')).toBeVisible();
        });

        test('SC-UOM-003: Duplicate Code Validation', async ({ page }) => {
            await page.goto(`${BASE_URL}/inventory/uoms`);

            await page.click('[data-testid="btn-new"]');
            await page.fill('[data-testid="uom-code"]', 'PCS');
            await page.fill('[data-testid="uom-name"]', 'Duplicate');
            await page.click('[data-testid="btn-save"]');

            await expect(page.locator('.toast-error')).toContainText(/exists|duplicate/i);
        });
    });

    test.describe('Category Hierarchy - SC-CAT', () => {
        test('SC-CAT-001: Create Root Category', async ({ page }) => {
            await page.goto(`${BASE_URL}/inventory/categories`);

            await page.click('[data-testid="btn-add-root"]');

            await page.fill('[data-testid="category-code"]', `CAT-${Date.now()}`);
            await page.fill('[data-testid="category-name"]', 'Test Category');

            await page.click('[data-testid="btn-save"]');
            await expect(page.locator('.toast-success')).toBeVisible();
        });

        test('SC-CAT-002: Create Sub-Category', async ({ page }) => {
            await page.goto(`${BASE_URL}/inventory/categories`);

            // Click on existing category
            await page.click('[data-testid="tree-node"]:first-child');

            // Add child
            await page.click('[data-testid="btn-add-child"]');

            await page.fill('[data-testid="category-code"]', `SUB-${Date.now()}`);
            await page.fill('[data-testid="category-name"]', 'Sub Category');

            await page.click('[data-testid="btn-save"]');
            await expect(page.locator('.toast-success')).toBeVisible();
        });

        test('SC-CAT-004: Edit Category', async ({ page }) => {
            await page.goto(`${BASE_URL}/inventory/categories`);

            await page.click('[data-testid="tree-node"]:first-child');
            await page.click('[data-testid="btn-edit"]');

            await page.fill('[data-testid="category-name"]', 'Updated Category Name');

            await page.click('[data-testid="btn-save"]');
            await expect(page.locator('.toast-success')).toBeVisible();
        });
    });

    test.describe('Price List - SC-PRICE', () => {
        test('SC-PRICE-001: Create Price List', async ({ page }) => {
            await page.goto(`${BASE_URL}/inventory/price-lists`);

            await page.click('[data-testid="btn-new"]');

            await page.fill('[data-testid="pricelist-code"]', `PL-${Date.now()}`);
            await page.fill('[data-testid="pricelist-name"]', 'Test Price List');

            await page.click('[data-testid="currency"]');
            await page.click('text=INR');

            await page.fill('[data-testid="valid-from"]', '2026-01-01');
            await page.fill('[data-testid="valid-to"]', '2026-12-31');

            await page.click('[data-testid="btn-save"]');
            await expect(page.locator('.toast-success')).toBeVisible();
        });

        test('SC-PRICE-002: Add Items to Price List', async ({ page }) => {
            await page.goto(`${BASE_URL}/inventory/price-lists`);

            // Open existing
            await page.click('[data-testid="grid-row"]:first-child');
            await page.click('[data-testid="btn-edit"]');

            // Items tab
            await page.click('[data-tab="items"]');

            // Add item
            await page.click('[data-testid="btn-add-item"]');
            await page.click('[data-testid="item-lookup"]');
            await page.click('[data-testid="item-option"]:first-child');

            await page.fill('[data-testid="item-price"]', '150.00');

            await page.click('[data-testid="btn-save"]');
            await expect(page.locator('.toast-success')).toBeVisible();
        });

        test('SC-PRICE-004: Date Range Validation', async ({ page }) => {
            await page.goto(`${BASE_URL}/inventory/price-lists`);

            await page.click('[data-testid="btn-new"]');

            await page.fill('[data-testid="pricelist-code"]', `PL-INVALID`);
            await page.fill('[data-testid="pricelist-name"]', 'Invalid Dates');

            // Invalid: To before From
            await page.fill('[data-testid="valid-from"]', '2026-12-31');
            await page.fill('[data-testid="valid-to"]', '2026-01-01');

            await page.click('[data-testid="btn-save"]');

            await expect(page.locator('.validation-error, .toast-error')).toBeVisible();
        });
    });
});
