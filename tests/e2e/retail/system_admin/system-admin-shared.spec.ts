/**
 * System Administration Core E2E Tests
 * Covers: Security, Audit Logs, File Explorer, Backup
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

test.describe('System Administration - Shared Core', () => {
    test.beforeEach(async ({ page }) => {
        await login(page);
    });

    test('FILE-EXPLORER: Search and Preview', async ({ page }) => {
        await page.goto(`${BASE_URL}/admin/file-explorer`);
        await page.fill('[data-testid="file-search-input"]', 'invoice');
        await page.press('[data-testid="file-search-input"]', 'Enter');

        // Verify results
        await expect(page.locator('[data-testid="file-list-item"]')).toBeVisible();
    });

    test('SECURITY: Password Policy Update', async ({ page }) => {
        await page.goto(`${BASE_URL}/admin/security`);
        await page.click('text=Password Policy');
        await page.fill('[data-testid="min-password-length"]', '10');
        await page.click('[data-testid="btn-save-security"]');

        await expect(page.locator('.toast-success')).toBeVisible();
    });

    test('AUDIT: Filter by User', async ({ page }) => {
        await page.goto(`${BASE_URL}/admin/audit-logs`);
        await page.click('[data-testid="filter-user"]');
        await page.click('text=admin');

        await expect(page.locator('table tr')).toContainText('admin');
    });

    test('BACKUP: Create Manual Backup', async ({ page }) => {
        await page.goto(`${BASE_URL}/admin/backup`);
        await page.click('[data-testid="btn-backup-now"]');
        await page.fill('[data-testid="backup-description"]', 'Test E2E Backup');
        await page.click('[data-testid="btn-start-backup"]');

        // Wait for progress (long timeout)
        await expect(page.locator('text=Backup Completed')).toBeVisible({ timeout: 60000 });
    });
});
