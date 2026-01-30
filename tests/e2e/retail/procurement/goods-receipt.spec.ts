/**
 * Goods Receipt E2E Tests
 * Generated from: tests/retail/procurement/goods_receipt_scenarios.md
 * Screen: /procurement/receipts
 * Component: GoodsReceiptFormPage.tsx
 */

import { test, expect, Page } from '@playwright/test';

const BASE_URL = process.env.BASE_URL || 'http://localhost:3001';
const GRN_URL = `${BASE_URL}/procurement/receipts`;

async function login(page: Page) {
    await page.goto(`${BASE_URL}/login`);
    await page.fill('[data-testid="username"]', 'warehouse');
    await page.fill('[data-testid="password"]', 'warehouse123');
    await page.click('[data-testid="btn-login"]');
    await page.waitForURL('**/dashboard');
}

async function navigateToGRN(page: Page) {
    await page.goto(GRN_URL);
    await page.waitForLoadState('networkidle');
}

test.describe('Goods Receipt - SC-GRN', () => {
    test.beforeEach(async ({ page }) => {
        await login(page);
        await navigateToGRN(page);
    });

    test('SC-GRN-001: Full Receipt (Happy Path)', async ({ page }) => {
        await page.click('[data-testid="btn-new"]');

        // Select PO
        await page.click('[data-testid="po-lookup"]');
        await page.click('[data-testid="po-option"]:first-child');

        // Lines should populate
        await expect(page.locator('[data-testid="receipt-line"]')).toBeVisible();

        // Enter received qty (full)
        const orderedQty = await page.inputValue('[data-testid="ordered-qty-0"]');
        await page.fill('[data-testid="received-qty-0"]', orderedQty);

        // Select location
        await page.click('[data-testid="location-select"]');
        await page.click('[data-testid="location-option"]:first-child');

        // Save
        await page.click('[data-testid="btn-save"]');
        await expect(page.locator('.toast-success')).toBeVisible();

        // Post
        await page.click('[data-testid="btn-post"]');
        await page.click('[data-testid="btn-confirm-post"]');

        await expect(page.locator('[data-testid="status-badge"]')).toContainText(/posted/i);
    });

    test('SC-GRN-002: Partial Receipt', async ({ page }) => {
        await page.click('[data-testid="btn-new"]');

        await page.click('[data-testid="po-lookup"]');
        await page.click('[data-testid="po-option"]:first-child');

        // Enter partial qty (e.g., 60 of 100)
        await page.fill('[data-testid="received-qty-0"]', '60');

        await page.click('[data-testid="location-select"]');
        await page.click('[data-testid="location-option"]:first-child');

        await page.click('[data-testid="btn-save"]');
        await page.click('[data-testid="btn-post"]');
        await page.click('[data-testid="btn-confirm-post"]');

        // PO should still be open
        await expect(page.locator('.toast-success')).toBeVisible();
    });

    test('SC-GRN-004: Over-Receipt Blocked', async ({ page }) => {
        await page.click('[data-testid="btn-new"]');

        await page.click('[data-testid="po-lookup"]');
        await page.click('[data-testid="po-option"]:first-child');

        // Get open qty and try to exceed
        const openQty = await page.inputValue('[data-testid="open-qty-0"]');
        const overQty = parseInt(openQty) + 10;
        await page.fill('[data-testid="received-qty-0"]', String(overQty));

        await page.click('[data-testid="location-select"]');
        await page.click('[data-testid="location-option"]:first-child');

        await page.click('[data-testid="btn-save"]');
        await page.click('[data-testid="btn-post"]');

        // Should show error
        await expect(page.locator('.toast-error, .validation-error')).toContainText(/exceed|over/i);
    });

    test('SC-GRN-005: Batch Capture at Receipt', async ({ page }) => {
        await page.click('[data-testid="btn-new"]');

        await page.click('[data-testid="po-lookup"]');
        // Select PO with batch-tracked item
        await page.fill('[data-testid="po-search"]', 'BATCH');
        await page.click('[data-testid="po-option"]:first-child');

        // Click batch icon on line
        await page.click('[data-testid="batch-icon-0"]');

        // Enter batch details
        await page.fill('[data-testid="batch-number"]', `BATCH-${Date.now()}`);
        await page.fill('[data-testid="expiry-date"]', '2027-12-31');
        await page.fill('[data-testid="batch-qty"]', '100');
        await page.click('[data-testid="btn-save-batch"]');

        // Continue with receipt
        await page.click('[data-testid="location-select"]');
        await page.click('[data-testid="location-option"]:first-child');

        await page.click('[data-testid="btn-save"]');
        await expect(page.locator('.toast-success')).toBeVisible();
    });

    test('SC-GRN-008: Print GRN', async ({ page }) => {
        // Find posted GRN
        await page.click('[data-testid="filter-status"]');
        await page.click('text=Posted');
        await page.click('[data-testid="grid-row"]:first-child');

        // Click Print
        const [popup] = await Promise.all([
            page.waitForEvent('popup'),
            page.click('[data-testid="btn-print"]'),
        ]);

        await popup.waitForLoadState();
        // Verify print preview opened
        expect(popup.url()).toContain('print');
        await popup.close();
    });
});
