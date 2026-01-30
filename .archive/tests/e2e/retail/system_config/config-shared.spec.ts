/**
 * System Configuration E2E Tests
 * Covers: Company, Location, Fiscal, Currency, Tax
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

test.describe('System Configuration', () => {
    test.beforeEach(async ({ page }) => {
        await login(page);
    });

    test('COMPANY: Update Profile', async ({ page }) => {
        await page.goto(`${BASE_URL}/config/company`);
        await page.click('[data-testid="btn-edit-company"]');
        await page.fill('[data-testid="company-name"]', 'Updated Olivine Retail');
        await page.click('[data-testid="btn-save-company"]');

        await expect(page.locator('.toast-success')).toBeVisible();
    });

    test('LOCATION: Create New Warehouse', async ({ page }) => {
        await page.goto(`${BASE_URL}/config/locations`);
        await page.click('[data-testid="btn-new-location"]');
        await page.fill('[data-testid="location-code"]', `WH-${Date.now()}`);
        await page.fill('[data-testid="location-name"]', 'North Warehouse');
        await page.click('[data-testid="location-type-select"]');
        await page.click('text=Warehouse');
        await page.click('[data-testid="btn-save-location"]');

        await expect(page.locator('.toast-success')).toBeVisible();
    });

    test('FISCAL: Open New Period', async ({ page }) => {
        await page.goto(`${BASE_URL}/config/fiscal-periods`);
        // Find a closed period
        await page.click('text=Closed');
        await page.click('[data-testid="btn-open-period"]');
        await page.click('[data-testid="btn-confirm-open"]');

        await expect(page.locator('text=Open')).toBeVisible();
    });

    test('CURRENCY: Add USD and Set Rate', async ({ page }) => {
        await page.goto(`${BASE_URL}/config/currencies`);
        await page.click('[data-testid="btn-add-currency"]');
        await page.fill('[data-testid="currency-code"]', 'USD');
        await page.fill('[data-testid="currency-name"]', 'US Dollar');
        await page.click('[data-testid="btn-save-currency"]');

        // Add rate
        await page.click('text=Exchange Rates');
        await page.click('[data-testid="btn-add-rate"]');
        await page.fill('[data-testid="exchange-rate"]', '83.50');
        await page.click('[data-testid="btn-save-rate"]');

        await expect(page.locator('.toast-success')).toBeVisible();
    });

    test('TAX: Create 18% GST Code', async ({ page }) => {
        await page.goto(`${BASE_URL}/config/taxes`);
        await page.click('[data-testid="btn-add-tax"]');
        await page.fill('[data-testid="tax-code"]', 'GST18');
        await page.fill('[data-testid="tax-rate"]', '18');
        await page.click('[data-testid="tax-type-select"]');
        await page.click('text=GST');
        await page.click('[data-testid="btn-save-tax"]');

        await expect(page.locator('.toast-success')).toBeVisible();
    });
});
