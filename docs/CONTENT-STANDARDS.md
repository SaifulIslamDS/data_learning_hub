# Data Learning Hub — Content Standards

These rules are mandatory for new learning content and for remediation of existing content.

## 1. No dummy learning content

Published learning pages must contain real educational value.

Do not ship:

- Lorem ipsum
- Placeholder sections
- Empty examples
- "Coming soon" presented as complete content
- Generic examples where only the chapter title changes
- Repeated generated worked-example templates across unrelated concepts
- Invented outputs presented as real-world evidence

## 2. Teach the subject directly

Learner-facing pages should focus on the actual topic.

Avoid unnecessary sections such as:

- How to learn SQL
- How to study this chapter
- Your learning journey
- Generic motivational filler
- Hypothetical instructions that replace actual examples

Short orientation text is acceptable only when it materially helps the learner use a tool or exercise.

## 3. Every practical chapter needs a learning contract

Where relevant, a chapter should include:

1. Clear topic title
2. Concise explanation
3. Syntax or tool action
4. Topic-specific worked example
5. Actual input
6. Actual operation, code, formula, or model action
7. Actual output/result
8. Explanation of why the result occurs
9. Immediate practice
10. Result checking or expected output
11. Common mistake/error
12. Short exercises
13. Previous/next navigation
14. Authoritative references

Not every concept needs every block, but practical topics must not omit the real example and practice loop.

## 4. Worked examples must be genuinely worked

A worked example must show enough information for the learner to reproduce it.

### SQL example requirement

Show:

- Table/data context
- Query
- Result table
- Explanation

### Python example requirement

Show:

- Data/input
- Executable code
- Output
- Explanation

### Statistics example requirement

Show:

- Given values/data
- Formula or method
- Calculation
- Numeric result
- Interpretation

### Excel example requirement

Show:

- Workbook/table context
- Formula or action
- Expected result
- Explanation

### Power BI example requirement

Show:

- Data/model context
- Power Query, relationship, visual, or DAX action
- Expected output/KPI
- Explanation

## 5. Practice must be real

Practice can use:

- In-browser execution
- Automatically checked answers
- Real downloadable workbook/notebook/project files
- Honest browser simulations
- Numeric validators
- Hidden tests
- Expected-output comparison

Practice must not be a decorative button that cannot verify or meaningfully support the task.

## 6. Real-data policy

Small controlled teaching datasets are allowed when they make a concept easier to understand.

Serious projects and portfolio work should increasingly use traceable public, licensed, or official datasets.

Every serious dataset should record:

- Dataset name
- Publisher/source
- Original source URL
- License or usage terms
- Snapshot/download date
- Data dictionary
- Modifications/cleaning performed
- Known limitations

Never imply that synthetic business data is a real company or real-world result.

## 7. Dataset reuse is encouraged

Prefer a shared dataset registry that allows the same dataset to support multiple learning tracks.

Example:

```text
Retail dataset
  ├─ Excel cleaning
  ├─ SQL analysis
  ├─ Power BI model
  ├─ Python EDA
  ├─ Statistics exercises
  └─ ML feature preparation
```

This creates continuity across tools.

## 8. Assessment should evaluate work

Multiple-choice questions can reinforce concepts but should not be the only assessment format.

The platform should progressively support:

### SQL
- Query execution
- Result-schema comparison
- Row/value comparison
- Equivalent valid solutions

### Python
- Code execution
- Hidden tests
- DataFrame/result checks

### Statistics
- Numeric tolerance checks
- Interpretation checks

### Excel
- Formula challenges
- Expected-value checks
- Downloadable workbook exercises

### Power BI
- DAX challenges
- Model reasoning
- Expected KPI checks
- Real application practice packages

## 9. Reference quality

Prefer authoritative primary documentation whenever possible.

Examples:

- Microsoft documentation
- Python documentation
- pandas / NumPy / scikit-learn documentation
- PostgreSQL / SQLite / DuckDB documentation
- Official statistical agencies
- World Bank / UN / WHO / government open-data documentation

Secondary sources may be used when they add educational value, but primary sources should anchor technical facts.

## 10. Every chapter should stand on its own

Many users will enter from a search engine.

A topic page should not require the learner to begin at Chapter 1 unless the concept genuinely depends on earlier knowledge.

Required prerequisites should be linked explicitly.

## 11. Bilingual integrity

English and Bangla versions should teach the same concept and produce the same technical result.

Do not let one language become a shortened or stale version of the other.

Code, formulas, function names, field names, and official terminology should remain technically correct in both versions.

## 12. Content quality automation

Future content audits should detect:

- Missing required fields
- Empty examples
- Missing expected outputs
- Missing exercise answers
- Broken internal links
- Broken downloads
- Missing dataset provenance
- Duplicate exercise text
- Near-duplicate worked examples
- Placeholder text
- TODO/FIXME markers in published content
- Missing references
- Orphan chapters
- Invalid previous/next navigation

## 13. Publication rule

A topic is not complete because a route exists.

A topic is complete only when its explanation, example, result, practice, exercises, references, and required assets are complete and validated.
