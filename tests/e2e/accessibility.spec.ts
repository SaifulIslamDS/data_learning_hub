import AxeBuilder from '@axe-core/playwright';
import { expect, test } from '@playwright/test';

test('offline recovery page has no critical or serious structural accessibility violations', async ({ page }) => {
  await page.goto('/offline/');

  const scan = await new AxeBuilder({ page })
    // Contrast will receive a dedicated design-system review during the native shell migration.
    .disableRules(['color-contrast'])
    .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
    .analyze();

  const blocking = scan.violations.filter((violation) =>
    ['critical', 'serious'].includes(violation.impact ?? ''),
  );

  expect(blocking, JSON.stringify(blocking, null, 2)).toEqual([]);
});
