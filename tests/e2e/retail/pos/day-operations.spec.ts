/**
 * POS Day Operations E2E Tests
 * Generated from: tests/retail/pos/*_scenarios.md
 * Screens: Day Open, Session Open, Session Close, Day Close
 */

import { test, expect, Page } from '@playwright/test';

const BASE_URL = process.env.BASE_URL || 'http://localhost:3001';

async function login(page: Page) {
    await page.goto(`${BASE_URL}/login`);
    await page.fill('[data-testid="username"]', 'cashier');
    await page.fill('[data-testid="password"]', 'cashier123');
    await page.click('[data-testid="btn-login"]');
    await page.waitForURL('**/dashboard');
}

test.describe('POS Day Operations', () => {
    test.beforeEach(async ({ page }) => {
        await login(page);
    });

    test.describe('Day Open - SC-DAYOPEN', () => {
        test('SC-DAYOPEN-001: Open Day (Happy Path)', async ({ page }) => {
            await page.goto(`${BASE_URL}/operations/pos/day-open`);

            // Verify date
            const dateValue = await page.inputValue('[data-testid="business-date"]');
            expect(dateValue).toBeTruthy();

            // Enter opening float
            await page.fill('[data-testid="opening-float"]', '5000');

            // Open day
            await page.click('[data-testid="btn-open-day"]');

            await expect(page.locator('.toast-success, [data-status="open"]')).toBeVisible();
        });

        test('SC-DAYOPEN-004: Opening Float Validation', async ({ page }) => {
            await page.goto(`${BASE_URL}/operations/pos/day-open`);

            // Enter negative
            await page.fill('[data-testid="opening-float"]', '-100');
            await page.click('[data-testid="btn-open-day"]');

            await expect(page.locator('.validation-error, .toast-error')).toBeVisible();
        });
    });

    test.describe('Session Open - SC-SESSION', () => {
        test('SC-SESSION-001: Start Shift (Happy Path)', async ({ page }) => {
            // Ensure day is open first
            await page.goto(`${BASE_URL}/operations/pos/day-open`);
            const alreadyOpen = await page.locator('text=already open').isVisible().catch(() => false);
            if (!alreadyOpen) {
                await page.fill('[data-testid="opening-float"]', '5000');
                await page.click('[data-testid="btn-open-day"]');
                await page.waitForTimeout(1000);
            }

            await page.goto(`${BASE_URL}/operations/pos/session-open`);

            // Select terminal
            await page.click('[data-testid="terminal-select"]');
            await page.click('[data-testid="terminal-option"]:first-child');

            // Enter opening cash
            await page.fill('[data-testid="opening-cash"]', '1000');

            // Start shift
            await page.click('[data-testid="btn-start-shift"]');

            // Should redirect to POS or show success
            await expect(page).toHaveURL(/pos|checkout|success/);
        });

        test('SC-SESSION-002: Cannot Start Without Day Open', async ({ page }) => {
            // Navigate directly without day open
            await page.goto(`${BASE_URL}/operations/pos/session-open`);

            // Should see error or redirect
            const hasError = await page.locator('text=/day.*open|open.*day/i').isVisible().catch(() => false);
            const redirected = page.url().includes('day-open');

            expect(hasError || redirected).toBeTruthy();
        });
    });

    test.describe('Session Close - SC-SESSCLOSE', () => {
        test('SC-SESSCLOSE-001: Close Shift (Happy Path)', async ({ page }) => {
            await page.goto(`${BASE_URL}/operations/pos/session-close`);

            // View summary
            await expect(page.locator('[data-testid="session-summary"]')).toBeVisible();

            // Enter counted cash
            await page.fill('[data-testid="counted-cash"]', '15000');

            // Close shift
            await page.click('[data-testid="btn-close-shift"]');

            await expect(page.locator('.toast-success')).toBeVisible();
        });

        test('SC-SESSCLOSE-002: Variance Over Threshold', async ({ page }) => {
            await page.goto(`${BASE_URL}/operations/pos/session-close`);

            // Get expected and enter different amount
            const expected = await page.inputValue('[data-testid="expected-cash"]').catch(() => '10000');
            const shortAmount = parseInt(expected) - 1000;
            await page.fill('[data-testid="counted-cash"]', String(shortAmount));

            // Check if variance shown
            await expect(page.locator('[data-testid="variance"]')).toBeVisible();
        });
    });

    test.describe('Day Close - SC-DAYCLOSE', () => {
        test('SC-DAYCLOSE-001: Close Day (Happy Path)', async ({ page }) => {
            await page.goto(`${BASE_URL}/operations/pos/day-close`);

            // View summary
            await expect(page.locator('[data-testid="day-summary"]')).toBeVisible();

            // Close day
            await page.click('[data-testid="btn-close-day"]');

            // May need confirmation
            const confirmBtn = page.locator('[data-testid="btn-confirm"]');
            if (await confirmBtn.isVisible()) {
                await confirmBtn.click();
            }

            await expect(page.locator('.toast-success, [data-status="closed"]')).toBeVisible();
        });

        test('SC-DAYCLOSE-002: Cannot Close With Open Sessions', async ({ page }) => {
            // This assumes a session is still open
            await page.goto(`${BASE_URL}/operations/pos/day-close`);

            await page.click('[data-testid="btn-close-day"]');

            // Should show error about open sessions
            const hasSessionError = await page.locator('text=/session.*open|close.*session/i').isVisible();
            // Or button should be disabled
            const btnDisabled = await page.locator('[data-testid="btn-close-day"]').isDisabled().catch(() => false);

            expect(hasSessionError || btnDisabled).toBeTruthy();
        });
    });
});
