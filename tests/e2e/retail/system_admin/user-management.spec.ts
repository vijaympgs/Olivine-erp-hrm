/**
 * User Management E2E Tests
 * Generated from: tests/retail/system_admin/user_management_scenarios.md
 * Screen: /admin/users
 * Component: UserManagementPage.tsx
 */

import { test, expect, Page } from '@playwright/test';

const BASE_URL = process.env.BASE_URL || 'http://localhost:3001';
const USERS_URL = `${BASE_URL}/admin/users`;

async function login(page: Page) {
    await page.goto(`${BASE_URL}/login`);
    await page.fill('[data-testid="username"]', 'admin');
    await page.fill('[data-testid="password"]', 'admin123');
    await page.click('[data-testid="btn-login"]');
    await page.waitForURL('**/dashboard');
}

test.describe('System Administration - User Management', () => {
    test.beforeEach(async ({ page }) => {
        await login(page);
        await page.goto(USERS_URL);
    });

    test('SC-USRMGT-001: View User List', async ({ page }) => {
        await expect(page.locator('h1, [data-testid="page-title"]')).toContainText(/User/i);
        await expect(page.locator('table, [data-testid="user-grid"]')).toBeVisible();
    });

    test('SC-USRMGT-002: Create User (Happy Path)', async ({ page }) => {
        const username = `test_${Date.now()}`;
        await page.click('[data-testid="btn-new"]');
        await page.fill('[data-testid="username"]', username);
        await page.fill('[data-testid="first-name"]', 'Test');
        await page.fill('[data-testid="last-name"]', 'User');
        await page.fill('[data-testid="email"]', `${username}@olivine.com`);
        await page.click('[data-testid="role-select"]');
        await page.click('text=Cashier');
        await page.fill('[data-testid="password"]', 'SecurePass123!');
        await page.fill('[data-testid="confirm-password"]', 'SecurePass123!');
        await page.click('[data-testid="btn-save"]');

        await expect(page.locator('.toast-success, [role="alert"]')).toBeVisible();
    });

    test('SC-USRMGT-009: Reset Password', async ({ page }) => {
        // Select first user
        await page.click('[data-testid="user-row"]:first-child');
        await page.click('[data-testid="btn-reset-password"]');
        await page.fill('[data-testid="new-password"]', 'NewSecurePass123!');
        await page.fill('[data-testid="confirm-new-password"]', 'NewSecurePass123!');
        await page.click('[data-testid="btn-confirm-reset"]');

        await expect(page.locator('.toast-success')).toBeVisible();
    });

    test('SC-USRMGT-013: Password Complexity Validation', async ({ page }) => {
        await page.click('[data-testid="btn-new"]');
        await page.fill('[data-testid="password"]', '123');
        await page.click('[data-testid="btn-save"]');
        await expect(page.locator('.field-error, [data-testid="password-error"]')).toBeVisible();
    });
});
