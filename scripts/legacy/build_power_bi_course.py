from __future__ import annotations

import csv
import json
import random
import zipfile
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'content/tutorials/power_bi_data_analytics.json'
DL = ROOT / 'assets/downloads'
DS = ROOT / 'assets/datasets'
PB_DIR = DS / 'power_bi_retail_model'
DL.mkdir(parents=True, exist_ok=True)
DS.mkdir(parents=True, exist_ok=True)
PB_DIR.mkdir(parents=True, exist_ok=True)

PBI = 'https://learn.microsoft.com/en-us/power-bi/'
DAX = 'https://learn.microsoft.com/en-us/dax/'
PQ = 'https://learn.microsoft.com/en-us/power-query/'

modules = [
    {'id': '01', 'title_en': 'Power BI Foundations and Workflow', 'title_bn': 'Power BI Foundation ও Workflow'},
    {'id': '02', 'title_en': 'Connect and Transform with Power Query', 'title_bn': 'Power Query দিয়ে Connect ও Transform'},
    {'id': '03', 'title_en': 'Semantic Modeling and Relationships', 'title_bn': 'Semantic Modeling ও Relationship'},
    {'id': '04', 'title_en': 'DAX Foundations', 'title_bn': 'DAX Foundation'},
    {'id': '05', 'title_en': 'Analytical DAX Patterns', 'title_bn': 'Analytical DAX Pattern'},
    {'id': '06', 'title_en': 'Reports, Visuals, and Interaction', 'title_bn': 'Report, Visual ও Interaction'},
    {'id': '07', 'title_en': 'Power BI Service, Sharing, and Security', 'title_bn': 'Power BI Service, Sharing ও Security'},
    {'id': '08', 'title_en': 'Performance, Accessibility, and Quality Assurance', 'title_bn': 'Performance, Accessibility ও Quality Assurance'},
    {'id': '09', 'title_en': 'Power BI Portfolio Project', 'title_bn': 'Power BI Portfolio Project'},
]

C: list[dict] = []

def add(id: str, module: str, title: str, bn: str, concept: str, use: str, code: str, operation: str, fill: str, terms: list[tuple[str, str]], level: str = 'Beginner', code_label: str = 'Power BI') -> None:
    C.append(dict(id=id, module=module, title=title, bn=bn, concept=concept, use=use, code=code, operation=operation, fill=fill, terms=terms, level=level, code_label=code_label))

# Module 01 — foundations
add('welcome-to-power-bi-analytics','01','Welcome to Power BI for Data Analytics','Data Analytics-এর জন্য Power BI-এ স্বাগতম',
    'Power BI is Microsoft’s business analytics platform for connecting to data, transforming it, building governed semantic models, creating interactive reports, and sharing insights. Power BI Desktop is the main authoring application; the Power BI service supports publishing, collaboration, refresh, and governed consumption.',
    'Analysts use Power BI when a repeatable report needs a defined model, reusable measures, interactive filtering, and a controlled delivery process rather than a one-off spreadsheet.',
    'Business question → Power Query → Semantic model → DAX measures → Report → Validate → Publish', 'workflow', 'semantic model',
    [('Power BI Desktop','The Windows authoring application used to connect, transform, model, and design reports.'),('Power BI service','The online service used to publish, share, refresh, and govern Power BI content.'),('Semantic model','A governed analytical layer containing tables, relationships, calculations, and metadata.'),('Report','One or more interactive pages built from a semantic model.')])
add('power-bi-ecosystem','01','Power BI Ecosystem: Desktop, Service, Mobile, and Fabric','Power BI Ecosystem: Desktop, Service, Mobile ও Fabric',
    'Power BI works as a connected ecosystem. Desktop is optimized for data preparation, modeling, DAX, and report authoring; the service is optimized for sharing and collaboration; mobile apps are optimized for consuming reports; Microsoft Fabric provides a broader analytics platform around Power BI.',
    'An analyst should choose the correct component for each task instead of treating Desktop and the service as interchangeable.',
    'Author in Desktop → Publish to a workspace → Share through an app → Consume in browser or mobile', 'ecosystem', 'Desktop',
    [('Desktop','Power BI Desktop authoring application.'),('Service','Cloud service for publishing and collaboration.'),('Mobile app','Application for viewing and interacting with reports on mobile devices.'),('Microsoft Fabric','Microsoft’s integrated analytics platform that includes Power BI experiences.')])
add('install-and-update-power-bi-desktop','01','Install and Update Power BI Desktop','Power BI Desktop Install ও Update',
    'Power BI Desktop is a free Windows application. Microsoft recommends the Microsoft Store installation for automatic updates, while the Download Center installer supports managed deployment scenarios.',
    'Analysts should keep Desktop reasonably current, record the version used for a project, and verify organizational policies before enabling preview features.',
    'Microsoft Store (recommended) or Microsoft Download Center → Install → Sign in if required → Check Options', 'checklist', 'Microsoft Store',
    [('Release cadence','The regular schedule on which Power BI Desktop is updated.'),('Preview feature','A feature available for testing before general availability.'),('Microsoft Store version','Installation channel that updates automatically.'),('Desktop version','The specific Power BI Desktop build used to author a file.')])
add('power-bi-desktop-interface','01','Explore the Power BI Desktop Interface','Power BI Desktop Interface Explore করুন',
    'Power BI Desktop organizes work across Report, Data, Model, DAX Query, and other authoring views. The ribbon, canvas, panes, fields, model objects, and status indicators support different stages of the analytical workflow.',
    'Recognizing where to transform data, manage relationships, create measures, and design visuals reduces accidental work in the wrong layer.',
    'Report view | Data view | Model view | Power Query Editor | DAX Query view', 'interface', 'Model view',
    [('Report view','View used to design report pages and visuals.'),('Data view','View used to inspect loaded table data and calculations.'),('Model view','View used to inspect and manage model tables, relationships, and metadata.'),('Power Query Editor','Separate editor used to connect, profile, and transform data before loading.')])
add('power-bi-analyst-workflow','01','The Power BI Analyst Workflow','Power BI Analyst Workflow',
    'A reliable Power BI workflow begins with a business question and metric definitions, then moves through source assessment, Power Query, semantic modeling, DAX, report design, validation, publication, and maintenance.',
    'Analysts use a staged workflow so that data cleaning, model logic, measures, and presentation can be reviewed independently.',
    'Requirements → Source audit → Transform → Model → Calculate → Visualize → Test → Publish → Monitor', 'workflow', 'requirements',
    [('Requirement','A defined business need the report must support.'),('Metric definition','A documented rule describing how a measure is calculated.'),('Validation','Evidence that data, model, measures, and visuals behave as intended.'),('Maintenance','Ongoing refresh, monitoring, documentation, and controlled change.')])
add('reports-dashboards-and-semantic-models','01','Reports, Dashboards, Apps, and Semantic Models','Report, Dashboard, App ও Semantic Model',
    'A Power BI report contains interactive pages connected to a semantic model. A dashboard is a service-only single canvas made from pinned tiles. An app packages selected workspace content for a defined audience.',
    'Analysts must use the correct term because report pages, dashboards, apps, and semantic models have different capabilities and governance boundaries.',
    'Semantic model → Report pages → Optional dashboard tiles → App for audience', 'artifact-choice', 'report',
    [('Report','Interactive multi-page analytical document.'),('Dashboard','Single-page tile canvas in the Power BI service.'),('App','Packaged distribution experience for a target audience.'),('Workspace','Collaborative container for Power BI items.')])
add('connectivity-and-storage-modes','01','Import, DirectQuery, Live Connection, and Direct Lake','Import, DirectQuery, Live Connection ও Direct Lake',
    'Storage and connectivity modes determine where data is stored and how queries are executed. Import loads data into the in-memory model; DirectQuery sends queries to the source; live connection uses an existing semantic model or Analysis Services model; Direct Lake is a Fabric-oriented mode that reads data from OneLake without traditional import.',
    'Analysts choose a mode based on freshness, scale, source performance, governance, feature requirements, and operational complexity—not simply because one mode sounds more real-time.',
    'Import = fastest interactive model for many scenarios | DirectQuery = source-backed queries | Live = existing model | Direct Lake = Fabric lake data', 'storage-mode', 'Import',
    [('Import mode','Loads compressed data into the Power BI semantic model.'),('DirectQuery','Keeps data in the source and sends queries when visuals are used.'),('Live connection','Connects a report to an existing semantic model or Analysis Services model.'),('Direct Lake','Fabric storage mode that reads OneLake data with minimal copying.')], level='Intermediate')

# Module 02 — Power Query
add('connect-to-excel-csv-and-folders','02','Connect to Excel, CSV, and Folder Sources','Excel, CSV ও Folder Source-এ Connect',
    'Power BI can connect to workbooks, delimited files, and folders. The connector, file structure, encoding, delimiters, and schema consistency determine whether the imported data is interpreted correctly.',
    'Analysts inspect source files before loading, preserve identifiers as text, verify dates and decimals, and use the folder connector only when files share a consistent structure.',
    'Home → Get data → Choose connector → Preview → Transform data', 'source-choice', 'Transform data',
    [('Connector','A component that defines how Power BI connects to a source.'),('Navigator','Window used to select source objects for loading or transformation.'),('Folder connector','Connector that combines files from a folder using a sample transformation.'),('Schema drift','Unexpected change in source columns or data types over time.')])
add('navigator-and-load-vs-transform','02','Navigator: Load or Transform Data','Navigator: Load নাকি Transform Data',
    'The Navigator previews source objects and offers Load or Transform Data. Load accepts the current source shape; Transform Data opens Power Query so profiling and cleaning can occur before model load.',
    'Analysts normally choose Transform Data when source quality, column selection, naming, or shaping needs review.',
    'Navigator → Select tables/sheets → Transform Data → Review query → Close & Apply', 'load-transform-choice', 'Transform Data',
    [('Load','Loads selected source objects using their current shape.'),('Transform Data','Opens selected objects in Power Query Editor.'),('Preview','A limited view of source values used before loading.'),('Close & Apply','Saves query changes and loads enabled queries into the model.')])
add('power-query-editor-and-applied-steps','02','Power Query Editor and Applied Steps','Power Query Editor ও Applied Steps',
    'Power Query records transformations as ordered steps. Each step receives a table and returns a new table, allowing refresh to repeat the same process against updated source data.',
    'Analysts use meaningful step names and inspect dependencies so another reviewer can understand the transformation pipeline.',
    'Source → Navigation → Promoted Headers → Changed Type → Filtered Rows → Renamed Columns', 'transform-order', 'Applied Steps',
    [('Query','A repeatable data connection and transformation definition.'),('Applied step','One transformation in a Power Query pipeline.'),('Formula bar','Area that displays the M expression for the selected step.'),('Refresh','Re-execution of source connections and transformation steps.')])
add('data-profiling-column-quality-distribution-profile','02','Column Quality, Distribution, and Profile','Column Quality, Distribution ও Profile',
    'Power Query profiling tools show valid, error, empty, distinct, and unique values, plus distributions and descriptive statistics. Profiling may be based on the top rows unless configured for the entire dataset.',
    'Analysts use profiling before and after transformation to identify missing data, invalid categories, unexpected ranges, and duplicated keys.',
    'View → Column quality | Column distribution | Column profile → Profile entire dataset', 'profile', 'Column profile',
    [('Column quality','Summary of valid, error, and empty values.'),('Column distribution','Frequency and distinctness summary for a column.'),('Column profile','Detailed statistics and value distribution.'),('Profiling scope','Whether profiling uses a sample or the entire dataset.')])
add('data-types-and-locale','02','Data Types and Locale','Data Type ও Locale',
    'Power Query data types affect parsing, relationships, aggregations, compression, and DAX behavior. Locale determines how text dates and decimal separators are interpreted.',
    'Analysts assign types deliberately, preserve leading-zero identifiers as text, and use Change Type Using Locale when source conventions differ.',
    'Column → Data type → Using Locale → Choose type and source locale', 'type-locale', 'locale',
    [('Data type','Rule defining how values are stored and interpreted.'),('Locale','Regional convention used to parse dates, numbers, and text.'),('Identifier','A code used to identify an entity and usually treated as text.'),('Type conversion error','A value that cannot be converted to the requested type.')])
add('select-remove-keep-and-filter-rows','02','Select Columns and Filter Rows','Column Select ও Row Filter',
    'Early column and row reduction can simplify a model, reduce memory, and make later steps clearer. Filters must match the intended analytical population and should not hide source-quality issues without documentation.',
    'Analysts keep only required fields, remove technical columns only after reviewing their purpose, and document date/status filters.',
    'Choose Columns → Remove Other Columns → Filter Rows → Verify row counts', 'filter-rows', 'Choose Columns',
    [('Column pruning','Removing fields not required by the analytical model.'),('Row filter','Rule that keeps or removes records.'),('Analytical population','The records intended to be represented by the report.'),('Control count','A row count used to verify a transformation.')])
add('replace-errors-and-handle-missing-values','02','Replace Errors and Handle Missing Values','Error Replace ও Missing Value Handle',
    'Errors, nulls, blanks, zeroes, and unknown categories are different states. Power Query can remove, replace, or retain them, but the correct action depends on business meaning.',
    'Analysts profile each issue, preserve evidence of source problems, and avoid replacing missing numeric values with zero unless zero is truly the correct business value.',
    'Identify issue → Decide rule → Replace/Remove/Retain → Add quality flag → Re-profile', 'missing-values', 'null',
    [('Null','A missing or unknown value.'),('Error value','A value that failed a transformation or conversion.'),('Imputation','Replacement of a missing value using a defined rule.'),('Quality flag','A field recording whether a row passed a data-quality rule.')])
add('text-date-and-number-transformations','02','Text, Date, and Number Transformations','Text, Date ও Number Transformation',
    'Power Query provides transformations for trimming and cleaning text, changing case, extracting components, calculating date parts, rounding numbers, and applying arithmetic operations.',
    'Analysts standardize categories, derive reporting periods, and create stable source-level fields while avoiding transformations that should remain dynamic DAX measures.',
    'Transform → Format/Extract/Date/Number → Verify data type and sample values', 'transform-functions', 'Trim',
    [('Trim','Removes leading and trailing spaces.'),('Clean','Removes non-printing characters.'),('Date part','A component such as year, month, or weekday.'),('Transformation layer','The stage where data shape and source-level values are prepared.')])
add('split-merge-and-custom-columns','02','Split, Merge, and Custom Columns','Column Split, Merge ও Custom Column',
    'Columns can be split by delimiter, position, or character transition; columns can be merged; custom columns can apply M expressions row by row.',
    'Analysts use these operations to normalize composite fields and create reusable source-level attributes, while checking that delimiters and formats are consistent.',
    'Split Column | Merge Columns | Add Column → Custom Column', 'column-shaping', 'Custom Column',
    [('Delimiter','Character used to separate values.'),('Split column','Operation that divides one field into multiple fields.'),('Merge columns','Operation that combines fields into one text value.'),('Custom column','Column created with an M expression.')])
add('group-by-in-power-query','02','Group By in Power Query','Power Query-তে Group By',
    'Power Query Group By summarizes rows into a new table using one or more keys and aggregations. It changes the table grain and should not be confused with interactive DAX measures.',
    'Analysts use Group By for preprocessing or source-level summaries when detailed rows are not required in the model.',
    'Home → Group By → Choose key columns → Choose aggregation → Validate totals', 'group-by', 'Group By',
    [('Grouping key','Field used to form groups.'),('Aggregation','Summary such as sum, count, minimum, or maximum.'),('Table grain','Meaning of one row after grouping.'),('Pre-aggregation','Summarization before loading into the model.')])
add('pivot-and-unpivot-columns','02','Pivot and Unpivot Columns','Column Pivot ও Unpivot',
    'Pivot converts distinct values into columns; unpivot converts repeated measure columns into attribute-value rows. Analytical models usually prefer a stable long format over separate columns for each month or category.',
    'Analysts unpivot monthly spreadsheets into tidy fact tables and pivot only when a downstream shape specifically requires it.',
    'Select identifier columns → Unpivot Other Columns → Rename Attribute and Value', 'pivot-unpivot', 'Unpivot',
    [('Pivot','Transforms row values into columns.'),('Unpivot','Transforms columns into attribute-value rows.'),('Wide format','Structure with repeated measures across multiple columns.'),('Long format','Structure with one measure column and attributes in rows.')])
add('merge-queries','02','Merge Queries','Query Merge',
    'Merge Queries combines tables by matching one or more key columns and selecting a join kind. The match quality depends on data type, normalization, uniqueness, and the intended relationship.',
    'Analysts use merges for enrichment and reconciliation, while checking unmatched rows and duplicate key effects before expanding related columns.',
    'Home → Merge Queries → Select keys → Choose join kind → Expand columns → Reconcile', 'merge', 'Left Outer',
    [('Merge','Power Query operation that joins tables.'),('Join kind','Rule deciding which matched and unmatched rows are retained.'),('Expand','Operation that selects columns from a nested joined table.'),('Unmatched row','A source row with no key match in the other table.')])
add('append-and-combine-files','02','Append Queries and Combine Files','Query Append ও File Combine',
    'Append stacks rows from tables with compatible columns. The folder combine experience applies a sample transformation to many files and then appends their results.',
    'Analysts use append for monthly extracts and folder ingestion, while monitoring file schema, hidden files, duplicate loads, and source metadata.',
    'Append Queries | Get Data → Folder → Combine & Transform Data', 'append', 'Append',
    [('Append','Operation that stacks rows from multiple tables.'),('Sample file','File used to define transformation logic for a folder import.'),('Source metadata','Information such as filename and folder path retained for auditing.'),('Schema consistency','Agreement of column structure across appended sources.')])
add('query-dependencies-reference-and-duplicate','02','Query Dependencies, Reference, and Duplicate','Query Dependency, Reference ও Duplicate',
    'Query Dependencies shows how queries depend on sources and one another. Reference creates a new query based on another query’s result; Duplicate copies the current query definition.',
    'Analysts build staging and model queries deliberately so cleaning logic is reused without creating unnecessary source connections.',
    'View → Query Dependencies | Right-click query → Reference / Duplicate', 'query-dependency', 'Reference',
    [('Staging query','Intermediate query used to centralize source and cleaning logic.'),('Reference','New query that starts from another query result.'),('Duplicate','Independent copy of a query’s existing steps.'),('Dependency graph','Visual map of query relationships.')], level='Intermediate')
add('m-language-basics','02','Power Query M Language Basics','Power Query M Language Basic',
    'M is the functional language behind Power Query. A query normally uses a let expression containing named steps and an in expression that returns the final step.',
    'Analysts read and edit M when interface-generated steps need clarification, reuse, parameters, or transformations not easily expressed through the ribbon.',
    'let\n    Source = Csv.Document(File.Contents(Path)),\n    Headers = Table.PromoteHeaders(Source),\n    Typed = Table.TransformColumnTypes(Headers, {{"Sales", type number}})\nin\n    Typed', 'm-code', 'let',
    [('M','Functional language used by Power Query.'),('let expression','Block that defines named values or steps.'),('in expression','Expression that returns the final result.'),('Table function','M function that transforms or creates tables.')], level='Intermediate', code_label='Power Query M')
add('parameters-privacy-levels-and-query-folding','02','Parameters, Privacy Levels, and Query Folding','Parameter, Privacy Level ও Query Folding',
    'Parameters make source paths and filters configurable. Privacy levels help prevent unintended data leakage between sources. Query folding allows supported transformations to be translated and executed by the source system.',
    'Analysts use parameters for controlled reuse, respect organizational privacy settings, and inspect folding when source-side execution affects refresh performance.',
    'Manage Parameters | Data source settings → Privacy | View Native Query / folding indicators', 'advanced-query', 'query folding',
    [('Parameter','Named value used to control a query.'),('Privacy level','Classification controlling how data sources may be combined.'),('Query folding','Translation of Power Query steps into source-native operations.'),('Native query','Query executed by the source system.')], level='Advanced')

# Module 03 — modeling
add('semantic-model-design-principles','03','Semantic Model Design Principles','Semantic Model Design Principle',
    'A semantic model organizes analytical tables, relationships, measures, hierarchies, formats, and metadata so report authors can ask consistent questions. Good models favor clear grain, reusable measures, understandable names, and predictable filtering.',
    'Analysts treat the model as a reusable product rather than a hidden technical step behind visuals.',
    'Business process → Fact grain → Dimensions → Relationships → Measures → Metadata', 'model-plan', 'grain',
    [('Semantic model','Analytical layer that defines data structure and calculations.'),('Metadata','Names, descriptions, formats, folders, and properties that explain model objects.'),('Business process','Event or activity measured by a fact table.'),('Model usability','Ease with which users can create correct analyses.')])
add('fact-and-dimension-tables','03','Fact and Dimension Tables','Fact ও Dimension Table',
    'Fact tables record measurable events at a declared grain. Dimension tables describe entities such as date, product, customer, geography, or employee and normally contain unique keys.',
    'Analysts separate facts and dimensions to support reusable filtering and prevent repeated descriptive attributes from creating inconsistent groupings.',
    'FactSales: one row per order line | DimProduct: one row per product | DimCustomer: one row per customer', 'fact-dimension', 'fact table',
    [('Fact table','Table containing measurable events at a defined grain.'),('Dimension table','Table containing descriptive attributes used for filtering and grouping.'),('Surrogate key','Model-controlled key used to identify a dimension row.'),('Degenerate dimension','Descriptive identifier stored directly in a fact table, such as an order number.')])
add('define-fact-table-grain','03','Define the Fact Table Grain','Fact Table Grain Define করুন',
    'Grain is the exact business meaning of one fact-table row. A row may represent an order, order line, daily balance, monthly target, or event; measures and relationships must respect that meaning.',
    'Analysts write the grain in one sentence before designing relationships or DAX, then validate uniqueness at that grain.',
    'FactSales grain: one row per OrderID + ProductKey line', 'grain-choice', 'grain',
    [('Grain','Exact meaning of one row.'),('Transaction fact','Fact table with one row per event.'),('Periodic snapshot','Fact table with one row per entity per regular period.'),('Accumulating snapshot','Fact table that tracks milestones of a process in one row.')])
add('star-schema','03','Build a Star Schema','Star Schema তৈরি করুন',
    'A star schema places a fact table at the center and connects it to denormalized dimensions through one-to-many relationships. This design supports intuitive filtering, efficient compression, and understandable DAX.',
    'Analysts prefer a star schema over a single flat table when multiple dimensions and reusable measures must remain consistent.',
    'DimDate 1→* FactSales *←1 DimProduct\n                     *←1 DimCustomer\n                     *←1 DimRegion', 'star-schema', 'star schema',
    [('Star schema','Dimensional model with facts connected directly to dimensions.'),('Snowflake schema','Model where dimensions are normalized into related subdimensions.'),('Denormalization','Combining descriptive attributes into a dimension for usability.'),('Filter propagation','Movement of filter context through model relationships.')])
add('relationships-cardinality-and-cross-filter-direction','03','Relationships, Cardinality, and Cross-filter Direction','Relationship, Cardinality ও Cross-filter Direction',
    'A relationship connects columns and defines cardinality, filter direction, and active status. The common analytical pattern is one-to-many from a dimension’s unique key to a fact table’s repeated foreign key.',
    'Analysts verify uniqueness on the one side and normally use single-direction filtering from dimension to fact unless a documented scenario requires otherwise.',
    'DimProduct[ProductKey] (1) → (*) FactSales[ProductKey] | Single direction', 'relationship', 'one-to-many',
    [('Cardinality','Whether relationship keys are one or many on each side.'),('Cross-filter direction','Direction in which filters propagate.'),('Active relationship','Default relationship used for filter propagation.'),('Foreign key','Fact-table column referring to a dimension key.')])
add('active-and-inactive-relationships','03','Active and Inactive Relationships','Active ও Inactive Relationship',
    'Only one relationship between two tables can be active for a given path. Inactive relationships remain available and can be activated in a measure with USERELATIONSHIP.',
    'Analysts use inactive relationships for role-playing dates such as Order Date and Ship Date while keeping the default reporting date explicit.',
    'Shipped Revenue = CALCULATE([Total Revenue], USERELATIONSHIP(DimDate[Date], FactSales[ShipDate]))', 'inactive-relationship', 'USERELATIONSHIP',
    [('Inactive relationship','Relationship stored in the model but not used by default.'),('Role-playing dimension','One dimension used in multiple semantic roles, such as Order Date and Ship Date.'),('USERELATIONSHIP','DAX function that activates a relationship for one calculation.'),('Relationship path','Sequence through which filters travel between tables.')], level='Intermediate', code_label='DAX')
add('many-to-many-and-bridge-tables','03','Many-to-many Relationships and Bridge Tables','Many-to-many Relationship ও Bridge Table',
    'Many-to-many scenarios occur when keys are repeated on both sides. A bridge table containing unique associations often creates clearer one-to-many paths and reduces ambiguous filtering.',
    'Analysts avoid using many-to-many cardinality as a shortcut before understanding the real business relationship and duplication risk.',
    'DimCustomer 1→* BridgeCustomerAccount *←1 DimAccount', 'bridge-table', 'bridge table',
    [('Many-to-many','Relationship where keys repeat on both sides.'),('Bridge table','Table that resolves associations between dimensions.'),('Ambiguity','More than one valid filter path between model objects.'),('Association table','Another name for a table storing many-to-many links.')], level='Advanced')
add('date-table','03','Create and Mark a Date Table','Date Table তৈরি ও Mark করুন',
    'A dedicated date table provides one row per date and attributes such as year, quarter, month, week, and fiscal period. Marking it as a date table supports reliable date behavior and model design.',
    'Analysts use a continuous date table related to each fact date and sort labels such as Month Name by numeric keys.',
    'DimDate = CALENDAR(DATE(2025,1,1), DATE(2026,12,31))', 'date-table', 'CALENDAR',
    [('Date table','Dimension containing one unique row for every required date.'),('Continuous date range','Sequence with no missing calendar dates.'),('Sort by column','Property used to order labels by another column.'),('Fiscal calendar','Organization-specific reporting calendar.')], code_label='DAX')
add('hierarchies-sort-by-and-default-summarization','03','Hierarchies, Sort By Column, and Default Summarization','Hierarchy, Sort By Column ও Default Summarization',
    'Hierarchies provide ordered drill paths; Sort By Column controls label ordering; default summarization controls how numeric fields behave when added to visuals.',
    'Analysts configure metadata so users do not accidentally alphabetize months or sum identifiers.',
    'Date hierarchy: Year → Quarter → Month → Date | Month Name sorted by Month Number', 'metadata', 'Sort by column',
    [('Hierarchy','Ordered group of fields used for drill navigation.'),('Sort by column','Model property that controls display order.'),('Default summarization','Default aggregation assigned to a numeric field.'),('Data category','Metadata describing geographic, URL, image, or other semantic meaning.')])
add('model-cleanup-names-formats-and-folders','03','Model Cleanup: Names, Formats, and Display Folders','Model Cleanup: Name, Format ও Display Folder',
    'A usable model hides technical keys, applies clear business names, sets formats, adds descriptions, and groups measures into display folders. Clean metadata reduces report errors and makes self-service analysis safer.',
    'Analysts review the Fields pane from the consumer’s perspective before report design begins.',
    'Hide keys → Rename fields → Format currency/percent → Add descriptions → Organize measures', 'model-cleanup', 'display folder',
    [('Display folder','Organizational folder for model fields and measures.'),('Format string','Rule controlling how a value is displayed.'),('Hidden field','Model field unavailable to ordinary report authors.'),('Description','Metadata explaining the purpose and definition of an object.')])

# Module 04 — DAX foundations
add('dax-overview','04','DAX Overview','DAX Overview',
    'Data Analysis Expressions (DAX) is the formula language used to create measures, calculated columns, calculated tables, and queries in Power BI semantic models. DAX evaluates expressions within model relationships and context.',
    'Analysts use DAX to centralize business metrics so every visual applies the same calculation rules.',
    'Total Revenue = SUM(FactSales[Revenue])', 'dax-basic', 'DAX',
    [('DAX','Formula language for tabular semantic models.'),('Expression','Combination of functions, operators, columns, and constants.'),('Measure','Calculation evaluated in the current filter context.'),('Calculated column','Column calculated row by row and stored in the model.')], code_label='DAX')
add('measures-vs-calculated-columns','04','Measures vs Calculated Columns','Measure বনাম Calculated Column',
    'Calculated columns are evaluated for every row during refresh and stored in the model. Measures are evaluated at query time in the filter context created by a visual or query.',
    'Analysts prefer measures for aggregations and dynamic KPIs, and use calculated columns only when a row-level attribute is needed for grouping, sorting, relationships, or filtering.',
    'Line Margin = FactSales[Revenue] - FactSales[Cost]\nTotal Margin = SUM(FactSales[Revenue]) - SUM(FactSales[Cost])', 'measure-column', 'measure',
    [('Measure','Dynamic calculation evaluated in filter context.'),('Calculated column','Stored row-level calculation.'),('Refresh time','Time when imported data and calculated columns are processed.'),('Query time','Time when measures are evaluated for report interactions.')], code_label='DAX')
add('dax-syntax-functions-and-operators','04','DAX Syntax, Functions, and Operators','DAX Syntax, Function ও Operator',
    'A DAX formula has an object name, equals sign, and expression. Table and column references use Table[Column]; measure references use [Measure]. Operators control arithmetic, comparison, concatenation, and logical behavior.',
    'Analysts format DAX consistently and use descriptive measure names so logic can be reviewed and reused.',
    'Gross Profit = [Total Revenue] - [Total Cost]', 'dax-expression', 'expression',
    [('Function','Named operation that accepts arguments and returns a value or table.'),('Operator','Symbol that performs arithmetic, comparison, or logical work.'),('Column reference','Reference written as Table[Column].'),('Measure reference','Reference written as [Measure].')], code_label='DAX')
add('aggregation-measures','04','Aggregation Measures','Aggregation Measure',
    'SUM, COUNT, COUNTROWS, DISTINCTCOUNT, MIN, MAX, and AVERAGE create foundational measures. The choice must reflect business grain and missing-value behavior.',
    'Analysts define base measures first and then compose them into ratios, variances, and KPIs.',
    'Order Count = DISTINCTCOUNT(FactSales[OrderID])\nUnits Sold = SUM(FactSales[Quantity])', 'dax-aggregate', 'DISTINCTCOUNT',
    [('Base measure','Simple reusable measure used by other calculations.'),('COUNTROWS','Counts rows in a table expression.'),('DISTINCTCOUNT','Counts distinct nonblank values plus a possible blank.'),('Additive measure','Measure that can be summed across all relevant dimensions.')], code_label='DAX')
add('row-context','04','Row Context','Row Context',
    'Row context represents the current row during calculated-column evaluation or iterator execution. It does not automatically filter related tables in the same way as filter context.',
    'Analysts identify row context when writing calculated columns and X-functions such as SUMX.',
    'Line Revenue = FactSales[Quantity] * FactSales[UnitPrice] * (1 - FactSales[DiscountPct])', 'row-context', 'row context',
    [('Row context','Current row available during row-by-row evaluation.'),('Iterator','Function that evaluates an expression for each row of a table.'),('Current row','Specific record being evaluated.'),('RELATED','Function that retrieves a value from a related one-side table in row context.')], code_label='DAX')
add('filter-context','04','Filter Context','Filter Context',
    'Filter context is the set of filters applied by visuals, slicers, page filters, relationships, and DAX expressions. A measure can return a different value in every visual cell because each cell has a different context.',
    'Analysts explain measure behavior by listing the filters active at the point of evaluation.',
    'A matrix cell for Region = Dhaka and Year = 2026 evaluates [Total Revenue] under both filters.', 'filter-context', 'filter context',
    [('Filter context','Filters active when an expression is evaluated.'),('Visual context','Context created by fields placed in a visual.'),('Slicer','Interactive control that adds filters.'),('Granularity','Level of detail represented by a visual cell or row.')], code_label='DAX')
add('calculate-and-context-transition','04','CALCULATE and Context Transition','CALCULATE ও Context Transition',
    'CALCULATE evaluates an expression in a modified filter context. It can add, replace, or remove filters. When used in row context, it also performs context transition, converting current-row values into filters.',
    'Analysts treat CALCULATE as the central DAX function and make every filter argument explicit and reviewable.',
    'Online Revenue = CALCULATE([Total Revenue], DimChannel[Channel] = "Online")', 'calculate', 'CALCULATE',
    [('CALCULATE','Evaluates an expression under modified filter context.'),('Context transition','Conversion of row context into filter context.'),('Filter argument','Condition or table expression supplied to CALCULATE.'),('Boolean filter','Simple column condition used as a CALCULATE filter.')], level='Intermediate', code_label='DAX')
add('filter-all-removefilters-keepfilters','04','FILTER, ALL, REMOVEFILTERS, and KEEPFILTERS','FILTER, ALL, REMOVEFILTERS ও KEEPFILTERS',
    'FILTER returns rows meeting an expression; ALL and REMOVEFILTERS clear filters; KEEPFILTERS intersects new filters with existing context. These functions control how a measure responds to report selections.',
    'Analysts use them to build shares, benchmarks, and conditional populations while avoiding accidental filter removal.',
    'Revenue Share = DIVIDE([Total Revenue], CALCULATE([Total Revenue], REMOVEFILTERS(DimProduct)))', 'filter-functions', 'REMOVEFILTERS',
    [('FILTER','Returns a filtered table.'),('ALL','Returns all values or rows while removing filters for the specified object.'),('REMOVEFILTERS','Clears filters from specified tables or columns.'),('KEEPFILTERS','Adds a filter without replacing existing filters on the same columns.')], level='Intermediate', code_label='DAX')
add('iterators-sumx-and-averagex','04','Iterators: SUMX and AVERAGEX','Iterator: SUMX ও AVERAGEX',
    'Iterator functions evaluate an expression row by row over a table and then aggregate the results. They are required when the desired value is not stored as one additive column.',
    'Analysts use SUMX for quantity-times-price calculations and validate whether iteration occurs over the correct table and grain.',
    'Revenue = SUMX(FactSales, FactSales[Quantity] * FactSales[UnitPrice] * (1 - FactSales[DiscountPct]))', 'iterator', 'SUMX',
    [('Iterator','Function that evaluates an expression for every row of a table.'),('SUMX','Iterator that sums row-level expression results.'),('AVERAGEX','Iterator that averages row-level expression results.'),('Table expression','Expression that returns a table for an iterator or filter.')], level='Intermediate', code_label='DAX')
add('variables-and-readable-dax','04','Variables and Readable DAX','Variable ও Readable DAX',
    'VAR stores a scalar or table result inside a DAX expression, and RETURN specifies the final result. Variables improve readability, debugging, and reuse within one calculation.',
    'Analysts use descriptive variables to separate intermediate business logic and avoid repeating expensive or error-prone expressions.',
    'Gross Margin % =\nVAR Revenue = [Total Revenue]\nVAR Profit = [Gross Profit]\nRETURN DIVIDE(Profit, Revenue)', 'dax-variables', 'VAR',
    [('VAR','Keyword defining a DAX variable.'),('RETURN','Keyword returning the final expression.'),('Scalar variable','Variable containing one value.'),('Table variable','Variable containing a table expression.')], code_label='DAX')
add('divide-blanks-and-defensive-dax','04','DIVIDE, BLANK, and Defensive DAX','DIVIDE, BLANK ও Defensive DAX',
    'DIVIDE safely handles zero or blank denominators. BLANK represents the absence of a meaningful result and often produces cleaner visuals than forced zeroes.',
    'Analysts define when a metric is not applicable, distinguish missing from zero, and avoid hiding data-quality problems with broad IFERROR-style logic.',
    'Average Order Value = DIVIDE([Total Revenue], [Order Count])', 'safe-division', 'DIVIDE',
    [('DIVIDE','DAX function for safe division with optional alternate result.'),('BLANK','Special DAX value representing no meaningful result.'),('Denominator','Value by which the numerator is divided.'),('Defensive calculation','Logic that handles invalid or undefined cases explicitly.')], code_label='DAX')
add('dax-query-view-and-evaluate','04','DAX Query View and EVALUATE','DAX Query View ও EVALUATE',
    'DAX Query View lets authors write and run DAX queries against the model, inspect results, and test calculations. DAX queries return tables and commonly use EVALUATE.',
    'Analysts use DAX queries to validate measures, inspect summarized results, and develop calculations outside report visuals.',
    'EVALUATE\nSUMMARIZECOLUMNS(\n    DimRegion[Region],\n    "Revenue", [Total Revenue]\n)', 'dax-query', 'EVALUATE',
    [('DAX query','Statement that returns tabular results from a semantic model.'),('EVALUATE','DAX statement that returns a table expression.'),('SUMMARIZECOLUMNS','Function used to group and calculate query results.'),('Query view','Power BI Desktop view for authoring and testing DAX queries.')], level='Intermediate', code_label='DAX Query')

# Module 05 — analytical DAX
add('date-intelligence-prerequisites','05','Time Intelligence Prerequisites','Time Intelligence Prerequisite',
    'Reliable time intelligence requires a valid date table, continuous dates, correct relationships, and measures that aggregate over fact dates. Calendar and fiscal definitions must be documented.',
    'Analysts validate the date model before using period functions so missing dates or incorrect relationships do not produce misleading trends.',
    'Date table → Mark as date table → Relate to fact → Build base measure → Add time measure', 'time-prereq', 'date table',
    [('Time intelligence','Calculations comparing values across defined time periods.'),('Date table','Dedicated table containing continuous dates and calendar attributes.'),('Calendar context','Dates active in the current filter context.'),('Fiscal period','Organization-defined accounting period.')], level='Intermediate')
add('year-to-date-quarter-to-date-month-to-date','05','YTD, QTD, and MTD Measures','YTD, QTD ও MTD Measure',
    'TOTALYTD, TOTALQTD, TOTALMTD, or CALCULATE with date functions can accumulate a base measure from the beginning of a period to the current date context.',
    'Analysts use these measures for progress reporting but label them clearly and compare like-for-like incomplete periods.',
    'Revenue YTD = TOTALYTD([Total Revenue], DimDate[Date])', 'period-to-date', 'TOTALYTD',
    [('YTD','Year-to-date accumulation.'),('QTD','Quarter-to-date accumulation.'),('MTD','Month-to-date accumulation.'),('Cutoff date','Latest date included in a period-to-date calculation.')], level='Intermediate', code_label='DAX')
add('previous-period-and-growth','05','Previous Period and Growth Measures','Previous Period ও Growth Measure',
    'DATEADD, SAMEPERIODLASTYEAR, and related functions shift date context to a comparable period. Growth measures compare current and prior values using a clearly defined denominator.',
    'Analysts check whether periods are complete and explain absolute variance separately from percentage growth.',
    'Revenue PY = CALCULATE([Total Revenue], SAMEPERIODLASTYEAR(DimDate[Date]))\nYoY % = DIVIDE([Total Revenue] - [Revenue PY], [Revenue PY])', 'growth', 'SAMEPERIODLASTYEAR',
    [('Prior period','Comparable period before the current one.'),('Absolute variance','Current value minus comparison value.'),('Growth rate','Variance divided by the comparison value.'),('Comparable period','Period aligned by duration and business calendar.')], level='Intermediate', code_label='DAX')
add('running-totals','05','Running Totals','Running Total',
    'A running total accumulates a measure from a defined starting point through the maximum date in the current context. The filter logic must preserve the intended date scope.',
    'Analysts use running totals for cumulative sales, budget consumption, and progress tracking.',
    'Revenue Running =\nVAR MaxDate = MAX(DimDate[Date])\nRETURN CALCULATE([Total Revenue], FILTER(ALLSELECTED(DimDate[Date]), DimDate[Date] <= MaxDate))', 'running-total', 'ALLSELECTED',
    [('Running total','Cumulative value through the current point.'),('ALLSELECTED','Function retaining outer selections while removing row/column context.'),('Maximum date','Latest date represented by the current visual point.'),('Cumulative scope','Date range included in accumulation.')], level='Intermediate', code_label='DAX')
add('moving-averages','05','Moving Averages','Moving Average',
    'A moving average summarizes a rolling date window to reduce short-term noise. The window length, date grain, and treatment of incomplete windows must be stated.',
    'Analysts use rolling averages to reveal trends without claiming that smoothing predicts the future.',
    'Revenue 3M Avg =\nAVERAGEX(\n    DATESINPERIOD(DimDate[Date], MAX(DimDate[Date]), -3, MONTH),\n    [Total Revenue]\n)', 'moving-average', 'DATESINPERIOD',
    [('Moving average','Average calculated over a rolling window.'),('Rolling window','Period that moves with the current date.'),('Smoothing','Reduction of short-term variation to reveal a trend.'),('Incomplete window','Early period containing fewer observations than requested.')], level='Advanced', code_label='DAX')
add('ranking-and-top-n','05','Ranking and Top N','Ranking ও Top N',
    'RANKX ranks items by an expression within a defined comparison table. Top-N visuals or measures must define ties, filter scope, and whether an “Other” category is needed.',
    'Analysts rank products, customers, or regions while preserving slicer selections and avoiding unstable tie behavior.',
    'Product Rank = RANKX(ALLSELECTED(DimProduct[Product]), [Total Revenue], , DESC, DENSE)', 'ranking', 'RANKX',
    [('RANKX','Iterator that ranks rows by an expression.'),('Dense rank','Ranking method without gaps after ties.'),('Comparison set','Items against which the current item is ranked.'),('Top N','Selection of the highest N items by a measure.')], level='Intermediate', code_label='DAX')
add('percent-of-total-and-contribution','05','Percent of Total and Contribution','Percent of Total ও Contribution',
    'A contribution measure divides the current value by a denominator calculated after removing selected dimension filters. The exact filters removed determine whether the denominator is grand total, page total, or selected total.',
    'Analysts use contribution measures to explain mix and concentration, and label the denominator scope clearly.',
    'Revenue Share = DIVIDE([Total Revenue], CALCULATE([Total Revenue], REMOVEFILTERS(DimProduct[Product])))', 'share', 'REMOVEFILTERS',
    [('Contribution','Share of a total attributable to an item.'),('Denominator scope','Filters retained or removed for the total.'),('Grand total','Total across the full allowed population.'),('Selected total','Total within current outer selections.')], level='Intermediate', code_label='DAX')
add('targets-variance-and-kpi-status','05','Targets, Variance, and KPI Status','Target, Variance ও KPI Status',
    'Target analysis requires a target fact table at a defined grain, compatible dimensions, and measures for actual, target, variance, and status. Targets should not be repeated across detailed fact rows.',
    'Analysts model monthly or regional targets separately and use color/status rules only after validating sign and threshold logic.',
    'Variance = [Total Revenue] - [Revenue Target]\nVariance % = DIVIDE([Variance], [Revenue Target])', 'target-kpi', 'variance',
    [('Target fact','Table containing planned values at a defined grain.'),('Variance','Actual value minus target or comparison value.'),('KPI status','Categorical interpretation based on documented thresholds.'),('Target grain','Dimensions and period represented by one target row.')], level='Intermediate', code_label='DAX')

# Module 06 — visuals and report interaction
add('visual-selection-principles','06','Choose the Right Visual','সঠিক Visual বেছে নিন',
    'Visual selection begins with the analytical task: comparison, trend, distribution, relationship, composition, detail, or geography. Decoration should never override accurate encoding.',
    'Analysts choose the simplest visual that answers the question and avoid visual types that distort magnitude or hide uncertainty.',
    'Comparison → bar/column | Trend → line | Distribution → histogram/box plot | Relationship → scatter', 'visual-choice', 'line chart',
    [('Visual encoding','Use of position, length, color, shape, or size to represent data.'),('Comparison','Evaluation of magnitude across categories.'),('Trend','Change over an ordered time axis.'),('Distribution','Pattern of values including center, spread, and unusual observations.')])
add('cards-tables-and-matrices','06','Cards, Tables, and Matrices','Card, Table ও Matrix',
    'Cards emphasize a small number of KPIs; tables show detailed records; matrices support grouped rows, columns, subtotals, and drill. Each requires intentional formatting and context labels.',
    'Analysts use cards for headline metrics and tables or matrices when users need exact values or hierarchical detail.',
    'Card: [Total Revenue] | Matrix: Region × Month with Revenue and Margin %', 'visual-layout', 'matrix',
    [('Card','Visual emphasizing one or a few values.'),('Table visual','Flat rows and columns.'),('Matrix visual','Pivot-style visual with grouped rows and columns.'),('Subtotal','Summary value for a group in a matrix.')])
add('bar-column-and-line-charts','06','Bar, Column, and Line Charts','Bar, Column ও Line Chart',
    'Bar and column charts compare categorical magnitudes; line charts show change over an ordered continuous axis. Axis baselines, sorting, category count, and time granularity affect interpretation.',
    'Analysts sort categorical comparisons by value when appropriate and use continuous date axes for trends when the model supports them.',
    'Bar: Revenue by Product | Line: Monthly Revenue | Column: Orders by Region', 'chart-choice', 'line chart',
    [('Categorical axis','Axis containing distinct labels.'),('Continuous axis','Axis representing a numeric or date continuum.'),('Baseline','Starting value of a quantitative axis.'),('Small multiple','Repeated visual panels using a shared scale and design.')])
add('scatter-combo-waterfall-and-other-visuals','06','Scatter, Combo, Waterfall, and Specialized Visuals','Scatter, Combo, Waterfall ও Specialized Visual',
    'Scatter plots show relationships between quantitative variables; combo charts combine compatible measures; waterfalls explain sequential contributions to change. Specialized visuals should be used only when their analytical purpose is clear.',
    'Analysts add meaningful labels, units, and reference lines and avoid combining scales that create misleading comparisons.',
    'Scatter: Revenue vs Margin by Product | Waterfall: Target → Volume → Price → Actual', 'special-visual', 'scatter',
    [('Scatter plot','Visual showing paired quantitative values.'),('Combo chart','Visual combining column and line series.'),('Waterfall chart','Visual showing positive and negative contributions to a total.'),('Secondary axis','Additional quantitative scale that requires careful interpretation.')], level='Intermediate')
add('slicers-filters-and-filter-pane','06','Slicers, Filters, and the Filter Pane','Slicer, Filter ও Filter Pane',
    'Power BI supports visual, page, report, drillthrough, and slicer filters. Filter placement affects discoverability, consistency, and user interpretation.',
    'Analysts expose important filters as slicers, use the filter pane for controlled conditions, and test how filters interact with each page.',
    'Slicer: Year | Page filter: Active Customers | Report filter: Exclude Test Records', 'filter-design', 'slicer',
    [('Slicer','On-canvas interactive filter visual.'),('Visual-level filter','Filter applied to one visual.'),('Page-level filter','Filter applied to all visuals on one page.'),('Report-level filter','Filter applied across all report pages.')])
add('visual-interactions','06','Edit Visual Interactions','Visual Interaction Edit করুন',
    'Selecting a data point can filter, highlight, or leave other visuals unchanged. Edit Interactions controls this behavior per visual pair.',
    'Analysts test cross-filtering to ensure selections support the intended question and do not create confusing partial highlights.',
    'Select source visual → Format → Edit interactions → Filter / Highlight / None', 'interaction', 'Edit interactions',
    [('Cross-filter','Interaction that removes unrelated data from another visual.'),('Cross-highlight','Interaction that emphasizes selected contribution while retaining totals.'),('Interaction source','Visual from which a selection originates.'),('Interaction target','Visual affected by the selection.')])
add('drill-down-and-hierarchies','06','Drill Down with Hierarchies','Hierarchy দিয়ে Drill Down',
    'Drill features move through hierarchy levels such as Year, Quarter, Month, and Date. Users can drill one point, expand all levels, or move back up.',
    'Analysts create intentional hierarchies and provide titles or navigation cues so users understand the current level.',
    'Year → Quarter → Month → Date', 'drill', 'hierarchy',
    [('Drill down','Move to a lower hierarchy level for a selected item.'),('Expand','Show current and next hierarchy levels together.'),('Drill up','Return to a higher hierarchy level.'),('Hierarchy level','One ordered field in a drill path.')])
add('drillthrough-pages','06','Drillthrough Pages','Drillthrough Page',
    'Drillthrough lets a user open a detail page filtered to a selected entity. The destination page receives the drillthrough field and can include a back button.',
    'Analysts use drillthrough for customer, product, project, or transaction detail without overcrowding summary pages.',
    'Summary visual → Right-click item → Drill through → Detail page', 'drillthrough', 'Drillthrough',
    [('Drillthrough','Navigation to a filtered detail page.'),('Drillthrough field','Field that carries context to the destination page.'),('Detail page','Page designed for one selected entity or category.'),('Back button','Navigation control returning to the source page.')])
add('report-page-tooltips','06','Report Page Tooltips','Report Page Tooltip',
    'A report page tooltip is a specially sized page shown when users hover over a visual data point. It can provide context without permanent dashboard clutter.',
    'Analysts keep tooltips concise, align them with the hovered grain, and avoid hiding essential information only in hover states.',
    'Create page → Page information: Tooltip On → Canvas: Tooltip size → Assign to visual', 'tooltip', 'Tooltip',
    [('Tooltip','Context shown on hover.'),('Report page tooltip','Custom report page used as a tooltip.'),('Hover context','Filter context generated by the hovered data point.'),('Tooltip field','Field that helps determine when a tooltip is relevant.')])
add('conditional-formatting-and-dynamic-titles','06','Conditional Formatting and Dynamic Titles','Conditional Formatting ও Dynamic Title',
    'Conditional formatting uses values, rules, field values, or measures to control colors, icons, bars, and labels. Dynamic titles use DAX measures to describe current context.',
    'Analysts use formatting to communicate meaning consistently, not to decorate, and ensure the same status color always means the same condition.',
    'Page Title = "Sales — " & COALESCE(SELECTEDVALUE(DimRegion[Region]), "All Regions")', 'dynamic-format', 'SELECTEDVALUE',
    [('Conditional formatting','Formatting controlled by data or rules.'),('Dynamic title','Title generated from current filter context.'),('Field value formatting','Formatting driven by a measure or column containing style values.'),('Status rule','Documented mapping from metric values to labels or colors.')], code_label='DAX')
add('bookmarks-buttons-and-page-navigation','06','Bookmarks, Buttons, and Page Navigation','Bookmark, Button ও Page Navigation',
    'Bookmarks capture selected report state, including page, filters, visibility, and spotlight settings. Buttons can trigger bookmarks, page navigation, drillthrough, or URLs.',
    'Analysts use bookmarks for guided stories, view switching, and help panels while documenting which state properties are captured.',
    'View → Bookmarks → Add | Insert → Buttons → Action', 'navigation', 'bookmark',
    [('Bookmark','Saved report state.'),('Selection pane','Pane controlling object visibility and layering.'),('Button action','Navigation or interaction triggered by a button.'),('Bookmark navigator','Visual control generated from bookmark groups.')])
add('dashboard-layout-and-information-hierarchy','06','Dashboard Layout and Information Hierarchy','Dashboard Layout ও Information Hierarchy',
    'A decision-ready report page uses a visual hierarchy: context and filters, headline KPIs, diagnostic trends, segment comparisons, and detail. Alignment, spacing, contrast, and consistent units improve comprehension.',
    'Analysts design for the questions users ask first, not for the maximum number of visuals that fit on a canvas.',
    'Header/context → KPI row → Trend and drivers → Segment detail → Notes and definitions', 'dashboard-layout', 'visual hierarchy',
    [('Visual hierarchy','Order in which a page directs attention.'),('Grid','Alignment structure used to organize page objects.'),('White space','Intentional empty space that separates and groups content.'),('Information density','Amount of information presented in a limited area.')])

# Module 07 — service and security
add('publish-from-desktop-to-service','07','Publish from Desktop to the Power BI Service','Desktop থেকে Power BI Service-এ Publish',
    'Publishing sends a report and its semantic model to a selected workspace. Publication does not automatically define audience permissions, refresh, endorsement, or lifecycle controls.',
    'Analysts publish only after validation, select the correct workspace, and verify the uploaded model and report before distribution.',
    'Home → Publish → Select workspace → Open in Power BI → Validate', 'publish', 'workspace',
    [('Publish','Upload Power BI content from Desktop to the service.'),('Workspace','Collaborative container in the service.'),('Semantic model item','Published model used by reports.'),('Report item','Published report connected to a semantic model.')])
add('workspaces-roles-and-collaboration','07','Workspaces, Roles, and Collaboration','Workspace, Role ও Collaboration',
    'Workspaces organize content and use roles such as Admin, Member, Contributor, and Viewer to control collaboration. Workspace access is different from app audience access and row-level security.',
    'Analysts apply least privilege and avoid using personal workspaces for team production content.',
    'Admin | Member | Contributor | Viewer → Assign according to responsibility', 'workspace-role', 'Viewer',
    [('Workspace role','Permission level for collaborating in a workspace.'),('Least privilege','Granting only the access required.'),('My workspace','Personal workspace not intended for governed team delivery.'),('Content ownership','Responsibility for maintaining and approving an item.')])
add('apps-and-audience-distribution','07','Power BI Apps and Audience Distribution','Power BI App ও Audience Distribution',
    'A Power BI app packages selected workspace content for consumers. Multiple audiences can receive different content selections while the workspace remains the authoring area.',
    'Analysts use apps for stable distribution and test navigation, permissions, and audience visibility before release.',
    'Workspace → Create/Update app → Define content and audiences → Publish app', 'app-audience', 'app',
    [('App','Packaged collection of Power BI content for consumers.'),('Audience','Group receiving a defined subset of app content.'),('App navigation','Organized links and sections shown to app users.'),('Update app','Action that publishes workspace changes to app users.')])
add('scheduled-refresh-and-gateways','07','Scheduled Refresh and Data Gateways','Scheduled Refresh ও Data Gateway',
    'Scheduled refresh updates imported semantic models. On-premises or private-network sources may require an on-premises data gateway. Credentials, privacy, capacity, and source availability affect refresh.',
    'Analysts configure refresh ownership, monitor history, document failure response, and test that source changes do not break Power Query.',
    'Semantic model settings → Data source credentials → Gateway connection → Scheduled refresh → Refresh history', 'refresh', 'gateway',
    [('Scheduled refresh','Service process that reloads imported data on a schedule.'),('Gateway','Software that securely connects cloud services to private data sources.'),('Credentials','Authentication information used to access a source.'),('Refresh history','Record of refresh outcomes and errors.')], level='Intermediate')
add('row-level-security','07','Row-level Security (RLS)','Row-level Security (RLS)',
    'RLS applies role filters to model rows so users see only permitted data. Roles are defined in Desktop and users or groups are assigned in the service. Workspace permissions can affect how RLS is enforced.',
    'Analysts test roles with representative users, avoid encoding security only in visuals, and document the access rule and identity source.',
    'Role filter example: DimRegion[Region] = "Dhaka"', 'rls', 'RLS',
    [('Row-level security','Model rules restricting rows visible to a user.'),('Role','Named set of model filter rules.'),('Test as role','Desktop feature for validating security behavior.'),('Dynamic RLS','Security rule using user identity to determine allowed rows.')], level='Intermediate', code_label='DAX')
add('object-level-security-and-sensitivity-concepts','07','Object-level Security and Sensitivity Concepts','Object-level Security ও Sensitivity Concept',
    'Object-level security can hide model tables or columns from unauthorized users in supported scenarios. Sensitivity labels classify content and help organizational information-protection policies travel with data.',
    'Analysts coordinate security and classification with administrators and avoid presenting labels as a substitute for access control.',
    'Classify content → Restrict access → Test effective permissions → Monitor distribution', 'security-review', 'sensitivity label',
    [('Object-level security','Security that hides model tables or columns.'),('Sensitivity label','Information-protection classification applied to content.'),('Effective permission','Access a user actually receives after all roles and sharing paths.'),('Data classification','Assignment of handling requirements to information.')], level='Advanced')
add('sharing-export-and-governance','07','Sharing, Export, and Governance','Sharing, Export ও Governance',
    'Power BI supports sharing, app distribution, subscriptions, export, Analyze in Excel, and embedded consumption according to licensing and tenant settings. Every distribution method changes how data can be accessed or copied.',
    'Analysts select the least risky delivery method that still meets the business need and document whether exported data is allowed.',
    'Audience need → Permission check → Distribution method → Export policy → Usage monitoring', 'governance', 'governance',
    [('Governance','Policies and controls for reliable, secure, and accountable data use.'),('Export data','Download of summarized or underlying visual data when permitted.'),('Subscription','Scheduled delivery of report snapshots or links.'),('Tenant setting','Organization-level Power BI configuration managed by administrators.')], level='Intermediate')

# Module 08 — quality
add('performance-analyzer-and-model-performance','08','Performance Analyzer and Model Performance','Performance Analyzer ও Model Performance',
    'Performance Analyzer records visual load stages such as DAX query, visual display, and other processing. Model size, relationship design, DAX complexity, source speed, and visual count all affect performance.',
    'Analysts measure before optimizing, isolate slow visuals, inspect generated queries, and simplify the model or report based on evidence.',
    'View → Performance Analyzer → Start recording → Refresh visuals → Copy query', 'performance', 'Performance Analyzer',
    [('Performance Analyzer','Power BI Desktop tool that records visual performance.'),('DAX query duration','Time spent evaluating the semantic-model query.'),('Visual display','Time spent rendering the visual.'),('Optimization','Evidence-based improvement of model, measure, or report performance.')], level='Intermediate')
add('accessible-power-bi-reports','08','Build Accessible Power BI Reports','Accessible Power BI Report তৈরি করুন',
    'Accessible reports use sufficient contrast, meaningful titles, alt text, logical tab order, keyboard-friendly navigation, non-color cues, and clear labels. Accessibility should be designed and tested, not added at the end.',
    'Analysts test keyboard navigation and screen-reader descriptions and avoid communicating status by color alone.',
    'Contrast → Alt text → Tab order → Keyboard test → Non-color cues → Clear titles', 'accessibility', 'alt text',
    [('Alt text','Text description of a visual for assistive technology.'),('Tab order','Sequence in which keyboard focus moves through objects.'),('Color contrast','Difference in luminance needed for readability.'),('Non-color cue','Text, icon, shape, or pattern that communicates meaning without color alone.')])
add('report-quality-assurance-and-release-checklist','08','Report Quality Assurance and Release Checklist','Report Quality Assurance ও Release Checklist',
    'Power BI QA covers source reconciliation, transformation checks, relationship behavior, measure validation, visual interactions, filters, security, accessibility, performance, refresh, documentation, and audience acceptance.',
    'Analysts keep a release checklist and evidence so changes can be reviewed, repeated, and rolled back when necessary.',
    'Data → Model → DAX → Visuals → Interaction → Security → Accessibility → Performance → Refresh → Sign-off', 'qa-checklist', 'sign-off',
    [('Quality assurance','Structured verification that a report meets requirements.'),('Regression test','Test confirming an existing behavior still works after change.'),('User acceptance test','Business-user validation against expected use cases.'),('Release evidence','Screenshots, totals, logs, and approvals supporting publication.')])

# Module 09 — portfolio
add('power-bi-project-requirements-and-model-plan','09','Portfolio Project Part 1: Requirements and Model Plan','Portfolio Project Part 1: Requirement ও Model Plan',
    'The final project begins with stakeholder questions, metric definitions, source inventory, quality risks, fact grain, dimension design, and a page-level report plan. Building visuals before these decisions creates rework and inconsistent metrics.',
    'Learners use the provided retail model files to define an auditable project scope and model diagram.',
    'Deliverables: requirements.md | metric_dictionary.csv | model_diagram | quality_log.csv | page_wireframes', 'project-plan', 'requirements',
    [('Project brief','Document defining purpose, audience, questions, scope, and deliverables.'),('Metric dictionary','Documented definitions for measures and business rules.'),('Wireframe','Low-fidelity layout plan for a report page.'),('Acceptance criterion','Testable condition used to decide whether the project is complete.')], level='Advanced')
add('power-bi-project-build-and-present','09','Portfolio Project Part 2: Build, Validate, and Present','Portfolio Project Part 2: Build, Validate ও Present',
    'The final project transforms the practice data, builds a star-schema semantic model, creates documented DAX measures, designs executive and diagnostic report pages, validates totals and interactions, and presents evidence-supported findings with limitations.',
    'A strong portfolio submission includes the PBIX file created by the learner, source files, data dictionary, screenshots or PDF export, measure library, validation evidence, and a concise project README.',
    'Deliverables: Retail_Analytics.pbix | source files | DAX measures | QA checklist | screenshots/PDF | README', 'project-checklist', 'PBIX',
    [('PBIX','Power BI Desktop project file format.'),('Executive page','Summary page for headline performance and decisions.'),('Diagnostic page','Page designed to investigate drivers and segments.'),('Insight narrative','Plain-language explanation connecting evidence, implication, limitation, and next action.')], level='Advanced')


def make_chapter(spec: dict, index: int) -> dict:
    title, bn, concept, use, code = spec['title'], spec['bn'], spec['concept'], spec['use'], spec['code']
    level = spec['level']
    sections = [
        {
            'title_en': f'What {title} means',
            'title_bn': f'{bn} কী',
            'body_en': concept + ' The purpose is not to memorize menu paths; it is to understand which layer owns the logic and how that choice affects refresh, reuse, security, and interpretation.',
            'body_bn': f'{bn} বুঝতে feature-এর নামের পাশাপাশি data কোন layer-এ transform, model, calculate বা present হচ্ছে তা বুঝতে হবে। সঠিক layer বেছে নিলে refresh, reuse, security ও interpretation বেশি reliable হয়।',
            'code': code,
            'code_label': spec.get('code_label', 'Power BI'),
        },
        {
            'title_en': 'How a data analyst uses it',
            'title_bn': 'Data analyst কীভাবে ব্যবহার করেন',
            'body_en': use + ' A professional workflow records the business rule, source grain, model assumptions, and validation evidence before the output is shared.',
            'body_bn': f'Data analyst {bn} ব্যবহার করার আগে business question, source grain, expected output এবং validation rule লিখে রাখেন। কাজের পরে result reconcile করেন এবং unsupported conclusion এড়িয়ে limitation document করেন।',
        },
        {
            'title_en': 'Rules, checks, and common mistakes',
            'title_bn': 'Rule, check ও common mistake',
            'body_en': 'Common mistakes include placing logic in the wrong layer, relying on automatic detection without verification, mixing grains, using unclear names, and trusting a visually plausible result without reconciliation. Change one thing at a time, validate it, and preserve evidence.',
            'body_bn': 'Common mistake হলো wrong layer-এ logic রাখা, automatic detection verify না করা, ভিন্ন grain mix করা, unclear name ব্যবহার করা এবং visually plausible result-কে reconciliation ছাড়া trust করা। একবারে একটি change করুন, validate করুন এবং evidence সংরক্ষণ করুন।',
        },
    ]
    terms = [
        {'term_en': term, 'term_bn': term, 'definition_en': definition, 'definition_bn': f'{term}: {definition} Power BI workflow-এ term-টির exact role chapter-এর example ও activity দিয়ে যাচাই করুন.'}
        for term, definition in spec['terms'][:4]
    ]
    worked = {
        'title_en': f'Worked example: {title}',
        'title_bn': f'Worked example: {bn}',
        'context_en': f'A retail analyst must use {title.lower()} in the provided practice model and produce an output another reviewer can reproduce.',
        'context_bn': f'একজন retail analyst practice model-এ {bn} ব্যবহার করে reproducible output তৈরি করবেন।',
        'steps_en': [
            'Write the business question, audience, required metric, and expected analytical grain.',
            'Identify whether the task belongs in Power Query, the semantic model, DAX, the report layer, or the Power BI service.',
            'Apply the feature or expression, then change one input, filter, or model assumption and observe the effect.',
            'Validate source totals, model relationships, filter behavior, and the final visual or calculation before communicating the result.',
        ],
        'steps_bn': [
            'Business question, audience, required metric ও expected analytical grain লিখুন।',
            'Taskটি Power Query, semantic model, DAX, report layer নাকি Power BI service-এ হওয়া উচিত তা নির্ধারণ করুন।',
            'Feature বা expression apply করে একটি input, filter বা model assumption বদলে effect observe করুন।',
            'Result communicate করার আগে source total, model relationship, filter behavior ও final visual/calculation validate করুন।',
        ],
        'conclusion_en': f'{title} is applied correctly only when the layer, grain, filter behavior, and validation evidence all support the stated business question.',
        'conclusion_bn': f'{bn} তখনই সঠিকভাবে apply হয়েছে যখন layer, grain, filter behavior ও validation evidence stated business question-কে support করে।',
    }
    mcq = {
        'type': 'mcq',
        'prompt_en': f'Which practice best supports a reliable use of {title}?',
        'prompt_bn': f'{bn} reliableভাবে ব্যবহার করতে কোন practice সবচেয়ে ভালো?',
        'options_en': ['Accept automatic behavior and design visuals immediately', 'Define the question and grain, apply the feature in the correct layer, and validate the result', 'Add more visuals until the result looks convincing'],
        'options_bn': ['Automatic behavior accept করে সঙ্গে সঙ্গে visual design করা', 'Question ও grain define করে correct layer-এ feature apply এবং result validate করা', 'Result convincing না হওয়া পর্যন্ত আরও visual add করা'],
        'answer_en': 'B', 'answer_bn': 'B',
        'explanation_en': 'Reliable Power BI work connects the business question, layer, model grain, calculation, and validation evidence.',
        'explanation_bn': 'Reliable Power BI কাজ business question, layer, model grain, calculation ও validation evidence-কে connect করে।',
    }
    fill = {
        'type': 'fill',
        'prompt_en': f'Complete the key term: {spec["fill"][:1]}____',
        'prompt_bn': f'Key term complete করুন: {spec["fill"][:1]}____',
        'answer_en': spec['fill'], 'answer_bn': spec['fill'],
        'explanation_en': f'The expected term is {spec["fill"]}.',
        'explanation_bn': f'Expected term হলো {spec["fill"]}।',
    }
    short = {
        'type': 'short',
        'prompt_en': f'Describe one analytical situation that needs {title}. State the correct Power BI layer and one validation check.',
        'prompt_bn': f'{bn} প্রয়োজন এমন একটি analytical situation লিখুন। Correct Power BI layer ও একটি validation check উল্লেখ করুন।',
        'answer_en': 'A strong response names the business question, the model or report grain, the layer where logic belongs, and a concrete check such as row-count reconciliation, relationship testing, measure comparison, filter testing, or refresh verification.',
        'answer_bn': 'Strong response-এ business question, model/report grain, logic-এর correct layer এবং row-count reconciliation, relationship test, measure comparison, filter test বা refresh verification-এর মতো concrete check থাকবে।',
    }
    activity = {
        'type': 'powerbi-demo',
        'operation': spec['operation'],
        'prompt_en': f'Use this guided simulation to practise {title}. Change one decision and explain how it affects model reliability or report interpretation.',
        'prompt_bn': f'Guided simulation ব্যবহার করে {bn} practice করুন। একটি decision বদলে model reliability বা report interpretation কীভাবে change হয় explain করুন।',
        'code': code,
        'items': [t[0] for t in spec['terms'][:4]],
    }
    recap = [
        {'en': concept.split('.')[0] + '.', 'bn': f'{bn} সঠিক business question ও analytical grain-এর সঙ্গে ব্যবহার করতে হবে।'},
        {'en': 'Put each transformation, relationship, calculation, and presentation rule in the layer best suited to its purpose.', 'bn': 'Transformation, relationship, calculation ও presentation rule purpose অনুযায়ী correct layer-এ রাখুন।'},
        {'en': 'Automatic detection and visually plausible output still require validation.', 'bn': 'Automatic detection ও visually plausible output-ও validate করতে হবে।'},
        {'en': 'Document definitions, assumptions, limitations, and evidence before publication.', 'bn': 'Publication-এর আগে definition, assumption, limitation ও evidence document করুন।'},
    ]
    refs = [
        {'title': 'Microsoft Learn — Power BI documentation', 'url': 'https://learn.microsoft.com/en-us/power-bi/'},
        {'title': 'Microsoft Learn — DAX reference', 'url': 'https://learn.microsoft.com/en-us/dax/'},
    ]
    if spec['module'] == '02': refs[1] = {'title': 'Microsoft Learn — Power Query documentation', 'url': 'https://learn.microsoft.com/en-us/power-query/'}
    return {
        'id': spec['id'], 'module': spec['module'], 'level': level,
        'title_en': title, 'title_bn': bn,
        'summary_en': concept,
        'summary_bn': f'{bn} ব্যবহার করে reliable Power BI data preparation, modeling, calculation, visualization বা delivery workflow তৈরি করার পদ্ধতি শিখুন।',
        'minutes': 45 if level == 'Beginner' else 60,
        'objectives': [
            {'en': f'Explain {title} in plain language.', 'bn': f'সহজ ভাষায় {bn} explain করুন।'},
            {'en': 'Place the task in the correct Power BI layer.', 'bn': 'Taskটি correct Power BI layer-এ place করুন।'},
            {'en': 'Apply the concept to the retail practice model.', 'bn': 'Retail practice model-এ concept apply করুন।'},
            {'en': 'Validate the output and communicate one limitation.', 'bn': 'Output validate করে একটি limitation communicate করুন।'},
        ],
        'sections': sections,
        'terms': terms,
        'worked_example': worked,
        'activity': activity,
        'exercises': [mcq, fill, short],
        'recap': recap,
        'references': refs,
    }

chapters = [make_chapter(spec, i) for i, spec in enumerate(C, 1)]
assert len(chapters) == 77, len(chapters)

tutorial = {
    'id': 'power-bi-data-analytics',
    'title_en': 'Power BI for Data Analytics Tutorial',
    'title_bn': 'Data Analytics-এর জন্য Power BI Tutorial',
    'short_title_en': 'Power BI Analytics',
    'short_title_bn': 'Power BI Analytics',
    'description_en': 'A complete analyst-first Power BI tutorial covering Desktop, Power Query, semantic modeling, relationships, DAX, report design, interaction, publishing, refresh, security, accessibility, performance, quality assurance, and an end-to-end portfolio project.',
    'description_bn': 'Power BI Desktop, Power Query, semantic modeling, relationship, DAX, report design, interaction, publishing, refresh, security, accessibility, performance, quality assurance ও portfolio project-এর complete analyst-first tutorial।',
    'status': 'published',
    'version': '2.4.0',
    'estimated_hours': 64,
    'modules': modules,
    'chapters': chapters,
    'final_quiz': {'title_en': 'Power BI for Data Analytics Final Quiz', 'title_bn': 'Power BI for Data Analytics Final Quiz', 'pass_percent': 75},
    'reference_groups': [
        {'title_en': 'Power BI foundations and reports', 'title_bn': 'Power BI foundation ও report', 'references': [
            {'title': 'What is Power BI?', 'url': 'https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview'},
            {'title': 'Get started with Power BI Desktop', 'url': 'https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-getting-started'},
            {'title': 'Overview of Power BI reports', 'url': 'https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-reports-overview'},
            {'title': 'Overview of visualizations in Power BI', 'url': 'https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualizations-overview'},
        ]},
        {'title_en': 'Power Query and modeling', 'title_bn': 'Power Query ও modeling', 'references': [
            {'title': 'What is Power Query?', 'url': 'https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query'},
            {'title': 'Query overview in Power BI Desktop', 'url': 'https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-query-overview'},
            {'title': 'Model relationships in Power BI Desktop', 'url': 'https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-relationships-understand'},
            {'title': 'Understand star schema and importance for Power BI', 'url': 'https://learn.microsoft.com/en-us/power-bi/guidance/star-schema'},
        ]},
        {'title_en': 'DAX and measures', 'title_bn': 'DAX ও measure', 'references': [
            {'title': 'DAX overview', 'url': 'https://learn.microsoft.com/en-us/dax/dax-overview'},
            {'title': 'DAX function reference', 'url': 'https://learn.microsoft.com/en-us/dax/dax-function-reference'},
            {'title': 'Learn DAX basics in Power BI Desktop', 'url': 'https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-quickstart-learn-dax-basics'},
            {'title': 'Measures in Power BI Desktop', 'url': 'https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-measures'},
        ]},
    ],
    'downloads': [
        {'title_en': 'Power BI Retail Practice Data (ZIP)', 'title_bn': 'Power BI Retail Practice Data (ZIP)', 'url': '/assets/downloads/power-bi-retail-practice-data.zip'},
        {'title_en': 'DAX Measure Library', 'title_bn': 'DAX Measure Library', 'url': '/assets/downloads/power-bi-dax-measures.txt'},
        {'title_en': 'Power Query M Examples', 'title_bn': 'Power Query M Example', 'url': '/assets/downloads/power-bi-power-query-m-examples.txt'},
        {'title_en': 'Power BI Project and QA Checklist', 'title_bn': 'Power BI Project ও QA Checklist', 'url': '/assets/downloads/power-bi-project-qa-checklist.csv'},
        {'title_en': 'Power BI Data Dictionary', 'title_bn': 'Power BI Data Dictionary', 'url': '/assets/datasets/power_bi_data_dictionary.csv'},
    ],
}
OUT.write_text(json.dumps(tutorial, ensure_ascii=False, indent=2), encoding='utf-8')

# ---------------- Practice data ----------------
rng = random.Random(240)
regions = [('R01','Dhaka'),('R02','Chattogram'),('R03','Khulna'),('R04','Rajshahi')]
products = [
    ('P101','Shirt','Apparel',14.00,24.00),('P102','Polo Shirt','Apparel',18.00,31.00),('P103','Trousers','Apparel',22.00,39.00),
    ('P104','Laptop Stand','Accessories',12.00,23.00),('P105','Keyboard','Accessories',15.00,28.00),('P106','Monitor','Electronics',110.00,169.00),
    ('P107','Headset','Electronics',24.00,42.00),('P108','Notebook','Stationery',2.00,4.00),('P109','Pen Set','Stationery',3.50,7.00),
    ('P110','Backpack','Accessories',19.00,35.00),('P111','Webcam','Electronics',31.00,55.00),('P112','Desk Lamp','Home Office',16.00,30.00),
]
segments = ['Consumer','Corporate','Small Business']
channels = ['Online','Retail','Partner']
first = ['Amina','Bashir','Chandra','Dalia','Emon','Farhana','Gopal','Hasan','Ishrat','Jamal','Karim','Laila','Mahin','Nusrat','Omar','Priya','Rashed','Salma','Tariq','Umme']
last = ['Ahmed','Akter','Chowdhury','Das','Haque','Islam','Khan','Mia','Rahman','Roy']
customers=[]
for i in range(1,61):
    region_key, region = regions[(i*3) % len(regions)]
    customers.append([f'C{i:03d}', f'{first[(i-1)%len(first)]} {last[(i*7)%len(last)]}', segments[i%3], region_key, region, (date(2024,10,1)+timedelta(days=i*4)).isoformat(), 'Yes' if i%11 else 'No'])

start=date(2025,1,1); end=date(2026,12,31)
dates=[]; d=start
while d<=end:
    dates.append([d.isoformat(),d.year,(d.month-1)//3+1,d.month,d.strftime('%B'),d.day,d.strftime('%A'),d.isocalendar().week,'FY'+str(d.year)])
    d+=timedelta(days=1)

sales=[]
order_count=360
for line_id in range(1,order_count+1):
    order_date=start+timedelta(days=rng.randrange((end-start).days+1))
    ship_date=order_date+timedelta(days=rng.randrange(1,8))
    customer=customers[rng.randrange(len(customers))]
    product=products[rng.randrange(len(products))]
    region_key=customer[3]
    qty=rng.randrange(1,8)
    unit_price=round(product[4]*(0.92+rng.random()*0.18),2)
    discount=[0,0,0.05,0.1,0.15][rng.randrange(5)]
    revenue=round(qty*unit_price*(1-discount),2)
    cost=round(qty*product[3],2)
    channel=channels[rng.randrange(len(channels))]
    sales.append([f'L{line_id:04d}',f'O{((line_id-1)//2)+1:04d}',order_date.isoformat(),ship_date.isoformat(),customer[0],product[0],region_key,channel,qty,unit_price,discount,revenue,cost,round(revenue-cost,2)])

targets=[]
for y in [2025,2026]:
    for m in range(1,13):
        for region_key,_ in regions:
            targets.append([f'{y}-{m:02d}-01',region_key,round(4500+rng.randrange(0,1800),2)])

files = {
    'DimDate.csv': (['Date','Year','QuarterNumber','MonthNumber','MonthName','Day','DayName','ISOWeek','FiscalYear'], dates),
    'DimProduct.csv': (['ProductKey','Product','Category','UnitCost','ListPrice'], [list(x) for x in products]),
    'DimCustomer.csv': (['CustomerKey','CustomerName','Segment','RegionKey','Region','SignupDate','Active'], customers),
    'DimRegion.csv': (['RegionKey','Region'], [list(x) for x in regions]),
    'FactSales.csv': (['SalesLineKey','OrderID','OrderDate','ShipDate','CustomerKey','ProductKey','RegionKey','Channel','Quantity','UnitPrice','DiscountPct','Revenue','Cost','GrossProfit'], sales),
    'FactTargets.csv': (['MonthStart','RegionKey','RevenueTarget'], targets),
}
for filename,(header,rows) in files.items():
    with (PB_DIR/filename).open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f); w.writerow(header); w.writerows(rows)

with zipfile.ZipFile(DL/'power-bi-retail-practice-data.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(PB_DIR.glob('*.csv')):
        z.write(p, arcname=p.name)

# Data dictionary
with (DS/'power_bi_data_dictionary.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f); w.writerow(['Table','Column','Data type','Role','Description'])
    dictionary = [
        ('DimDate','Date','Date','Primary key','One row per calendar date from 2025-01-01 through 2026-12-31.'),
        ('DimProduct','ProductKey','Text','Primary key','Unique product identifier.'),('DimProduct','Category','Text','Dimension attribute','Product reporting category.'),
        ('DimCustomer','CustomerKey','Text','Primary key','Unique customer identifier.'),('DimCustomer','Segment','Text','Dimension attribute','Customer segment.'),
        ('DimRegion','RegionKey','Text','Primary key','Unique region identifier.'),
        ('FactSales','SalesLineKey','Text','Primary key','Unique order-line identifier.'),('FactSales','OrderID','Text','Degenerate dimension','Order identifier repeated across lines.'),
        ('FactSales','OrderDate','Date','Foreign key','Active relationship to DimDate[Date].'),('FactSales','ShipDate','Date','Foreign key','Inactive relationship to DimDate[Date].'),
        ('FactSales','CustomerKey','Text','Foreign key','Relationship to DimCustomer.'),('FactSales','ProductKey','Text','Foreign key','Relationship to DimProduct.'),
        ('FactSales','RegionKey','Text','Foreign key','Relationship to DimRegion.'),('FactSales','Revenue','Decimal','Additive measure input','Line revenue after discount.'),
        ('FactSales','Cost','Decimal','Additive measure input','Line cost.'),('FactSales','GrossProfit','Decimal','Validation column','Revenue minus cost; learners may recalculate as a measure.'),
        ('FactTargets','MonthStart','Date','Composite grain','First day of target month.'),('FactTargets','RegionKey','Text','Composite grain','Target region.'),
        ('FactTargets','RevenueTarget','Decimal','Target value','Monthly revenue target by region.'),
    ]
    w.writerows(dictionary)

(DL/'power-bi-dax-measures.txt').write_text('''// Base measures\nTotal Revenue = SUM(FactSales[Revenue])\nTotal Cost = SUM(FactSales[Cost])\nGross Profit = [Total Revenue] - [Total Cost]\nGross Margin % = DIVIDE([Gross Profit], [Total Revenue])\nOrder Count = DISTINCTCOUNT(FactSales[OrderID])\nUnits Sold = SUM(FactSales[Quantity])\nAverage Order Value = DIVIDE([Total Revenue], [Order Count])\nCustomer Count = DISTINCTCOUNT(FactSales[CustomerKey])\n\n// Time intelligence\nRevenue YTD = TOTALYTD([Total Revenue], DimDate[Date])\nRevenue PY = CALCULATE([Total Revenue], SAMEPERIODLASTYEAR(DimDate[Date]))\nRevenue YoY = [Total Revenue] - [Revenue PY]\nRevenue YoY % = DIVIDE([Revenue YoY], [Revenue PY])\nRevenue Running =\nVAR MaxDate = MAX(DimDate[Date])\nRETURN CALCULATE([Total Revenue], FILTER(ALLSELECTED(DimDate[Date]), DimDate[Date] <= MaxDate))\n\n// Contribution and ranking\nRevenue Share = DIVIDE([Total Revenue], CALCULATE([Total Revenue], REMOVEFILTERS(DimProduct[Product])))\nProduct Rank = RANKX(ALLSELECTED(DimProduct[Product]), [Total Revenue], , DESC, DENSE)\n\n// Target and alternate date\nRevenue Target = SUM(FactTargets[RevenueTarget])\nRevenue Variance = [Total Revenue] - [Revenue Target]\nRevenue Variance % = DIVIDE([Revenue Variance], [Revenue Target])\nShipped Revenue = CALCULATE([Total Revenue], USERELATIONSHIP(DimDate[Date], FactSales[ShipDate]))\n''',encoding='utf-8')

(DL/'power-bi-power-query-m-examples.txt').write_text('''// Example 1: Load and type FactSales.csv\nlet\n    Source = Csv.Document(File.Contents(ParameterFolder & "FactSales.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),\n    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),\n    Typed = Table.TransformColumnTypes(Headers, {\n        {"SalesLineKey", type text}, {"OrderID", type text}, {"OrderDate", type date}, {"ShipDate", type date},\n        {"CustomerKey", type text}, {"ProductKey", type text}, {"RegionKey", type text}, {"Channel", type text},\n        {"Quantity", Int64.Type}, {"UnitPrice", Currency.Type}, {"DiscountPct", Percentage.Type},\n        {"Revenue", Currency.Type}, {"Cost", Currency.Type}, {"GrossProfit", Currency.Type}\n    })\nin\n    Typed\n\n// Example 2: Add a refresh quality flag\nlet\n    Source = FactSales_Staging,\n    QualityFlag = Table.AddColumn(Source, "QualityStatus", each if [Quantity] <= 0 or [Revenue] < 0 then "Check" else "Valid", type text)\nin\n    QualityFlag\n\n// Example 3: Parameterized folder path\nParameterFolder = "C:\\DataLearningHub\\PowerBI\\" meta [IsParameterQuery=true, Type="Text", IsParameterQueryRequired=true]\n''',encoding='utf-8')

with (DL/'power-bi-project-qa-checklist.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f); w.writerow(['Phase','Check','Evidence','Status'])
    rows=[
        ('Requirements','Audience, decisions, questions, and exclusions are documented.','','Not Started'),
        ('Source','Every file/table has an owner, grain, refresh expectation, and quality notes.','','Not Started'),
        ('Power Query','Data types, error/null handling, source filters, and applied steps are reviewed.','','Not Started'),
        ('Model','Fact grain, unique dimension keys, relationships, directions, and inactive dates are tested.','','Not Started'),
        ('DAX','Base measures reconcile to independent controls; ratios use safe denominators.','','Not Started'),
        ('Reports','Titles, units, filters, interactions, drill, and tooltips match the business question.','','Not Started'),
        ('Security','Workspace roles, app audience, RLS, and export permissions are tested.','','Not Started'),
        ('Accessibility','Contrast, alt text, tab order, keyboard navigation, and non-color cues are tested.','','Not Started'),
        ('Performance','Performance Analyzer evidence is reviewed and slow visuals are investigated.','','Not Started'),
        ('Refresh','Credentials, gateway, schedule, history, owner, and failure response are documented.','','Not Started'),
        ('Release','UAT, sign-off, version note, screenshots, and rollback information are retained.','','Not Started'),
    ]; w.writerows(rows)

print(f'Built {len(chapters)} Power BI tutorial chapters and practice assets.')
