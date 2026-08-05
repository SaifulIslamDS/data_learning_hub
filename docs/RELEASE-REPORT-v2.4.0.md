# v2.4.0 Release Report — Complete Power BI for Data Analytics Tutorial

## Release objective

Publish a complete tutorial-first Power BI course while retaining the existing Data Foundations, Excel, SQL, statistics, and platform UX baseline.

## Delivered

- 77 bilingual Power BI chapters
- 9 curriculum modules
- 231 chapter exercises
- 77 worked examples
- 77 browser-side Power BI simulations
- Randomized 30-question final quiz
- Searchable examples and references
- Retail star-schema practice dataset
- DAX measure library
- Power Query M examples
- Project and QA checklist
- Power BI data dictionary

## Footer adjustment

Applied exactly across the shared generated footer:

```html
<div class="footer-bottom-links">
  <a href="/about/">About</a>
</div>
```

Removed the `Inspired by tafshir027/stats` link from the footer-bottom area and replaced `Privacy & credits` with `About`. Credits remain documented outside that footer area.

## Platform totals

| Component | Count |
|---|---:|
| Published tutorials | 4 |
| Tutorial chapters | 220 |
| Chapter exercises | 660 |
| Retained lessons | 108 |
| Statistical labs | 20 |
| Generated HTML pages | 389 |
| Checked local references | 20,367 |
| Broken local references | 0 |

## Practice model

| Table | Rows |
|---|---:|
| DimDate | 730 |
| DimProduct | 12 |
| DimCustomer | 60 |
| DimRegion | 4 |
| FactSales | 360 |
| FactTargets | 96 |

All practice data is synthetic. Automated tests verify keys, dates, row counts, ZIP contents, and gross-profit reconciliation.

## Browser validation

Passed:

- Sticky header
- Four-course tutorial library
- Power BI course/module navigation
- Browser simulation
- Completion state
- EN/BN switching
- Exercises and quiz
- Mobile chapter drawer
- Exact footer behavior
- Existing Data Foundations, Excel, SQL, playground, and statistics regression

## Release boundary

A static site cannot execute Power BI Desktop or publish reports. The course therefore provides complete teaching, code, models, decisions, datasets, and implementation instructions without misrepresenting the browser simulation as Power BI itself.
