/**
 * Customer Master E2E Tests
 * Generated from: tests/retail/customers/customer_master_scenarios.md
 * Screen: /partners/customers
 * Component: CustomerMasterSetup.tsx
 */

import { test, expect, Page } from '@playwright/test';

const BASE_URL = process.env.BASE_URL || 'http://localhost:3001';
const CUSTOMER_URL = `${BASE_URL}/partners/customers`;

// Test data
const TEST_CUSTOMER = {
    code: `CUST-${Date.now()}`,
    name: 'Automation Test Customer',
    email: 'test@customer.com',
    phone: '+91-9876543210',
    type: 'Retail',
};

async function login(page: Page) {
    await page.goto(`${BASE_URL}/login`);
    await page.fill('[data-testid="username"]', 'admin');
    await page.fill('[data-testid="password"]', 'admin123');
    await page.click('[data-testid="btn-login"]');
    await page.waitForURL('**/dashboard');
}

async function navigateToCustomer(page: Page) {
    await page.goto(CUSTOMER_URL);
    await page.waitForLoadState('networkidle');
}

test.describe('Customer Master - SC-CUST', () => {
    test.beforeEach(async ({ page }) => {
        await login(page);
        await navigateToCustomer(page);
    });

    test('SC-CUST-001: Create Customer (Happy Path)', async ({ page }) => {
        await page.click('[data-testid="btn-new"]');

        await page.fill('[data-testid="customer-code"]', TEST_CUSTOMER.code);
        await page.fill('[data-testid="customer-name"]', TEST_CUSTOMER.name);
        await page.click('[data-testid="customer-type"]');
        await page.click(`text=${TEST_CUSTOMER.type}`);
        await page.fill('[data-testid="email"]', TEST_CUSTOMER.email);
        await page.fill('[data-testid="phone"]', TEST_CUSTOMER.phone);

        await page.click('[data-testid="btn-save"]');
        await expect(page.locator('.toast-success')).toBeVisible();
    });

    test('SC-CUST-002: Create Intercompany Customer', async ({ page }) => {
        await page.click('[data-testid="btn-new"]');

        await page.fill('[data-testid="customer-code"]', `IC-CUST-${Date.now()}`);
        await page.fill('[data-testid="customer-name"]', 'IC Test Customer');

        await page.click('[data-tab="intercompany"]');
        await page.click('[data-testid="is-intercompany"]');
        await page.click('[data-testid="related-company"]');
        await page.click('[data-testid="company-option"]:first-child');

        await page.click('[data-testid="btn-save"]');
        await expect(page.locator('.toast-success')).toBeVisible();
    });

    test('SC-CUST-003: Edit Customer', async ({ page }) => {
        await page.fill('[data-testid="search-input"]', TEST_CUSTOMER.code);
        await page.press('[data-testid="search-input"]', 'Enter');

        await page.click(`text=${TEST_CUSTOMER.code}`);
        await page.click('[data-testid="btn-edit"]');

        await page.fill('[data-testid="customer-name"]', `${TEST_CUSTOMER.name} Updated`);
        await page.click('[data-testid="btn-save"]');

        await expect(page.locator('.toast-success')).toBeVisible();
    });

    test('SC-CUST-004: Set Credit Limit', async ({ page }) => {
        await page.click('[data-testid="grid-row"]:first-child');
        await page.click('[data-testid="btn-edit"]');

        await page.click('[data-tab="credit"]');
        await page.click('[data-testid="enable-credit"]');
        await page.fill('[data-testid="credit-limit"]', '50000');

        await page.click('[data-testid="btn-save"]');
        await expect(page.locator('.toast-success')).toBeVisible();
    });

    test('SC-CUST-006: Address Management', async ({ page }) => {
        await page.click('[data-testid="grid-row"]:first-child');
        await page.click('[data-testid="btn-edit"]');

        await page.click('[data-tab="addresses"]');
        await page.click('[data-testid="btn-add-address"]');

        await page.fill('[data-testid="address-street"]', '123 Test Street');
        await page.fill('[data-testid="address-city"]', 'Test City');
        await page.fill('[data-testid="address-state"]', 'Test State');
        await page.fill('[data-testid="address-pin"]', '123456');

        await page.click('[data-testid="btn-save"]');
        await expect(page.locator('.toast-success')).toBeVisible();
    });

    test('SC-CUST-007: Duplicate Code Validation', async ({ page }) => {
        await page.click('[data-testid="btn-new"]');
        await page.fill('[data-testid="customer-code"]', 'DUP-CUST-001');
        await page.fill('[data-testid="customer-name"]', 'Dup Test');
        await page.click('[data-testid="btn-save"]');
        await page.waitForTimeout(1000);

        await page.click('[data-testid="btn-new"]');
        await page.fill('[data-testid="customer-code"]', 'DUP-CUST-001');
        await page.fill('[data-testid="customer-name"]', 'Dup Test 2');
        await page.click('[data-testid="btn-save"]');

        await expect(page.locator('.toast-error')).toContainText(/duplicate|exists/i);
    });
});
