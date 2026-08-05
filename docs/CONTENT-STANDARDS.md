# Content and Accuracy Standards — v2.4.0

## Teaching style

- English first with full Bangla support
- Define technical terms before depending on them
- Use plain language without removing necessary precision
- Connect every topic to a practical analyst scenario
- Separate concept, implementation, validation, interpretation, and limitation

## Power BI terminology

- Use current Microsoft terminology, including **semantic model** where appropriate
- Distinguish Power BI Desktop, Power BI service, reports, dashboards, apps, workspaces, and semantic models
- Distinguish Power Query transformations, semantic-model relationships, DAX calculations, report interactions, and service governance
- Keep DAX, M, field names, commands, and product labels in their official form in both languages

## Implementation honesty

The browser-side Power BI simulator teaches decisions and calculations. It must never imply that a static webpage can execute or publish a real `.pbix` report.

## Sources

Power BI chapter references must use official Microsoft Learn pages. Version-sensitive behavior should be verified against current Microsoft documentation before content changes are published.

## Practice data

- Use synthetic data only
- Document grain, keys, types, relationships, and calculations
- Reconcile `GrossProfit = Revenue - Cost`
- Ensure fact-table foreign keys resolve to dimensions
- Ensure relevant fact dates exist in `DimDate`

## Accessibility

Tutorial pages, activities, forms, tables, language controls, theme controls, and navigation must remain keyboard accessible, responsive, and usable in both light and dark themes.
