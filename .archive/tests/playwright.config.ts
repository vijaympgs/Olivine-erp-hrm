/**
 * Playwright Configuration for Olivine Retail E2E Tests
 * 
 * Usage:
 *   npx playwright test                    # Run all tests
 *   npx playwright test --grep "SC-ITEM"   # Run specific scenario
 *   npx playwright test --ui               # Open UI mode
 *   npx playwright test --project=chromium # Run in Chrome only
 */

import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
    // Test directory
    testDir: './tests/e2e',

    // Run tests in parallel
    fullyParallel: true,

    // Fail the build on CI if you accidentally left test.only in the source code
    forbidOnly: !!process.env.CI,

    // Retry on CI only
    retries: process.env.CI ? 2 : 0,

    // Opt out of parallel tests on CI
    workers: process.env.CI ? 1 : undefined,

    // Reporter to use
    reporter: [
        ['list'],
        ['html', { open: 'never', outputFolder: 'playwright-report' }],
        ['json', { outputFile: 'test-results/results.json' }],
    ],

    // Shared settings for all the projects below
    use: {
        // Base URL for navigation
        baseURL: process.env.BASE_URL || 'http://localhost:3001',

        // Collect trace when retrying the failed test
        trace: 'on-first-retry',

        // Take screenshot on failure
        screenshot: 'only-on-failure',

        // Video recording
        video: 'retain-on-failure',

        // Viewport
        viewport: { width: 1920, height: 1080 },

        // Action timeout
        actionTimeout: 10000,

        // Navigation timeout
        navigationTimeout: 30000,
    },

    // Configure projects for major browsers
    projects: [
        {
            name: 'chromium',
            use: { ...devices['Desktop Chrome'] },
        },
        {
            name: 'firefox',
            use: { ...devices['Desktop Firefox'] },
        },
        {
            name: 'webkit',
            use: { ...devices['Desktop Safari'] },
        },
    ],

    // Web server to start before tests
    webServer: {
        command: 'cd frontend && npm run dev',
        url: 'http://localhost:3001',
        reuseExistingServer: true,
        timeout: 120 * 1000,
    },
});
