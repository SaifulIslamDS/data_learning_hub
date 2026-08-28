import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const errors = [];

const read = (file) => fs.readFileSync(path.join(root, file), 'utf8');

const site = read('public/assets/js/site.js');
if (site.includes('function languageSwitch')) {
  errors.push('Bangla/language toggle renderer is still present in public/assets/js/site.js');
}
if (site.includes('language-button')) {
  errors.push('Language toggle button wiring is still present in public/assets/js/site.js');
}
if (/data-lang=["']bn["']/.test(site)) {
  errors.push('A visible Bangla toggle button is still present in public/assets/js/site.js');
}

const generator = read('scripts/legacy/tutorial_generator.py');
if (generator.includes('tutorial-objectives')) {
  errors.push('Legacy tutorial generator still renders the generic tutorial-objectives card');
}
if (generator.includes('href="#objectives"')) {
  errors.push('Legacy tutorial generator still renders the Objectives jump link');
}

const renderer = read('src/components/legacy-page.tsx');
if (!renderer.includes('prepareTutorialHtml')) {
  errors.push('LegacyPage is not using the tutorial-first HTML normalizer');
}

if (errors.length) {
  console.error(errors.join('\n'));
  process.exit(1);
}

console.log('Tutorial-first UI audit passed: objective card removed and Bangla toggle disabled.');
