/**
 * POS Checkout E2E Tests
 * Generated from: tests/retail/pos/pos_checkout_scenarios.md
 * Screen: /pos/ui
 * Component: PosPage.tsx → PosDesktop.tsx
 */

import { test, expect, Page } from '@playwright/test';

const BASE_URL = process.env.BASE_URL || 'http://localhost:3001';
const POS_URL = `${BASE_URL}/pos/ui`;
const DAY_OPEN_URL = `${BASE_URL}/operations/pos/day-open`;
const SESSION_OPEN_URL = `${BASE_URL}/operations/pos/session-open`;

// Test data
const TEST_ITEM = {
    code: 'SKU-001',
    price: 100,
};

const TEST_CUSTOMER = {
    code: 'CUST-001',
    name: 'Test Customer',
};

// Helper functions
async function login(page: Page) {
    await page.goto(`${BASE_URL}/login`);
    await page.fill('[data-testid="username"]', 'cashier');
    await page.fill('[data-testid="password"]', 'cashier123');
    await page.click('[data-testid="btn-login"]');
    await page.waitForURL('**/dashboard');
}

async function ensureDayOpen(page: Page) {
    await page.goto(DAY_OPEN_URL);
    // Check if day already open
    const alreadyOpen = await page.locator('text=already open').isVisible().catch(() => false);
    if (!alreadyOpen) {
        await page.fill('[data-testid="opening-float"]', '5000');
        await page.click('[data-testid="btn-open-day"]');
        await page.waitForTimeout(1000);
    }
}

async function ensureSessionOpen(page: Page) {
    await page.goto(SESSION_OPEN_URL);
    const alreadyOpen = await page.locator('text=session active').isVisible().catch(() => false);
    if (!alreadyOpen) {
        await page.click('[data-testid="terminal-select"]');
        await page.click('[data-testid="terminal-option"]:first-child');
        await page.fill('[data-testid="opening-cash"]', '1000');
        await page.click('[data-testid="btn-start-shift"]');
        await page.waitForTimeout(1000);
    }
}

async function navigateToPOS(page: Page) {
    await page.goto(POS_URL);
    await page.waitForLoadState('networkidle');
}

test.describe('POS Checkout - SC-POS', () => {
    test.beforeEach(async ({ page }) => {
        await login(page);
        await ensureDayOpen(page);
        await ensureSessionOpen(page);
        await navigateToPOS(page);
    });

    test('SC-POS-001: Simple Cash Sale (Happy Path)', async ({ page }) => {
        // Step 2: Search for item
        await page.fill('[data-testid="product-search"]', TEST_ITEM.code);
        await page.press('[data-testid="product-search"]', 'Enter');

        // Step 3: Select item (should auto-add or click)
        await page.click(`[data-testid="search-result-${TEST_ITEM.code}"]`).catch(async () => {
            // Item might auto-add
        });

        // Step 4: Verify cart line
        await expect(page.locator('[data-testid="cart-line"]')).toBeVisible();

        // Step 5: Click Pay
        await page.click('[data-testid="btn-pay"]');

        // Step 6: Verify total
        await expect(page.locator('[data-testid="tender-total"]')).toContainText('100');

        // Step 7: Click Cash tender
        await page.click('[data-tender="CASH"]');

        // Step 8: Enter amount
        await page.fill('[data-testid="cash-amount"]', '100');

        // Step 9: Complete
        await page.click('[data-testid="btn-complete"]');

        // Step 10: Verify receipt/success
        await expect(page.locator('[data-testid="receipt"], .success-message')).toBeVisible();
    });

    test('SC-POS-002: Multiple Items Sale', async ({ page }) => {
        // Add first item
        await page.fill('[data-testid="product-search"]', 'SKU-001');
        await page.press('[data-testid="product-search"]', 'Enter');
        await page.waitForTimeout(500);

        // Add second item
        await page.fill('[data-testid="product-search"]', 'SKU-002');
        await page.press('[data-testid="product-search"]', 'Enter');
        await page.waitForTimeout(500);

        // Verify cart has 2 items
        const lineCount = await page.locator('[data-testid="cart-line"]').count();
        expect(lineCount).toBeGreaterThanOrEqual(2);

        // Complete sale
        await page.click('[data-testid="btn-pay"]');
        await page.click('[data-tender="CASH"]');
        await page.fill('[data-testid="cash-amount"]', '200');
        await page.click('[data-testid="btn-complete"]');
    });

    test('SC-POS-003: Sale with Customer Selection', async ({ page }) => {
        // Step 1: Click Customer button
        await page.click('[data-testid="btn-customer"]');

        // Step 2: Search customer
        await page.fill('[data-testid="customer-search"]', TEST_CUSTOMER.code);
        await page.press('[data-testid="customer-search"]', 'Enter');

        // Step 3: Select customer
        await page.click(`text=${TEST_CUSTOMER.name}`);

        // Step 4: Verify customer in header
        await expect(page.locator('[data-testid="selected-customer"]')).toContainText(TEST_CUSTOMER.name);

        // Continue with sale
        await page.fill('[data-testid="product-search"]', TEST_ITEM.code);
        await page.press('[data-testid="product-search"]', 'Enter');
        await page.click('[data-testid="btn-pay"]');
        await page.click('[data-tender="CASH"]');
        await page.fill('[data-testid="cash-amount"]', '100');
        await page.click('[data-testid="btn-complete"]');
    });

    test('SC-POS-004: Apply Line Discount (Percentage)', async ({ page }) => {
        // Add item
        await page.fill('[data-testid="product-search"]', TEST_ITEM.code);
        await page.press('[data-testid="product-search"]', 'Enter');
        await page.waitForTimeout(500);

        // Select line
        await page.click('[data-testid="cart-line"]:first-child');

        // Click discount
        await page.click('[data-testid="btn-line-discount"]');

        // Enter 10%
        await page.fill('[data-testid="discount-value"]', '10');
        await page.click('[data-testid="btn-apply-discount"]');

        // Verify discounted total (90 instead of 100)
        await expect(page.locator('[data-testid="line-total"]')).toContainText('90');
    });

    test('SC-POS-006: Hold and Recall', async ({ page }) => {
        // Add items
        await page.fill('[data-testid="product-search"]', TEST_ITEM.code);
        await page.press('[data-testid="product-search"]', 'Enter');
        await page.waitForTimeout(500);

        // Hold transaction
        await page.click('[data-testid="btn-hold"]');
        await page.fill('[data-testid="hold-reference"]', 'Customer step out');
        await page.click('[data-testid="btn-confirm-hold"]');

        // Verify cart cleared
        await expect(page.locator('[data-testid="cart-line"]')).toHaveCount(0);

        // Recall
        await page.click('[data-testid="btn-recall"]');
        await page.click('[data-testid="held-transaction"]:first-child');

        // Verify cart restored
        await expect(page.locator('[data-testid="cart-line"]')).toBeVisible();
    });

    test('SC-POS-007: Void Line Item', async ({ page }) => {
        // Add 2 items
        await page.fill('[data-testid="product-search"]', 'SKU-001');
        await page.press('[data-testid="product-search"]', 'Enter');
        await page.waitForTimeout(300);
        await page.fill('[data-testid="product-search"]', 'SKU-002');
        await page.press('[data-testid="product-search"]', 'Enter');
        await page.waitForTimeout(300);

        // Verify 2 lines
        expect(await page.locator('[data-testid="cart-line"]').count()).toBe(2);

        // Remove first line
        await page.click('[data-testid="cart-line"]:first-child');
        await page.click('[data-testid="btn-remove-line"]');

        // Verify 1 line
        expect(await page.locator('[data-testid="cart-line"]').count()).toBe(1);
    });

    test('SC-POS-008: Void Entire Transaction', async ({ page }) => {
        // Add item
        await page.fill('[data-testid="product-search"]', TEST_ITEM.code);
        await page.press('[data-testid="product-search"]', 'Enter');
        await page.waitForTimeout(500);

        // Cancel sale
        await page.click('[data-testid="btn-cancel-sale"]');
        await page.fill('[data-testid="cancel-reason"]', 'Customer changed mind');
        await page.click('[data-testid="btn-confirm-cancel"]');

        // Verify cart empty
        await expect(page.locator('[data-testid="cart-line"]')).toHaveCount(0);
    });

    test('SC-POS-012: Item Not Found', async ({ page }) => {
        // Search invalid
        await page.fill('[data-testid="product-search"]', 'INVALID-SKU-XYZ');
        await page.press('[data-testid="product-search"]', 'Enter');

        // Verify no results message
        await expect(page.locator('text=/no.*found/i, [data-testid="no-results"]')).toBeVisible();
    });
});
