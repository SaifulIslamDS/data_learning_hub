# v2.1.0 Release Report — Tutorial Platform Core and Complete Data Foundations

## Objective

Convert Data Learning Hub from a roadmap-led learning system into a self-contained tutorial platform where users can learn directly from sequential chapters, examples, activities, exercises, and assessment.

## Product outcome

The primary experience is now:

```text
Tutorials → Subject → Chapter → Example → Try It → Exercises → Next Chapter
```

No onboarding or study-plan setup is required to start learning.

## Delivered tutorial

**Data Foundations Tutorial** contains:

- 21 complete English/Bangla chapters
- 84 learning objectives
- 63+ topic-specific teaching sections
- 84+ key terms
- 21 worked examples
- 21 interactive activities
- 63 chapter exercises
- 30-question randomized final quiz
- Mini project using the shared retail dataset

## Platform components

- Tutorial library
- Course contents page
- Persistent desktop chapter sidebar
- Searchable mobile chapter drawer
- Previous and next chapter navigation
- Chapter completion tracking
- Complete exercise library
- Example library
- Reference and course glossary library
- Final quiz and browser-local score
- Print-friendly chapter output
- Tutorial chapter inclusion in global search

## Architecture

Tutorial source is separated under `content/tutorials/`. `scripts/tutorial_generator.py` generates all course, chapter, exercise, quiz, example, and reference pages. The deployed output remains ordinary static HTML, CSS, and Vanilla JavaScript.

## Compatibility

The release preserves:

- 108 existing comprehensive lessons
- 20 statistical laboratories
- Existing topic and lab URLs
- Datasets and projects
- Guided learning dashboard
- Language and theme preferences
- Bookmark and completion data
- v1-to-v2 storage migration

## Validation

```text
170 HTML pages
2,233 local HTML and asset references
0 broken local references
21/21 tutorial chapters validated
63/63 exercises validated
Statistical tests passed
JavaScript syntax checks passed
Browser smoke test passed
```

## Publication boundary

Data Foundations is the only complete tutorial published in v2.1.0. Statistics remains a comprehensive lesson library. Excel, SQL, Power BI, and Python remain curriculum-ready until their complete tutorial releases.

## Next release

**v2.2.0 — Complete Excel for Data Analytics Tutorial**
