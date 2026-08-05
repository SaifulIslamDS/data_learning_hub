from __future__ import annotations

import csv
import json
import random
import textwrap
import zipfile
from datetime import date, timedelta
from pathlib import Path

import nbformat as nbf

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'content/tutorials/python_data_analytics.json'
DL = ROOT / 'assets/downloads'
DS = ROOT / 'assets/datasets'
PY_DIR = DS / 'python_retail_project'
DL.mkdir(parents=True, exist_ok=True)
DS.mkdir(parents=True, exist_ok=True)
PY_DIR.mkdir(parents=True, exist_ok=True)

PYTHON = 'https://docs.python.org/3/'
NUMPY = 'https://numpy.org/doc/stable/'
PANDAS = 'https://pandas.pydata.org/docs/'
MATPLOTLIB = 'https://matplotlib.org/stable/'
SCIPY = 'https://docs.scipy.org/doc/scipy/'
JUPYTER = 'https://jupyter.org/'
PYODIDE = 'https://pyodide.org/en/stable/'

modules = [
    {'id':'01','title_en':'Python and Notebook Workflow','title_bn':'Python ও Notebook Workflow'},
    {'id':'02','title_en':'Python Language Foundations','title_bn':'Python Language Foundation'},
    {'id':'03','title_en':'NumPy for Numerical Analysis','title_bn':'Numerical Analysis-এর জন্য NumPy'},
    {'id':'04','title_en':'pandas DataFrame Foundations','title_bn':'pandas DataFrame Foundation'},
    {'id':'05','title_en':'Data Cleaning and Transformation','title_bn':'Data Cleaning ও Transformation'},
    {'id':'06','title_en':'Exploratory Analysis and Statistics','title_bn':'Exploratory Analysis ও Statistics'},
    {'id':'07','title_en':'Visualization with Matplotlib','title_bn':'Matplotlib দিয়ে Visualization'},
    {'id':'08','title_en':'Time Series, Reproducibility, and Delivery','title_bn':'Time Series, Reproducibility ও Delivery'},
    {'id':'09','title_en':'Python Analytics Portfolio Project','title_bn':'Python Analytics Portfolio Project'},
]

S: list[dict] = []
def add(id,module,title,bn,concept,use,code,terms,level='Beginner',packages=None,fill=None):
    S.append(dict(id=id,module=module,title=title,bn=bn,concept=concept,use=use,code=textwrap.dedent(code).strip(),terms=terms,level=level,packages=packages or [],fill=fill or terms[0][0]))

# 01 — workflow
add('welcome-to-python-analytics','01','Welcome to Python for Data Analytics','Data Analytics-এর জন্য Python-এ স্বাগতম','Python is a general-purpose programming language that analysts use to automate repeatable data work, inspect large datasets, apply statistical methods, and create reproducible outputs.','Use Python when the analysis must be repeatable, reviewable, or too complex for a manual spreadsheet workflow.',"""
print('Question → Load → Inspect → Clean → Analyze → Visualize → Validate → Communicate')
""",[('Python','A general-purpose programming language.'),('Script','A saved file containing executable Python code.'),('Reproducibility','Ability to rerun an analysis and obtain the same result.'),('Workflow','Ordered steps used to complete an analytical task.')])
add('install-python-and-create-environment','01','Install Python and Create an Environment','Python Install ও Environment তৈরি','A Python environment isolates the interpreter and packages used by one project. The course baseline is stable Python 3.14, while most examples remain compatible with recent Python 3 releases.','Record the Python and package versions used for an analysis so another reviewer can recreate it.',"""
import sys, platform
print('Python:', sys.version.split()[0])
print('Platform:', platform.system())
""",[('Interpreter','Program that executes Python code.'),('Environment','Isolated collection of Python and packages.'),('Package','Installable Python library.'),('Version','Specific release of a tool or library.')])
add('jupyter-notebooks-and-cells','01','Jupyter Notebooks and Cells','Jupyter Notebook ও Cell','A Jupyter notebook combines narrative text, executable code, and output in an ordered document. Cell execution order matters because notebook state can differ from visual order.','Use notebooks for exploration and explanation, but restart and run all cells before delivery to prove reproducibility.',"""
message = 'A notebook contains code, explanation, and output.'
print(message)
""",[('Notebook','JSON-based computational document.'),('Code cell','Cell that executes code.'),('Markdown cell','Cell containing formatted narrative text.'),('Kernel','Process that runs notebook code.')])
add('python-scripts-and-project-folders','01','Python Scripts and Project Folders','Python Script ও Project Folder','A script is a `.py` file executed from top to bottom. A clear project structure separates source data, notebooks, reusable code, outputs, and documentation.','Move stable logic from exploratory notebooks into scripts or functions so it can be reused and tested.',"""
from pathlib import Path
folders = ['data/raw','data/processed','notebooks','src','outputs']
for folder in folders:
    print(Path(folder))
""",[('Module','Python file that can be imported.'),('Project root','Top-level folder of a project.'),('Raw data','Original source data preserved unchanged.'),('Output','Generated table, chart, file, or report.')])
add('install-and-import-packages','01','Install and Import Packages','Package Install ও Import','Python packages extend the language. Analysts commonly use NumPy for arrays, pandas for tabular data, Matplotlib for visualization, and SciPy for scientific and statistical routines.','Pin or record package versions and import only the libraries required by the project.',"""
import numpy as np
import pandas as pd
print('NumPy:', np.__version__)
print('pandas:', pd.__version__)
""",[('pip','Standard Python package installer.'),('Import','Statement that makes a module available.'),('Alias','Short name assigned during import.'),('Dependency','Package required by another project or package.')],packages=['numpy','pandas'])
add('read-errors-and-tracebacks','01','Read Errors and Tracebacks','Error ও Traceback পড়ুন','A traceback records where an exception occurred and the chain of calls that led to it. Reading the final exception type and message is usually the fastest starting point.','Debug from the bottom of the traceback, reproduce the problem with a small input, and change one cause at a time.',"""
try:
    int('not-a-number')
except ValueError as error:
    print(type(error).__name__)
    print(error)
""",[('Exception','Runtime event indicating an error.'),('Traceback','Report showing the call path to an exception.'),('ValueError','Exception raised for an invalid value.'),('Debugging','Systematic process of finding and correcting defects.')])
add('comments-docstrings-and-style','01','Comments, Docstrings, and Readable Style','Comment, Docstring ও Readable Style','Readable analytical code uses descriptive names, small functions, consistent formatting, comments for reasoning, and docstrings for reusable interfaces.','Write code for the next reviewer, not only for the current author.',"""
def net_revenue(gross: float, discount: float) -> float:
    # Return revenue after a proportional discount.
    return gross * (1 - discount)

print(net_revenue(1000, 0.10))
""",[('Comment','Non-executed note beginning with `#`.'),('Docstring','String documenting a module, class, or function.'),('Style guide','Shared conventions for readable code.'),('Type hint','Annotation describing an expected type.')])
add('first-analytical-program','01','Build Your First Analytical Program','প্রথম Analytical Program তৈরি','A useful first program takes a small set of values, computes a transparent metric, and prints an interpretation with units and limitations.','Separate input, calculation, validation, and communication even in a small script.',"""
sales = [1200, 1450, 1325, 1600, 1750]
average = sum(sales) / len(sales)
print(f'Average daily sales: BDT {average:,.2f}')
print('Limitation: only five days are included.')
""",[('Input','Data supplied to a program.'),('Calculation','Rule used to transform input into a result.'),('Validation','Check that the result is reasonable.'),('Interpretation','Plain-language meaning of a result.')])

# 02 — language foundations
add('variables-and-assignment','02','Variables and Assignment','Variable ও Assignment','A variable binds a name to an object. Assignment does not create a permanent spreadsheet cell; it makes a name refer to a value in the current program state.','Use descriptive snake_case names and avoid overwriting names with unrelated meanings.',"""
monthly_revenue = 125000
currency = 'BDT'
print(monthly_revenue, currency)
""",[('Variable','Name referring to an object.'),('Assignment','Binding a name to a value.'),('Object','Value stored and manipulated by Python.'),('snake_case','Naming style using lowercase words and underscores.')])
add('numbers-booleans-and-none','02','Numbers, Booleans, and None','Number, Boolean ও None','Python represents whole numbers with `int`, decimal numbers with `float`, logical values with `bool`, and absence with `None`.','Check types when importing or calculating because text that looks numeric will not behave like a number.',"""
values = [42, 12.5, True, None]
for value in values:
    print(repr(value), type(value).__name__)
""",[('int','Integer number type.'),('float','Floating-point number type.'),('bool','Logical True or False type.'),('None','Singleton representing no value.')])
add('strings-and-formatting','02','Strings and Formatting','String ও Formatting','Strings store text. Analysts clean, compare, split, normalize, and format strings when working with categories, identifiers, and report text.','Preserve identifiers such as postal codes as text and use formatted strings for readable outputs.',"""
region = 'dhaka '
clean = region.strip().title()
revenue = 125430.5
print(f'{clean}: BDT {revenue:,.2f}')
""",[('String','Sequence of Unicode characters.'),('Method','Function attached to an object.'),('f-string','Formatted string literal.'),('Whitespace','Spaces, tabs, and line breaks.')])
add('lists-and-sequences','02','Lists and Sequences','List ও Sequence','A list is an ordered, mutable collection. Lists are useful for small collections, but tabular analytics usually belongs in NumPy arrays or pandas objects.','Use indexing and slicing carefully and remember that Python positions start at zero.',"""
sales = [1200, 1450, 1325, 1600]
print(sales[0])
print(sales[-1])
print(sales[1:3])
""",[('List','Ordered mutable collection.'),('Index','Position used to access an item.'),('Slice','Selected range of a sequence.'),('Mutable','Able to change after creation.')])
add('tuples-and-unpacking','02','Tuples and Unpacking','Tuple ও Unpacking','A tuple is an ordered immutable collection. Unpacking assigns its elements to multiple names and is useful for fixed records or function returns.','Use tuples when the group should not be changed accidentally.',"""
record = ('Dhaka', 125000, 0.18)
region, revenue, margin = record
print(region, revenue, margin)
""",[('Tuple','Ordered immutable collection.'),('Unpacking','Assigning sequence items to separate names.'),('Immutable','Unable to change in place.'),('Record','Related values describing one entity or event.')])
add('dictionaries-and-key-value-data','02','Dictionaries and Key-Value Data','Dictionary ও Key-Value Data','A dictionary maps unique keys to values. It resembles a labeled record and is widely used for configuration, JSON-like data, and lookup logic.','Use stable descriptive keys and handle missing keys intentionally.',"""
metric = {'name':'Revenue','value':125000,'currency':'BDT'}
print(metric['name'])
print(metric.get('owner', 'Not assigned'))
""",[('Dictionary','Mapping of keys to values.'),('Key','Unique label in a mapping.'),('Value','Object associated with a key.'),('get','Method that can return a default for a missing key.')])
add('sets-and-unique-values','02','Sets and Unique Values','Set ও Unique Value','A set stores unique unordered values and supports membership, union, intersection, and difference operations.','Use sets for uniqueness checks and category comparisons, not when order or duplicates must be preserved.',"""
expected = {'Dhaka','Khulna','Rajshahi'}
observed = {'Dhaka','Khulna','Sylhet'}
print('Unexpected:', observed - expected)
print('Missing:', expected - observed)
""",[('Set','Unordered collection of unique values.'),('Membership','Whether an item exists in a collection.'),('Union','All values from two sets.'),('Difference','Values in one set but not another.')])
add('comparison-and-logical-operators','02','Comparison and Logical Operators','Comparison ও Logical Operator','Comparison operators produce Boolean results. Logical operators combine conditions using `and`, `or`, and `not`.','Use parentheses to make complex business rules readable and test boundary values explicitly.',"""
revenue = 120000
margin = 0.22
meets_target = revenue >= 100000 and margin >= 0.20
print(meets_target)
""",[('Comparison','Test such as equal, greater, or less.'),('Boolean expression','Expression that returns True or False.'),('and','True only when both conditions are true.'),('or','True when at least one condition is true.')])
add('conditional-statements','02','Conditional Statements','Conditional Statement','`if`, `elif`, and `else` choose which block of code runs based on ordered conditions.','Order rules from specific to general and ensure category thresholds do not overlap unintentionally.',"""
variance_pct = -0.08
if variance_pct >= 0:
    status = 'On or above target'
elif variance_pct >= -0.05:
    status = 'Watch'
else:
    status = 'Below target'
print(status)
""",[('if','Begins a conditional branch.'),('elif','Adds another tested branch.'),('else','Fallback branch.'),('Branch','One possible path through code.')])
add('for-loops','02','For Loops','For Loop','A `for` loop repeats a block for each item in an iterable.','Prefer vectorized pandas or NumPy operations for column calculations, but use loops for clear control flow or small collections.',"""
regions = ['Dhaka','Khulna','Rajshahi']
for position, region in enumerate(regions, start=1):
    print(position, region)
""",[('Loop','Repeated execution of code.'),('Iterable','Object that can provide items one at a time.'),('Iteration','One pass through a loop.'),('enumerate','Function yielding position and value.')])
add('while-loops-and-control-flow','02','While Loops and Control Flow','While Loop ও Control Flow','A `while` loop repeats while a condition remains true. `break` stops a loop and `continue` skips to the next iteration.','Use while loops only when the stopping condition is explicit and protected against infinite execution.',"""
remaining = 3
while remaining > 0:
    print('Retries left:', remaining)
    remaining -= 1
""",[('while','Loop controlled by a Boolean condition.'),('break','Immediately exits a loop.'),('continue','Skips to the next iteration.'),('Infinite loop','Loop whose condition never becomes false.')])
add('list-comprehensions','02','List Comprehensions','List Comprehension','A list comprehension creates a list from an iterable using a compact expression and optional condition.','Use comprehensions for simple readable transformations; use a normal loop when logic becomes difficult to explain.',"""
sales = [800, 1200, 1500, 600]
high_sales = [value for value in sales if value >= 1000]
print(high_sales)
""",[('Comprehension','Compact collection-building syntax.'),('Expression','Code that produces a value.'),('Filter condition','Boolean test selecting items.'),('Transformation','Rule changing each selected item.')])
add('functions-and-return-values','02','Functions and Return Values','Function ও Return Value','A function packages reusable logic behind a name, parameters, and a return value.','Use functions to separate calculations from input/output and make unit testing possible.',"""
def gross_profit(revenue, cost):
    return revenue - cost

print(gross_profit(125000, 83000))
""",[('Function','Reusable named block of code.'),('Parameter','Name defined by a function.'),('Argument','Value passed to a function.'),('return','Statement sending a result back to the caller.')])
add('function-arguments-and-defaults','02','Function Arguments and Defaults','Function Argument ও Default','Functions can accept positional, keyword, and default arguments. Explicit keyword arguments improve readability when several values have similar types.','Use defaults only when the assumption is safe and documented.',"""
def net_sales(gross, discount_rate=0.0):
    return gross * (1 - discount_rate)

print(net_sales(1000))
print(net_sales(1000, discount_rate=0.10))
""",[('Positional argument','Argument matched by position.'),('Keyword argument','Argument matched by parameter name.'),('Default argument','Value used when an argument is omitted.'),('Signature','Definition of a function interface.')])
add('scope-and-pure-functions','02','Scope and Pure Functions','Scope ও Pure Function','Scope controls where a name can be accessed. A pure function depends only on its inputs and does not alter external state.','Prefer explicit inputs and returned outputs over hidden global changes in analytical code.',"""
tax_rate = 0.05

def add_tax(amount, rate):
    return amount * (1 + rate)

print(add_tax(1000, tax_rate))
""",[('Scope','Region in which a name is visible.'),('Local variable','Name defined inside a function.'),('Global variable','Name defined at module level.'),('Pure function','Function without hidden side effects.')])
add('exceptions-and-defensive-code','02','Exceptions and Defensive Code','Exception ও Defensive Code','Defensive code validates assumptions and raises or handles exceptions with useful messages.','Reject invalid inputs early rather than allowing incorrect values to silently affect later results.',"""
def margin(revenue, profit):
    if revenue == 0:
        raise ValueError('Revenue must be non-zero')
    return profit / revenue

try:
    print(margin(0, 100))
except ValueError as error:
    print(error)
""",[('raise','Statement that triggers an exception.'),('Validation','Check that input satisfies a requirement.'),('try','Block that may raise an exception.'),('except','Block that handles a matching exception.')])
add('modules-pathlib-and-files','02','Modules, pathlib, and Files','Module, pathlib ও File','The standard library provides modules for paths, CSV, JSON, dates, statistics, and many other tasks. `pathlib` creates platform-aware paths.','Build paths relative to the project root and specify text encodings explicitly.',"""
from pathlib import Path
path = Path('outputs') / 'summary.txt'
print(path.as_posix())
""",[('Standard library','Modules distributed with Python.'),('pathlib','Object-oriented path library.'),('Path','Object representing a filesystem path.'),('Encoding','Rule mapping text characters to bytes.')])

# 03 NumPy
add('numpy-arrays','03','NumPy Arrays','NumPy Array','A NumPy `ndarray` stores homogeneous numerical data in one or more dimensions.','Use arrays for efficient numerical operations and as the foundation beneath many pandas and scientific workflows.',"""
import numpy as np
sales = np.array([1200, 1450, 1325, 1600])
print(sales)
print(type(sales).__name__)
""",[('ndarray','NumPy n-dimensional array.'),('Element','One value in an array.'),('Homogeneous','Stored using a common data type.'),('Dimension','Axis along which values are organized.')],packages=['numpy'])
add('array-shape-size-and-dtype','03','Array Shape, Size, and dtype','Array Shape, Size ও dtype','Shape describes array dimensions, size counts elements, and dtype describes stored value representation.','Inspect shape and dtype before calculations because silent type coercion can change results.',"""
import numpy as np
matrix = np.array([[1,2,3],[4,5,6]], dtype='float64')
print(matrix.shape, matrix.size, matrix.dtype)
""",[('shape','Length of each array dimension.'),('size','Total number of elements.'),('dtype','NumPy element data type.'),('axis','Numbered dimension of an array.')],packages=['numpy'])
add('creating-arrays','03','Create Arrays','Array তৈরি','NumPy creates arrays from Python collections or helper functions such as `arange`, `linspace`, `zeros`, and `ones`.','Choose a construction method that makes range boundaries and step assumptions explicit.',"""
import numpy as np
print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5))
""",[('arange','Creates evenly spaced values using a step.'),('linspace','Creates a fixed count of evenly spaced values.'),('zeros','Creates an array filled with zero.'),('ones','Creates an array filled with one.')],packages=['numpy'])
add('indexing-and-slicing-arrays','03','Index and Slice Arrays','Array Index ও Slice','Array indexing selects elements, rows, columns, or multidimensional regions. Slices usually create views rather than independent copies.','Confirm whether an operation changes the original array and copy explicitly when independent data is required.',"""
import numpy as np
matrix = np.array([[10,20,30],[40,50,60]])
print(matrix[0, 1])
print(matrix[:, 1:])
""",[('Indexing','Selecting positions from an array.'),('Slicing','Selecting a range along an axis.'),('View','Array sharing memory with another array.'),('Copy','Independent array with separate memory.')],packages=['numpy'])
add('vectorized-operations','03','Vectorized Operations','Vectorized Operation','Vectorization applies an operation to entire arrays without an explicit Python loop.','Use vectorized expressions for clarity and performance, then verify units and boundary behavior.',"""
import numpy as np
revenue = np.array([1000, 1200, 1500])
cost = np.array([700, 850, 990])
profit = revenue - cost
print(profit)
""",[('Vectorization','Array-wide operation implemented efficiently.'),('Elementwise','Applied independently to matching elements.'),('Universal function','NumPy function operating elementwise.'),('Operand','Value used by an operator.')],packages=['numpy'])
add('broadcasting','03','Broadcasting','Broadcasting','Broadcasting lets NumPy combine arrays with compatible shapes without manually repeating values.','Check shapes explicitly because a broadcast can be valid mathematically but wrong for the business grain.',"""
import numpy as np
sales = np.array([[100,120,140],[80,90,110]])
rates = np.array([1.0, 1.1, 0.9])
print(sales * rates)
""",[('Broadcasting','Rules for operating on compatible array shapes.'),('Compatible shape','Dimensions that can align or equal one.'),('Scalar','Single numerical value.'),('Grain','Meaning represented by one array element or row.')],packages=['numpy'],level='Intermediate')
add('boolean-masks','03','Boolean Masks and Filtering','Boolean Mask ও Filtering','A Boolean mask is an array of True and False values used to select matching elements.','Build masks from explicit conditions and inspect selected counts before summarizing.',"""
import numpy as np
sales = np.array([800, 1200, 1500, 600])
mask = sales >= 1000
print(mask)
print(sales[mask])
""",[('Boolean mask','True/False array used for selection.'),('Condition','Expression generating a Boolean result.'),('Filtering','Keeping values that satisfy a condition.'),('Selection count','Number of values retained.')],packages=['numpy'])
add('aggregation-and-axis','03','Aggregation and Axis','Aggregation ও Axis','Aggregation functions reduce many values to summaries. The `axis` argument controls whether a calculation runs by row, column, or over all elements.','State the analytical grain whenever using an axis-based summary.',"""
import numpy as np
sales = np.array([[100,120,140],[80,90,110]])
print('By product:', sales.sum(axis=0))
print('By region:', sales.sum(axis=1))
""",[('Aggregation','Reduction from many values to a summary.'),('axis=0','Operation down rows, returning column summaries.'),('axis=1','Operation across columns, returning row summaries.'),('Reduction','Operation producing fewer values.')],packages=['numpy'])
add('missing-and-invalid-numbers','03','Missing and Invalid Numbers','Missing ও Invalid Number','Floating-point arrays can represent missing numeric values with `NaN`. Infinite values and invalid operations require separate checks.','Count missing and non-finite values before calculation and choose a documented treatment.',"""
import numpy as np
values = np.array([10.0, np.nan, 30.0, np.inf])
print('Missing:', np.isnan(values).sum())
print('Finite:', np.isfinite(values).sum())
print('Mean ignoring NaN:', np.nanmean(values[np.isfinite(values)]))
""",[('NaN','Floating-point marker for missing or undefined value.'),('infinity','Value larger than any finite floating-point number.'),('isfinite','Check for values excluding NaN and infinity.'),('nanmean','Mean that ignores NaN values.')],packages=['numpy'])
add('random-generation-and-reproducibility','03','Random Generation and Reproducibility','Random Generation ও Reproducibility','NumPy random generators create simulated samples. A fixed seed or generator state makes a demonstration reproducible.','Use modern `default_rng`, record the seed, and do not confuse simulation with observed evidence.',"""
import numpy as np
rng = np.random.default_rng(42)
sample = rng.normal(loc=100, scale=15, size=5)
print(np.round(sample, 2))
""",[('Random generator','Object producing pseudo-random values.'),('Seed','Initial state used to reproduce a sequence.'),('Simulation','Generated experiment representing a model.'),('Distribution','Probability model used to generate values.')],packages=['numpy'])

# 04 pandas foundations
add('series-and-dataframes','04','Series and DataFrames','Series ও DataFrame','A pandas Series is a labeled one-dimensional array; a DataFrame is a labeled two-dimensional table with potentially different column types.','Use DataFrames for tabular analytical data and preserve column names, types, and row meaning.',"""
import pandas as pd
df = pd.DataFrame({'region':['Dhaka','Khulna'],'revenue':[1200,950]})
print(df)
""",[('Series','One-dimensional labeled pandas array.'),('DataFrame','Two-dimensional labeled pandas table.'),('Index','Labels identifying rows.'),('Column','Labeled variable in a DataFrame.')],packages=['pandas'])
add('create-dataframes','04','Create DataFrames','DataFrame তৈরি','DataFrames can be created from dictionaries, lists of records, arrays, and many file formats.','Create small examples with explicit column names and inspect inferred types immediately.',"""
import pandas as pd
records = [{'region':'Dhaka','sales':1200},{'region':'Khulna','sales':950}]
df = pd.DataFrame(records)
print(df)
""",[('Record','Mapping describing one row.'),('Constructor','Callable creating a new object.'),('Column order','Order in which fields are displayed.'),('Type inference','Automatic choice of column data types.')],packages=['pandas'])
add('read-csv-files','04','Read CSV Files','CSV File পড়ুন','`read_csv` parses delimited text into a DataFrame. Delimiter, encoding, headers, missing markers, date parsing, and data types affect the imported result.','Inspect source files and specify critical options rather than trusting defaults blindly.',"""
import pandas as pd
df = pd.read_csv('python_retail_sales.csv')
print(df.head(3))
print(df.shape)
""",[('CSV','Delimited plain-text table format.'),('Delimiter','Character separating fields.'),('Header','Row containing column names.'),('Parser','Software converting text into structured values.')],packages=['pandas'])
add('read-excel-and-json','04','Read Excel and JSON Data','Excel ও JSON Data পড়ুন','pandas reads spreadsheet sheets and JSON structures, but file layout and nested structure determine the correct options.','Confirm sheet names, header rows, merged cells, JSON orientation, and types before analysis.',"""
import pandas as pd
from io import StringIO
sample = '[{"region":"Dhaka","sales":1200},{"region":"Khulna","sales":950}]'
df = pd.read_json(StringIO(sample))
print(df)
""",[('Excel sheet','Named grid within a workbook.'),('JSON','Text format representing objects and arrays.'),('Orientation','How JSON maps records, columns, or values.'),('Schema','Expected fields and data types.')],packages=['pandas'])
add('inspect-a-dataframe','04','Inspect a DataFrame','DataFrame Inspect করুন','Initial inspection uses shape, column names, dtypes, sample rows, summary information, and missing-value counts.','Do not start analysis until row meaning, key fields, and critical type issues are understood.',"""
import pandas as pd
df = pd.read_csv('python_retail_sales.csv')
print(df.shape)
print(df.dtypes.head())
print(df.isna().sum().sort_values(ascending=False).head())
""",[('shape','Number of rows and columns.'),('dtype','Data type assigned to a column.'),('head','First rows of a DataFrame.'),('info','Compact summary of columns and non-null counts.')],packages=['pandas'])
add('select-columns','04','Select Columns','Column Select করুন','Column selection returns a Series for one column or a DataFrame for a list of columns.','Select only necessary fields and avoid accidental chained modifications.',"""
import pandas as pd
df = pd.read_csv('python_retail_sales.csv')
print(df['revenue'].head())
print(df[['order_date','region','revenue']].head())
""",[('Column selection','Choosing one or more named columns.'),('Series result','One-dimensional result from a single column.'),('DataFrame result','Two-dimensional result from multiple columns.'),('Projection','Relational term for selecting fields.')],packages=['pandas'])
add('select-rows-with-loc-and-iloc','04','Select Rows with loc and iloc','loc ও iloc দিয়ে Row Select','`loc` selects by labels and conditions; `iloc` selects by integer positions.','Use label-based selection for business logic and positional selection only when positions are meaningful and stable.',"""
import pandas as pd
df = pd.DataFrame({'region':['Dhaka','Khulna','Rajshahi'],'sales':[1200,950,1100]})
print(df.loc[df['sales'] >= 1000, ['region','sales']])
print(df.iloc[:2, :])
""",[('loc','Label-based pandas indexer.'),('iloc','Integer-position pandas indexer.'),('Row label','Value identifying a row in the index.'),('Position','Zero-based physical location.')],packages=['pandas'])
add('filter-rows','04','Filter Rows','Row Filter করুন','Boolean conditions filter DataFrame rows. Multiple conditions require parentheses and elementwise operators such as `&` and `|`.','Count rows before and after filtering and document inclusion and exclusion rules.',"""
import pandas as pd
df = pd.read_csv('python_retail_sales.csv')
filtered = df[(df['region'] == 'Dhaka') & (df['revenue'] >= 1000)]
print(filtered[['order_id','region','revenue']].head())
print('Rows:', len(filtered))
""",[('Boolean indexing','Filtering rows with a True/False Series.'),('Elementwise operator','Operator applied to each aligned value.'),('Inclusion rule','Condition required to retain a row.'),('Exclusion rule','Condition removing a row.')],packages=['pandas'])
add('sort-values','04','Sort Values','Value Sort করুন','`sort_values` orders rows by one or more columns with independent ascending or descending directions.','Make tie-breaking rules explicit so rankings are deterministic.',"""
import pandas as pd
df = pd.read_csv('python_retail_sales.csv')
ranked = df.sort_values(['revenue','order_id'], ascending=[False, True])
print(ranked[['order_id','revenue']].head())
""",[('sort_values','Method ordering rows by column values.'),('Ascending','Low-to-high ordering.'),('Descending','High-to-low ordering.'),('Tie-breaker','Additional field resolving equal values.')],packages=['pandas'])
add('create-and-assign-columns','04','Create and Assign Columns','Column তৈরি ও Assign','New columns can be calculated from existing columns using vectorized expressions or `assign`.','Name derived fields clearly, state units, and preserve the source columns needed for validation.',"""
import pandas as pd
df = pd.DataFrame({'revenue':[1200,950],'cost':[800,700]})
df = df.assign(profit=df['revenue'] - df['cost'])
print(df)
""",[('Derived column','Column calculated from other fields.'),('assign','Method returning a DataFrame with added columns.'),('Vectorized expression','Column calculation applied to all rows.'),('Lineage','Trace from source fields to a derived result.')],packages=['pandas'])
add('rename-drop-and-reorder','04','Rename, Drop, and Reorder Columns','Column Rename, Drop ও Reorder','Column names can be standardized with `rename`; unnecessary columns can be removed with `drop`; lists control display order.','Avoid destructive removal until source fields have been validated and documented.',"""
import pandas as pd
df = pd.DataFrame({'Sales Amount':[1200], 'Temp':[1], 'Region':['Dhaka']})
df = df.rename(columns={'Sales Amount':'sales_amount'}).drop(columns='Temp')
df = df[['Region','sales_amount']]
print(df)
""",[('rename','Method changing labels.'),('drop','Method removing rows or columns.'),('Column order','Displayed sequence of fields.'),('Naming convention','Consistent rules for field names.')],packages=['pandas'])
add('data-types-and-conversion','04','Data Types and Conversion','Data Type ও Conversion','pandas supports numeric, text, Boolean, categorical, and datetime types. Conversion functions can coerce invalid values to missing markers for review.','Convert deliberately and count conversion failures instead of silently replacing invalid data.',"""
import pandas as pd
s = pd.Series(['100','bad','250'])
converted = pd.to_numeric(s, errors='coerce')
print(converted)
print('Failures:', converted.isna().sum())
""",[('to_numeric','Function converting values to numbers.'),('coercion','Conversion of invalid values to missing data.'),('nullable dtype','Type capable of representing missing values.'),('conversion failure','Value that cannot be converted as expected.')],packages=['pandas'])
add('parse-dates','04','Parse and Use Dates','Date Parse ও ব্যবহার','`to_datetime` converts date-like values into pandas datetime data, enabling date parts, sorting, resampling, and time differences.','Specify format or day-first expectations when source dates are ambiguous.',"""
import pandas as pd
s = pd.Series(['2026-01-05','2026-02-10'])
dates = pd.to_datetime(s, format='%Y-%m-%d')
print(dates.dt.month_name())
""",[('datetime','Type representing dates and times.'),('parse','Convert text into structured values.'),('format string','Pattern describing date components.'),('dt accessor','pandas interface for datetime properties.')],packages=['pandas'])
add('export-dataframes','04','Export DataFrames','DataFrame Export করুন','DataFrames can be written to CSV, Excel, JSON, Parquet, and other formats. Index, encoding, data types, and formatting affect the output.','Export only approved fields and validate the produced file by reading it back when delivery matters.',"""
import pandas as pd
from io import StringIO
df = pd.DataFrame({'region':['Dhaka'],'sales':[1200]})
buffer = StringIO()
df.to_csv(buffer, index=False)
print(buffer.getvalue())
""",[('to_csv','Method writing delimited text.'),('index=False','Option excluding row labels from output.'),('serialization','Conversion of an object into a storable format.'),('round-trip test','Write then read to validate output.')],packages=['pandas'])

# 05 cleaning and transformation
add('profile-data-quality','05','Profile Data Quality','Data Quality Profile করুন','A data-quality profile measures row counts, uniqueness, missingness, invalid types, ranges, categories, and duplicates before transformation.','Create a baseline profile so every cleaning decision can be reconciled.',"""
import pandas as pd
df = pd.read_csv('python_retail_sales.csv')
profile = pd.DataFrame({'dtype':df.dtypes.astype(str),'missing':df.isna().sum(),'unique':df.nunique(dropna=False)})
print(profile.head(8))
""",[('Profile','Summary describing data structure and quality.'),('Completeness','Extent to which required values are present.'),('Uniqueness','Extent to which key values are distinct.'),('Validity','Whether values follow defined rules.')],packages=['pandas'])
add('handle-missing-values','05','Handle Missing Values','Missing Value Handle করুন','Missing values can be removed, filled, modeled, or retained depending on why they are missing and how the field is used.','Measure missingness by segment and document the treatment; do not automatically fill everything with zero.',"""
import pandas as pd
df = pd.DataFrame({'segment':['A','A','B'],'score':[10,None,30]})
df['score_filled'] = df['score'].fillna(df.groupby('segment')['score'].transform('median'))
print(df)
""",[('Missing value','Unavailable or unrecorded value.'),('fillna','Method replacing missing values.'),('Imputation','Estimated replacement for missing data.'),('Deletion','Removing rows or columns containing missing values.')],packages=['pandas'])
add('detect-and-remove-duplicates','05','Detect and Remove Duplicates','Duplicate Detect ও Remove','Duplicates must be evaluated at the correct business key. Entirely identical rows and repeated entities are different quality problems.','Define the key, inspect duplicate groups, preserve evidence, and choose which record to keep.',"""
import pandas as pd
df = pd.DataFrame({'order_id':[1,1,2],'updated':['2026-01-01','2026-01-03','2026-01-02'],'sales':[100,110,90]})
df['updated'] = pd.to_datetime(df['updated'])
clean = df.sort_values('updated').drop_duplicates('order_id', keep='last')
print(clean)
""",[('Duplicate','Repeated row or business entity.'),('Business key','Field set identifying the intended entity.'),('keep','Rule selecting retained duplicate.'),('deduplication','Process of resolving duplicate records.')],packages=['pandas'])
add('clean-text-and-categories','05','Clean Text and Categories','Text ও Category Clean','Text cleaning standardizes case, whitespace, punctuation, and category mappings while preserving identifiers and meaning.','Inspect category frequencies before and after cleaning to detect accidental merges.',"""
import pandas as pd
s = pd.Series([' dhaka','DHAKA ','Dhaka','ctg'])
clean = s.str.strip().str.title().replace({'Ctg':'Chattogram'})
print(clean.value_counts())
""",[('String accessor','`.str` interface for vectorized text methods.'),('Normalization','Making equivalent values use one representation.'),('Category mapping','Dictionary translating source categories.'),('Identifier','Value used to distinguish an entity.')],packages=['pandas'])
add('validate-ranges-and-business-rules','05','Validate Ranges and Business Rules','Range ও Business Rule Validate','Validation rules test allowed ranges, category sets, date order, and cross-field consistency.','Create explicit Boolean flags instead of silently correcting values that require review.',"""
import pandas as pd
df = pd.DataFrame({'quantity':[2,-1,5],'revenue':[200,100,-20]})
df['valid'] = df['quantity'].gt(0) & df['revenue'].ge(0)
print(df)
""",[('Range rule','Allowed minimum and maximum.'),('Cross-field rule','Condition involving multiple columns.'),('Validity flag','Boolean field marking rule compliance.'),('Exception log','Record of values needing review.')],packages=['pandas'])
add('detect-and-treat-outliers','05','Detect and Treat Outliers','Outlier Detect ও Treat','Outliers are unusual values, not automatically errors. Statistical rules such as IQR fences identify candidates that require domain review.','Keep raw values, flag candidates, investigate causes, and compare results with and without treatment.',"""
import pandas as pd
s = pd.Series([10,11,12,13,14,100])
q1, q3 = s.quantile([0.25,0.75])
iqr = q3-q1
flag = (s < q1-1.5*iqr) | (s > q3+1.5*iqr)
print(pd.DataFrame({'value':s,'outlier':flag}))
""",[('Outlier','Observation unusually far from other values.'),('IQR','Difference between third and first quartiles.'),('Fence','Threshold used to flag candidate outliers.'),('Winsorization','Capping values at defined limits.')],packages=['pandas'])
add('groupby-and-aggregation','05','GroupBy and Aggregation','GroupBy ও Aggregation','The split-apply-combine pattern groups rows, applies summaries, and combines results.','Define the group keys and output grain before aggregating.',"""
import pandas as pd
df = pd.read_csv('python_retail_sales.csv')
summary = df.groupby('region', as_index=False).agg(orders=('order_id','nunique'), revenue=('revenue','sum'), profit=('profit','sum'))
print(summary)
""",[('groupby','Operation splitting rows by key values.'),('aggregation','Summary calculated per group.'),('named aggregation','Syntax assigning output column names.'),('output grain','Meaning of one result row.')],packages=['pandas'])
add('transform-and-window-like-calculations','05','Transform and Group-Level Calculations','Transform ও Group-Level Calculation','`transform` returns a value aligned to each original row, enabling group totals, shares, and standardized values.','Use transform when the output must retain the original row grain.',"""
import pandas as pd
df = pd.DataFrame({'region':['A','A','B'],'sales':[100,300,200]})
df['region_total'] = df.groupby('region')['sales'].transform('sum')
df['share'] = df['sales'] / df['region_total']
print(df)
""",[('transform','Group operation returning row-aligned output.'),('Alignment','Matching results to index labels.'),('Share','Row value divided by its group total.'),('Row grain','One output per original row.')],packages=['pandas'])
add('pivot-tables-and-crosstabs','05','Pivot Tables and Crosstabs','Pivot Table ও Crosstab','`pivot_table` summarizes values by row and column categories; `crosstab` counts or normalizes category combinations.','Specify aggregation and missing-category handling explicitly.',"""
import pandas as pd
df = pd.read_csv('python_retail_sales.csv')
pivot = pd.pivot_table(df, index='region', columns='channel', values='revenue', aggfunc='sum', fill_value=0)
print(pivot)
""",[('pivot_table','Spreadsheet-like grouped summary.'),('crosstab','Frequency table of category combinations.'),('margin','Optional totals added to a table.'),('fill_value','Replacement for missing combinations.')],packages=['pandas'])
add('reshape-with-melt-and-pivot','05','Reshape with melt and pivot','melt ও pivot দিয়ে Reshape','Wide and long layouts serve different analytical tasks. `melt` converts repeated columns into rows; `pivot` reconstructs unique row-column combinations.','Confirm identifier and measured-value fields before reshaping.',"""
import pandas as pd
wide = pd.DataFrame({'region':['A','B'],'Jan':[100,80],'Feb':[120,90]})
long = wide.melt(id_vars='region', var_name='month', value_name='sales')
print(long)
""",[('Wide data','Repeated measures stored in separate columns.'),('Long data','One observation per row with variable labels.'),('melt','Method converting wide data to long.'),('pivot','Method converting unique long data to wide.')],packages=['pandas'])
add('merge-and-join-dataframes','05','Merge and Join DataFrames','DataFrame Merge ও Join','`merge` combines tables using keys and join types. Cardinality mistakes can duplicate facts and inflate metrics.','Declare expected cardinality with `validate`, inspect unmatched keys, and reconcile totals.',"""
import pandas as pd
orders = pd.DataFrame({'order_id':[1,2],'customer_id':['C1','C2'],'sales':[100,200]})
customers = pd.DataFrame({'customer_id':['C1','C2'],'segment':['Retail','Corporate']})
result = orders.merge(customers, on='customer_id', how='left', validate='many_to_one')
print(result)
""",[('merge','Key-based combination of DataFrames.'),('join type','Rule controlling matched and unmatched rows.'),('cardinality','Relationship between key uniqueness in tables.'),('unmatched key','Key without a corresponding row.')],packages=['pandas'])
add('concat-and-append-datasets','05','Concatenate Datasets','Dataset Concatenate করুন','`concat` combines DataFrames vertically or horizontally. Vertical combination requires compatible schemas and deliberate source tracking.','Add source identifiers and validate column differences before concatenation.',"""
import pandas as pd
jan = pd.DataFrame({'month':['Jan'],'sales':[100]})
feb = pd.DataFrame({'month':['Feb'],'sales':[120]})
combined = pd.concat([jan,feb], ignore_index=True)
print(combined)
""",[('concat','Function combining pandas objects along an axis.'),('vertical append','Adding rows from multiple datasets.'),('schema drift','Unexpected changes in fields or types.'),('source field','Column identifying origin of rows.')],packages=['pandas'])
add('method-chaining-and-pipelines','05','Method Chaining and Pipelines','Method Chaining ও Pipeline','Method chaining expresses a sequence of DataFrame transformations as a readable pipeline.','Use one logical transformation per line and insert checks at important boundaries.',"""
import pandas as pd
df = pd.read_csv('python_retail_sales.csv')
result = (df
          .query('revenue >= 0')
          .assign(margin=lambda x: x['profit'] / x['revenue'])
          .groupby('region', as_index=False)
          .agg(revenue=('revenue','sum'), profit=('profit','sum')))
print(result)
""",[('Method chain','Sequence of object methods.'),('query','Method filtering with expression syntax.'),('lambda','Anonymous function used inline.'),('pipeline','Ordered reproducible transformations.')],packages=['pandas'])

# 06 EDA and statistics
add('eda-workflow','06','Exploratory Data Analysis Workflow','EDA Workflow','EDA investigates structure, quality, distributions, relationships, and unusual cases before formal modeling or decisions.','Start with questions and grain, inspect quality, analyze one variable, compare groups, examine relationships, and record findings and limitations.',"""
import pandas as pd
df = pd.read_csv('python_retail_sales.csv')
print(df[['revenue','profit','quantity']].describe().round(2))
print(df.groupby('region')['revenue'].sum().sort_values(ascending=False))
""",[('EDA','Exploratory data analysis.'),('Univariate','Analysis of one variable.'),('Bivariate','Analysis of two variables.'),('Finding log','Record of evidence, interpretation, and follow-up.')],packages=['pandas'])
add('descriptive-statistics-with-pandas','06','Descriptive Statistics with pandas','pandas দিয়ে Descriptive Statistics','pandas provides count, mean, median, standard deviation, quantiles, and categorical frequencies.','Always pair summaries with units, sample size, distribution shape, and data-quality context.',"""
import pandas as pd
df = pd.read_csv('python_retail_sales.csv')
print(df['revenue'].describe(percentiles=[0.25,0.5,0.75,0.9]).round(2))
""",[('describe','Method generating descriptive summaries.'),('mean','Arithmetic average.'),('median','Middle ordered value.'),('quantile','Value below which a proportion of data falls.')],packages=['pandas'])
add('distribution-analysis','06','Analyze Distributions','Distribution Analyze করুন','Distribution analysis examines center, spread, shape, tails, and unusual values rather than relying on one average.','Compare mean and median, calculate quantiles, and visualize the distribution before choosing a summary.',"""
import pandas as pd
df = pd.read_csv('python_retail_sales.csv')
s = df['revenue']
print({'mean':round(s.mean(),2),'median':round(s.median(),2),'skew':round(s.skew(),2),'iqr':round(s.quantile(.75)-s.quantile(.25),2)})
""",[('Distribution','Pattern of values and probabilities.'),('Skewness','Asymmetry of a distribution.'),('Tail','Extreme end of a distribution.'),('Spread','Degree of variability.')],packages=['pandas'])
add('segment-comparison','06','Compare Segments','Segment Compare করুন','Grouped summaries compare categories while preserving counts, totals, rates, and uncertainty.','Check whether group sizes and data-quality patterns make comparisons fair.',"""
import pandas as pd
df = pd.read_csv('python_retail_sales.csv')
comparison = df.groupby('channel').agg(rows=('order_id','size'), avg_revenue=('revenue','mean'), avg_margin=('margin','mean'))
print(comparison.round(3))
""",[('Segment','Subset defined by shared characteristics.'),('Group size','Number of observations in a segment.'),('Rate','Numerator divided by a relevant denominator.'),('Comparability','Extent to which groups can be fairly compared.')],packages=['pandas'])
add('correlation-analysis','06','Correlation Analysis','Correlation Analysis','Correlation measures the direction and strength of association between numerical variables. It does not establish causation.','Inspect scatterplots, outliers, nonlinearity, and sample size before interpreting a correlation coefficient.',"""
import pandas as pd
df = pd.read_csv('python_retail_sales.csv')
print(df[['quantity','revenue','profit','discount']].corr(numeric_only=True).round(3))
""",[('Correlation','Standardized measure of association.'),('Pearson correlation','Linear correlation coefficient.'),('Association','Variables changing together.'),('Causation','Change in one variable producing change in another.')],packages=['pandas'])
add('sampling-with-python','06','Sampling with Python','Python দিয়ে Sampling','pandas can draw random or stratified samples. A sample is useful only when its selection process supports the intended population inference.','Set a random state for reproducibility and compare sample composition with the full population.',"""
import pandas as pd
df = pd.read_csv('python_retail_sales.csv')
sample = df.sample(n=10, random_state=42)
print(sample[['order_id','region','revenue']])
""",[('Sample','Subset selected from a population.'),('random_state','Seed-like value for reproducible sampling.'),('Stratification','Sampling within defined groups.'),('Representativeness','How well a sample reflects the target population.')],packages=['pandas'])
add('confidence-intervals-with-scipy','06','Confidence Intervals with SciPy','SciPy দিয়ে Confidence Interval','A confidence interval estimates a population parameter using a sample estimate and sampling uncertainty.','State the confidence level, method, assumptions, sample size, estimate, and interval together.',"""
import pandas as pd
from scipy import stats
df = pd.read_csv('python_retail_sales.csv')
sample = df['revenue'].dropna()
mean = sample.mean()
sem = stats.sem(sample)
low, high = stats.t.interval(0.95, df=len(sample)-1, loc=mean, scale=sem)
print(round(mean,2), round(low,2), round(high,2))
""",[('Confidence interval','Range produced by a method with a stated coverage rate.'),('Standard error','Estimated variability of a sample statistic.'),('t distribution','Distribution used for mean inference with estimated variance.'),('coverage','Long-run proportion of intervals containing the parameter.')],packages=['pandas','scipy'],level='Intermediate')
add('hypothesis-tests-with-scipy','06','Hypothesis Tests with SciPy','SciPy দিয়ে Hypothesis Test','A hypothesis test evaluates how compatible observed data are with a stated null model.','Predefine hypotheses and significance level, check assumptions, report effect size and interval, and avoid treating p-values as business importance.',"""
import pandas as pd
from scipy import stats
df = pd.read_csv('python_retail_sales.csv')
a = df.loc[df['channel']=='Online','revenue']
b = df.loc[df['channel']=='Retail','revenue']
result = stats.ttest_ind(a, b, equal_var=False)
print('t=', round(result.statistic,3), 'p=', round(result.pvalue,4))
print('mean difference=', round(a.mean()-b.mean(),2))
""",[('Null hypothesis','Reference claim tested by the procedure.'),('p-value','Probability of equal or more extreme data under the null model.'),('significance level','Predefined decision threshold.'),('effect size','Magnitude of the observed difference or relationship.')],packages=['pandas','scipy'],level='Intermediate')
add('simple-linear-regression','06','Simple Linear Regression','Simple Linear Regression','Simple linear regression estimates a straight-line relationship between one predictor and one outcome.','Inspect residuals and uncertainty, and avoid causal claims from observational association.',"""
import pandas as pd
from scipy import stats
df = pd.read_csv('python_retail_sales.csv')
model = stats.linregress(df['quantity'], df['revenue'])
print('slope=', round(model.slope,2), 'intercept=', round(model.intercept,2), 'r²=', round(model.rvalue**2,3))
""",[('Predictor','Variable used to explain or predict an outcome.'),('Outcome','Variable being modeled.'),('Slope','Expected outcome change per predictor unit.'),('R-squared','Proportion of variation explained by the fitted line.')],packages=['pandas','scipy'],level='Intermediate')
add('ab-test-analysis','06','A/B Test Analysis','A/B Test Analysis','An A/B test compares outcomes between randomly assigned variants. Conversion analysis uses counts, rates, uncertainty, and practical impact.','Confirm randomization, exposure definition, metric window, sample ratio, and decision threshold before testing.',"""
from scipy import stats
import numpy as np
conversions = np.array([120, 145])
visitors = np.array([2000, 1980])
rates = conversions / visitors
pooled = conversions.sum()/visitors.sum()
se = np.sqrt(pooled*(1-pooled)*(1/visitors[0]+1/visitors[1]))
z = (rates[1]-rates[0])/se
p = 2*stats.norm.sf(abs(z))
print('rates=', np.round(rates,4), 'lift=', round(rates[1]-rates[0],4), 'p=', round(p,4))
""",[('Variant','Alternative experience in an experiment.'),('Conversion rate','Conversions divided by eligible exposures.'),('Lift','Difference or relative change between variants.'),('Randomization','Chance-based assignment reducing systematic differences.')],packages=['numpy','scipy'],level='Intermediate')

# 07 visualization
add('matplotlib-figure-and-axes','07','Matplotlib Figure and Axes','Matplotlib Figure ও Axes','A Matplotlib Figure is the full canvas and an Axes is one plotting area containing scales, labels, and artists.','Use the object-oriented interface so chart structure and formatting remain explicit.',"""
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1,2,3],[2,4,3])
ax.set(title='Simple trend', xlabel='Period', ylabel='Value')
plt.show()
""",[('Figure','Top-level Matplotlib canvas.'),('Axes','Plotting area inside a figure.'),('Artist','Visible element in a figure.'),('object-oriented interface','Plotting by calling methods on Figure and Axes objects.')],packages=['matplotlib'])
add('line-charts','07','Line Charts','Line Chart','Line charts show change over an ordered continuous axis, commonly time.','Sort dates, use consistent intervals, label units, and avoid connecting unrelated categories.',"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('python_retail_sales.csv', parse_dates=['order_date'])
monthly = df.set_index('order_date').resample('MS')['revenue'].sum()
fig, ax = plt.subplots()
monthly.plot(ax=ax)
ax.set(title='Monthly revenue', ylabel='BDT', xlabel='Month')
plt.show()
""",[('Line chart','Chart connecting ordered observations.'),('Time axis','Ordered date or time scale.'),('resample','Time-based grouping operation.'),('trend','General direction of change.')],packages=['pandas','matplotlib'])
add('bar-charts','07','Bar Charts','Bar Chart','Bar charts compare magnitudes across discrete categories using length from a common baseline.','Sort when ranking is important, keep a zero baseline, and limit categories to a readable count.',"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('python_retail_sales.csv')
summary = df.groupby('region')['revenue'].sum().sort_values()
fig, ax = plt.subplots()
summary.plot.barh(ax=ax)
ax.set(title='Revenue by region', xlabel='BDT', ylabel='Region')
plt.show()
""",[('Bar chart','Categorical magnitude comparison.'),('baseline','Axis value from which bar length begins.'),('category order','Sequence of categories in a chart.'),('horizontal bar','Bar extending along the x-axis.')],packages=['pandas','matplotlib'])
add('histograms','07','Histograms','Histogram','A histogram groups numerical values into bins to show distribution shape. Bin width affects the visible pattern.','Compare several reasonable bin choices and report sample size and units.',"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('python_retail_sales.csv')
fig, ax = plt.subplots()
ax.hist(df['revenue'], bins=15, edgecolor='black')
ax.set(title='Order revenue distribution', xlabel='Revenue (BDT)', ylabel='Orders')
plt.show()
""",[('Histogram','Distribution chart using numerical bins.'),('bin','Interval grouping numerical observations.'),('frequency','Count of observations in a bin.'),('density','Normalized frequency per unit width.')],packages=['pandas','matplotlib'])
add('box-plots','07','Box Plots','Box Plot','A box plot summarizes median, quartiles, spread, and candidate outliers.','Use it to compare distributions across groups, not as proof that flagged points are errors.',"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('python_retail_sales.csv')
groups = [g['revenue'].values for _, g in df.groupby('channel')]
labels = [name for name,_ in df.groupby('channel')]
fig, ax = plt.subplots()
ax.boxplot(groups, tick_labels=labels)
ax.set(title='Revenue by channel', ylabel='BDT')
plt.show()
""",[('Box','Range from first to third quartile.'),('Median line','Line marking the middle value.'),('Whisker','Line extending to non-outlier range.'),('candidate outlier','Point beyond the plot rule.')],packages=['pandas','matplotlib'])
add('scatter-plots','07','Scatter Plots','Scatter Plot','Scatter plots show paired numerical values and help reveal direction, form, strength, clusters, and outliers.','Avoid drawing a trend conclusion without checking scale, subgroup structure, and unusual points.',"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('python_retail_sales.csv')
fig, ax = plt.subplots()
ax.scatter(df['quantity'], df['revenue'], alpha=.55)
ax.set(title='Quantity and revenue', xlabel='Quantity', ylabel='Revenue (BDT)')
plt.show()
""",[('Scatter plot','Chart of paired numerical observations.'),('alpha','Transparency level.'),('cluster','Group of nearby points.'),('nonlinear relationship','Association not well represented by a straight line.')],packages=['pandas','matplotlib'])
add('subplots-and-small-multiples','07','Subplots and Small Multiples','Subplot ও Small Multiple','Subplots place multiple Axes in one Figure. Small multiples repeat a consistent chart across segments.','Share scales where comparison requires it and avoid overcrowding one canvas.',"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('python_retail_sales.csv')
fig, axes = plt.subplots(1, 2, figsize=(9,3))
axes[0].hist(df['revenue'], bins=12)
axes[0].set_title('Revenue')
axes[1].hist(df['margin'].dropna(), bins=12)
axes[1].set_title('Margin')
fig.tight_layout()
plt.show()
""",[('subplot','One Axes in a multi-panel Figure.'),('small multiple','Repeated chart separated by group.'),('shared scale','Common axis range used across panels.'),('tight_layout','Layout adjustment reducing overlap.')],packages=['pandas','matplotlib'])
add('labels-legends-and-annotations','07','Labels, Legends, and Annotations','Label, Legend ও Annotation','Titles, axis labels, legends, notes, and annotations give a chart the context needed for interpretation.','Label units and time periods, use legends only when necessary, and annotate evidence rather than decoration.',"""
import matplotlib.pyplot as plt
months = ['Jan','Feb','Mar','Apr']
sales = [100,120,115,150]
fig, ax = plt.subplots()
ax.plot(months, sales, marker='o', label='Sales')
ax.annotate('Campaign', xy=('Apr',150), xytext=('Mar',160), arrowprops={'arrowstyle':'->'})
ax.set(title='Monthly sales', ylabel='BDT thousands')
ax.legend()
plt.show()
""",[('Axis label','Text describing a scale and unit.'),('Legend','Key identifying visual encodings.'),('Annotation','Text attached to a specific data point.'),('title','Concise statement of chart subject or finding.')],packages=['matplotlib'])
add('responsible-chart-formatting','07','Responsible Chart Formatting','Responsible Chart Formatting','Responsible formatting preserves proportional scales, readable labels, accessible contrast, and honest context.','Do not truncate bar axes, hide uncertainty, overload color, or remove important comparisons.',"""
import matplotlib.pyplot as plt
categories = ['A','B','C']
values = [92,95,98]
fig, ax = plt.subplots()
ax.bar(categories, values)
ax.set_ylim(0, 105)
ax.set(title='Scores with a zero baseline', ylabel='Score')
plt.show()
""",[('Truncated axis','Axis starting away from a meaningful baseline.'),('contrast','Visual difference supporting readability.'),('uncertainty','Range or variability around an estimate.'),('accessibility','Design usable by people with varied needs.')],packages=['matplotlib'])
add('save-and-export-figures','07','Save and Export Figures','Figure Save ও Export','Matplotlib can save figures as raster or vector files with controlled size, resolution, background, and bounding box.','Choose formats based on delivery context and verify labels remain readable at final size.',"""
import io
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1,2,3],[3,2,4])
ax.set_title('Export-ready figure')
buffer = io.BytesIO()
fig.savefig(buffer, format='png', dpi=150, bbox_inches='tight')
print('PNG bytes:', len(buffer.getvalue()))
""",[('savefig','Method writing a figure to a file-like object.'),('DPI','Dots per inch for raster output.'),('raster','Pixel-based image format.'),('vector','Shape-based scalable image format.')],packages=['matplotlib'])

# 08 time series / reproducibility
add('datetime-index-and-time-series','08','Datetime Index and Time Series','Datetime Index ও Time Series','A time series is ordered by time, often using a DatetimeIndex for slicing, resampling, and rolling analysis.','Confirm time zone, frequency, duplicates, and missing periods before calculating trends.',"""
import pandas as pd
df = pd.read_csv('python_retail_sales.csv', parse_dates=['order_date'])
ts = df.set_index('order_date').sort_index()
print(ts.loc['2026-01':'2026-03', 'revenue'].head())
""",[('Time series','Observations ordered by time.'),('DatetimeIndex','pandas index containing datetime values.'),('frequency','Spacing between time observations.'),('time zone','Regional convention for clock time.')],packages=['pandas'])
add('resampling-time-series','08','Resample Time Series','Time Series Resample করুন','Resampling changes time frequency by grouping periods or generating new timestamps.','Choose sum for flows such as sales and mean or last value for measures with different meanings.',"""
import pandas as pd
df = pd.read_csv('python_retail_sales.csv', parse_dates=['order_date'])
monthly = df.set_index('order_date').resample('MS')['revenue'].sum()
print(monthly.head())
""",[('resampling','Changing time-series frequency.'),('downsampling','Aggregating to a lower frequency.'),('upsampling','Creating a higher-frequency index.'),('flow measure','Value accumulated over a period.')],packages=['pandas'])
add('rolling-windows','08','Rolling Windows and Moving Averages','Rolling Window ও Moving Average','A rolling window calculates each result from a moving set of recent observations.','Define window size, minimum periods, alignment, and whether the current period is included.',"""
import pandas as pd
s = pd.Series([100,120,90,130,150], index=pd.date_range('2026-01-01', periods=5, freq='MS'))
print(s.rolling(window=3, min_periods=1).mean())
""",[('rolling window','Moving group of adjacent observations.'),('moving average','Average calculated over a rolling window.'),('min_periods','Minimum observations required for a result.'),('alignment','Timestamp associated with a window result.')],packages=['pandas'])
add('reproducible-notebook-workflow','08','Reproducible Notebook Workflow','Reproducible Notebook Workflow','A reproducible notebook runs from a clean kernel in order, records dependencies and data sources, and separates parameters, transformations, outputs, and conclusions.','Restart and run all, remove hidden state, and keep raw data unchanged.',"""
from datetime import datetime, timezone
metadata = {'run_utc': datetime.now(timezone.utc).isoformat(), 'status':'complete'}
print(metadata)
""",[('hidden state','Variables existing from earlier out-of-order execution.'),('restart and run all','Notebook validation from a fresh kernel.'),('parameter','Value controlling analysis behavior.'),('run metadata','Information describing an execution.')])
add('manage-environments-and-requirements','08','Manage Environments and Requirements','Environment ও Requirement Manage','A requirements file or environment definition records project dependencies. Exact pins improve repeatability but require planned updates.','Separate application dependencies from transient tooling and test updates before adoption.',"""
requirements = ['numpy>=2.0','pandas>=3.0','matplotlib>=3.10','scipy>=1.16']
print('\\n'.join(requirements))
""",[('requirements file','Text file listing Python dependencies.'),('version constraint','Rule limiting acceptable package versions.'),('pin','Exact version requirement.'),('dependency update','Controlled change to a newer package release.')])
add('logging-and-quality-checks','08','Logging and Quality Checks','Logging ও Quality Check','Logging records important workflow events; assertions and tests verify expected conditions.','Log row counts and key decisions, and fail clearly when critical assumptions are violated.',"""
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
rows = 360
logging.info('Loaded %s rows', rows)
assert rows > 0, 'Dataset must not be empty'
print('Quality checks passed')
""",[('logging','Structured runtime messages.'),('assertion','Statement requiring a condition to be true.'),('test','Repeatable check of expected behavior.'),('quality gate','Condition required before progression.')])
add('write-analytical-outputs','08','Write Analytical Outputs','Analytical Output লিখুন','Analytical delivery can include cleaned data, summary tables, charts, notebooks, scripts, and a concise report.','Separate evidence from interpretation and include definitions, methods, limitations, and file lineage.',"""
import pandas as pd
summary = pd.DataFrame({'metric':['Revenue','Profit'],'value':[125000,42000]})
print(summary.to_string(index=False))
""",[('deliverable','Output provided to a stakeholder.'),('summary table','Compact table of key measures.'),('lineage','Documented origin and transformations.'),('limitation','Condition restricting interpretation.')],packages=['pandas'])
add('privacy-security-and-responsible-python','08','Privacy, Security, and Responsible Python','Privacy, Security ও Responsible Python','Analytical code can expose sensitive data through files, logs, notebooks, charts, or repository history.','Minimize personal data, avoid embedding secrets, sanitize outputs, and follow organizational access and retention rules.',"""
columns = ['customer_id','email','revenue']
public_columns = [c for c in columns if c not in {'email'}]
print('Approved for public output:', public_columns)
""",[('personal data','Information relating to an identifiable person.'),('secret','Credential such as password or API token.'),('data minimization','Using only data necessary for the purpose.'),('retention','Rules controlling how long data is kept.')])

# 09 project
add('python-project-brief-and-questions','09','Portfolio Project Part 1: Brief and Questions','Portfolio Project Part 1: Brief ও Question','The final project begins with stakeholder questions, metric definitions, data inventory, assumptions, and acceptance criteria.','Use the retail practice data to define a focused analysis before writing code.',"""
questions = [
    'How are revenue and profit changing over time?',
    'Which regions, channels, and products drive performance?',
    'Where are discounts associated with weak margin?'
]
for q in questions:
    print('-', q)
""",[('Project brief','Document defining purpose, audience, scope, and deliverables.'),('Stakeholder question','Decision-oriented question from an intended user.'),('Metric definition','Documented rule for calculating a measure.'),('acceptance criterion','Testable condition for completion.')],level='Advanced')
add('python-project-clean-and-validate','09','Portfolio Project Part 2: Clean and Validate','Portfolio Project Part 2: Clean ও Validate','The project must load source files, preserve raw data, profile quality, clean documented issues, and reconcile row counts and totals.','Produce a quality log and a clean analytical dataset rather than hiding corrections inside later calculations.',"""
import pandas as pd
df = pd.read_csv('python_retail_sales.csv', parse_dates=['order_date'])
checks = {
    'rows': len(df),
    'duplicate_order_lines': int(df.duplicated(['order_id','product_id']).sum()),
    'missing_revenue': int(df['revenue'].isna().sum()),
    'negative_revenue': int(df['revenue'].lt(0).sum()),
}
print(checks)
""",[('quality log','Record of detected issues and treatments.'),('reconciliation','Comparison proving values remain consistent.'),('clean dataset','Validated analysis-ready data.'),('raw preservation','Keeping source files unchanged.')],packages=['pandas'],level='Advanced')
add('python-project-analyze-and-visualize','09','Portfolio Project Part 3: Analyze and Visualize','Portfolio Project Part 3: Analyze ও Visualize','The analysis combines descriptive summaries, segment comparisons, time trends, distributions, relationships, and selected statistical methods.','Every chart and table should answer a named question and include a validation check.',"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('python_retail_sales.csv', parse_dates=['order_date'])
monthly = df.set_index('order_date').resample('MS').agg(revenue=('revenue','sum'), profit=('profit','sum'))
print(monthly.tail())
fig, ax = plt.subplots()
monthly['revenue'].plot(ax=ax, title='Monthly revenue')
ax.set_ylabel('BDT')
plt.show()
""",[('analytical evidence','Calculated or visual result supporting a finding.'),('segment analysis','Comparison across defined groups.'),('trend analysis','Evaluation of change over time.'),('visual validation','Check that chart values match underlying summaries.')],packages=['pandas','matplotlib'],level='Advanced')
add('python-project-report-and-publish','09','Portfolio Project Part 4: Report and Publish','Portfolio Project Part 4: Report ও Publish','A portfolio-ready project includes source data references, a clean notebook, reusable code, output files, a README, findings, limitations, and instructions to reproduce the work.','Publish only synthetic or authorized data and distinguish evidence from recommendation.',"""
deliverables = ['README.md','notebooks/retail_analysis.ipynb','src/analysis.py','outputs/summary.csv','outputs/revenue_trend.png','requirements.txt']
for item in deliverables:
    print(item)
""",[('README','Project documentation and reproduction guide.'),('portfolio','Curated evidence of skills and decisions.'),('finding','Evidence-based statement from analysis.'),('recommendation','Proposed action informed by evidence and context.')],level='Advanced')

assert len(S) == 94, len(S)

def chapter(spec: dict) -> dict:
    title,bn,concept,use,code = spec['title'],spec['bn'],spec['concept'],spec['use'],spec['code']
    terms=[{'term_en':t,'term_bn':t,'definition_en':d,'definition_bn':f'{t}: {d} Chapter-এর example ও code দিয়ে term-টির ব্যবহার যাচাই করুন।'} for t,d in spec['terms']]
    refs=[{'title':'Python 3 documentation','url':PYTHON},{'title':'pandas documentation','url':PANDAS}]
    if 'numpy' in spec['packages']: refs[1]={'title':'NumPy documentation','url':NUMPY}
    if 'matplotlib' in spec['packages']: refs[1]={'title':'Matplotlib documentation','url':MATPLOTLIB}
    if 'scipy' in spec['packages']: refs.append({'title':'SciPy documentation','url':SCIPY})
    concept_body = concept if len(concept) >= 120 else concept + f' In analytical work, {title.lower()} should be connected to a clearly defined question, known row grain, and a validation check so the result can be reviewed and repeated.'
    concept_body_bn = f'{bn} data analytics workflow-এ কেন প্রয়োজন, কী input নেয়, কীভাবে process হয় এবং কী output দেয়—সেটি সহজ ভাষায় বুঝুন। বাস্তব কাজে question, row grain, input type ও validation check স্পষ্ট না হলে result ভুলভাবে interpret হতে পারে।'
    sections=[
        {'title_en':f'What {title} means','title_bn':f'{bn} কী','body_en':concept_body,'body_bn':concept_body_bn,'code':code,'code_label':'Python'},
        {'title_en':'How an analyst uses it','title_bn':'Analyst কীভাবে ব্যবহার করেন','body_en':use+' Define the question and data grain first, then validate the output before interpretation.','body_bn':f'Analyst {bn} ব্যবহার করার আগে business question ও data grain define করেন, code run করেন, output validate করেন এবং limitation লিখে রাখেন।'},
        {'title_en':'Rules, checks, and common mistakes','title_bn':'Rule, check ও common mistake','body_en':'Common mistakes include trusting inferred data types, changing raw data, writing long stateful notebooks, ignoring missing values, confusing row and group grain, and reporting output without validation. Use small reproducible steps and preserve evidence.','body_bn':'Common mistake হলো inferred type trust করা, raw data বদলে ফেলা, long stateful notebook লেখা, missing value ignore করা, row ও group grain mix করা এবং validation ছাড়া output report করা।'},
    ]
    worked={
        'title_en':f'Worked example: {title}','title_bn':f'Worked example: {bn}',
        'context_en':f'A retail analyst applies {title.lower()} to the supplied synthetic retail dataset and must produce a result another reviewer can rerun.',
        'context_bn':f'একজন retail analyst supplied synthetic retail dataset-এ {bn} apply করে reproducible result তৈরি করবেন।',
        'steps_en':['State the analytical question, row grain, required fields, and expected result.','Run the starter code and inspect both the output and the underlying input.','Change one value, condition, or parameter and explain why the result changes.','Validate row counts, totals, types, assumptions, and limitations before communicating.'],
        'steps_bn':['Analytical question, row grain, required field ও expected result লিখুন।','Starter code run করে output এবং underlying input inspect করুন।','একটি value, condition বা parameter বদলে result কেন change হয় explain করুন।','Communicate করার আগে row count, total, type, assumption ও limitation validate করুন।'],
        'conclusion_en':f'{title} is useful only when code, data grain, validation evidence, and interpretation agree.','conclusion_bn':f'{bn} তখনই useful যখন code, data grain, validation evidence ও interpretation পরস্পরের সঙ্গে consistent।'
    }
    mcq={'type':'mcq','prompt_en':f'Which practice makes {title} most reliable?','prompt_bn':f'{bn} সবচেয়ে reliable করতে কোন practice সঠিক?','options_en':['Run code once and trust the output','Define grain and assumptions, run reproducibly, and validate the result','Add more code until the notebook looks advanced'],'options_bn':['একবার code run করে output trust করা','Grain ও assumption define করে reproducibly run এবং result validate করা','Notebook advanced দেখাতে আরও code add করা'],'answer_en':'B','answer_bn':'B','explanation_en':'Reliable analysis connects the question, data grain, code, validation, and interpretation.','explanation_bn':'Reliable analysis question, data grain, code, validation ও interpretation-কে connect করে।'}
    fill={'type':'fill','prompt_en':f'Complete the key term: {spec["fill"][:1]}____','prompt_bn':f'Key term complete করুন: {spec["fill"][:1]}____','answer_en':spec['fill'],'answer_bn':spec['fill'],'explanation_en':f'The expected term is {spec["fill"]}.','explanation_bn':f'Expected term হলো {spec["fill"]}।'}
    short={'type':'short','prompt_en':f'Describe one business question that needs {title}. Name the input, expected output, and one validation check.','prompt_bn':f'{bn} প্রয়োজন এমন একটি business question লিখুন। Input, expected output ও একটি validation check উল্লেখ করুন।','answer_en':'A strong response states the decision question, row grain, required fields, method, expected output, and a concrete check such as row-count reconciliation, dtype validation, total comparison, boundary test, or chart-to-table comparison.','answer_bn':'Strong response-এ decision question, row grain, required field, method, expected output এবং row-count reconciliation, dtype validation, total comparison, boundary test বা chart-to-table comparison-এর মতো concrete check থাকবে।'}
    return {'id':spec['id'],'module':spec['module'],'level':spec['level'],'title_en':title,'title_bn':bn,'summary_en':concept,'summary_bn':f'{bn} ব্যবহার করে reproducible data analytics workflow তৈরি করার পদ্ধতি শিখুন।','minutes':45 if spec['level']=='Beginner' else 60,'objectives':[{'en':f'Explain {title} in plain language.','bn':f'সহজ ভাষায় {bn} explain করুন।'},{'en':'Run and modify the Python example.','bn':'Python example run ও modify করুন।'},{'en':'Apply the concept to an analytical question.','bn':'Analytical question-এ concept apply করুন।'},{'en':'Validate the output and communicate one limitation.','bn':'Output validate করে একটি limitation communicate করুন।'}],'sections':sections,'terms':terms,'worked_example':worked,'activity':{'type':'python-playground','prompt_en':f'Run the Python example for {title}. Change one input or rule and explain the new result.','prompt_bn':f'{bn}-এর Python example run করুন। একটি input বা rule বদলে নতুন result explain করুন।','code':code,'packages':spec['packages'],'dataset':'/assets/datasets/python_retail_sales.csv'},'exercises':[mcq,fill,short],'recap':[{'en':concept.split('.')[0]+'.','bn':f'{bn} business question ও data grain-এর সঙ্গে ব্যবহার করতে হবে।'},{'en':'Prefer explicit, readable, reproducible code over hidden state and manual corrections.','bn':'Hidden state ও manual correction-এর বদলে explicit, readable, reproducible code ব্যবহার করুন।'},{'en':'Inspect types, missing values, row counts, and totals before trusting output.','bn':'Output trust করার আগে type, missing value, row count ও total inspect করুন।'},{'en':'Document assumptions, limitations, versions, and evidence.','bn':'Assumption, limitation, version ও evidence document করুন।'}],'references':refs}

chapters=[chapter(x) for x in S]
tutorial={
'id':'python-data-analytics','title_en':'Python for Data Analytics Tutorial','title_bn':'Data Analytics-এর জন্য Python Tutorial','short_title_en':'Python Analytics','short_title_bn':'Python Analytics','description_en':'A complete analyst-first Python tutorial covering Python foundations, Jupyter, NumPy, pandas, cleaning, transformation, exploratory analysis, statistics, Matplotlib, time series, reproducibility, browser practice, and a portfolio project.','description_bn':'Python foundation, Jupyter, NumPy, pandas, cleaning, transformation, exploratory analysis, statistics, Matplotlib, time series, reproducibility, browser practice ও portfolio project-এর complete analyst-first tutorial।','status':'published','version':'2.5.0','estimated_hours':85,'modules':modules,'chapters':chapters,'final_quiz':{'title_en':'Python for Data Analytics Final Quiz','title_bn':'Python for Data Analytics Final Quiz','pass_percent':75},
'reference_groups':[
 {'title_en':'Python and Jupyter','title_bn':'Python ও Jupyter','references':[{'title':'Python 3.14 documentation','url':'https://docs.python.org/3.14/'},{'title':'The Python Tutorial','url':'https://docs.python.org/3/tutorial/'},{'title':'Project Jupyter','url':'https://jupyter.org/'},{'title':'Installing Jupyter','url':'https://jupyter.org/install'}]},
 {'title_en':'NumPy, pandas, and SciPy','title_bn':'NumPy, pandas ও SciPy','references':[{'title':'NumPy user guide','url':'https://numpy.org/doc/stable/user/'},{'title':'pandas user guide','url':'https://pandas.pydata.org/docs/user_guide/'},{'title':'10 minutes to pandas','url':'https://pandas.pydata.org/docs/user_guide/10min.html'},{'title':'SciPy documentation','url':'https://docs.scipy.org/doc/scipy/'}]},
 {'title_en':'Visualization and browser runtime','title_bn':'Visualization ও browser runtime','references':[{'title':'Matplotlib quick start','url':'https://matplotlib.org/stable/users/explain/quick_start.html'},{'title':'Matplotlib tutorials','url':'https://matplotlib.org/stable/tutorials/'},{'title':'Pyodide documentation','url':'https://pyodide.org/en/stable/'},{'title':'Using Pyodide','url':'https://pyodide.org/en/stable/usage/'}]},
],
'downloads':[
 {'title_en':'Python Retail Practice Package (ZIP)','title_bn':'Python Retail Practice Package (ZIP)','url':'/assets/downloads/python-retail-analytics-practice-package.zip'},
 {'title_en':'Starter Jupyter Notebook','title_bn':'Starter Jupyter Notebook','url':'/assets/downloads/python-retail-analytics-starter.ipynb'},
 {'title_en':'Completed Example Notebook','title_bn':'Completed Example Notebook','url':'/assets/downloads/python-retail-analytics-completed.ipynb'},
 {'title_en':'Python Practice Scripts','title_bn':'Python Practice Script','url':'/assets/downloads/python-analytics-practice-scripts.py'},
 {'title_en':'Requirements File','title_bn':'Requirements File','url':'/assets/downloads/python-analytics-requirements.txt'},
 {'title_en':'Python Data Dictionary','title_bn':'Python Data Dictionary','url':'/assets/datasets/python_retail_data_dictionary.csv'},
]}
OUT.write_text(json.dumps(tutorial,ensure_ascii=False,indent=2),encoding='utf-8')

# Synthetic retail datasets
rng=random.Random(250)
regions=['Dhaka','Chattogram','Khulna','Rajshahi']
channels=['Online','Retail','Partner']
categories=['Apparel','Electronics','Accessories','Stationery']
products=[('P101','Shirt','Apparel',800),('P102','Polo Shirt','Apparel',1100),('P103','Trousers','Apparel',1500),('P104','Keyboard','Electronics',2200),('P105','Monitor','Electronics',14500),('P106','Headset','Electronics',3200),('P107','Backpack','Accessories',1800),('P108','Laptop Stand','Accessories',1600),('P109','Notebook','Stationery',180),('P110','Pen Set','Stationery',350),('P111','Desk Lamp','Accessories',2200),('P112','Webcam','Electronics',4200)]
start=date(2025,1,1)
rows=[]
for i in range(1,721):
    d=start+timedelta(days=rng.randrange(0,730))
    pid,pname,category,base=products[rng.randrange(len(products))]
    qty=rng.randrange(1,8); discount=[0,0,0.05,0.10,0.15][rng.randrange(5)]
    unit=round(base*(0.93+rng.random()*0.15),2); revenue=round(qty*unit*(1-discount),2)
    cost=round(revenue*(0.58+rng.random()*0.18),2); profit=round(revenue-cost,2)
    rows.append([f'O{i:04d}',d.isoformat(),f'C{rng.randrange(1,121):03d}',pid,pname,category,regions[rng.randrange(4)],channels[rng.randrange(3)],qty,unit,discount,revenue,cost,profit,round(profit/revenue,4) if revenue else None])
headers=['order_id','order_date','customer_id','product_id','product_name','category','region','channel','quantity','unit_price','discount','revenue','cost','profit','margin']
with (DS/'python_retail_sales.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f);w.writerow(headers);w.writerows(rows)
customers=[]
segments=['Consumer','Corporate','Small Business']
for i in range(1,121): customers.append([f'C{i:03d}',segments[i%3],regions[(i*3)%4],(date(2024,1,1)+timedelta(days=i*4)).isoformat(), 'Active' if i%9 else 'Inactive'])
with (DS/'python_customers.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f);w.writerow(['customer_id','segment','home_region','signup_date','status']);w.writerows(customers)
# deliberately messy sample
messy=[['order_id','order_date','region','revenue','status'],['O001','01/02/2026',' dhaka','1200','complete'],['O001','01/02/2026','DHAKA ','1200','complete'],['O002','not-a-date','Ctg','-50','pending'],['O003','2026-02-05','Khulna','','Complete']]
with (DS/'python_messy_orders.csv').open('w',newline='',encoding='utf-8') as f: csv.writer(f).writerows(messy)

# Dictionary
with (DS/'python_retail_data_dictionary.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f);w.writerow(['file','field','type','description'])
    desc={'order_id':'Synthetic order identifier','order_date':'Order date in ISO format','customer_id':'Synthetic customer identifier','product_id':'Product key','product_name':'Product label','category':'Product category','region':'Sales region','channel':'Sales channel','quantity':'Units sold','unit_price':'Unit price in BDT','discount':'Proportional discount','revenue':'Net revenue in BDT','cost':'Estimated cost in BDT','profit':'Revenue minus cost','margin':'Profit divided by revenue'}
    for h in headers:w.writerow(['python_retail_sales.csv',h,'number' if h in {'quantity','unit_price','discount','revenue','cost','profit','margin'} else 'date' if h=='order_date' else 'text',desc[h]])
    for h,d in [('customer_id','Customer key'),('segment','Customer segment'),('home_region','Customer home region'),('signup_date','Signup date'),('status','Customer status')]:w.writerow(['python_customers.csv',h,'date' if h=='signup_date' else 'text',d])

# Script library
script='''"""Practice functions for the Data Learning Hub Python Analytics course."""\nfrom pathlib import Path\nimport pandas as pd\n\ndef load_sales(path="python_retail_sales.csv"):\n    df = pd.read_csv(path, parse_dates=["order_date"])\n    df["margin"] = df["profit"].div(df["revenue"]).where(df["revenue"].ne(0))\n    return df\n\ndef quality_report(df):\n    return pd.DataFrame({"dtype": df.dtypes.astype(str), "missing": df.isna().sum(), "unique": df.nunique(dropna=False)})\n\ndef regional_summary(df):\n    return df.groupby("region", as_index=False).agg(orders=("order_id","nunique"), revenue=("revenue","sum"), profit=("profit","sum"))\n\nif __name__ == "__main__":\n    sales = load_sales()\n    print(quality_report(sales))\n    print(regional_summary(sales))\n'''
(DL/'python-analytics-practice-scripts.py').write_text(script,encoding='utf-8')
(DL/'python-analytics-requirements.txt').write_text('numpy>=2.0\npandas>=3.0\nmatplotlib>=3.10\nscipy>=1.16\njupyterlab>=4\nopenpyxl>=3.1\n',encoding='utf-8')

# Notebooks
starter=nbf.v4.new_notebook(); starter['metadata']={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python','version':'3.14'}}
starter['cells']=[nbf.v4.new_markdown_cell('# Python Retail Analytics — Starter\nUse the supplied synthetic CSV files. Restart and run all before delivery.'),nbf.v4.new_code_cell("from pathlib import Path\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt"),nbf.v4.new_code_cell("DATA = Path('.')\nsales = pd.read_csv(DATA / 'python_retail_sales.csv', parse_dates=['order_date'])\nsales.head()"),nbf.v4.new_markdown_cell('## 1. Quality audit\nProfile shape, types, missing values, duplicates, ranges, and key uniqueness.'),nbf.v4.new_code_cell("# Your quality-audit code"),nbf.v4.new_markdown_cell('## 2. Analysis\nCalculate revenue, profit, margin, trends, and segment comparisons.'),nbf.v4.new_code_cell("# Your analytical code"),nbf.v4.new_markdown_cell('## 3. Visualization and findings\nCreate decision-ready charts and write findings with limitations.'),nbf.v4.new_code_cell("# Your visualization code")]
nbf.write(starter,DL/'python-retail-analytics-starter.ipynb')
completed=nbf.v4.new_notebook();completed['metadata']=starter['metadata'];completed['cells']=[nbf.v4.new_markdown_cell('# Python Retail Analytics — Completed Example\nSynthetic educational data.'),nbf.v4.new_code_cell("from pathlib import Path\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nDATA = Path('.')"),nbf.v4.new_code_cell("sales = pd.read_csv(DATA / 'python_retail_sales.csv', parse_dates=['order_date'])\nprint(sales.shape)\nprint(sales.isna().sum().sort_values(ascending=False).head())\nprint('Duplicates:', sales.duplicated(['order_id','product_id']).sum())"),nbf.v4.new_code_cell("summary = sales.groupby('region', as_index=False).agg(orders=('order_id','nunique'), revenue=('revenue','sum'), profit=('profit','sum'))\nsummary['margin'] = summary['profit']/summary['revenue']\nsummary.sort_values('revenue', ascending=False)"),nbf.v4.new_code_cell("monthly = sales.set_index('order_date').resample('MS').agg(revenue=('revenue','sum'),profit=('profit','sum'))\nax = monthly['revenue'].plot(title='Monthly revenue', figsize=(9,4))\nax.set_ylabel('BDT')\nplt.show()"),nbf.v4.new_markdown_cell('## Interpretation\nUse the output to write evidence, implication, limitation, and next action. Validate totals before publication.')]
nbf.write(completed,DL/'python-retail-analytics-completed.ipynb')

# Package zip
zip_path=DL/'python-retail-analytics-practice-package.zip'
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
    for p in [DS/'python_retail_sales.csv',DS/'python_customers.csv',DS/'python_messy_orders.csv',DS/'python_retail_data_dictionary.csv',DL/'python-retail-analytics-starter.ipynb',DL/'python-retail-analytics-completed.ipynb',DL/'python-analytics-practice-scripts.py',DL/'python-analytics-requirements.txt']:
        z.write(p,p.name)
print(f'Built {len(chapters)} Python chapters and practice package.')
