/**
 * Supplier Master E2E Tests
 * Generated from: tests/retail/masters/supplier_master_scenarios.md
 * Screen: /partners/suppliers
 * Component: SupplierMasterSetup.tsx
 */

import { test, expect, Page } from '@playwright/test';

const BASE_URL = process.env.BASE_URL || 'http://localhost:3001';
const SUPPLIER_URL = `${BASE_URL}/partners/suppliers`;

// Test data
const TEST_SUPPLIER = {
    code: `SUP-${Date.now()}`,
    name: 'Automation Test Supplier',
    email: 'test@supplier.com',
    phone: '+91-9876543210',
    paymentTerms: 'Net 30',
};

async function login(page: Page) {
    await page.goto(`${BASE_URL}/login`);
    await page.fill('[data-testid="username"]', 'admin');
    await page.fill('[data-testid="password"]', 'admin123');
    await page.click('[data-testid="btn-login"]');
    await page.waitForURL('**/dashboard');
}

async function navigateToSupplier(page: Page) {
    await page.goto(SUPPLIER_URL);
    await page.waitForLoadState('networkidle');
}

test.describe('Supplier Master - SC-SUP', () => {
    test.beforeEach(async ({ page }) => {
        await login(page);
        await navigateToSupplier(page);
    });

    test('SC-SUP-001: Create Supplier (Happy Path)', async ({ page }) => {
        // Click New
        await page.click('[data-testid="btn-new"]');

        // Enter details
        await page.fill('[data-testid="supplier-code"]', TEST_SUPPLIER.code);
        await page.fill('[data-testid="supplier-name"]', TEST_SUPPLIER.name);
        await page.click('[data-testid="payment-terms"]');
        await page.click(`text=${TEST_SUPPLIER.paymentTerms}`);
        await page.fill('[data-testid="email"]', TEST_SUPPLIER.email);
        await page.fill('[data-testid="phone"]', TEST_SUPPLIER.phone);

        // Save
        await page.click('[data-testid="btn-save"]');
        await expect(page.locator('.toast-success')).toBeVisible();
    });

    test('SC-SUP-002: Create Intercompany Supplier', async ({ page }) => {
        await page.click('[data-testid="btn-new"]');

        // Basic info
        await page.fill('[data-testid="supplier-code"]', `IC-SUP-${Date.now()}`);
        await page.fill('[data-testid="supplier-name"]', 'IC Test Supplier');

        // IC tab
        await page.click('[data-tab="intercompany"]');
        await page.click('[data-testid="is-intercompany"]'); // Toggle ON
        await page.click('[data-testid="related-company"]');
        await page.click('[data-testid="company-option"]:first-child');

        await page.click('[data-testid="btn-save"]');
        await expect(page.locator('.toast-success')).toBeVisible();
    });

    test('SC-SUP-003: Edit Supplier', async ({ page }) => {
        // Search
        await page.fill('[data-testid="search-input"]', TEST_SUPPLIER.code);
        await page.press('[data-testid="search-input"]', 'Enter');

        // Select and edit
        await page.click(`text=${TEST_SUPPLIER.code}`);
        await page.click('[data-testid="btn-edit"]');

        // Modify
        await page.fill('[data-testid="supplier-name"]', `${TEST_SUPPLIER.name} Updated`);
        await page.click('[data-testid="btn-save"]');

        await expect(page.locator('.toast-success')).toBeVisible();
    });

    test('SC-SUP-004: Duplicate Code Validation', async ({ page }) => {
        // Create first
        await page.click('[data-testid="btn-new"]');
        await page.fill('[data-testid="supplier-code"]', 'DUP-SUP-001');
        await page.fill('[data-testid="supplier-name"]', 'Duplicate Test');
        await page.click('[data-testid="btn-save"]');
        await page.waitForTimeout(1000);

        // Try duplicate
        await page.click('[data-testid="btn-new"]');
        await page.fill('[data-testid="supplier-code"]', 'DUP-SUP-001');
        await page.fill('[data-testid="supplier-name"]', 'Duplicate Test 2');
        await page.click('[data-testid="btn-save"]');

        await expect(page.locator('.toast-error')).toContainText(/duplicate|exists/i);
    });

    test('SC-SUP-005: Required Field Validation', async ({ page }) => {
        await page.click('[data-testid="btn-new"]');
        await page.click('[data-testid="btn-save"]');

        await expect(page.locator('.field-error, [data-error]')).toBeVisible();
    });

    test('SC-SUP-006: Bank Details Tab', async ({ page }) => {
        // Find existing supplier
        await page.click('[data-testid="grid-row"]:first-child');
        await page.click('[data-testid="btn-edit"]');

        // Bank tab
        await page.click('[data-tab="bank"]');
        await page.fill('[data-testid="bank-name"]', 'Test Bank');
        await page.fill('[data-testid="account-number"]', '1234567890');
        await page.fill('[data-testid="ifsc"]', 'TEST0001234');

        await page.click('[data-testid="btn-save"]');
        await expect(page.locator('.toast-success')).toBeVisible();
    });
});
