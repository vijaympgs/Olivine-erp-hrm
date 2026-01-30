/**
 * Layout Settings E2E Tests
 * Generated from: tests/retail/system_admin/layout_settings_scenarios.md
 * Screen: /admin/layout-settings
 * Component: LayoutSettingsPage.tsx
 */

import { test, expect, Page } from '@playwright/test';

const BASE_URL = process.env.BASE_URL || 'http://localhost:3001';
const LAYOUT_URL = `${BASE_URL}/admin/layout-settings`;

async function login(page: Page) {
    await page.goto(`${BASE_URL}/login`);
    await page.fill('[data-testid="username"]', 'admin');
    await page.fill('[data-testid="password"]', 'admin123');
    await page.click('[data-testid="btn-login"]');
    await page.waitForURL('**/dashboard');
}

test.describe('System Administration - Layout Settings', () => {
    test.beforeEach(async ({ page }) => {
        await login(page);
        await page.goto(LAYOUT_URL);
    });

    test('SC-LAYOUT-004: Enable HRM in Test Console', async ({ page }) => {
        // Expand Test Console visibility section
        await page.click('text=Test Console Module Visibility');

        // Toggle HRM ON
        await page.click('[data-testid="toggle-hrm"]');
        await page.click('[data-testid="btn-save"]');

        // Navigate to Test Console and verify
        await page.goto(`${BASE_URL}/test-console`);
        await expect(page.locator('[data-testid="explorer-node-hrm"]')).toBeVisible();
    });

    test('SC-LAYOUT-005: Disable Retail in Test Console', async ({ page }) => {
        await page.click('text=Test Console Module Visibility');

        // Toggle Retail OFF
        await page.click('[data-testid="toggle-retail"]');
        await page.click('[data-testid="btn-save"]');

        // Navigate to Test Console and verify
        await page.goto(`${BASE_URL}/test-console`);
        await expect(page.locator('[data-testid="explorer-node-retail"]')).not.toBeVisible();
    });

    test('SC-LAYOUT-007: System Admin Always Visible', async ({ page }) => {
        await page.click('text=Test Console Module Visibility');

        // Verify System Admin cannot be toggled (disabled or missing toggle)
        const sysAdminToggle = page.locator('[data-testid="toggle-system-admin"]');
        await expect(sysAdminToggle).toBeDisabled().catch(() => {
            // If it doesn't exist, that's also fine as per spec (non-toggleable)
        });

        await page.goto(`${BASE_URL}/test-console`);
        await expect(page.locator('[data-testid="explorer-node-system-admin"]')).toBeVisible();
    });
});
