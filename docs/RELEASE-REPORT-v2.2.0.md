# v2.2.0 Release Report — Complete Excel for Data Analytics Tutorial

## Objective

Publish a complete, tutorial-first Excel course for aspiring Data Analysts and make the shared header sticky across every route.

## Delivered

### Global UI adjustment

The generated `#site-header` container is sticky on all routes. The visible header uses a persistent surface, border, backdrop blur, and scrolled shadow. Browser tests verify its viewport position before and after scrolling on the homepage, Excel tutorial pages, Data Foundations pages, and retained statistical-lab pages.

### Complete Excel tutorial

- 56 sequential chapters
- 8 course modules
- 224 learning objectives
- 168 substantive teaching sections
- 224 key terms
- 56 worked examples
- 56 interactive activities
- 168 chapter exercises
- randomized 30-question final quiz
- complete examples and reference libraries
- module-aware desktop sidebar and mobile drawer
- chapter completion stored locally

### Curriculum coverage

Workbook foundations; data entry and control; formulas and references; core, conditional, logical, text, date, lookup, and dynamic-array functions; conditional formatting; descriptive statistics; correlation/trend functions; What-If Analysis; PivotTables; slicers; charts; dashboards; Power Query; Data Model; Power Pivot/DAX foundations; Analysis ToolPak; auditing; performance; sharing; and a two-part retail-sales project.

### Practice assets

`assets/downloads/excel-analytics-practice-workbook.xlsx` includes:

- Read_Me
- Raw_Sales
- Lookup_Tables
- Formula_Practice
- Cleaning_Practice
- Pivot_Practice
- Dashboard_Brief
- Answer_Guide

The course also links the synthetic retail-sales CSV and its data dictionary.

### Multi-course resource architecture

Tutorials, Exercises, Examples, Quiz, and References now have subject-level index pages. Navigation no longer assumes Data Foundations is the only published course.

## Preserved

- 21-chapter Data Foundations tutorial
- 108 retained comprehensive lessons
- 20 retained statistical labs
- datasets, projects, career paths, curriculum maps
- EN/BN switching, theme, bookmarks, progress, migration
- static Netlify deployment

## Validation baseline

```text
2 published tutorials
77 complete tutorial chapters
231 chapter exercises
108 retained lessons
20 retained labs
235 generated HTML files
6,704 local references checked
0 broken local references
```

All statistical tests, tutorial audits, curriculum audits, link audits, JavaScript syntax checks, workbook checks, and browser smoke tests pass.

## Release boundary

SQL, Power BI, and Python remain curriculum-ready and are not represented as complete tutorial content.

## Next release

**v2.3.0 — Complete SQL for Data Analytics Tutorial**
