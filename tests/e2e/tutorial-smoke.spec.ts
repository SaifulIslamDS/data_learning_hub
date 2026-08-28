import { expect, test } from '@playwright/test';

test('tutorial page follows the tutorial-first standard', async ({ page }) => {
  await page.goto('/tutorials/data-foundations/observations-variables-and-values/');

  await expect(page.getByRole('heading', { level: 1, name: 'Observations, Variables, and Values' })).toBeVisible();
  await expect(page.locator('.tutorial-objectives')).toHaveCount(0);
  await expect(page.locator('a[href="#objectives"]')).toHaveCount(0);
  await expect(page.getByText('What you will learn', { exact: true })).toHaveCount(0);

  await expect(page.locator('.language-switch')).toHaveCount(0);
  await expect(page.locator('[data-lang="bn"]')).toHaveCount(0);

  await expect(page.locator('#concept-1')).toBeVisible();
});

test('theme and primary navigation still work', async ({ page }) => {
  await page.goto('/');

  await expect(page.getByRole('link', { name: 'Tutorials' }).first()).toBeVisible();
  const themeButton = page.locator('[data-action="theme"]').first();
  await expect(themeButton).toBeVisible();

  await themeButton.click();
  await expect(page.locator('html')).toHaveAttribute('data-theme', 'dark');
});
