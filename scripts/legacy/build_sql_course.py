from __future__ import annotations
import csv, json, random
from pathlib import Path
from datetime import date, timedelta

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'content/tutorials/sql_data_analytics.json'
DL=ROOT/'assets/downloads'
DS=ROOT/'assets/datasets'
DL.mkdir(parents=True,exist_ok=True); DS.mkdir(parents=True,exist_ok=True)

PG='https://www.postgresql.org/docs/current/'
SQLITE='https://www.sqlite.org/lang.html'
SQLJS='https://github.com/sql-js/sql.js/'

modules=[
 {'id':'01','title_en':'SQL and Relational Foundations','title_bn':'SQL ও Relational Foundation'},
 {'id':'02','title_en':'Select, Filter, and Sort','title_bn':'Select, Filter ও Sort'},
 {'id':'03','title_en':'Expressions and Functions','title_bn':'Expression ও Function'},
 {'id':'04','title_en':'Aggregation and Business Metrics','title_bn':'Aggregation ও Business Metric'},
 {'id':'05','title_en':'Joins and Set Operations','title_bn':'Join ও Set Operation'},
 {'id':'06','title_en':'Subqueries and CTEs','title_bn':'Subquery ও CTE'},
 {'id':'07','title_en':'Window Functions and Analytical Patterns','title_bn':'Window Function ও Analytical Pattern'},
 {'id':'08','title_en':'Data Modeling, Quality, and Performance','title_bn':'Data Modeling, Quality ও Performance'},
 {'id':'09','title_en':'Portfolio Analytics Projects','title_bn':'Portfolio Analytics Project'},
]

# id, module, level, title, bn, concept, analyst_use, code, lab_query, fill_answer, terms
C=[]
def add(id,module,title,bn,concept,use,code,query,fill,terms,level='Beginner'):
 C.append(dict(id=id,module=module,title=title,bn=bn,concept=concept,use=use,code=code,query=query,fill=fill,terms=terms,level=level))

add('welcome-to-sql-analytics','01','Welcome to SQL for Data Analytics','Data Analytics-এর জন্য SQL-এ স্বাগতম',
    'SQL is a declarative language for asking a relational database to return, combine, summarize, or change data. You describe the result you need; the database engine decides how to execute the request.',
    'Analysts use SQL to retrieve trustworthy rows from operational systems, calculate repeatable metrics, prepare datasets for dashboards, and investigate business questions without copying data manually between files.',
    "SELECT order_id, order_date, status\nFROM orders\nORDER BY order_date DESC\nLIMIT 5;",
    "SELECT order_id, order_date, status FROM orders ORDER BY order_date DESC LIMIT 5;",'SELECT',
    [('SQL','Structured Query Language used to work with relational data.'),('Query','A statement sent to a database.'),('Database','An organized collection of related data.'),('Result set','Rows and columns returned by a query.')])
add('relational-databases-and-tables','01','Relational Databases and Tables','Relational Database ও Table',
    'A relational database stores data in tables. Each table represents one kind of entity or event, each row represents one occurrence, and each column represents one defined attribute.',
    'A clear table grain lets an analyst know what one row means. Without that grain, counts, joins, and totals can be duplicated or misinterpreted.',
    "SELECT name, type\nFROM sqlite_master\nWHERE type = 'table'\nORDER BY name;",
    "SELECT name AS table_name FROM sqlite_master WHERE type='table' ORDER BY name;",'table',
    [('Table','A named set of rows with defined columns.'),('Row','One record at the table grain.'),('Column','A named attribute with a data type.'),('Grain','The real-world meaning of one row.')])
add('sql-dialects-postgresql-and-sqlite','01','SQL Dialects: PostgreSQL and SQLite','SQL Dialect: PostgreSQL ও SQLite',
    'Core SQL ideas are portable, but database systems implement different functions, data types, date syntax, and administrative features. This course teaches PostgreSQL-oriented analytical SQL while the in-browser lab executes SQLite.',
    'Recognizing dialect differences prevents analysts from copying a query that looks valid but uses a function unavailable in the target platform. The analytical logic can often be translated while preserving the question.',
    "-- PostgreSQL\nSELECT DATE_TRUNC('month', order_date) AS month\nFROM orders;\n\n-- SQLite lab equivalent\nSELECT strftime('%Y-%m-01', order_date) AS month\nFROM orders;",
    "SELECT strftime('%Y-%m-01', order_date) AS month, COUNT(*) AS orders FROM orders GROUP BY 1 ORDER BY 1;",'dialect',
    [('Dialect','A database system’s implementation of SQL.'),('PostgreSQL','The primary teaching dialect for production-style SQL.'),('SQLite','The embedded engine used in the browser practice environment.'),('Portability','How easily SQL logic moves between systems.')])
add('practice-database-schema','01','Explore the Practice Database Schema','Practice Database Schema Explore করুন',
    'A schema describes tables, columns, keys, and relationships. Before writing analytical SQL, inspect the schema and identify the grain and join keys of every table you plan to use.',
    'Schema inspection reduces guesswork. It helps an analyst choose the correct table, avoid joining unrelated columns, and understand whether a value is stored directly or must be calculated.',
    "PRAGMA table_info('orders');",
    "PRAGMA table_info('orders');",'schema',
    [('Schema','The structural definition of database objects.'),('Primary key','A column or set of columns that uniquely identifies a row.'),('Foreign key','A column that references a row in another table.'),('Relationship','A defined connection between table records.')])
add('select-fundamentals','01','SELECT Fundamentals','SELECT Foundation',
    'SELECT chooses the expressions and columns that will appear in a result. FROM identifies the source table. Selecting only required columns makes the result easier to read and usually reduces unnecessary data movement.',
    'Analysts use focused SELECT lists to create understandable datasets for review, export, dashboards, and downstream calculations. SELECT * is useful for quick exploration but weak for stable production queries.',
    "SELECT customer_id, customer_name, segment\nFROM customers;",
    "SELECT customer_id, customer_name, segment FROM customers ORDER BY customer_id LIMIT 10;",'FROM',
    [('SELECT','Clause that defines returned columns or expressions.'),('FROM','Clause that identifies source tables.'),('Expression','A calculation or value returned as a column.'),('Projection','Choosing the columns included in a result.')])
add('aliases-comments-and-formatting','01','Aliases, Comments, and Readable Formatting','Alias, Comment ও Readable Formatting',
    'Aliases rename output columns or tables for clarity. Comments explain intent. Consistent indentation separates clauses and makes logic reviewable without changing the query result.',
    'Readable SQL is a control mechanism. Analysts frequently revisit queries months later or hand them to reviewers, so names and formatting should expose the business meaning rather than hide it.',
    "SELECT\n  o.order_id,\n  o.order_date AS purchased_on,\n  o.status\nFROM orders AS o\n-- Keep completed and shipped orders\nWHERE o.status IN ('Completed', 'Shipped');",
    "SELECT o.order_id, o.order_date AS purchased_on, o.status FROM orders AS o WHERE o.status IN ('Completed','Shipped') ORDER BY o.order_id LIMIT 8;",'AS',
    [('Alias','A temporary name assigned in a query.'),('Comment','Text ignored by the SQL engine and used for explanation.'),('Indentation','Visual spacing that exposes query structure.'),('Naming convention','A consistent rule for object and alias names.')])
add('logical-query-processing-order','01','Logical Query Processing Order','Logical Query Processing Order',
    'Although SELECT appears first in written SQL, a query is logically evaluated from its row sources and filters toward grouping, final selection, sorting, and limiting. This explains why some aliases are unavailable in WHERE.',
    'Understanding logical order helps an analyst debug missing rows, invalid alias references, and aggregation errors. It also encourages calculations to be placed in the stage where their inputs exist.',
    "FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT",
    "SELECT region, COUNT(*) AS order_count FROM orders WHERE status <> 'Cancelled' GROUP BY region HAVING COUNT(*) >= 2 ORDER BY order_count DESC;",'WHERE',
    [('Logical order','Conceptual order in which query clauses are evaluated.'),('Row source','Tables or derived tables available to a query.'),('Filter stage','The point at which rows or groups are removed.'),('Output stage','The point at which selected expressions are returned.')])

# Module 02
add('distinct-values','02','DISTINCT Values','DISTINCT Value',
    'DISTINCT removes duplicate combinations from the selected output columns. It does not repair duplicate source rows; it only changes the returned result.',
    'Analysts use DISTINCT to inspect category domains and identify possible duplicates, but should investigate why duplicates exist before using DISTINCT as a permanent fix.',
    "SELECT DISTINCT region, channel\nFROM orders\nORDER BY region, channel;",
    "SELECT DISTINCT region, channel FROM orders ORDER BY region, channel;",'DISTINCT',
    [('DISTINCT','Removes duplicate output rows.'),('Combination','The complete set of selected values considered for uniqueness.'),('Duplicate','A repeated record or repeated selected combination.'),('Domain','The observed set of values in a field.')])
add('where-filtering','02','Filter Rows with WHERE','WHERE দিয়ে Row Filter',
    'WHERE keeps only rows whose condition evaluates to true. It is applied before grouping, which makes it the correct place to restrict dates, statuses, customers, or other row-level conditions.',
    'Row filters define the analytical population. A missing or incorrect WHERE condition can change every downstream KPI, so filters should be explicit and documented.',
    "SELECT order_id, order_date, region\nFROM orders\nWHERE region = 'Dhaka';",
    "SELECT order_id, order_date, region, status FROM orders WHERE region='Dhaka' ORDER BY order_date;",'WHERE',
    [('Predicate','A condition that evaluates to true, false, or unknown.'),('Filter','A rule that removes rows from the result.'),('Population','The set of rows included in the analysis.'),('Condition','A logical test used by a clause.')])
add('comparison-operators','02','Comparison Operators','Comparison Operator',
    'Comparison operators test equality, inequality, and order. Text comparisons depend on collation and case rules, while numerical and date comparisons depend on valid data types.',
    'Analysts use comparisons to define thresholds, date boundaries, exceptions, and segments. Values should be compared to compatible types rather than relying on accidental text conversion.',
    "SELECT product_name, list_price\nFROM products\nWHERE list_price >= 50;",
    "SELECT product_id, product_name, list_price FROM products WHERE list_price >= 50 ORDER BY list_price DESC;",'>=',
    [('Comparison operator','Symbol such as =, <>, >, or <= used to compare values.'),('Equality','A test that two values are the same.'),('Inequality','A test that values differ or fall on different sides of a threshold.'),('Collation','Rules used to compare and order text.')])
add('and-or-not','02','Combine Conditions with AND, OR, and NOT','AND, OR ও NOT দিয়ে Condition Combine',
    'AND requires all connected predicates to be true. OR requires at least one. NOT reverses a condition. Parentheses make precedence explicit and protect the intended population.',
    'Complex business filters often mix several rules. Analysts should group related conditions with parentheses and test intermediate counts to ensure OR does not accidentally include too many rows.',
    "SELECT order_id, region, channel, status\nFROM orders\nWHERE region = 'Dhaka'\n  AND (channel = 'Online' OR channel = 'Retail')\n  AND NOT status = 'Cancelled';",
    "SELECT order_id, region, channel, status FROM orders WHERE region='Dhaka' AND (channel='Online' OR channel='Retail') AND NOT status='Cancelled' ORDER BY order_id;",'AND',
    [('AND','Logical operator requiring every condition to be true.'),('OR','Logical operator requiring at least one condition to be true.'),('NOT','Logical operator that reverses a condition.'),('Precedence','Rules controlling which condition is evaluated first.')])
add('in-and-between','02','IN and BETWEEN','IN ও BETWEEN',
    'IN compares a value with a defined list. BETWEEN tests an inclusive lower and upper boundary. Both improve readability when the business rule naturally uses a set or range.',
    'Analysts use IN for category selections and BETWEEN for numeric or date bands. Because BETWEEN is inclusive, exact boundary treatment should be checked against the reporting definition.',
    "SELECT order_id, order_date, region\nFROM orders\nWHERE region IN ('Dhaka', 'Chattogram')\n  AND order_date BETWEEN '2026-01-01' AND '2026-03-31';",
    "SELECT order_id, order_date, region FROM orders WHERE region IN ('Dhaka','Chattogram') AND order_date BETWEEN '2026-01-01' AND '2026-03-31' ORDER BY order_date;",'BETWEEN',
    [('IN','Tests whether a value belongs to a list or subquery.'),('BETWEEN','Tests an inclusive range.'),('Boundary','The lower or upper edge of a range.'),('Inclusive','Including the stated endpoints.')])
add('like-and-pattern-matching','02','LIKE and Pattern Matching','LIKE ও Pattern Matching',
    'LIKE matches text patterns. The percent sign represents any sequence of characters and the underscore represents one character. Pattern matching can be case-sensitive or insensitive depending on the system.',
    'Analysts use patterns to inspect product codes, names, email domains, and inconsistent categories. Broad leading wildcards can be expensive on large databases and may signal a data-standardization problem.',
    "SELECT customer_name, city\nFROM customers\nWHERE customer_name LIKE 'A%';",
    "SELECT customer_id, customer_name, city FROM customers WHERE customer_name LIKE 'A%' ORDER BY customer_name;",'LIKE',
    [('LIKE','Operator for simple text pattern matching.'),('Wildcard','A symbol representing unknown characters.'),('Prefix search','Pattern matching from the start of text.'),('Case sensitivity','Whether uppercase and lowercase are treated as different.')])
add('null-and-three-valued-logic','02','NULL and Three-Valued Logic','NULL ও Three-Valued Logic',
    'NULL represents a missing or unknown value, not zero or an empty string. Comparisons with NULL do not return true or false; they return unknown, so IS NULL and IS NOT NULL are required.',
    'Missing values affect counts, averages, joins, and classifications. Analysts must distinguish genuinely unknown values from not-applicable values and decide how each metric handles them.',
    "SELECT customer_id, customer_name, city\nFROM customers\nWHERE city IS NULL;",
    "SELECT customer_id, customer_name, city FROM customers WHERE city IS NULL ORDER BY customer_id;",'IS NULL',
    [('NULL','A marker for missing or unknown data.'),('Unknown','The third logical state produced by some NULL comparisons.'),('IS NULL','Predicate used to identify NULL values.'),('Not applicable','A business reason a value may intentionally be absent.')])
add('order-by-limit-offset','02','ORDER BY, LIMIT, and OFFSET','ORDER BY, LIMIT ও OFFSET',
    'ORDER BY defines result order. LIMIT restricts returned rows, and OFFSET skips rows. Without ORDER BY, a database does not guarantee a stable display sequence.',
    'Analysts use ordering for top lists and quality review. LIMIT is useful for exploration, while OFFSET pagination can become inefficient or unstable when the underlying data changes.',
    "SELECT order_id, order_date, region\nFROM orders\nORDER BY order_date DESC, order_id DESC\nLIMIT 10 OFFSET 0;",
    "SELECT order_id, order_date, region, status FROM orders ORDER BY order_date DESC, order_id DESC LIMIT 10 OFFSET 0;",'ORDER BY',
    [('ORDER BY','Clause that defines result sorting.'),('LIMIT','Maximum number of rows returned.'),('OFFSET','Number of rows skipped before returning results.'),('Deterministic order','An order fully defined by one or more columns.')])

# Module 03
add('arithmetic-expressions','03','Arithmetic Expressions','Arithmetic Expression',
    'SQL expressions can add, subtract, multiply, divide, and combine stored values. Parentheses make business formulas explicit, and numeric type behavior should be checked to avoid unintended integer division or rounding.',
    'Analysts calculate revenue, cost, margin, discount, and unit economics directly in queries so the logic is repeatable and can be reviewed beside the source fields.',
    "SELECT quantity, unit_price, discount_pct,\n       quantity * unit_price * (1 - discount_pct) AS net_revenue\nFROM order_items;",
    "SELECT order_item_id, quantity, unit_price, discount_pct, ROUND(quantity*unit_price*(1-discount_pct),2) AS net_revenue FROM order_items ORDER BY order_item_id LIMIT 12;",'ROUND',
    [('Expression','A combination of values, columns, operators, and functions.'),('Operator precedence','Rules determining calculation order.'),('Derived column','A result calculated rather than stored.'),('Net revenue','Revenue after a stated discount rule.')])
add('case-expressions','03','CASE Expressions','CASE Expression',
    'CASE returns a value based on ordered conditions. The first matching WHEN branch wins, so ranges must be arranged carefully and an ELSE branch should handle unexpected values.',
    'Analysts use CASE to create segments, flags, bands, and business labels in a transparent way that can be reused in aggregation and reporting.',
    "SELECT order_id,\n       CASE\n         WHEN status = 'Cancelled' THEN 'Excluded'\n         WHEN channel = 'Online' THEN 'Digital'\n         ELSE 'Store-assisted'\n       END AS order_group\nFROM orders;",
    "SELECT order_id, status, channel, CASE WHEN status='Cancelled' THEN 'Excluded' WHEN channel='Online' THEN 'Digital' ELSE 'Store-assisted' END AS order_group FROM orders ORDER BY order_id LIMIT 15;",'CASE',
    [('CASE','Conditional expression returning one value.'),('WHEN','A condition branch inside CASE.'),('ELSE','Fallback result when no WHEN matches.'),('Flag','A derived value identifying a business condition.')])
add('coalesce-and-nullif','03','COALESCE and NULLIF','COALESCE ও NULLIF',
    'COALESCE returns the first non-NULL value from a list. NULLIF returns NULL when two expressions are equal and is commonly used to prevent division by zero or convert placeholder values.',
    'Analysts use these functions to make missing-value rules explicit instead of silently treating every absence as zero. The replacement must match the business meaning.',
    "SELECT customer_name, COALESCE(city, 'Unknown') AS city_label\nFROM customers;\n\nSELECT revenue / NULLIF(order_count, 0) AS average_order_value;",
    "SELECT customer_id, customer_name, COALESCE(city,'Unknown') AS city_label FROM customers ORDER BY customer_id;",'COALESCE',
    [('COALESCE','Returns the first non-NULL expression.'),('NULLIF','Returns NULL when two values are equal.'),('Fallback','A substitute used when preferred data is absent.'),('Division by zero','An invalid calculation prevented with an explicit rule.')])
add('string-functions','03','String Functions','String Function',
    'String functions clean, combine, split, and standardize text. PostgreSQL and SQLite provide overlapping but not identical function names, so analysts should document the target dialect.',
    'Text standardization improves grouping and matching. It is useful for categories, customer names, identifiers, and campaign labels, but it should not erase meaningful distinctions.',
    "SELECT customer_name,\n       UPPER(TRIM(customer_name)) AS standardized_name,\n       LENGTH(customer_name) AS name_length\nFROM customers;",
    "SELECT customer_id, customer_name, UPPER(TRIM(customer_name)) AS standardized_name, LENGTH(customer_name) AS name_length FROM customers ORDER BY customer_id LIMIT 12;",'TRIM',
    [('String','Text data stored as characters.'),('TRIM','Removes leading and trailing spaces.'),('Concatenation','Combining text values.'),('Standardization','Applying a consistent representation to values.')])
add('date-and-time-functions','03','Date and Time Functions','Date ও Time Function',
    'Date functions extract calendar parts, shift periods, and calculate reporting buckets. PostgreSQL uses rich date types and functions; SQLite stores date text or numbers and uses functions such as strftime in the browser lab.',
    'Analysts use date logic for monthly trends, aging, cohorts, period comparisons, and service-level monitoring. Time zones and incomplete periods should be defined before interpretation.',
    "-- PostgreSQL: DATE_TRUNC('month', order_date)\n-- SQLite practice:\nSELECT strftime('%Y-%m', order_date) AS order_month, COUNT(*)\nFROM orders\nGROUP BY order_month;",
    "SELECT strftime('%Y-%m', order_date) AS order_month, COUNT(*) AS orders FROM orders GROUP BY order_month ORDER BY order_month;",'strftime',
    [('Date function','A function that extracts or transforms date/time values.'),('Date grain','The time level used for analysis, such as day or month.'),('Time zone','A regional rule for interpreting timestamps.'),('Incomplete period','A reporting period that has not yet ended.')])
add('type-conversion-and-cast','03','Type Conversion and CAST','Type Conversion ও CAST',
    'CAST converts an expression to a target data type when the database supports the conversion. Explicit conversion is safer than relying on implicit rules that may differ across systems.',
    'Analysts convert imported text to numbers or dates, align join keys, and control calculation behavior. Failed conversions often reveal quality problems that should be measured rather than hidden.',
    "SELECT product_id, list_price, CAST(list_price AS REAL) AS numeric_price\nFROM products;",
    "SELECT product_id, product_name, list_price, CAST(list_price AS REAL) AS numeric_price FROM products ORDER BY product_id;",'CAST',
    [('Data type','A definition of the kind of value a column holds.'),('CAST','Explicitly converts a value to another type.'),('Implicit conversion','Automatic conversion performed by the database.'),('Type mismatch','A conflict between incompatible value types.')])
add('conditional-aggregation','03','Conditional Aggregation','Conditional Aggregation',
    'Conditional aggregation places CASE inside an aggregate to calculate several business conditions in one grouped query. Each condition should define its numerator and denominator clearly.',
    'Analysts use this pattern for status counts, channel revenue, SLA compliance, and segmented KPIs without running separate queries for every category.',
    "SELECT region,\n       COUNT(*) AS all_orders,\n       SUM(CASE WHEN status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_orders\nFROM orders\nGROUP BY region;",
    "SELECT region, COUNT(*) AS all_orders, SUM(CASE WHEN status='Cancelled' THEN 1 ELSE 0 END) AS cancelled_orders FROM orders GROUP BY region ORDER BY region;",'SUM',
    [('Conditional aggregation','Aggregate calculations restricted by a condition.'),('Numerator','The counted or summed events of interest.'),('Denominator','The population used to calculate a rate.'),('Indicator','A 1/0 value representing whether a condition is met.')])
add('sql-data-quality-profiling','03','Profile Data Quality with SQL','SQL দিয়ে Data Quality Profile',
    'A quality profile counts missing values, duplicate keys, invalid categories, and suspicious ranges before analytical conclusions are produced. Profiling queries should be repeatable and saved with the project.',
    'Analysts use SQL quality checks to decide whether data is fit for a purpose, identify remediation work, and document limitations in reports.',
    "SELECT\n  COUNT(*) AS rows,\n  SUM(CASE WHEN city IS NULL THEN 1 ELSE 0 END) AS missing_city,\n  COUNT(DISTINCT customer_id) AS unique_customers\nFROM customers;",
    "SELECT COUNT(*) AS rows, SUM(CASE WHEN city IS NULL THEN 1 ELSE 0 END) AS missing_city, COUNT(DISTINCT customer_id) AS unique_customers FROM customers;",'COUNT',
    [('Data profile','A summary of data structure and quality.'),('Completeness','Extent to which required values are present.'),('Uniqueness','Extent to which expected keys are not duplicated.'),('Validity','Extent to which values follow allowed rules.')])

# Module 04
add('aggregate-functions','04','Aggregate Functions','Aggregate Function',
    'Aggregate functions summarize a set of rows into one result. COUNT, SUM, AVG, MIN, and MAX treat NULL values differently, so the measured field and population must be explicit.',
    'Analysts use aggregates to create KPIs and distribution summaries. A single total without the relevant period, population, and units is not a complete metric definition.',
    "SELECT COUNT(*) AS orders, MIN(order_date) AS first_order, MAX(order_date) AS last_order\nFROM orders;",
    "SELECT COUNT(*) AS orders, MIN(order_date) AS first_order, MAX(order_date) AS last_order FROM orders;",'COUNT',
    [('Aggregate function','A function that summarizes multiple rows.'),('COUNT(*)','Counts rows, including rows containing NULL columns.'),('AVG','Calculates the mean of non-NULL values.'),('Metric grain','The level at which a metric is summarized.')])
add('group-by','04','GROUP BY','GROUP BY',
    'GROUP BY partitions rows into groups with the same selected key values. Every selected expression should either define a group or be calculated with an aggregate.',
    'Analysts group by region, category, month, or customer segment to compare performance. Adding a dimension changes the result grain and can make totals appear duplicated when joined later.',
    "SELECT region, COUNT(*) AS order_count\nFROM orders\nGROUP BY region\nORDER BY order_count DESC;",
    "SELECT region, COUNT(*) AS order_count FROM orders GROUP BY region ORDER BY order_count DESC;",'GROUP BY',
    [('GROUP BY','Clause that forms groups of equal key values.'),('Dimension','A descriptive field used to split a metric.'),('Measure','A numeric value summarized by an aggregate.'),('Result grain','The meaning of one row in the grouped output.')])
add('having','04','Filter Groups with HAVING','HAVING দিয়ে Group Filter',
    'HAVING filters after groups and aggregate values have been calculated. WHERE filters source rows before grouping. Using the correct stage keeps the analytical population and group criteria separate.',
    'Analysts use HAVING to retain customers, products, or regions that meet a minimum activity or performance rule.',
    "SELECT customer_id, COUNT(*) AS orders\nFROM orders\nGROUP BY customer_id\nHAVING COUNT(*) >= 3;",
    "SELECT customer_id, COUNT(*) AS orders FROM orders GROUP BY customer_id HAVING COUNT(*) >= 3 ORDER BY orders DESC, customer_id;",'HAVING',
    [('HAVING','Clause that filters grouped results.'),('Pre-aggregation filter','A WHERE condition applied before grouping.'),('Post-aggregation filter','A HAVING condition applied after grouping.'),('Threshold','A defined minimum or maximum rule.')])
add('multiple-dimension-grouping','04','Group by Multiple Dimensions','Multiple Dimension দিয়ে Group',
    'Grouping by multiple columns creates one row for each unique combination. The number of output rows grows as dimensions become more detailed.',
    'Analysts add dimensions gradually and reconcile totals at each level. This makes it easier to detect duplicated joins or unexpected category combinations.',
    "SELECT region, channel, status, COUNT(*) AS orders\nFROM orders\nGROUP BY region, channel, status;",
    "SELECT region, channel, status, COUNT(*) AS orders FROM orders GROUP BY region, channel, status ORDER BY region, channel, status;",'dimension',
    [('Multi-dimensional group','A group defined by more than one field.'),('Combination','A distinct set of dimension values.'),('Cardinality','The number of distinct values in a field.'),('Drill-down','Moving from a summary to a more detailed grain.')])
add('ratios-percentages-and-aov','04','Ratios, Percentages, and Average Order Value','Ratio, Percentage ও Average Order Value',
    'A ratio divides a numerator by a denominator defined at a compatible grain. Casting and NULLIF protect decimal behavior and zero denominators.',
    'Analysts calculate cancellation rate, conversion rate, margin percentage, and average order value. The denominator must match the business definition, not merely the rows convenient to query.',
    "SELECT\n  COUNT(*) AS orders,\n  SUM(CASE WHEN status='Cancelled' THEN 1 ELSE 0 END) AS cancelled,\n  100.0 * SUM(CASE WHEN status='Cancelled' THEN 1 ELSE 0 END) / NULLIF(COUNT(*),0) AS cancellation_rate\nFROM orders;",
    "SELECT COUNT(*) AS orders, SUM(CASE WHEN status='Cancelled' THEN 1 ELSE 0 END) AS cancelled, ROUND(100.0*SUM(CASE WHEN status='Cancelled' THEN 1 ELSE 0 END)/NULLIF(COUNT(*),0),2) AS cancellation_rate FROM orders;",'NULLIF',
    [('Ratio','One quantity divided by another.'),('Rate','A ratio representing frequency or proportion.'),('Average order value','Revenue divided by qualifying orders.'),('Compatible grain','Numerator and denominator measured over the same population.')])
add('deduplication-with-grouping','04','Detect Duplicates with GROUP BY','GROUP BY দিয়ে Duplicate Detect',
    'Duplicate detection groups by the expected business key and keeps groups with more than one row. The correct key depends on the process, not only on a column named id.',
    'Analysts profile duplicate transactions, customer records, or events before deciding whether to remove, merge, or preserve them.',
    "SELECT customer_name, signup_date, COUNT(*) AS copies\nFROM customers\nGROUP BY customer_name, signup_date\nHAVING COUNT(*) > 1;",
    "SELECT customer_name, signup_date, COUNT(*) AS copies FROM customers GROUP BY customer_name, signup_date HAVING COUNT(*) > 1 ORDER BY copies DESC;",'COUNT',
    [('Business key','Fields that should uniquely identify a real-world record.'),('Duplicate group','Rows sharing the expected key.'),('False duplicate','Similar rows that legitimately represent different events.'),('Deduplication rule','Documented logic for resolving repeated records.')])
add('aggregation-pitfalls','04','Aggregation Pitfalls','Aggregation Pitfall',
    'Aggregates can be wrong when joins multiply rows, filters exclude required records, or values are summarized at incompatible grains. A plausible total is not evidence of correctness.',
    'Analysts reconcile row counts and totals before and after joins, compare results with known controls, and calculate at the correct intermediate grain.',
    "SELECT o.order_id, COUNT(*) AS item_rows, SUM(oi.quantity * oi.unit_price) AS gross_value\nFROM orders o\nJOIN order_items oi ON oi.order_id = o.order_id\nGROUP BY o.order_id;",
    "SELECT o.order_id, COUNT(*) AS item_rows, ROUND(SUM(oi.quantity*oi.unit_price),2) AS gross_value FROM orders o JOIN order_items oi ON oi.order_id=o.order_id GROUP BY o.order_id ORDER BY o.order_id LIMIT 12;",'grain',
    [('Fan-out','Row multiplication caused by one-to-many joins.'),('Reconciliation','Comparison of calculated values with trusted controls.'),('Double counting','Counting the same event more than once.'),('Intermediate grain','The row meaning used before a final summary.')])

# Module 05
add('keys-and-relationships','05','Keys and Table Relationships','Key ও Table Relationship',
    'Keys define identity and relationships. A primary key is unique within its table; a foreign key points to a related record. Join logic should use business-supported keys with compatible types.',
    'Analysts inspect key uniqueness and relationship cardinality before combining tables. This prevents silent data loss and multiplication.',
    "SELECT COUNT(*) AS rows, COUNT(DISTINCT order_id) AS unique_orders\nFROM orders;",
    "SELECT COUNT(*) AS rows, COUNT(DISTINCT order_id) AS unique_orders FROM orders;",'primary key',
    [('Primary key','Column set that uniquely identifies a row.'),('Foreign key','Column set referencing another table.'),('Cardinality','Relationship pattern such as one-to-many.'),('Referential integrity','Requirement that references point to valid rows.')])
add('inner-join','05','INNER JOIN','INNER JOIN',
    'INNER JOIN returns only row pairs that satisfy the join condition. Unmatched rows on either side are excluded.',
    'Analysts use inner joins when only records with confirmed matches are relevant, but should quantify excluded rows before accepting the result.',
    "SELECT o.order_id, c.customer_name, o.order_date\nFROM orders o\nINNER JOIN customers c ON c.customer_id = o.customer_id;",
    "SELECT o.order_id, c.customer_name, o.order_date, o.region FROM orders o INNER JOIN customers c ON c.customer_id=o.customer_id ORDER BY o.order_id LIMIT 15;",'ON',
    [('INNER JOIN','Join that keeps matched row pairs only.'),('Join condition','Predicate defining how rows pair.'),('Matched row','A row whose key finds a counterpart.'),('Unmatched row','A row without a qualifying counterpart.')])
add('left-join','05','LEFT JOIN','LEFT JOIN',
    'LEFT JOIN keeps every row from the left table and adds matching values from the right. Right-side columns become NULL where no match exists.',
    'Analysts use left joins to preserve a base population, find missing relationships, and add optional attributes without dropping records.',
    "SELECT c.customer_id, c.customer_name, COUNT(o.order_id) AS orders\nFROM customers c\nLEFT JOIN orders o ON o.customer_id = c.customer_id\nGROUP BY c.customer_id, c.customer_name;",
    "SELECT c.customer_id, c.customer_name, COUNT(o.order_id) AS orders FROM customers c LEFT JOIN orders o ON o.customer_id=c.customer_id GROUP BY c.customer_id,c.customer_name ORDER BY orders, c.customer_id;",'LEFT JOIN',
    [('LEFT JOIN','Join preserving every left-side row.'),('Base population','The table whose rows must remain.'),('Optional match','A relationship that may be absent.'),('NULL extension','NULL values added for unmatched right-side columns.')])
add('multiple-table-joins','05','Join Multiple Tables','Multiple Table Join',
    'Multi-table joins build a wider analytical dataset by following relationships through several tables. Each added relationship can change row count and grain.',
    'Analysts often combine orders, items, products, and customers. They validate after every join rather than debugging an entire chain at the end.',
    "SELECT o.order_id, c.segment, p.category, oi.quantity, oi.unit_price\nFROM orders o\nJOIN customers c ON c.customer_id=o.customer_id\nJOIN order_items oi ON oi.order_id=o.order_id\nJOIN products p ON p.product_id=oi.product_id;",
    "SELECT o.order_id, c.segment, p.category, oi.quantity, oi.unit_price FROM orders o JOIN customers c ON c.customer_id=o.customer_id JOIN order_items oi ON oi.order_id=o.order_id JOIN products p ON p.product_id=oi.product_id ORDER BY o.order_id LIMIT 18;",'JOIN',
    [('Join chain','A sequence of relationships across multiple tables.'),('Bridge','An intermediate table connecting entities.'),('Wide dataset','A result containing columns from several sources.'),('Validation checkpoint','A count or total checked after each transformation.')])
add('self-join','05','Self Joins','Self Join',
    'A self join uses the same table twice with different aliases. It is useful when rows reference other rows in the same entity, such as employees and managers.',
    'Analysts use self joins for hierarchies, comparisons between peer records, and parent-child structures.',
    "SELECT e.employee_name, m.employee_name AS manager_name\nFROM employees e\nLEFT JOIN employees m ON m.employee_id = e.manager_id;",
    "SELECT e.employee_id, e.employee_name, m.employee_name AS manager_name, e.team FROM employees e LEFT JOIN employees m ON m.employee_id=e.manager_id ORDER BY e.employee_id;",'alias',
    [('Self join','A join from a table to another instance of itself.'),('Hierarchy','A parent-child organizational structure.'),('Parent row','A record referenced by another row.'),('Table alias','A distinct name for each table instance.')])
add('cross-join','05','CROSS JOIN','CROSS JOIN',
    'CROSS JOIN returns every combination of rows from two sources. The result count equals the product of the source row counts.',
    'Analysts use cross joins intentionally for scenarios, calendars, targets, or complete category combinations. An accidental missing join condition can create the same multiplication and should be treated as an error.',
    "SELECT r.region, c.channel\nFROM (SELECT DISTINCT region FROM orders) r\nCROSS JOIN (SELECT DISTINCT channel FROM orders) c;",
    "SELECT r.region, c.channel FROM (SELECT DISTINCT region FROM orders) r CROSS JOIN (SELECT DISTINCT channel FROM orders) c ORDER BY r.region,c.channel;",'CROSS JOIN',
    [('CROSS JOIN','Join returning the Cartesian product.'),('Cartesian product','Every possible pair of rows.'),('Scenario grid','A complete set of combinations for planning or comparison.'),('Accidental cross join','Unintended multiplication caused by a missing condition.')])
add('union-and-union-all','05','UNION and UNION ALL','UNION ও UNION ALL',
    'UNION stacks compatible result sets and removes duplicates. UNION ALL stacks them without deduplication and is usually faster when duplicate preservation is correct.',
    'Analysts combine periods, sources, or event types with set operations. Column count, order, and compatible types must align.',
    "SELECT 'Customer' AS entity, customer_name AS name FROM customers\nUNION ALL\nSELECT 'Employee', employee_name FROM employees;",
    "SELECT 'Customer' AS entity, customer_name AS name FROM customers UNION ALL SELECT 'Employee', employee_name FROM employees ORDER BY entity,name LIMIT 25;",'UNION ALL',
    [('UNION','Stacks results and removes duplicates.'),('UNION ALL','Stacks results and preserves duplicates.'),('Set operation','Combines complete query results.'),('Compatible columns','Columns aligned by count, position, and type.')])
add('exists-semi-and-anti-joins','05','EXISTS, Semi Joins, and Anti Joins','EXISTS, Semi Join ও Anti Join',
    'EXISTS tests whether a related row exists without returning its columns. NOT EXISTS identifies base rows with no qualifying related rows.',
    'Analysts use semi-join logic to select customers who ordered and anti-join logic to find customers with no orders, products never sold, or missing reference matches.',
    "SELECT c.customer_id, c.customer_name\nFROM customers c\nWHERE NOT EXISTS (\n  SELECT 1 FROM orders o WHERE o.customer_id=c.customer_id\n);",
    "SELECT c.customer_id, c.customer_name FROM customers c WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id=c.customer_id) ORDER BY c.customer_id;",'NOT EXISTS',
    [('EXISTS','Predicate that tests whether a subquery returns a row.'),('Semi join','Keeps base rows that have a match.'),('Anti join','Keeps base rows that have no match.'),('Correlated predicate','Condition that refers to the outer row.')])
add('join-debugging-and-reconciliation','05','Debug and Reconcile Joins','Join Debug ও Reconcile',
    'Join debugging compares row counts, distinct keys, unmatched records, and control totals before and after combination. The aim is to explain every change in grain.',
    'Analysts create reconciliation queries as part of the deliverable, especially when financial or operational totals depend on multi-table joins.',
    "SELECT\n  (SELECT COUNT(*) FROM orders) AS order_rows,\n  (SELECT COUNT(DISTINCT order_id) FROM order_items) AS orders_with_items,\n  (SELECT COUNT(*) FROM orders o WHERE NOT EXISTS (SELECT 1 FROM order_items i WHERE i.order_id=o.order_id)) AS orders_without_items;",
    "SELECT (SELECT COUNT(*) FROM orders) AS order_rows, (SELECT COUNT(DISTINCT order_id) FROM order_items) AS orders_with_items, (SELECT COUNT(*) FROM orders o WHERE NOT EXISTS (SELECT 1 FROM order_items i WHERE i.order_id=o.order_id)) AS orders_without_items;",'reconciliation',
    [('Join audit','Checks proving a join behaved as intended.'),('Control total','A trusted value used for comparison.'),('Unmatched-key report','A list of keys failing to join.'),('Row multiplication','Increase caused by one-to-many matches.')])

# Module 06
add('scalar-subqueries','06','Scalar Subqueries','Scalar Subquery',
    'A scalar subquery returns one value and can be used in a comparison or selected expression. It must never return more than one row.',
    'Analysts compare records with a global benchmark, such as products priced above the average or customers exceeding overall order frequency.',
    "SELECT product_name, list_price\nFROM products\nWHERE list_price > (SELECT AVG(list_price) FROM products);",
    "SELECT product_id, product_name, list_price FROM products WHERE list_price>(SELECT AVG(list_price) FROM products) ORDER BY list_price DESC;",'subquery',
    [('Scalar subquery','Subquery that returns one value.'),('Benchmark','A reference value used for comparison.'),('Outer query','The query containing a subquery.'),('Single-row requirement','Rule that scalar subqueries return at most one row.')])
add('subqueries-in-from','06','Subqueries in FROM','FROM-এর মধ্যে Subquery',
    'A subquery in FROM creates a derived table that can be filtered, joined, or summarized by an outer query. It should have a meaningful alias.',
    'Analysts use derived tables to calculate at one grain and then summarize at another, such as order totals before regional averages.',
    "SELECT region, AVG(order_value) AS average_order_value\nFROM (\n  SELECT o.order_id, o.region, SUM(oi.quantity*oi.unit_price*(1-oi.discount_pct)) AS order_value\n  FROM orders o JOIN order_items oi ON oi.order_id=o.order_id\n  GROUP BY o.order_id,o.region\n) q\nGROUP BY region;",
    "SELECT region, ROUND(AVG(order_value),2) AS average_order_value FROM (SELECT o.order_id,o.region,SUM(oi.quantity*oi.unit_price*(1-oi.discount_pct)) AS order_value FROM orders o JOIN order_items oi ON oi.order_id=o.order_id GROUP BY o.order_id,o.region) q GROUP BY region ORDER BY region;",'derived table',
    [('Derived table','A subquery used as a row source.'),('Outer aggregation','Summary applied after an inner calculation.'),('Alias requirement','A name assigned to the derived result.'),('Grain transition','Changing from one row meaning to another.')])
add('correlated-subqueries','06','Correlated Subqueries','Correlated Subquery',
    'A correlated subquery refers to columns from the current outer row and is logically evaluated in that row’s context. It can be expressive but may be slower than a join or window function.',
    'Analysts use correlated logic for group-relative comparisons and existence checks, then compare performance and clarity with alternative patterns.',
    "SELECT p.product_name, p.list_price\nFROM products p\nWHERE p.list_price > (\n  SELECT AVG(p2.list_price) FROM products p2 WHERE p2.category=p.category\n);",
    "SELECT p.product_id,p.product_name,p.category,p.list_price FROM products p WHERE p.list_price>(SELECT AVG(p2.list_price) FROM products p2 WHERE p2.category=p.category) ORDER BY p.category,p.list_price DESC;",'correlated',
    [('Correlated subquery','Subquery referencing the current outer row.'),('Group-relative comparison','Comparison with a benchmark inside the row’s group.'),('Execution context','Values available while an expression is evaluated.'),('Rewrite','An alternative formulation using joins or windows.')])
add('exists-subqueries','06','EXISTS Subqueries','EXISTS Subquery',
    'EXISTS returns true as soon as a subquery finds a qualifying row. The selected expression inside EXISTS is not used; SELECT 1 is a common convention.',
    'Analysts use EXISTS when they care about the presence of related activity rather than the number or attributes of matches.',
    "SELECT p.product_id, p.product_name\nFROM products p\nWHERE EXISTS (\n  SELECT 1 FROM order_items oi WHERE oi.product_id=p.product_id\n);",
    "SELECT p.product_id,p.product_name FROM products p WHERE EXISTS (SELECT 1 FROM order_items oi WHERE oi.product_id=p.product_id) ORDER BY p.product_id;",'EXISTS',
    [('EXISTS subquery','Subquery used only to test presence.'),('Short-circuit','Stopping after the first qualifying row.'),('Presence test','Question of whether any related row exists.'),('SELECT 1','Convention showing returned subquery columns are irrelevant.')])
add('common-table-expressions','06','Common Table Expressions','Common Table Expression',
    'A common table expression, introduced with WITH, names an intermediate result for one statement. It can make a multi-stage analytical query easier to read and validate.',
    'Analysts use CTEs to separate cleaning, joining, calculation, and final presentation into understandable stages.',
    "WITH order_totals AS (\n  SELECT order_id, SUM(quantity*unit_price*(1-discount_pct)) AS revenue\n  FROM order_items\n  GROUP BY order_id\n)\nSELECT AVG(revenue) AS average_order_value FROM order_totals;",
    "WITH order_totals AS (SELECT order_id,SUM(quantity*unit_price*(1-discount_pct)) AS revenue FROM order_items GROUP BY order_id) SELECT ROUND(AVG(revenue),2) AS average_order_value FROM order_totals;",'WITH',
    [('CTE','Named intermediate result defined with WITH.'),('WITH clause','Clause that introduces one or more CTEs.'),('Pipeline stage','A logical transformation step.'),('Readability','Ease with which query intent can be reviewed.')])
add('recursive-ctes','06','Recursive CTEs','Recursive CTE',
    'A recursive CTE repeatedly references its own growing result until no new rows are produced. It normally contains an anchor query and a recursive query connected with UNION ALL.',
    'Analysts use recursive CTEs for organizational hierarchies, category trees, paths, and generated sequences. A stopping condition is essential.',
    "WITH RECURSIVE hierarchy(employee_id, employee_name, manager_id, level) AS (\n  SELECT employee_id, employee_name, manager_id, 0 FROM employees WHERE manager_id IS NULL\n  UNION ALL\n  SELECT e.employee_id,e.employee_name,e.manager_id,h.level+1\n  FROM employees e JOIN hierarchy h ON e.manager_id=h.employee_id\n)\nSELECT * FROM hierarchy ORDER BY level, employee_id;",
    "WITH RECURSIVE hierarchy(employee_id,employee_name,manager_id,level) AS (SELECT employee_id,employee_name,manager_id,0 FROM employees WHERE manager_id IS NULL UNION ALL SELECT e.employee_id,e.employee_name,e.manager_id,h.level+1 FROM employees e JOIN hierarchy h ON e.manager_id=h.employee_id) SELECT * FROM hierarchy ORDER BY level,employee_id;",'RECURSIVE',
    [('Recursive CTE','CTE that references itself.'),('Anchor member','Initial rows of a recursive query.'),('Recursive member','Part that produces the next level.'),('Termination','Condition that stops recursion.')],level='Intermediate')
add('modular-query-design','06','Modular Query Design','Modular Query Design',
    'Modular SQL breaks a complex question into named, testable stages. Each stage should have a defined grain, purpose, and validation check.',
    'Analysts build maintainable queries by separating source selection, quality rules, metric calculations, and presentation rather than nesting everything in one expression.',
    "WITH valid_orders AS (...),\norder_totals AS (...),\ncustomer_metrics AS (...)\nSELECT * FROM customer_metrics;",
    "WITH valid_orders AS (SELECT * FROM orders WHERE status<>'Cancelled'), order_totals AS (SELECT o.customer_id,o.order_id,SUM(oi.quantity*oi.unit_price*(1-oi.discount_pct)) AS revenue FROM valid_orders o JOIN order_items oi ON oi.order_id=o.order_id GROUP BY o.customer_id,o.order_id), customer_metrics AS (SELECT customer_id,COUNT(*) AS orders,SUM(revenue) AS revenue FROM order_totals GROUP BY customer_id) SELECT * FROM customer_metrics ORDER BY revenue DESC;",'CTE',
    [('Module','A self-contained query stage with one purpose.'),('Contract','Expected columns and grain produced by a stage.'),('Validation query','Check that confirms a stage behaved correctly.'),('Maintainability','Ease of safely reviewing and changing logic.')],level='Intermediate')

# Module 07
add('window-function-foundations','07','Window Function Foundations','Window Function Foundation',
    'A window function calculates across related rows while preserving each row. The OVER clause defines the window, unlike GROUP BY which collapses rows.',
    'Analysts use windows for rankings, running totals, comparisons, and percentages while retaining detailed records.',
    "SELECT order_id, region, order_date,\n       COUNT(*) OVER (PARTITION BY region) AS region_orders\nFROM orders;",
    "SELECT order_id,region,order_date,COUNT(*) OVER (PARTITION BY region) AS region_orders FROM orders ORDER BY region,order_date,order_id LIMIT 25;",'OVER',
    [('Window function','Function evaluated over related rows without collapsing them.'),('OVER','Clause defining a window calculation.'),('PARTITION BY','Divides rows into independent windows.'),('Window order','Order used inside a window calculation.')],level='Intermediate')
add('row-number-rank-dense-rank','07','ROW_NUMBER, RANK, and DENSE_RANK','ROW_NUMBER, RANK ও DENSE_RANK',
    'ROW_NUMBER assigns unique sequential positions. RANK gives ties the same rank and leaves gaps. DENSE_RANK gives ties the same rank without gaps.',
    'Analysts choose the ranking function based on how ties should affect top lists, league tables, and percentile groups.',
    "SELECT product_name, category, list_price,\n       DENSE_RANK() OVER (PARTITION BY category ORDER BY list_price DESC) AS price_rank\nFROM products;",
    "SELECT product_id,product_name,category,list_price,DENSE_RANK() OVER (PARTITION BY category ORDER BY list_price DESC) AS price_rank FROM products ORDER BY category,price_rank,product_id;",'DENSE_RANK',
    [('ROW_NUMBER','Unique sequential row position.'),('RANK','Tie-aware rank with gaps.'),('DENSE_RANK','Tie-aware rank without gaps.'),('Tie rule','Defined treatment of equal values.')],level='Intermediate')
add('running-totals','07','Running Totals','Running Total',
    'A running total accumulates a measure according to a defined order. The window frame should be explicit when duplicate sort values could affect results.',
    'Analysts use cumulative sales, budget usage, inventory movement, and progress measures. A stable ordering key is required for reproducible results.',
    "WITH daily AS (\n SELECT order_date, COUNT(*) AS orders FROM orders GROUP BY order_date\n)\nSELECT order_date, orders,\n       SUM(orders) OVER (ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_orders\nFROM daily;",
    "WITH daily AS (SELECT order_date,COUNT(*) AS orders FROM orders GROUP BY order_date) SELECT order_date,orders,SUM(orders) OVER (ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_orders FROM daily ORDER BY order_date;",'ROWS',
    [('Running total','Cumulative sum through the current row.'),('Window frame','Subset of window rows available to a function.'),('UNBOUNDED PRECEDING','Frame boundary starting at the first row.'),('Current row','Frame boundary ending at the current position.')],level='Intermediate')
add('moving-averages','07','Moving Averages','Moving Average',
    'A moving average summarizes a rolling set of recent periods. It smooths short-term variation but introduces lag and depends on a complete, ordered time series.',
    'Analysts use rolling averages to monitor trends and reduce noise. Missing dates and partial windows should be handled deliberately.',
    "WITH daily AS (SELECT order_date, COUNT(*) AS orders FROM orders GROUP BY order_date)\nSELECT order_date, orders,\n       AVG(orders) OVER (ORDER BY order_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS seven_row_average\nFROM daily;",
    "WITH daily AS (SELECT order_date,COUNT(*) AS orders FROM orders GROUP BY order_date) SELECT order_date,orders,ROUND(AVG(orders) OVER (ORDER BY order_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2) AS moving_average FROM daily ORDER BY order_date;",'PRECEDING',
    [('Moving average','Average over a rolling window.'),('Window size','Number of rows or periods included.'),('Smoothing','Reducing short-term variation.'),('Lag','Delay introduced by averaging past periods.')],level='Intermediate')
add('lag-and-lead','07','LAG and LEAD','LAG ও LEAD',
    'LAG reads a value from a previous row and LEAD reads a later row within the window order. They avoid self joins for many period-over-period comparisons.',
    'Analysts calculate changes, gaps, repeat intervals, and next-event status with these functions.',
    "WITH monthly AS (SELECT strftime('%Y-%m',order_date) AS month,COUNT(*) AS orders FROM orders GROUP BY 1)\nSELECT month,orders,LAG(orders) OVER (ORDER BY month) AS previous_orders\nFROM monthly;",
    "WITH monthly AS (SELECT strftime('%Y-%m',order_date) AS month,COUNT(*) AS orders FROM orders GROUP BY 1) SELECT month,orders,LAG(orders) OVER (ORDER BY month) AS previous_orders, orders-LAG(orders) OVER (ORDER BY month) AS change FROM monthly ORDER BY month;",'LAG',
    [('LAG','Returns a prior row’s value.'),('LEAD','Returns a later row’s value.'),('Period-over-period','Comparison with the previous reporting period.'),('Default value','Value returned when the requested offset does not exist.')],level='Intermediate')
add('first-value-and-last-value','07','FIRST_VALUE and LAST_VALUE','FIRST_VALUE ও LAST_VALUE',
    'FIRST_VALUE and LAST_VALUE return boundary values within a window frame. LAST_VALUE often surprises learners because the default frame may end at the current row rather than the partition end.',
    'Analysts compare events with first purchase, latest status, or boundary values. The frame definition must match the intended boundary.',
    "SELECT customer_id, order_date,\n       FIRST_VALUE(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS first_order\nFROM orders;",
    "SELECT customer_id,order_id,order_date,FIRST_VALUE(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS first_order FROM orders ORDER BY customer_id,order_date;",'FIRST_VALUE',
    [('FIRST_VALUE','Returns the first value in the window frame.'),('LAST_VALUE','Returns the last value in the window frame.'),('Boundary value','Value at a defined start or end.'),('Frame sensitivity','Dependence of a result on frame boundaries.')],level='Intermediate')
add('ntile-and-percentile-bands','07','NTILE and Percentile Bands','NTILE ও Percentile Band',
    'NTILE assigns ordered rows to a requested number of approximately equal groups. It is useful for segmentation but may split equal values across groups.',
    'Analysts create quartiles, deciles, and value tiers for targeting or review. The population and sorting measure should be documented.',
    "WITH customer_revenue AS (...)\nSELECT customer_id,revenue,NTILE(4) OVER (ORDER BY revenue DESC) AS value_quartile\nFROM customer_revenue;",
    "WITH customer_revenue AS (SELECT o.customer_id,SUM(oi.quantity*oi.unit_price*(1-oi.discount_pct)) AS revenue FROM orders o JOIN order_items oi ON oi.order_id=o.order_id WHERE o.status<>'Cancelled' GROUP BY o.customer_id) SELECT customer_id,ROUND(revenue,2) AS revenue,NTILE(4) OVER (ORDER BY revenue DESC) AS value_quartile FROM customer_revenue ORDER BY revenue DESC;",'NTILE',
    [('NTILE','Assigns ordered rows to numbered groups.'),('Quartile','One of four ordered groups.'),('Quantile band','A segment based on relative position.'),('Equal-value split','Tied values placed in different bands due to row counts.')],level='Intermediate')
add('top-n-per-group','07','Top N per Group','প্রতি Group-এর Top N',
    'Top-N-per-group ranks rows inside each partition and filters the rank in an outer query. This answers questions such as the top products in every category.',
    'Analysts use this pattern for local leaders, exception lists, and focused reporting without losing group context.',
    "WITH ranked AS (\n SELECT product_id,product_name,category,list_price,\n        ROW_NUMBER() OVER (PARTITION BY category ORDER BY list_price DESC,product_id) AS rn\n FROM products\n)\nSELECT * FROM ranked WHERE rn <= 2;",
    "WITH ranked AS (SELECT product_id,product_name,category,list_price,ROW_NUMBER() OVER (PARTITION BY category ORDER BY list_price DESC,product_id) AS rn FROM products) SELECT * FROM ranked WHERE rn<=2 ORDER BY category,rn;",'ROW_NUMBER',
    [('Top N per group','Highest-ranked rows retained inside every partition.'),('Partition','Independent group for ranking.'),('Tie breaker','Additional sort key producing deterministic order.'),('Outer filter','Filter applied after the rank is calculated.')],level='Intermediate')
add('cohort-retention-with-sql','07','Cohort Retention with SQL','SQL দিয়ে Cohort Retention',
    'Cohort analysis groups entities by a starting period and measures their activity in later periods. It requires a clear first-event rule and consistent period indexing.',
    'Analysts use cohorts to separate acquisition timing from retention behavior. Small cohorts and incomplete recent periods should be labeled.',
    "WITH first_order AS (...), activity AS (...) SELECT cohort_month, period_number, COUNT(DISTINCT customer_id) FROM activity GROUP BY 1,2;",
    "WITH first_order AS (SELECT customer_id,MIN(strftime('%Y-%m',order_date)) AS cohort_month FROM orders WHERE status<>'Cancelled' GROUP BY customer_id), activity AS (SELECT o.customer_id,f.cohort_month,(CAST(strftime('%Y',o.order_date) AS INTEGER)-CAST(substr(f.cohort_month,1,4) AS INTEGER))*12+(CAST(strftime('%m',o.order_date) AS INTEGER)-CAST(substr(f.cohort_month,6,2) AS INTEGER)) AS period_number FROM orders o JOIN first_order f ON f.customer_id=o.customer_id WHERE o.status<>'Cancelled') SELECT cohort_month,period_number,COUNT(DISTINCT customer_id) AS active_customers FROM activity GROUP BY cohort_month,period_number ORDER BY cohort_month,period_number;",'cohort',
    [('Cohort','Entities sharing a defined starting period or event.'),('Retention','Continued qualifying activity after the start.'),('Cohort month','Period of the first qualifying event.'),('Period number','Elapsed periods since cohort start.')],level='Advanced')

# Module 08
add('create-table-data-types-constraints','08','CREATE TABLE, Data Types, and Constraints','CREATE TABLE, Data Type ও Constraint',
    'CREATE TABLE defines columns, data types, keys, and constraints. Constraints prevent invalid states closer to the source and document expected rules.',
    'Analysts benefit from well-modeled tables because valid types and keys reduce cleaning work and make queries more reliable.',
    "CREATE TABLE targets (\n  target_month DATE NOT NULL,\n  region TEXT NOT NULL,\n  revenue_target NUMERIC CHECK (revenue_target >= 0),\n  PRIMARY KEY (target_month, region)\n);",
    "DROP TABLE IF EXISTS demo_targets; CREATE TABLE demo_targets(target_month TEXT NOT NULL,region TEXT NOT NULL,revenue_target REAL CHECK(revenue_target>=0),PRIMARY KEY(target_month,region)); INSERT INTO demo_targets VALUES('2026-07-01','Dhaka',50000); SELECT * FROM demo_targets;",'constraint',
    [('DDL','SQL statements defining database objects.'),('Constraint','Rule enforced by the database.'),('NOT NULL','Constraint requiring a value.'),('CHECK','Constraint testing an expression for inserted or updated rows.')],level='Intermediate')
add('insert-update-delete-safely','08','INSERT, UPDATE, and DELETE Safely','INSERT, UPDATE ও DELETE নিরাপদভাবে',
    'INSERT adds rows, UPDATE changes matching rows, and DELETE removes matching rows. UPDATE and DELETE without a correct WHERE clause can affect every row.',
    'Analysts usually work read-only, but data preparation and sandbox tasks may modify tables. Preview the target rows, use transactions, and verify affected counts.',
    "BEGIN;\nUPDATE demo_targets SET revenue_target=55000 WHERE target_month='2026-07-01' AND region='Dhaka';\nSELECT * FROM demo_targets;\nROLLBACK;",
    "DROP TABLE IF EXISTS demo_changes; CREATE TABLE demo_changes(id INTEGER PRIMARY KEY,status TEXT); INSERT INTO demo_changes VALUES(1,'Open'),(2,'Open'); UPDATE demo_changes SET status='Closed' WHERE id=1; SELECT * FROM demo_changes ORDER BY id;",'WHERE',
    [('DML','Statements that insert, update, or delete data.'),('Affected rows','Number of rows changed by a statement.'),('Read-only role','Database permission that prevents modifications.'),('Sandbox','Isolated environment used for safe practice.')],level='Intermediate')
add('transactions','08','Transactions','Transaction',
    'A transaction treats several changes as one unit. COMMIT makes them permanent; ROLLBACK cancels them. Atomicity protects the database from partial changes.',
    'Analysts use transactions when testing transformations or maintaining controlled reporting tables so a failed step does not leave inconsistent data.',
    "BEGIN;\n-- related changes\nCOMMIT;\n-- or ROLLBACK;",
    "DROP TABLE IF EXISTS demo_tx; CREATE TABLE demo_tx(id INTEGER PRIMARY KEY,value INTEGER); BEGIN; INSERT INTO demo_tx VALUES(1,100); UPDATE demo_tx SET value=120 WHERE id=1; COMMIT; SELECT * FROM demo_tx;",'COMMIT',
    [('Transaction','A unit of work committed or rolled back together.'),('COMMIT','Makes transaction changes permanent.'),('ROLLBACK','Cancels uncommitted changes.'),('Atomicity','Property that all transaction steps succeed or none do.')],level='Intermediate')
add('views','08','Views','View',
    'A view stores a query definition and exposes it like a table. It centralizes repeated logic but does not automatically guarantee performance or correct governance.',
    'Analysts use views to publish approved metric logic, simplify access, and hide unnecessary source complexity.',
    "CREATE VIEW completed_orders AS\nSELECT * FROM orders WHERE status='Completed';",
    "DROP VIEW IF EXISTS demo_completed_orders; CREATE VIEW demo_completed_orders AS SELECT order_id,customer_id,order_date,region FROM orders WHERE status='Completed'; SELECT * FROM demo_completed_orders ORDER BY order_id LIMIT 10;",'VIEW',
    [('View','Named stored query exposed as a virtual table.'),('Semantic layer','Shared business definitions presented for analysis.'),('Encapsulation','Hiding lower-level complexity behind a stable interface.'),('Materialized view','Stored query result refreshed separately in systems that support it.')],level='Intermediate')
add('indexes-and-explain','08','Indexes and EXPLAIN','Index ও EXPLAIN',
    'An index is a data structure that can speed selective lookups and joins while adding storage and write cost. EXPLAIN shows the execution plan chosen by the optimizer.',
    'Analysts should understand basic plans to recognize full scans, missing filters, and expensive joins, while leaving production tuning changes to controlled review.',
    "CREATE INDEX idx_orders_customer_date ON orders(customer_id, order_date);\nEXPLAIN SELECT * FROM orders WHERE customer_id=10 ORDER BY order_date;",
    "EXPLAIN QUERY PLAN SELECT * FROM orders WHERE customer_id=10 ORDER BY order_date;",'EXPLAIN',
    [('Index','Structure that can accelerate data access.'),('Execution plan','Steps selected by the database to run a query.'),('Full scan','Reading all rows of a table.'),('Selectivity','How narrowly a condition reduces rows.')],level='Advanced')
add('star-schema-for-analytics','08','Star Schema for Analytics','Analytics-এর জন্য Star Schema',
    'A star schema places measurable events in a fact table and descriptive context in dimension tables. A consistent grain and conformed dimensions support reliable reporting.',
    'Analysts use star schemas in warehouses and BI models because they simplify filtering, aggregation, and reuse across dashboards.',
    "-- Fact: order_items at line grain\n-- Dimensions: customers, products, dates, employees\nSELECT p.category, SUM(oi.quantity*oi.unit_price) AS gross_sales\nFROM order_items oi JOIN products p ON p.product_id=oi.product_id\nGROUP BY p.category;",
    "SELECT p.category,ROUND(SUM(oi.quantity*oi.unit_price*(1-oi.discount_pct)),2) AS net_sales FROM order_items oi JOIN products p ON p.product_id=oi.product_id GROUP BY p.category ORDER BY net_sales DESC;",'fact table',
    [('Fact table','Table of measurable events at a defined grain.'),('Dimension table','Table of descriptive attributes used for filtering and grouping.'),('Star schema','Model with a central fact connected to dimensions.'),('Conformed dimension','Shared dimension used consistently across facts.')],level='Intermediate')

# Module 09
add('sales-kpi-scorecard','09','Project: Sales KPI Scorecard','Project: Sales KPI Scorecard',
    'A scorecard query calculates a small set of clearly defined KPIs from validated order and item data. Each KPI needs a period, population, formula, and reconciliation rule.',
    'This project combines filters, joins, conditional aggregation, and ratios to produce decision-ready metrics without hiding the calculation logic.',
    "WITH order_totals AS (...) SELECT COUNT(*) AS orders, SUM(revenue) AS revenue, AVG(revenue) AS aov FROM order_totals;",
    "WITH order_totals AS (SELECT o.order_id,SUM(oi.quantity*oi.unit_price*(1-oi.discount_pct)) AS revenue FROM orders o JOIN order_items oi ON oi.order_id=o.order_id WHERE o.status<>'Cancelled' GROUP BY o.order_id) SELECT COUNT(*) AS orders,ROUND(SUM(revenue),2) AS revenue,ROUND(AVG(revenue),2) AS average_order_value FROM order_totals;",'KPI',
    [('KPI','A defined measure linked to an objective.'),('Scorecard','Compact set of monitored metrics.'),('Metric definition','Population, formula, time period, and units of a KPI.'),('Reconciliation rule','Check that validates the final metric.')],level='Intermediate')
add('customer-segmentation-sql-project','09','Project: Customer Segmentation','Project: Customer Segmentation',
    'Customer segmentation summarizes behavior at customer grain and assigns interpretable groups using order frequency, recency, and revenue.',
    'This project demonstrates multi-stage SQL, aggregation, window functions, and CASE while keeping the segment logic reviewable.',
    "WITH customer_metrics AS (...) SELECT *, NTILE(4) OVER (ORDER BY revenue DESC) AS value_band FROM customer_metrics;",
    "WITH customer_metrics AS (SELECT c.customer_id,c.customer_name,COUNT(DISTINCT o.order_id) AS orders,MAX(o.order_date) AS last_order,COALESCE(SUM(oi.quantity*oi.unit_price*(1-oi.discount_pct)),0) AS revenue FROM customers c LEFT JOIN orders o ON o.customer_id=c.customer_id AND o.status<>'Cancelled' LEFT JOIN order_items oi ON oi.order_id=o.order_id GROUP BY c.customer_id,c.customer_name) SELECT customer_id,customer_name,orders,last_order,ROUND(revenue,2) AS revenue,NTILE(4) OVER (ORDER BY revenue DESC) AS value_band FROM customer_metrics ORDER BY revenue DESC;",'segment',
    [('Customer grain','One row per customer.'),('Recency','Time since the most recent qualifying event.'),('Frequency','Number of qualifying events.'),('Value band','Relative segment based on customer value.')],level='Advanced')
add('funnel-analysis-sql-project','09','Project: Funnel Analysis','Project: Funnel Analysis',
    'Funnel analysis counts users reaching ordered stages such as visit, product view, add to cart, and purchase. Stage definitions and time windows must be consistent.',
    'This project uses conditional aggregation and distinct customer counts to identify where users leave a process.',
    "SELECT campaign, COUNT(DISTINCT CASE WHEN event_name='visit' THEN customer_id END) AS visitors, ... FROM web_events GROUP BY campaign;",
    "SELECT campaign,COUNT(DISTINCT CASE WHEN event_name='visit' THEN customer_id END) AS visitors,COUNT(DISTINCT CASE WHEN event_name='product_view' THEN customer_id END) AS viewers,COUNT(DISTINCT CASE WHEN event_name='add_to_cart' THEN customer_id END) AS carts,COUNT(DISTINCT CASE WHEN event_name='purchase' THEN customer_id END) AS purchasers FROM web_events GROUP BY campaign ORDER BY campaign;",'funnel',
    [('Funnel','Ordered stages toward an outcome.'),('Stage','A defined event in the journey.'),('Conversion rate','Entities reaching a later stage divided by an earlier stage.'),('Drop-off','Loss between two funnel stages.')],level='Advanced')
add('data-quality-audit-sql-project','09','Project: SQL Data Quality Audit','Project: SQL Data Quality Audit',
    'A data quality audit combines structural checks, key checks, missing-value counts, referential integrity checks, and business-rule exceptions into a repeatable control report.',
    'This project treats quality evidence as part of analytics rather than an informal step performed once and forgotten.',
    "SELECT 'orphan_order_items' AS check_name, COUNT(*) AS failures FROM order_items i LEFT JOIN orders o ON o.order_id=i.order_id WHERE o.order_id IS NULL;",
    "SELECT 'missing_customer_city' AS check_name,COUNT(*) AS failures FROM customers WHERE city IS NULL UNION ALL SELECT 'orphan_orders',COUNT(*) FROM orders o LEFT JOIN customers c ON c.customer_id=o.customer_id WHERE c.customer_id IS NULL UNION ALL SELECT 'orphan_items',COUNT(*) FROM order_items i LEFT JOIN orders o ON o.order_id=i.order_id WHERE o.order_id IS NULL UNION ALL SELECT 'invalid_discount',COUNT(*) FROM order_items WHERE discount_pct<0 OR discount_pct>1;",'audit',
    [('Quality audit','Repeatable set of tests for data fitness.'),('Orphan record','Child row without a valid parent.'),('Business rule','Domain-specific validity requirement.'),('Control report','Output showing checks, failures, and status.')],level='Advanced')
add('final-sql-analytics-portfolio-project','09','Final Project: Retail SQL Analytics Portfolio','Final Project: Retail SQL Analytics Portfolio',
    'The final project turns a business question into a documented SQL analysis with schema review, quality checks, reusable query stages, metrics, segments, trends, and limitations.',
    'A strong portfolio submission includes the questions, SQL files, result evidence, validation controls, plain-language findings, and recommendations that do not exceed the data.',
    "-- Deliverables: 1_schema_audit.sql, 2_quality_checks.sql, 3_kpis.sql, 4_segments.sql, 5_trends.sql, README.md",
    "WITH order_totals AS (SELECT o.order_id,o.customer_id,o.order_date,o.region,SUM(oi.quantity*oi.unit_price*(1-oi.discount_pct)) AS revenue FROM orders o JOIN order_items oi ON oi.order_id=o.order_id WHERE o.status<>'Cancelled' GROUP BY o.order_id,o.customer_id,o.order_date,o.region), monthly AS (SELECT strftime('%Y-%m',order_date) AS month,COUNT(*) AS orders,SUM(revenue) AS revenue,AVG(revenue) AS aov FROM order_totals GROUP BY 1) SELECT month,orders,ROUND(revenue,2) AS revenue,ROUND(aov,2) AS aov,LAG(ROUND(revenue,2)) OVER (ORDER BY month) AS previous_revenue FROM monthly ORDER BY month;",'README',
    [('Portfolio project','Evidence of an end-to-end analytical workflow.'),('Deliverable','File or output required for review.'),('Finding','Evidence-supported statement from analysis.'),('Limitation','Condition restricting interpretation or use.')],level='Advanced')

module_titles={m['id']:m for m in modules}

def bn_para(text:str)->str:
    # Deliberately bilingual to preserve exact SQL terminology while explaining in Bangla.
    return text

def make_chapter(spec,index):
    title=spec['title']; bn=spec['bn']; concept=spec['concept']; use=spec['use']; code=spec['code']; q=spec['query']
    dialect="The browser practice uses SQLite through sql.js. The course explanation emphasizes portable SQL and identifies PostgreSQL syntax where it differs. Query results are temporary and remain in the current browser page."
    dialect_bn="Browser practice-এ sql.js-এর মাধ্যমে SQLite ব্যবহার করা হয়। Explanation portable SQL-কে গুরুত্ব দেয় এবং PostgreSQL syntax আলাদা হলে তা উল্লেখ করে। Query result temporary এবং current browser page-এর মধ্যেই থাকে।"
    sections=[
      {'title_en':f'What {title} means','title_bn':f'{bn} কী',
       'body_en':concept+' The important first step is to define the row population and result grain before interpreting any returned value. SQL syntax is only useful when it represents the intended business question.',
       'body_bn':f'{bn} বুঝতে প্রথমে source table-এর row grain, included population এবং expected output নির্ধারণ করতে হবে। SQL syntax নিজে decision নয়; এটি business question-কে reproducible query-তে প্রকাশ করে। ভুল grain বা population ব্যবহার করলে technically valid query-ও ভুল conclusion দিতে পারে।',
       'code':code,'code_label':'SQL'},
      {'title_en':'How a data analyst uses it','title_bn':'Data analyst কীভাবে ব্যবহার করেন',
       'body_en':use+' A responsible workflow records the filter rules, validates row counts, checks NULL behavior, and reconciles important totals before publishing the result.',
       'body_bn':f'Data analyst এই concept ব্যবহার করে repeatable analysis তৈরি করেন। Query run করার আগে filter, join key, date boundary ও unit লিখে রাখেন; run করার পরে row count, NULL, duplicate এবং control total যাচাই করেন। এই validation ছাড়া result দেখতে plausible হলেও reliable নাও হতে পারে।'},
      {'title_en':'Rules, dialect notes, and common mistakes','title_bn':'Rule, dialect note ও common mistake',
       'body_en':dialect+' Common mistakes include using the wrong grain, relying on implicit conversion, omitting deterministic ordering, or treating missing values as ordinary zeroes. Test the smallest useful result before extending the query.',
       'body_bn':dialect_bn+' Common mistake হলো wrong grain-এ join বা aggregate করা, implicit conversion-এর ওপর নির্ভর করা, deterministic order না দেওয়া এবং NULL-কে zero ধরে নেওয়া। বড় query লেখার আগে ছোট verified result তৈরি করুন।'}]
    terms=[]
    for term,definition in spec['terms'][:4]:
      terms.append({'term_en':term,'term_bn':term,'definition_en':definition,'definition_bn':f'{term}: {definition} এই term-এর অর্থ query context ও result grain-এর সঙ্গে মিলিয়ে বুঝতে হবে।'})
    worked={
      'title_en':f'Worked example: {title}', 'title_bn':f'Worked example: {bn}',
      'context_en':f'A retail analyst needs to apply {title.lower()} to the practice database and produce a result that another reviewer can reproduce.',
      'context_bn':f'একজন retail analyst practice database-এ {bn} apply করে এমন result তৈরি করবেন যা অন্য reviewer reproduce করতে পারবেন।',
      'steps_en':['State the business question, qualifying rows, time period, and intended result grain.','Inspect the required tables and confirm that the selected columns and join keys represent that grain.','Run the SQL in the browser practice area, then change one filter or expression and compare the result.','Validate row counts, NULL behavior, and at least one control total before writing the interpretation.'],
      'steps_bn':['Business question, qualifying row, time period ও intended result grain লিখুন।','Required table inspect করে selected column ও join key ওই grain represent করে কিনা যাচাই করুন।','Browser practice area-তে SQL run করে একটি filter বা expression বদলে result compare করুন।','Interpretation লেখার আগে row count, NULL behavior ও অন্তত একটি control total validate করুন।'],
      'conclusion_en':f'{title} is correctly applied only when the returned rows answer the stated question and the validation evidence supports the calculation.',
      'conclusion_bn':f'{bn} তখনই সঠিকভাবে apply হয়েছে যখন returned row stated question-এর উত্তর দেয় এবং validation evidence calculation-কে support করে।'}
    mcq_prompt=f'Which practice best supports a reliable use of {title}?'
    exercises=[
      {'type':'mcq','prompt_en':mcq_prompt,'prompt_bn':f'{bn} reliableভাবে use করতে কোন practice সবচেয়ে ভালো?',
       'options_en':['Copy a long query and trust the output','Define the grain, run the query, and validate counts or totals','Use SELECT * and remove unexpected rows manually'],
       'options_bn':['Long query copy করে output trust করা','Grain define করে query run এবং count বা total validate করা','SELECT * ব্যবহার করে unexpected row manually remove করা'],
       'answer_en':'B','answer_bn':'B','explanation_en':'Correct SQL analysis connects the question, grain, query logic, and validation evidence.','explanation_bn':'সঠিক SQL analysis question, grain, query logic ও validation evidence-কে যুক্ত করে।'},
      {'type':'fill','prompt_en':f'Complete the key SQL term: {spec["fill"][:1]}____','prompt_bn':f'Key SQL term complete করুন: {spec["fill"][:1]}____',
       'answer_en':spec['fill'],'answer_bn':spec['fill'],'explanation_en':f'The expected term is {spec["fill"]}.','explanation_bn':f'Expected term হলো {spec["fill"]}।'},
      {'type':'short','prompt_en':f'Write one analytical question that could use {title}, then state the result grain and one validation check.','prompt_bn':f'{bn} ব্যবহার করে একটি analytical question লিখুন, result grain এবং একটি validation check উল্লেখ করুন।',
       'answer_en':f'A strong response defines a measurable question, identifies one row of the output, and names a check such as source-row count, distinct-key count, unmatched-key count, or control-total reconciliation.',
       'answer_bn':'Strong response-এ measurable question, output-এর এক row কী represent করে এবং source-row count, distinct-key count, unmatched-key count বা control-total reconciliation-এর মতো check থাকবে।'}]
    recap=[
      {'en':concept.split('.')[0]+'.','bn':f'{bn} business question ও result grain-এর সঙ্গে ব্যবহার করতে হবে।'},
      {'en':'The SQL should be readable, deterministic where ordering matters, and explicit about filters.','bn':'SQL readable, filter-explicit এবং প্রয়োজন হলে deterministically ordered হওয়া উচিত।'},
      {'en':'Browser practice uses SQLite; production examples explain PostgreSQL-oriented differences.','bn':'Browser practice SQLite ব্যবহার করে; production difference PostgreSQL-orientedভাবে ব্যাখ্যা করা হয়।'},
      {'en':'A result is publishable only after quality and reconciliation checks.','bn':'Quality ও reconciliation check-এর পরে result publish করা উচিত।'}]
    refs=[{'title':'PostgreSQL 18 Documentation — SQL Language','url':'https://www.postgresql.org/docs/current/sql.html'},
          {'title':'SQLite SQL Language Reference','url':'https://www.sqlite.org/lang.html'}]
    return {'id':spec['id'],'module':spec['module'],'level':spec['level'],'title_en':title,'title_bn':bn,
      'summary_en':concept,'summary_bn':f'{bn} ব্যবহার করে relational data থেকে reproducible ও validated analytical result তৈরি করার পদ্ধতি শিখুন।',
      'minutes':45 if spec['level']=='Beginner' else 60,'objectives':[
        {'en':f'Explain {title} in plain language.','bn':f'সহজ ভাষায় {bn} explain করুন।'},
        {'en':'Write or adapt a query using the practice database.','bn':'Practice database ব্যবহার করে query লিখুন বা adapt করুন।'},
        {'en':'State the result grain and important NULL or join behavior.','bn':'Result grain এবং গুরুত্বপূর্ণ NULL বা join behavior উল্লেখ করুন।'},
        {'en':'Validate the result and communicate one limitation.','bn':'Result validate করে একটি limitation communicate করুন।'}],
      'sections':sections,'terms':terms,'worked_example':worked,
      'activity':{'type':'sql-playground','prompt_en':f'Edit and run the query for {title}. Change one condition or selected column, then explain why the result changed.','prompt_bn':f'{bn}-এর query edit ও run করুন। একটি condition বা selected column বদলে result কেন পরিবর্তন হলো explain করুন।','sql':q,'dialect_note_en':'Runs in SQLite in your browser. PostgreSQL differences are explained in the chapter.','dialect_note_bn':'Browser-এ SQLite দিয়ে run হয়; PostgreSQL difference chapter-এ explain করা হয়েছে।'},
      'exercises':exercises,'recap':recap,'references':refs}

chapters=[make_chapter(s,i) for i,s in enumerate(C,1)]

tutorial={
 'id':'sql-data-analytics','title_en':'SQL for Data Analytics Tutorial','title_bn':'Data Analytics-এর জন্য SQL Tutorial',
 'short_title_en':'SQL Analytics','short_title_bn':'SQL Analytics',
 'description_en':'A complete analyst-first SQL tutorial using portable relational concepts, PostgreSQL-oriented explanations, and browser-side SQLite practice for querying, joining, aggregating, window functions, quality checks, and portfolio projects.',
 'description_bn':'Portable relational concept, PostgreSQL-oriented explanation এবং browser-side SQLite practice ব্যবহার করে querying, joining, aggregation, window function, quality check ও portfolio project শেখার complete analyst-first SQL tutorial।',
 'status':'published','version':'2.3.0','estimated_hours':58,'modules':modules,'chapters':chapters,
 'final_quiz':{'title_en':'SQL for Data Analytics Final Quiz','title_bn':'SQL for Data Analytics Final Quiz','pass_percent':75},
 'reference_groups':[
  {'title_en':'PostgreSQL SQL language','title_bn':'PostgreSQL SQL language','references':[
    {'title':'PostgreSQL 18 — SQL Language','url':'https://www.postgresql.org/docs/current/sql.html'},
    {'title':'PostgreSQL Tutorial','url':'https://www.postgresql.org/docs/current/tutorial.html'},
    {'title':'PostgreSQL SELECT','url':'https://www.postgresql.org/docs/current/sql-select.html'},
    {'title':'PostgreSQL Table Expressions and Joins','url':'https://www.postgresql.org/docs/current/queries-table-expressions.html'},
    {'title':'PostgreSQL Aggregate Functions','url':'https://www.postgresql.org/docs/current/functions-aggregate.html'},
    {'title':'PostgreSQL Window Functions','url':'https://www.postgresql.org/docs/current/tutorial-window.html'}]},
  {'title_en':'Browser practice engine','title_bn':'Browser practice engine','references':[
    {'title':'SQLite SQL Language','url':'https://www.sqlite.org/lang.html'},
    {'title':'SQLite SELECT','url':'https://www.sqlite.org/lang_select.html'},
    {'title':'SQLite Window Functions','url':'https://www.sqlite.org/windowfunctions.html'},
    {'title':'sql.js — SQLite in WebAssembly','url':'https://github.com/sql-js/sql.js/'}]}
 ],
 'downloads':[
   {'title_en':'SQL Analytics Practice Database Script','title_bn':'SQL Analytics Practice Database Script','url':'/assets/downloads/sql-analytics-practice-database.sql'},
   {'title_en':'SQL Analytics Practice Queries','title_bn':'SQL Analytics Practice Query','url':'/assets/downloads/sql-analytics-practice-queries.sql'},
   {'title_en':'SQL Practice Data Dictionary','title_bn':'SQL Practice Data Dictionary','url':'/assets/datasets/sql_practice_data_dictionary.csv'}]
}
OUT.write_text(json.dumps(tutorial,ensure_ascii=False,indent=2),encoding='utf-8')

# Deterministic practice database.
rng=random.Random(230)
regions=['Dhaka','Chattogram','Khulna','Rajshahi']
channels=['Online','Retail','Partner']
segments=['Consumer','Corporate','Small Business']
categories=[('Shirt','Apparel'),('Polo Shirt','Apparel'),('Trousers','Apparel'),('Laptop Stand','Accessories'),('Keyboard','Accessories'),('Monitor','Electronics'),('Headset','Electronics'),('Notebook','Stationery'),('Pen Set','Stationery'),('Backpack','Accessories'),('Webcam','Electronics'),('Desk Lamp','Home Office')]
lines=[]
lines += ["PRAGMA foreign_keys = ON;","DROP TABLE IF EXISTS web_events;","DROP TABLE IF EXISTS order_items;","DROP TABLE IF EXISTS orders;","DROP TABLE IF EXISTS products;","DROP TABLE IF EXISTS customers;","DROP TABLE IF EXISTS employees;"]
lines += ["CREATE TABLE employees(employee_id INTEGER PRIMARY KEY, employee_name TEXT NOT NULL, manager_id INTEGER, team TEXT NOT NULL, hire_date TEXT NOT NULL, FOREIGN KEY(manager_id) REFERENCES employees(employee_id));"]
employees=[(1,'Nadia Rahman',None,'Analytics','2022-01-10'),(2,'Arif Hossain',1,'Sales','2022-06-01'),(3,'Mina Akter',1,'Sales','2023-02-15'),(4,'Tanvir Ahmed',2,'Dhaka','2023-05-20'),(5,'Sadia Islam',2,'Chattogram','2024-01-12'),(6,'Rafi Khan',3,'Online','2024-03-01'),(7,'Lamia Noor',3,'Partner','2024-07-18')]
for r in employees: lines.append("INSERT INTO employees VALUES(%s,%s,%s,%s,%s);"%(r[0],repr(r[1]),'NULL' if r[2] is None else r[2],repr(r[3]),repr(r[4])))
lines += ["CREATE TABLE customers(customer_id INTEGER PRIMARY KEY, customer_name TEXT NOT NULL, segment TEXT NOT NULL, city TEXT, signup_date TEXT NOT NULL, active INTEGER NOT NULL CHECK(active IN (0,1)));" ]
first=['Amina','Bashir','Chandra','Dalia','Emon','Farhana','Gopal','Hasan','Ishrat','Jamal','Karim','Laila','Mahin','Nusrat','Omar','Priya','Rashed','Salma','Tariq','Umme']
last=['Ahmed','Akter','Chowdhury','Das','Haque','Islam','Khan','Mia','Rahman','Roy']
customers=[]
for i in range(1,61):
 city=None if i in (17,44) else regions[(i*3)%len(regions)]
 customers.append((i,f'{first[(i-1)%len(first)]} {last[(i*7)%len(last)]}',segments[i%3],city,(date(2025,1,1)+timedelta(days=i*4)).isoformat(),1 if i%11 else 0))
for r in customers: lines.append("INSERT INTO customers VALUES(%d,%s,%s,%s,%s,%d);"%(r[0],repr(r[1]),repr(r[2]),'NULL' if r[3] is None else repr(r[3]),repr(r[4]),r[5]))
lines += ["CREATE TABLE products(product_id INTEGER PRIMARY KEY, product_name TEXT NOT NULL, category TEXT NOT NULL, unit_cost REAL NOT NULL CHECK(unit_cost>=0), list_price REAL NOT NULL CHECK(list_price>=0));"]
products=[]
for i,(name,cat) in enumerate(categories,101):
 cost=round(8+(i-100)*4.7,2); price=round(cost*(1.35+(i%3)*.12),2); products.append((i,name,cat,cost,price))
for r in products: lines.append("INSERT INTO products VALUES(%d,%s,%s,%.2f,%.2f);"%(r[0],repr(r[1]),repr(r[2]),r[3],r[4]))
lines += ["CREATE TABLE orders(order_id INTEGER PRIMARY KEY, customer_id INTEGER NOT NULL, order_date TEXT NOT NULL, region TEXT NOT NULL, channel TEXT NOT NULL, status TEXT NOT NULL, salesperson_id INTEGER, FOREIGN KEY(customer_id) REFERENCES customers(customer_id), FOREIGN KEY(salesperson_id) REFERENCES employees(employee_id));"]
orders=[]
start=date(2026,1,1)
statuses=['Completed','Completed','Shipped','Completed','Cancelled']
for i in range(1,181):
 cust=1+((i*13)%60); dt=(start+timedelta(days=(i*3)%205)).isoformat(); region=regions[(cust*3)%4]; ch=channels[i%3]; status=statuses[i%5]; salesperson=4+(i%4)
 orders.append((1000+i,cust,dt,region,ch,status,salesperson))
for r in orders: lines.append("INSERT INTO orders VALUES(%d,%d,%s,%s,%s,%s,%d);"%(r[0],r[1],repr(r[2]),repr(r[3]),repr(r[4]),repr(r[5]),r[6]))
lines += ["CREATE TABLE order_items(order_item_id INTEGER PRIMARY KEY, order_id INTEGER NOT NULL, product_id INTEGER NOT NULL, quantity INTEGER NOT NULL CHECK(quantity>0), unit_price REAL NOT NULL CHECK(unit_price>=0), discount_pct REAL NOT NULL CHECK(discount_pct BETWEEN 0 AND 1), FOREIGN KEY(order_id) REFERENCES orders(order_id), FOREIGN KEY(product_id) REFERENCES products(product_id));"]
n=1
for o in orders:
 for j in range(1+(o[0]%3)):
  p=products[(o[0]+j*5)%len(products)]; qty=1+((o[0]+j)%5); disc=[0,.05,.1,.15][(o[0]+j)%4]
  lines.append("INSERT INTO order_items VALUES(%d,%d,%d,%d,%.2f,%.2f);"%(n,o[0],p[0],qty,p[4],disc)); n+=1
lines += ["CREATE TABLE web_events(event_id INTEGER PRIMARY KEY, customer_id INTEGER NOT NULL, event_time TEXT NOT NULL, event_name TEXT NOT NULL, campaign TEXT NOT NULL, FOREIGN KEY(customer_id) REFERENCES customers(customer_id));"]
event_id=1
campaigns=['Search','Social','Email']
for c in range(1,51):
 base=date(2026,6,1)+timedelta(days=c%25); camp=campaigns[c%3]
 stages=['visit','product_view']
 if c%4!=0: stages.append('add_to_cart')
 if c%3!=0: stages.append('purchase')
 for k,stage in enumerate(stages):
  lines.append("INSERT INTO web_events VALUES(%d,%d,%s,%s,%s);"%(event_id,c,repr(base.isoformat()+f' {9+k:02d}:00:00'),repr(stage),repr(camp))); event_id+=1
lines += ["CREATE INDEX idx_orders_customer_date ON orders(customer_id,order_date);","CREATE INDEX idx_items_order ON order_items(order_id);","CREATE INDEX idx_events_customer ON web_events(customer_id,event_time);"]
seed='\n'.join(lines)+'\n'
(DL/'sql-analytics-practice-database.sql').write_text(seed,encoding='utf-8')
queries=['-- SQL Analytics practice queries. Run after sql-analytics-practice-database.sql','']
for i,ch in enumerate(chapters,1): queries += [f'-- {i:02d}. {ch["title_en"]}',ch['activity']['sql'].rstrip(';')+';','']
(DL/'sql-analytics-practice-queries.sql').write_text('\n'.join(queries),encoding='utf-8')

with (DS/'sql_practice_data_dictionary.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.writer(f); w.writerow(['table','grain','column','type','description'])
 rows=[
 ('customers','One row per customer','customer_id','INTEGER','Unique customer key'),('customers','One row per customer','customer_name','TEXT','Display name'),('customers','One row per customer','segment','TEXT','Commercial segment'),('customers','One row per customer','city','TEXT','City; may be NULL'),('customers','One row per customer','signup_date','TEXT date','Signup date'),('customers','One row per customer','active','INTEGER 0/1','Current active flag'),
 ('products','One row per product','product_id','INTEGER','Unique product key'),('products','One row per product','product_name','TEXT','Product name'),('products','One row per product','category','TEXT','Product category'),('products','One row per product','unit_cost','REAL','Unit cost'),('products','One row per product','list_price','REAL','List price'),
 ('orders','One row per order','order_id','INTEGER','Unique order key'),('orders','One row per order','customer_id','INTEGER','Customer foreign key'),('orders','One row per order','order_date','TEXT date','Order date'),('orders','One row per order','region','TEXT','Sales region'),('orders','One row per order','channel','TEXT','Sales channel'),('orders','One row per order','status','TEXT','Order status'),('orders','One row per order','salesperson_id','INTEGER','Employee foreign key'),
 ('order_items','One row per order line','order_item_id','INTEGER','Unique line key'),('order_items','One row per order line','order_id','INTEGER','Order foreign key'),('order_items','One row per order line','product_id','INTEGER','Product foreign key'),('order_items','One row per order line','quantity','INTEGER','Units'),('order_items','One row per order line','unit_price','REAL','Selling price per unit'),('order_items','One row per order line','discount_pct','REAL','Discount as decimal'),
 ('employees','One row per employee','employee_id','INTEGER','Unique employee key'),('employees','One row per employee','manager_id','INTEGER','Self-referencing manager key'),('web_events','One row per event','event_id','INTEGER','Unique event key'),('web_events','One row per event','event_name','TEXT','Funnel event'),('web_events','One row per event','campaign','TEXT','Acquisition campaign')]
 w.writerows(rows)
print(f'Wrote {OUT} with {len(chapters)} chapters and SQL practice assets.')
