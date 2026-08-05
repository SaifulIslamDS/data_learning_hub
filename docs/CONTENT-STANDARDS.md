# Content and Accuracy Standards — v2.5.0

## Teaching style

- English first with full Bangla support
- Define technical terms before depending on them
- Use plain language without removing necessary precision
- Connect every topic to a practical analyst scenario
- Separate concept, implementation, validation, interpretation, and limitation

## Python baseline

- Teach stable Python 3.14 behavior.
- Use official Python, NumPy, pandas, Matplotlib, SciPy, Jupyter, and Pyodide documentation as primary references.
- Keep Python names, code, functions, methods, exceptions, package names, and field names in their official form in both languages.
- Explain version-sensitive behavior rather than presenting it as timeless syntax.
- Distinguish local Python/Jupyter workflows from browser-side Pyodide execution.

## Code standards

- Every example must run independently or state its prerequisite state.
- Preserve raw input data and create transformed outputs separately.
- Use explicit imports and descriptive names.
- Define row grain, units, assumptions, and expected output.
- Validate types, missing values, row counts, keys, totals, boundaries, and analytical assumptions where relevant.
- Avoid hidden state, unexplained magic values, destructive file changes, and unsupported causal claims.
- Examples must not require secrets, private credentials, or user data.

## Browser execution honesty

Pyodide provides browser-side CPython and selected packages. The site must explain that:

- The first run downloads a WebAssembly runtime and requested packages.
- Browser execution has memory, performance, package, filesystem, and concurrency constraints.
- It is suitable for learning and small analytical examples, not a replacement for every local or production Python environment.
- Learner code and supplied datasets remain local to the browser in this implementation.

## Practice data

- Use synthetic data only.
- Document grain, keys, types, units, and calculations.
- Include deliberately messy data only when the exercise identifies its purpose.
- Reconcile calculated revenue, cost, profit, and margin fields.

## Accessibility

Tutorial pages, editors, outputs, plots, forms, tables, language controls, theme controls, and navigation must remain keyboard accessible, responsive, and usable in light and dark themes.
