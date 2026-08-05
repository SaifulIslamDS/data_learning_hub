from __future__ import annotations

import csv
import json
import random
import textwrap
import zipfile
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TUTORIAL_OUT = ROOT / 'content/tutorials/data_analytics_workflows.json'
PROJECT_OUT = ROOT / 'content/projects/portfolio_projects.json'
DS = ROOT / 'assets/datasets/portfolio'
DL = ROOT / 'assets/downloads/portfolio'
DS.mkdir(parents=True, exist_ok=True)
DL.mkdir(parents=True, exist_ok=True)
(ROOT / 'content/projects').mkdir(parents=True, exist_ok=True)

IBM_CRISP = 'https://www.ibm.com/docs/en/spss-modeler/18.6.0?topic=dm-crisp-help-overview'
NIST_EDA = 'https://www.itl.nist.gov/div898/handbook/eda/section1/eda11.htm'
GITHUB_README = 'https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes'
POWER_BI_GUIDANCE = 'https://learn.microsoft.com/en-us/power-bi/guidance/'
POWER_BI_STAR = 'https://learn.microsoft.com/en-us/power-bi/guidance/star-schema'
POSTGRES = 'https://www.postgresql.org/docs/current/tutorial.html'
PANDAS = 'https://pandas.pydata.org/docs/user_guide/'
OPENSTAX = 'https://openstax.org/details/books/introductory-statistics-2e'

modules = [
    {'id':'01','title_en':'Business Understanding and Project Scope','title_bn':'Business Understanding ও Project Scope'},
    {'id':'02','title_en':'Data Understanding and Acquisition','title_bn':'Data Understanding ও Acquisition'},
    {'id':'03','title_en':'Data Quality and Preparation','title_bn':'Data Quality ও Preparation'},
    {'id':'04','title_en':'Analysis Planning and Exploratory Analysis','title_bn':'Analysis Planning ও Exploratory Analysis'},
    {'id':'05','title_en':'Statistical and Business Evaluation','title_bn':'Statistical ও Business Evaluation'},
    {'id':'06','title_en':'Cross-tool Implementation','title_bn':'Cross-tool Implementation'},
    {'id':'07','title_en':'Communication and Decision Delivery','title_bn':'Communication ও Decision Delivery'},
    {'id':'08','title_en':'Quality Assurance, Governance, and Portfolio','title_bn':'Quality Assurance, Governance ও Portfolio'},
]

# id, module, EN title, BN title, concept, practical use, key terms
SPECS = [
('analytics-workflow-overview','01','The End-to-End Analytics Workflow','End-to-End Analytics Workflow','An analytics workflow is an iterative sequence that connects a decision need to trusted data, analysis, validation, communication, and follow-through. It is not a rigid waterfall: findings can send the analyst back to the question, source, or preparation step.','Use a visible workflow to prevent premature charting, undocumented data changes, and recommendations that are disconnected from the original decision.', [('Workflow','Ordered but iterative project stages.'),('Iteration','Returning to an earlier stage after learning something new.'),('Decision','Action or choice the analysis is intended to support.'),('Evidence','Validated output used to support a conclusion.')]),
('stakeholder-and-decision-context','01','Stakeholders and Decision Context','Stakeholder ও Decision Context','A stakeholder is a person or group affected by the analysis or responsible for acting on it. Decision context specifies who will use the result, when they need it, what choices they control, and what constraints apply.','Interview the sponsor and likely users before defining metrics so the project solves a real decision rather than producing an attractive but unused report.', [('Stakeholder','Person or group that uses or is affected by the work.'),('Sponsor','Person accountable for the project outcome.'),('Decision context','Circumstances in which the result will be used.'),('Constraint','Limit on time, data, budget, policy, or action.')]),
('problem-statement-and-analytical-question','01','Problem Statements and Analytical Questions','Problem Statement ও Analytical Question','A problem statement describes the observed business situation and its consequence. An analytical question converts that situation into a specific question that data can answer without promising causality or certainty the data cannot support.','Rewrite vague requests such as “improve sales” into measurable questions about periods, segments, metrics, and decisions.', [('Problem statement','Concise description of the situation and consequence.'),('Analytical question','Specific question answerable with data.'),('Scope','Boundaries of the work.'),('Target quantity','Metric or relationship the analysis estimates.')]),
('scope-constraints-and-success-criteria','01','Scope, Constraints, and Success Criteria','Scope, Constraint ও Success Criteria','Scope defines what is included and excluded. Success criteria describe observable conditions for a useful result, including data quality, analytical accuracy, delivery format, timing, and stakeholder acceptance.','Create a one-page boundary statement before analysis so new requests can be assessed as in-scope, deferred, or a separate project.', [('In scope','Work explicitly included.'),('Out of scope','Work intentionally excluded.'),('Success criterion','Observable condition for acceptable completion.'),('Acceptance','Formal confirmation that deliverables meet requirements.')]),
('kpi-tree-and-metric-definitions','01','KPI Trees and Metric Definitions','KPI Tree ও Metric Definition','A KPI tree connects an outcome metric to its drivers and diagnostic measures. A metric definition must state formula, grain, filters, time window, owner, and interpretation so different tools produce the same number.','Use a metric dictionary before building Excel formulas, SQL queries, DAX measures, or pandas aggregations.', [('KPI','Key performance indicator tied to an objective.'),('Driver','Factor that influences an outcome metric.'),('Grain','Level represented by one row or observation.'),('Metric dictionary','Controlled definitions for calculations and filters.')]),
('project-charter-and-assumptions-log','01','Project Charter and Assumptions Log','Project Charter ও Assumptions Log','A project charter records the decision, scope, stakeholders, deliverables, timeline, risks, and ownership. An assumptions log records beliefs that affect the analysis and must later be verified, revised, or disclosed.','Keep the charter and assumptions with the project repository so reviewers can understand why the work was performed and what remains uncertain.', [('Charter','Short document authorizing and defining the work.'),('Assumption','Unverified belief used temporarily.'),('Risk','Uncertain event that can affect the outcome.'),('Dependency','External input or action required for progress.')]),

('source-inventory-and-ownership','02','Source Inventory and Data Ownership','Source Inventory ও Data Ownership','A source inventory lists every file, table, report, extract, and manual input required by the project. Ownership identifies who controls the source and who can clarify definitions, refresh timing, and access restrictions.','Record source location, owner, refresh frequency, access method, and known limitations before combining data.', [('Source system','Originating application or record system.'),('Data owner','Person accountable for a data asset.'),('Refresh','Process that updates data.'),('Lineage','Trace of data from source through transformations.')]),
('access-privacy-and-minimization','02','Data Access, Privacy, and Minimization','Data Access, Privacy ও Minimization','Data minimization means using only fields and records necessary for the stated purpose. Access should follow authorization, privacy, confidentiality, and retention requirements even when the dataset is technically available.','Remove direct identifiers from practice extracts and document why each sensitive field is required before analysis.', [('Personal data','Information relating to an identifiable person.'),('Minimization','Limiting data to what is necessary.'),('Authorization','Permission to access or use data.'),('Retention','Period for keeping data and outputs.')]),
('entities-keys-and-row-grain','02','Entities, Keys, and Row Grain','Entity, Key ও Row Grain','Entities are the people, products, orders, events, or periods represented in data. Keys identify records or connect tables. Grain states exactly what one row means and is essential before aggregation or joining.','Write a grain statement for every table and test primary-key uniqueness before calculating metrics.', [('Entity','Real-world thing represented by data.'),('Primary key','Field or fields uniquely identifying a row.'),('Foreign key','Field connecting to another table.'),('Row grain','Business meaning of one row.')]),
('data-dictionary-and-semantic-meaning','02','Data Dictionaries and Semantic Meaning','Data Dictionary ও Semantic Meaning','A data dictionary describes field names, types, units, allowed values, business meaning, source, and quality notes. Semantic meaning matters because similar labels can represent different rules in different systems.','Resolve ambiguous fields such as revenue, active customer, or completion status before analysis and preserve agreed definitions.', [('Data dictionary','Documentation of fields and their meaning.'),('Unit','Measurement scale such as BDT, days, or percent.'),('Domain','Allowed set of values for a field.'),('Semantic meaning','Business interpretation attached to data.')]),
('sampling-and-representativeness','02','Sampling and Representativeness','Sampling ও Representativeness','A sample represents only the records selected by a process. Representativeness depends on who or what could enter the sample, who was excluded, and whether selection relates to the outcome being studied.','Compare the analysis population with the business population and disclose coverage gaps before generalizing findings.', [('Population','Full group the conclusion concerns.'),('Sample','Observed subset used in analysis.'),('Coverage','Extent to which the source includes the target population.'),('Selection bias','Systematic difference caused by selection.')]),
('initial-profiling-and-data-understanding','02','Initial Profiling and Data Understanding','Initial Profiling ও Data Understanding','Initial profiling checks shape, fields, types, missingness, uniqueness, category values, ranges, dates, and simple distributions. The purpose is to understand the data before deciding how to clean or analyze it.','Create a reusable profiling table and record unexpected values as questions rather than silently correcting them.', [('Profile','Structured summary of a dataset.'),('Missingness','Pattern and amount of absent values.'),('Cardinality','Number of distinct values.'),('Range check','Test against plausible minimum and maximum values.')]),

('data-quality-plan','03','Build a Data Quality Plan','Data Quality Plan তৈরি','A data quality plan translates business requirements into tests for completeness, validity, uniqueness, consistency, timeliness, and reconciliation. Each test needs an owner, threshold, evidence, and response when it fails.','Define quality gates before cleaning so acceptance is based on stated requirements rather than visual inspection alone.', [('Quality dimension','Aspect such as completeness or validity.'),('Threshold','Acceptable limit for a test.'),('Exception','Record that fails a quality rule.'),('Remediation','Action taken to correct or manage a defect.')]),
('missing-duplicate-and-invalid-values','03','Missing, Duplicate, and Invalid Values','Missing, Duplicate ও Invalid Value','Missing values, duplicated records, and invalid values are different defects and require different responses. Deleting all affected rows can create bias or remove legitimate repeated events.','Classify each issue, estimate its impact, choose a treatment, and retain a record of the original condition.', [('Missing value','Expected value that is absent.'),('Duplicate','Repeated record or event beyond the intended grain.'),('Invalid value','Value outside an allowed rule or domain.'),('Treatment','Documented response to a data issue.')]),
('standardize-types-categories-and-units','03','Standardize Types, Categories, and Units','Type, Category ও Unit Standardize','Standardization makes logically equivalent values consistent while preserving meaning. Dates, identifiers, text labels, currencies, percentages, and measurement units require explicit conversion rules.','Use mapping tables and validation counts rather than uncontrolled find-and-replace operations.', [('Standardization','Applying a consistent representation.'),('Mapping table','Approved correspondence between raw and standard values.'),('Type conversion','Changing data representation intentionally.'),('Unit conversion','Expressing measures in a common unit.')]),
('joins-merges-and-reconciliation','03','Joins, Merges, and Reconciliation','Join, Merge ও Reconciliation','Combining tables can lose unmatched records or multiply rows when key relationships are misunderstood. Reconciliation compares row counts, distinct keys, totals, and unmatched records before and after a join.','Prove the expected relationship and reconcile totals in SQL, Power Query, Excel, or pandas before using the combined result.', [('Join','Operation that combines related rows.'),('One-to-many','Relationship where one key matches multiple rows.'),('Unmatched record','Row without a corresponding key.'),('Reconciliation','Comparison proving totals and counts remain explainable.')]),
('outliers-and-unusual-records','03','Outliers and Unusual Records','Outlier ও Unusual Record','An outlier is unusual relative to a reference distribution, but it may be an error, a rare valid case, or an important signal. Automatic removal can hide operational problems or meaningful high-value events.','Flag unusual records, investigate their origin, compare results with and without them, and document any exclusion rule.', [('Outlier','Observation unusually distant from others.'),('Influence','Degree to which a record changes a result.'),('Winsorization','Capping values at chosen limits.'),('Sensitivity analysis','Comparing results under alternative treatments.')]),
('transformation-lineage-and-audit-trail','03','Transformation Lineage and Audit Trails','Transformation Lineage ও Audit Trail','Transformation lineage records how raw inputs become analytical outputs. An audit trail includes formulas, queries, code, refresh steps, version information, and evidence that each stage can be reviewed.','Separate raw, intermediate, and final data; name steps clearly; and keep transformation logic in reusable scripts or queries.', [('Transformation','Rule that changes data form or value.'),('Audit trail','Evidence of actions and decisions.'),('Raw layer','Preserved source data.'),('Processed layer','Data prepared for analysis.')]),
('clean-dataset-handoff','03','Create a Clean Dataset Handoff','Clean Dataset Handoff তৈরি','A clean handoff includes the prepared data, dictionary, quality report, transformation notes, refresh instructions, known limitations, and responsible owner. Clean does not mean perfect; it means fit for the stated purpose with documented exceptions.','Package the analytical dataset so another analyst can reproduce the next stage without guessing how it was created.', [('Handoff','Transfer of an asset and its supporting context.'),('Fitness for use','Suitability for a defined analytical purpose.'),('Known issue','Documented unresolved limitation.'),('Refresh instruction','Procedure for updating the dataset.')]),

('analysis-plan-and-evidence-map','04','Analysis Plans and Evidence Maps','Analysis Plan ও Evidence Map','An analysis plan connects each business question to required metrics, segments, comparisons, statistical methods, visuals, validation checks, and expected outputs. It prevents analysis from becoming an unstructured search for interesting charts.','Create a table mapping questions to evidence before opening the analytical tool.', [('Analysis plan','Planned methods and outputs for each question.'),('Evidence map','Link between claims and supporting calculations.'),('Comparison','Reference used to interpret a result.'),('Analytical method','Technique used to answer a question.')]),
('descriptive-overview-and-baselines','04','Descriptive Overview and Baselines','Descriptive Overview ও Baseline','A descriptive overview establishes counts, totals, averages, medians, ranges, distributions, and data coverage. A baseline provides a reference such as prior period, target, control group, or organizational average.','Begin with reconciled overview metrics before drilling into segments or relationships.', [('Baseline','Reference value for comparison.'),('Summary statistic','Number describing a feature of data.'),('Coverage period','Dates represented in the dataset.'),('Denominator','Base count used in a rate or percentage.')]),
('segment-comparison-and-drilldown','04','Segment Comparison and Drill-down','Segment Comparison ও Drill-down','Segment analysis compares meaningful groups such as region, channel, product, customer cohort, department, or project. Differences must be interpreted with group size, exposure, mix, and uncertainty.','Move from overall metrics to pre-defined segments and then investigate only differences that matter to the decision.', [('Segment','Defined subgroup of observations.'),('Drill-down','Moving from summary to detailed level.'),('Mix effect','Change caused by different composition of groups.'),('Small-base warning','Caution when a rate uses few observations.')]),
('time-trends-seasonality-and-events','04','Time Trends, Seasonality, and Events','Time Trend, Seasonality ও Event','Time analysis separates level, trend, recurring seasonal patterns, and event-related changes. Calendar completeness, comparable periods, and business events must be considered before explaining a movement.','Build a complete time axis, compare like-for-like periods, and annotate campaigns, closures, policy changes, or system outages.', [('Trend','Longer-term direction of a series.'),('Seasonality','Pattern repeating at a regular interval.'),('Event annotation','Recorded occurrence that may explain a change.'),('Comparable period','Period with a fair basis for comparison.')]),
('distributions-and-variability','04','Distributions and Variability','Distribution ও Variability','A distribution shows how values are spread, concentrated, skewed, or separated into groups. Averages alone can hide variability, long tails, multiple modes, and unequal risk.','Use histograms, box plots, quantiles, and robust summaries to describe both typical values and spread.', [('Distribution','Pattern of values across a range.'),('Skewness','Asymmetry of a distribution.'),('Quantile','Cut point dividing ordered data.'),('Robust statistic','Measure less sensitive to extreme values.')]),
('relationships-and-confounding','04','Relationships, Correlation, and Confounding','Relationship, Correlation ও Confounding','Association describes variables changing together, but it does not establish that one causes the other. Confounding occurs when another variable influences both the apparent driver and outcome.','Use scatter plots, grouped comparisons, domain knowledge, and adjusted analyses while avoiding causal language for observational data.', [('Association','Observed relationship between variables.'),('Correlation','Standardized measure of linear or ranked association.'),('Confounder','Variable related to both exposure and outcome.'),('Causality','Claim that changing one factor changes another.')]),
('hypotheses-anomalies-and-follow-up','04','Hypotheses, Anomalies, and Follow-up Questions','Hypothesis, Anomaly ও Follow-up Question','EDA generates hypotheses and follow-up questions; it does not automatically confirm them. An anomaly should be checked against data quality, operations, timing, and alternative explanations before escalation.','Maintain an insight log with evidence status: observed, validated, tested, unresolved, or rejected.', [('Hypothesis','Testable proposed explanation.'),('Anomaly','Unexpected pattern or observation.'),('Insight log','Record of findings, evidence, and status.'),('Triangulation','Checking a finding with multiple sources or methods.')]),
('exploratory-analysis-checkpoint','04','Exploratory Analysis Checkpoint','Exploratory Analysis Checkpoint','A checkpoint reviews whether the analysis has answered the original questions, whether new questions are justified, and whether data limitations change the scope. This is where uncontrolled exploration is converted into a focused evaluation plan.','Present a short evidence review before investing in advanced statistical testing or report production.', [('Checkpoint','Formal review before the next stage.'),('Evidence review','Assessment of current findings and support.'),('Scope change','Approved alteration to project boundaries.'),('Go/no-go decision','Decision to continue, revise, or stop.')]),

('uncertainty-and-confidence','05','Uncertainty and Confidence','Uncertainty ও Confidence','Sample-based estimates vary. Confidence intervals and uncertainty statements communicate a plausible range under stated assumptions rather than claiming an exact population truth.','Report estimates with sample size, interval, assumptions, and practical context when the data represents a sample or noisy process.', [('Estimate','Value calculated from observed data.'),('Standard error','Estimated variability of an estimator.'),('Confidence interval','Range produced by a repeated-sampling procedure.'),('Precision','Narrowness or stability of an estimate.')]),
('hypothesis-tests-and-effect-size','05','Hypothesis Tests and Effect Size','Hypothesis Test ও Effect Size','A hypothesis test measures compatibility with a null model, while effect size describes the magnitude of a difference or relationship. Statistical significance alone does not show business importance.','Predefine the test, significance level, assumptions, and meaningful effect before examining results.', [('Null hypothesis','Reference claim evaluated by a test.'),('p-value','Probability of a result at least as extreme under the null model.'),('Effect size','Magnitude of a difference or relationship.'),('Statistical power','Probability of detecting a specified effect.')]),
('experiments-and-ab-tests','05','Experiments and A/B Tests','Experiment ও A/B Test','A controlled experiment assigns eligible units to alternatives so outcome differences can be attributed more credibly to the treatment. Randomization, exposure integrity, sample size, and pre-defined metrics are central.','Audit assignment, exclusions, exposure, outcome windows, and guardrail metrics before interpreting conversion differences.', [('Treatment','Intervention being evaluated.'),('Control','Reference condition.'),('Randomization','Chance-based assignment to groups.'),('Guardrail metric','Measure protecting against harmful side effects.')]),
('regression-and-adjusted-analysis','05','Regression and Adjusted Analysis','Regression ও Adjusted Analysis','Regression estimates conditional relationships while accounting for selected variables. Interpretation depends on model form, coding, assumptions, residual behavior, and the possibility of omitted variables.','Use regression to quantify adjusted association or prediction, then validate residuals and avoid causal claims without a credible design.', [('Coefficient','Estimated change associated with a predictor.'),('Residual','Observed value minus fitted value.'),('Adjustment','Including variables to compare conditional relationships.'),('Model specification','Chosen functional form and variables.')]),
('forecast-evaluation-and-backtesting','05','Forecast Evaluation and Backtesting','Forecast Evaluation ও Backtesting','A forecast must be evaluated on future-like holdout periods, not only on the data used to fit it. Backtesting repeats historical forecast origins to assess stability across time.','Compare against simple baselines and report error by horizon, segment, and operational consequence.', [('Forecast horizon','Time between prediction and outcome.'),('Holdout period','Data reserved for evaluation.'),('Backtest','Historical simulation of forecasting performance.'),('Baseline forecast','Simple reference model used for comparison.')]),
('business-significance-and-decision-thresholds','05','Business Significance and Decision Thresholds','Business Significance ও Decision Threshold','Business significance connects analytical magnitude to cost, benefit, risk, capacity, and feasibility. A decision threshold specifies when evidence is strong and valuable enough to trigger action.','Translate results into expected impact, uncertainty, implementation cost, and downside before recommending action.', [('Business significance','Practical value of a result.'),('Decision threshold','Rule that triggers an action.'),('Expected value','Probability-weighted benefit or cost.'),('Trade-off','Balance between competing objectives or risks.')]),

('choose-the-right-analytical-tool','06','Choose the Right Analytical Tool','সঠিক Analytical Tool বেছে নিন','Tool choice should follow data size, complexity, refresh needs, collaboration, governance, reproducibility, and audience requirements. The same analytical question can be answered in several tools, but not with equal maintainability.','Use a decision matrix rather than personal preference to select Excel, SQL, Power BI, Python, or a combination.', [('Tool fit','Suitability of a tool for the task.'),('Scalability','Ability to handle growth in data or use.'),('Maintainability','Ease of reviewing and updating work.'),('Handoff risk','Risk that others cannot operate or verify the solution.')]),
('excel-analytical-workflow','06','Implement the Workflow in Excel','Excel-এ Workflow Implement','Excel is effective for controlled tabular analysis, reviewable formulas, PivotTables, Power Query, and stakeholder-friendly workbooks. Risk increases when logic is hidden across cells or raw data is manually edited.','Separate input, transformation, calculation, output, and control sheets; use tables, named logic, reconciliation checks, and documentation.', [('Workbook architecture','Planned organization of sheets and logic.'),('Excel Table','Structured range with managed references.'),('PivotTable','Interactive grouped summary.'),('Control check','Formula or rule verifying workbook integrity.')]),
('sql-analytical-workflow','06','Implement the Workflow in SQL','SQL-এ Workflow Implement','SQL is suited to extracting, joining, filtering, aggregating, and validating relational data close to its source. A reliable SQL workflow uses explicit grain, readable CTEs, documented filters, and reconciliation queries.','Create a base dataset, quality checks, metric queries, and reproducible output views while preserving source tables.', [('CTE','Named query expression used within a statement.'),('View','Saved query exposed as a virtual table.'),('Query grain','Level returned by each result row.'),('Reconciliation query','Query that validates counts or totals.')]),
('power-bi-analytical-workflow','06','Implement the Workflow in Power BI','Power BI-এ Workflow Implement','Power BI combines Power Query preparation, semantic modeling, DAX measures, interactive reports, and governed sharing. A strong solution begins with a star schema and measure definitions before visual design.','Separate fact and dimension tables, create reusable measures, validate filter behavior, and design pages around stakeholder decisions.', [('Semantic model','Business-ready model used by reports.'),('Star schema','Fact table connected to dimensions.'),('DAX measure','Context-sensitive calculation.'),('Report interaction','Filtering or navigation behavior between visuals.')]),
('python-analytical-workflow','06','Implement the Workflow in Python','Python-এ Workflow Implement','Python supports reproducible preparation, statistical analysis, automation, visualization, and reusable code. Clear project folders, functions, environment files, tests, and restart-and-run validation make notebooks reliable.','Preserve raw files, build repeatable transformations, validate outputs, and export decision-ready tables and charts.', [('Notebook','Executable document combining code and narrative.'),('Environment','Defined interpreter and package set.'),('Function','Reusable block of code.'),('Reproducible run','Execution from clean state with consistent output.')]),
('cross-tool-reconciliation','06','Cross-tool Reconciliation','Cross-tool Reconciliation','Cross-tool reconciliation proves that agreed metrics match when calculated in Excel, SQL, Power BI, and Python. Differences often come from filters, grain, date logic, duplicates, null handling, or rounding.','Create a metric control table containing expected totals, row counts, distinct keys, date coverage, and tolerance rules for every implementation.', [('Control total','Expected aggregate used for validation.'),('Tolerance','Allowed numerical difference.'),('Filter parity','Use of equivalent filters across tools.'),('Cross-tool agreement','Consistent result under the same definition.')]),

('write-an-evidence-based-insight','07','Write an Evidence-based Insight','Evidence-based Insight লিখুন','An insight combines a specific observation, supporting evidence, business meaning, limitation, and recommended next step. It is stronger than a chart description and narrower than an unsupported story.','Use the structure evidence → interpretation → implication → limitation → action.', [('Observation','What the analysis directly shows.'),('Interpretation','Meaning assigned in context.'),('Implication','Why the finding matters.'),('Recommendation','Proposed action based on evidence and constraints.')]),
('select-decision-ready-visuals','07','Select Decision-ready Visuals','Decision-ready Visual বেছে নিন','A visual should match the analytical question: comparison, trend, distribution, relationship, composition, geography, or process. Titles, units, baselines, annotations, and accessible color choices are part of the evidence.','Choose the simplest visual that preserves the necessary comparison and remove decoration that does not aid interpretation.', [('Visual encoding','Use of position, length, color, or shape to represent data.'),('Annotation','Text or mark explaining important context.'),('Baseline','Reference line or value.'),('Accessibility','Design usable by people with varied abilities.')]),
('dashboard-and-report-structure','07','Dashboard and Report Structure','Dashboard ও Report Structure','A decision-ready report organizes pages around audience questions, not around available chart types. Summary, drivers, detail, definitions, and data-quality context should follow a deliberate information hierarchy.','Sketch the report structure before building visuals and test whether a first-time user can answer the priority questions.', [('Information hierarchy','Order that guides attention and understanding.'),('Summary page','High-level view of outcomes and decisions.'),('Drillthrough','Navigation from summary to relevant detail.'),('Metric note','Definition or caveat attached to a measure.')]),
('recommendations-and-action-plans','07','Recommendations and Action Plans','Recommendation ও Action Plan','A recommendation must identify the action, owner, timing, expected effect, evidence, assumptions, risks, and monitoring metric. Analysis cannot choose actions that the organization lacks authority or capacity to implement.','Offer prioritized options and distinguish immediate actions, experiments, further investigation, and monitoring.', [('Action owner','Person accountable for execution.'),('Priority','Relative urgency and value.'),('Monitoring metric','Measure used after action.'),('Contingency','Alternative response if assumptions fail.')]),
('executive-presentation-and-handoff','07','Executive Presentation and Handoff','Executive Presentation ও Handoff','An executive handoff summarizes the decision, evidence, recommendation, limitations, and next action while preserving technical details in appendices and project files. The audience should know what to do and where to verify the result.','Prepare a concise presentation, a reproducible repository, a data dictionary, and an owner-facing operating note.', [('Executive summary','Concise decision-focused overview.'),('Appendix','Supporting technical detail.'),('Handoff note','Instructions for using and maintaining the output.'),('Call to action','Explicit requested decision or next step.')]),

('analytical-qa-checklist','08','Analytical QA and Validation Checklist','Analytical QA ও Validation Checklist','Analytical QA verifies source coverage, transformations, calculations, assumptions, visuals, labels, refresh behavior, and narrative consistency. A project should not be considered complete because the dashboard opens without error.','Use independent checks and sign-off evidence for metrics that influence decisions.', [('Quality assurance','Planned activities that prevent defects.'),('Validation','Evidence that an output meets requirements.'),('Sign-off','Recorded approval by a responsible reviewer.'),('Regression check','Test that an update did not break prior results.')]),
('peer-review-and-challenge','08','Peer Review and Constructive Challenge','Peer Review ও Constructive Challenge','Peer review asks another analyst to challenge definitions, code, assumptions, joins, methods, charts, and conclusions. Review is most useful when evidence is easy to reproduce and issues are recorded without blame.','Provide a review checklist and resolve findings before final publication.', [('Peer review','Evaluation by another qualified person.'),('Challenge','Deliberate test of assumptions and logic.'),('Finding','Recorded issue or improvement opportunity.'),('Resolution','Documented response to a review finding.')]),
('reproducibility-versioning-and-refresh','08','Reproducibility, Versioning, and Refresh','Reproducibility, Versioning ও Refresh','Reproducibility requires preserved inputs, executable logic, environment information, and documented steps. Versioning records changes; refresh instructions explain how new data enters the solution and what checks run afterward.','Tag stable releases, retain change notes, and test the full refresh path before handoff.', [('Version control','System for recording changes over time.'),('Release','Named stable state of a project.'),('Refresh path','Steps for updating inputs and outputs.'),('Change log','Chronological record of modifications.')]),
('portfolio-case-study-and-readme','08','Portfolio Case Study and README','Portfolio Case Study ও README','A portfolio case study should explain the business question, data, process, tools, analysis, validation, findings, limitations, and deliverables. A README helps reviewers understand why the project is useful and how to inspect it.','Write for a recruiter or manager who has limited time but may inspect technical evidence after the summary.', [('Case study','Structured narrative of a completed project.'),('README','Repository landing document explaining purpose and use.'),('Artifact','File or output demonstrating work.'),('Evidence link','Path from a claim to its supporting output.')]),
('portfolio-presentation-and-interview','08','Portfolio Presentation and Interview Walkthrough','Portfolio Presentation ও Interview Walkthrough','A strong walkthrough explains the decision problem, demonstrates analytical judgment, shows validation, and discusses trade-offs. Tool features matter less than a clear explanation of why each choice was made.','Prepare a five-minute summary, a ten-minute technical walkthrough, and concise answers about limitations and next steps.', [('Walkthrough','Guided explanation of a project.'),('Trade-off','Choice between competing benefits or constraints.'),('Technical depth','Level of implementation detail.'),('Reflection','What the analyst learned and would improve.')]),
]

scenario_cycle = [
    ('retail sales performance','regional revenue, profit, and product mix'),
    ('customer retention','cohort retention, repeat purchases, and churn signals'),
    ('marketing experiment','conversion, revenue, and guardrail metrics'),
    ('workforce planning','headcount, turnover, absence, and workforce mix'),
    ('budget control','budget utilization, variance, and forecast risk'),
    ('NGO program monitoring','beneficiary reach, output delivery, cost, and utilization'),
]


def chapter_from_spec(spec: tuple, index: int) -> dict:
    cid, module, title, bn, concept, use, terms = spec
    scenario, evidence = scenario_cycle[index % len(scenario_cycle)]
    code = f"Question → Data → Quality → Analysis → Validation → Insight → Action\nFocus: {title}"
    objective_en = [
        f'Explain {title} in plain language and connect it to an end-to-end analytics project.',
        f'Apply {title} to a realistic {scenario} case.',
        'Identify the required evidence, controls, and deliverables.',
        'State one limitation and one decision-ready next step.',
    ]
    objective_bn = [
        f'সহজ ভাষায় {bn} explain করে end-to-end analytics project-এর সঙ্গে connect করুন।',
        f'একটি বাস্তব {scenario} case-এ {bn} apply করুন।',
        'Required evidence, control ও deliverable identify করুন।',
        'একটি limitation এবং একটি decision-ready next step লিখুন।',
    ]
    sections = [
        {
            'title_en': f'What {title} means', 'title_bn': f'{bn} কী',
            'body_en': concept + ' In a complete analytics project, this stage must leave visible evidence that another reviewer can inspect. The analyst should state the decision, data grain, definitions, assumptions, and expected output rather than relying on memory or undocumented discussion.',
            'body_bn': f'{bn} একটি complete analytics project-এর গুরুত্বপূর্ণ অংশ। এই stage-এ decision, data grain, definition, assumption এবং expected output স্পষ্টভাবে লিখতে হবে, যাতে অন্য reviewer evidence inspect করে একই logic বুঝতে পারেন।',
            'code': code, 'code_label': 'Workflow'
        },
        {
            'title_en': 'How an analyst applies it', 'title_bn': 'Analyst কীভাবে apply করেন',
            'body_en': use + f' In the {scenario} case, the analyst connects this step to {evidence}. The output is recorded in the project charter, data dictionary, analysis plan, validation log, report, or repository so it can be reused across Excel, SQL, Power BI, and Python.',
            'body_bn': f'{scenario} case-এ analyst এই step-কে {evidence}-এর সঙ্গে connect করেন। Output project charter, data dictionary, analysis plan, validation log, report অথবা repository-তে record করতে হবে, যাতে Excel, SQL, Power BI ও Python-এ reuse করা যায়।'
        },
        {
            'title_en': 'Controls, mistakes, and completion evidence', 'title_bn': 'Control, mistake ও completion evidence',
            'body_en': 'Common failures include beginning with a preferred tool, changing definitions mid-project, omitting excluded records, accepting unreconciled totals, and writing conclusions that exceed the evidence. Completion should be demonstrated with a named artifact, an owner, a validation result, and a documented limitation—not only a verbal claim that the step is finished.',
            'body_bn': 'Common mistake হলো preferred tool দিয়ে শুরু করা, project চলাকালে definition বদলানো, excluded record না লেখা, unreconciled total accept করা এবং evidence-এর চেয়ে বড় conclusion দেওয়া। Completion প্রমাণ করতে named artifact, owner, validation result ও documented limitation প্রয়োজন।'
        },
    ]
    worked = {
        'title_en': f'Worked example: {title} for {scenario}',
        'title_bn': f'Worked example: {scenario}-এর জন্য {bn}',
        'context_en': f'A Data Analyst must apply {title.lower()} to a synthetic {scenario} project before producing the final decision deliverable.',
        'context_bn': f'একজন Data Analyst final decision deliverable তৈরির আগে synthetic {scenario} project-এ {bn} apply করবেন।',
        'steps_en': [
            'Restate the stakeholder decision, project boundary, and row grain.',
            f'Identify the exact evidence required for {evidence}.',
            'Perform the step in the chosen tool and record a validation check.',
            'Write the result, limitation, owner, and next action in the project log.'
        ],
        'steps_bn': [
            'Stakeholder decision, project boundary ও row grain আবার লিখুন।',
            f'{evidence}-এর জন্য exact evidence identify করুন।',
            'Chosen tool-এ step perform করে validation check record করুন।',
            'Project log-এ result, limitation, owner ও next action লিখুন।'
        ],
        'conclusion_en': f'{title} is complete only when the project artifact, validation evidence, and decision context agree.',
        'conclusion_bn': f'{bn} তখনই complete, যখন project artifact, validation evidence ও decision context consistent।'
    }
    checklist = [
        f'Define the output for {title}',
        'Record the input data and row grain',
        'Perform one validation or reconciliation check',
        'Write one limitation and next action',
    ]
    exercises = [
        {'type':'mcq','question_en':f'Which result best shows that {title} is complete?','question_bn':f'কোন result দেখায় যে {bn} complete?','options_en':['A named artifact with validation evidence and limitation','A screenshot without definitions','A verbal statement that the work is done'],'options_bn':['Validation evidence ও limitationসহ named artifact','Definition ছাড়া screenshot','কাজ শেষ হয়েছে—এমন verbal statement'],'answer':0,'explanation_en':'Completion requires inspectable evidence, not only an output image or verbal claim.','explanation_bn':'Completion-এর জন্য inspectable evidence প্রয়োজন।'},
        {'type':'fill','question_en':f'Complete the sentence: {title} should connect the analytical work to the _____.','question_bn':f'Sentence complete করুন: {bn} analytical work-কে _____-এর সঙ্গে connect করবে।','answer_text':'decision','accepted':['decision','business decision','stakeholder decision'],'explanation_en':'The workflow exists to support a defined decision.','explanation_bn':'Workflow একটি defined decision support করার জন্য।'},
        {'type':'short','question_en':f'Apply {title} to the {scenario} case. State the artifact, one validation check, and one limitation.','question_bn':f'{scenario} case-এ {bn} apply করুন। Artifact, একটি validation check ও একটি limitation লিখুন।','guidance_en':'Name a concrete file, table, query, report, checklist, or decision note.','guidance_bn':'Concrete file, table, query, report, checklist অথবা decision note লিখুন।'}
    ]
    refs = [{'title':'IBM CRISP-DM overview','url':IBM_CRISP},{'title':'NIST Exploratory Data Analysis','url':NIST_EDA}]
    if module == '06': refs = [{'title':'Power BI guidance','url':POWER_BI_GUIDANCE},{'title':'PostgreSQL tutorial','url':POSTGRES},{'title':'pandas user guide','url':PANDAS}]
    if module == '08': refs = [{'title':'GitHub README documentation','url':GITHUB_README},{'title':'IBM CRISP-DM review process','url':'https://www.ibm.com/docs/en/spss-modeler/saas?topic=evaluation-review-process'}]
    return {
        'id':cid,'module':module,'level':'Beginner' if module in {'01','02'} else 'Intermediate',
        'title_en':title,'title_bn':bn,
        'summary_en':concept,'summary_bn':f'{bn} ব্যবহার করে complete analytics workflow-এ reproducible ও decision-ready output তৈরির পদ্ধতি শিখুন।',
        'minutes':45 if module not in {'05','06','08'} else 60,
        'objectives':[{'en':e,'bn':b} for e,b in zip(objective_en,objective_bn)],
        'sections':sections,
        'terms':[{'term_en':a,'term_bn':a,'definition_en':b,'definition_bn':f'{a}: {b} Project context-এ term-টির exact meaning ও evidence লিখুন।'} for a,b in terms],
        'worked_example':worked,
        'activity':{'type':'project-checklist','prompt_en':f'Complete this project checkpoint for {title}.','prompt_bn':f'{bn}-এর project checkpoint complete করুন।','items':checklist},
        'exercises':exercises,
        'recap':[
            {'en':concept.split('.')[0]+'.','bn':f'{bn} decision ও evidence-এর সঙ্গে যুক্ত থাকতে হবে।'},
            {'en':'State the row grain, definitions, assumptions, and owner.','bn':'Row grain, definition, assumption ও owner লিখুন।'},
            {'en':'Retain validation evidence and known limitations.','bn':'Validation evidence ও known limitation সংরক্ষণ করুন।'},
            {'en':'Use the output to support a specific next action.','bn':'Output দিয়ে specific next action support করুন।'},
        ],
        'references':refs,
    }

chapters = [chapter_from_spec(spec, i) for i,spec in enumerate(SPECS)]
assert len(chapters) == 49, len(chapters)

tutorial = {
    'id':'data-analytics-workflows',
    'title_en':'Data Analytics Workflows and Portfolio Projects Tutorial',
    'title_bn':'Data Analytics Workflow ও Portfolio Project Tutorial',
    'short_title_en':'Analytics Workflows',
    'short_title_bn':'Analytics Workflow',
    'description_en':'A complete project-first tutorial that connects business understanding, data quality, exploratory analysis, statistics, Excel, SQL, Power BI, Python, communication, QA, and portfolio delivery.',
    'description_bn':'Business understanding, data quality, exploratory analysis, statistics, Excel, SQL, Power BI, Python, communication, QA ও portfolio delivery-কে connect করা complete project-first tutorial।',
    'status':'published','version':'2.6.0','estimated_hours':45,
    'modules':modules,'chapters':chapters,
    'final_quiz':{'title_en':'Data Analytics Workflows Final Quiz','title_bn':'Data Analytics Workflow Final Quiz','pass_percent':75},
    'reference_groups':[
        {'title_en':'Analytics process and exploration','title_bn':'Analytics process ও exploration','references':[{'title':'IBM CRISP-DM overview','url':IBM_CRISP},{'title':'NIST Exploratory Data Analysis','url':NIST_EDA},{'title':'OpenStax Introductory Statistics','url':OPENSTAX}]},
        {'title_en':'Tool implementation','title_bn':'Tool implementation','references':[{'title':'PostgreSQL tutorial','url':POSTGRES},{'title':'Power BI guidance','url':POWER_BI_GUIDANCE},{'title':'Power BI star schema guidance','url':POWER_BI_STAR},{'title':'pandas user guide','url':PANDAS}]},
        {'title_en':'Portfolio documentation','title_bn':'Portfolio documentation','references':[{'title':'GitHub README documentation','url':GITHUB_README},{'title':'GitHub repository best practices','url':'https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories'}]},
    ],
    'downloads':[
        {'title_en':'Analytics Portfolio Toolkit','title_bn':'Analytics Portfolio Toolkit','url':'/assets/downloads/portfolio/data-analytics-portfolio-toolkit.zip'},
        {'title_en':'Project Charter Template','title_bn':'Project Charter Template','url':'/assets/downloads/portfolio/project-charter-template.md'},
        {'title_en':'Portfolio README Template','title_bn':'Portfolio README Template','url':'/assets/downloads/portfolio/portfolio-readme-template.md'},
        {'title_en':'Project QA Checklist','title_bn':'Project QA Checklist','url':'/assets/downloads/portfolio/project-qa-checklist.csv'},
    ]
}
TUTORIAL_OUT.write_text(json.dumps(tutorial, ensure_ascii=False, indent=2), encoding='utf-8')

# Shared portfolio templates
templates = {
'project-charter-template.md': '''# Project Charter\n\n## Decision to support\n\n## Stakeholders and owner\n\n## Problem statement\n\n## Analytical questions\n\n## Scope / out of scope\n\n## Data sources and row grain\n\n## Metric definitions\n\n## Deliverables\n\n## Success criteria\n\n## Risks, assumptions, and limitations\n\n## Timeline and review points\n''',
'analysis-plan-template.md': '''# Analysis Plan\n\n| Question | Metric / method | Segment | Comparison | Evidence | Validation | Output |\n|---|---|---|---|---|---|---|\n''',
'portfolio-readme-template.md': '''# Project title\n\n## Executive summary\nDescribe the decision, strongest finding, recommendation, and limitation.\n\n## Business problem\n\n## Data\nDescribe sources, row grain, period, dictionary, and privacy.\n\n## Workflow\nBusiness understanding → data audit → preparation → analysis → validation → communication.\n\n## Tools\nExplain why each tool was used.\n\n## Analysis and evidence\nLink every important claim to a table, query, chart, notebook, or report page.\n\n## Findings and recommendations\n\n## Validation and limitations\n\n## Repository structure\n\n## How to reproduce\n''',
'presentation-outline-template.md': '''# Portfolio Presentation Outline\n1. Decision and stakeholder\n2. Data and scope\n3. Quality and preparation\n4. Analytical approach\n5. Three strongest findings\n6. Recommendation and expected impact\n7. Limitations and next validation\n8. Technical walkthrough\n''',
}
for name, text in templates.items(): (DL/name).write_text(text, encoding='utf-8')

for name, headers in {
'project-qa-checklist.csv':['phase','check','status','evidence','reviewer','notes'],
'metric-dictionary-template.csv':['metric','business_definition','formula','grain','filters','time_window','owner','validation'],
'data-quality-audit-template.csv':['dataset','field_or_test','quality_dimension','rule','result','threshold','action','owner'],
'insight-log-template.csv':['insight_id','observation','evidence','interpretation','business_implication','limitation','recommended_action','status'],
}.items():
    with (DL/name).open('w',newline='',encoding='utf-8') as f: csv.writer(f).writerow(headers)

rng = random.Random(260)
regions = ['Dhaka','Chattogram','Khulna','Rajshahi']

# Data writers
def write_csv(path: Path, headers: list[str], rows: list[list]):
    with path.open('w', newline='', encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(headers); w.writerows(rows)

def write_dict(path: Path, file_fields: list[tuple[str,str,str,str]]):
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['file','field','type','description']); w.writerows(file_fields)

project_specs = []

# 1 Retail sales 360
retail_rows=[]
products=[('P101','Shirt','Apparel',800),('P102','Polo Shirt','Apparel',1100),('P103','Trousers','Apparel',1500),('P104','Keyboard','Electronics',2200),('P105','Monitor','Electronics',14500),('P106','Headset','Electronics',3200),('P107','Backpack','Accessories',1800),('P108','Notebook','Stationery',180)]
start=date(2025,1,1)
for i in range(1,901):
    d=start+timedelta(days=rng.randrange(0,730)); pid,pname,cat,base=rng.choice(products); qty=rng.randrange(1,8); disc=rng.choice([0,0,0.05,0.10,0.15]); price=round(base*(.93+rng.random()*.16),2); rev=round(qty*price*(1-disc),2); cost=round(rev*(.58+rng.random()*.18),2)
    retail_rows.append([f'O{i:05d}',d.isoformat(),f'C{rng.randrange(1,241):04d}',pid,pname,cat,rng.choice(regions),rng.choice(['Online','Retail','Partner']),qty,price,disc,rev,cost,round(rev-cost,2)])
write_csv(DS/'retail_sales_360.csv',['order_id','order_date','customer_id','product_id','product_name','category','region','channel','quantity','unit_price','discount','revenue','cost','profit'],retail_rows)
write_dict(DS/'retail_sales_360_dictionary.csv',[('retail_sales_360.csv',h,'number' if h in {'quantity','unit_price','discount','revenue','cost','profit'} else 'date' if h=='order_date' else 'text',h.replace('_',' ').title()) for h in ['order_id','order_date','customer_id','product_id','product_name','category','region','channel','quantity','unit_price','discount','revenue','cost','profit']])

# 2 Retention tables
cust=[]; tx=[]
segments=['Consumer','Corporate','Small Business']
for i in range(1,301):
    signup=start+timedelta(days=rng.randrange(0,365)); cust.append([f'C{i:04d}',signup.isoformat(),rng.choice(segments),rng.choice(regions),rng.choice(['Organic','Paid Search','Social','Referral'])])
    active_months=rng.randrange(1,19); orders=rng.randrange(1,active_months+3)
    for j in range(orders):
        od=signup+timedelta(days=rng.randrange(0,min(720,max(30,active_months*30)))); tx.append([f'T{i:04d}-{j+1:02d}',f'C{i:04d}',od.isoformat(),round(250+rng.random()*5500,2),rng.choice(['Web','App','Store'])])
write_csv(DS/'retention_customers.csv',['customer_id','signup_date','segment','region','acquisition_channel'],cust)
write_csv(DS/'retention_transactions.csv',['transaction_id','customer_id','transaction_date','revenue','channel'],tx)
write_dict(DS/'customer_retention_dictionary.csv',[(f,h,'date' if 'date' in h else 'number' if h=='revenue' else 'text',h.replace('_',' ').title()) for f,hs in [('retention_customers.csv',['customer_id','signup_date','segment','region','acquisition_channel']),('retention_transactions.csv',['transaction_id','customer_id','transaction_date','revenue','channel'])] for h in hs])

# 3 Marketing experiment
mkt=[]
for i in range(1,2001):
    variant='Treatment' if i%2 else 'Control'; device=rng.choice(['Mobile','Desktop','Tablet']); source=rng.choice(['Search','Social','Email','Direct']); base=.075 if variant=='Control' else .088; conv=1 if rng.random() < base + (0.012 if source=='Email' else 0) else 0; revenue=round((350+rng.random()*3800) if conv else 0,2)
    mkt.append([f'V{i:05d}',variant,device,source,(start+timedelta(days=rng.randrange(0,60))).isoformat(),conv,revenue,round(20+rng.random()*180,2),1 if rng.random()<.02 else 0])
write_csv(DS/'marketing_ab_test.csv',['visitor_id','variant','device','source','visit_date','converted','revenue','session_seconds','complaint_flag'],mkt)
write_dict(DS/'marketing_ab_test_dictionary.csv',[('marketing_ab_test.csv',h,'number' if h in {'converted','revenue','session_seconds','complaint_flag'} else 'date' if h=='visit_date' else 'text',h.replace('_',' ').title()) for h in ['visitor_id','variant','device','source','visit_date','converted','revenue','session_seconds','complaint_flag']])

# 4 HR workforce
hr=[]
departments=['Sales','Operations','Finance','IT','HR','Programs']
for i in range(1,501):
    hire=date(2018,1,1)+timedelta(days=rng.randrange(0,2800)); age=rng.randrange(21,59); salary=round(22000+rng.random()*98000,2); perf=rng.choice([2,3,3,3,4,4,5]); overtime=rng.choice(['Yes','No','No']); left=1 if rng.random() < (.20 if overtime=='Yes' else .09) else 0
    hr.append([f'E{i:04d}',rng.choice(departments),rng.choice(['Analyst','Officer','Manager','Specialist','Coordinator']),rng.choice(regions),hire.isoformat(),age,rng.choice(['Female','Male']),salary,perf,overtime,rng.randrange(0,22),left])
write_csv(DS/'hr_workforce.csv',['employee_id','department','job_role','location','hire_date','age','gender','monthly_salary','performance_rating','overtime','absence_days','left_company'],hr)
write_dict(DS/'hr_workforce_dictionary.csv',[('hr_workforce.csv',h,'number' if h in {'age','monthly_salary','performance_rating','absence_days','left_company'} else 'date' if h=='hire_date' else 'text',h.replace('_',' ').title()) for h in ['employee_id','department','job_role','location','hire_date','age','gender','monthly_salary','performance_rating','overtime','absence_days','left_company']])

# 5 Budget actual
fin=[]
accounts=['Salaries','Rent','Travel','IT Services','Training','Marketing','Professional Fees','Utilities']
for month in range(1,25):
    y=2025+(month-1)//12; m=(month-1)%12+1
    for dept in ['Operations','Sales','Finance','IT']:
        for acc in accounts:
            budget=round(40000+rng.random()*260000,2); actual=round(budget*(.75+rng.random()*.55),2)
            fin.append([f'{y}-{m:02d}',dept,acc,budget,actual,round(actual-budget,2),rng.choice(['Approved','Approved','Additional Approval'])])
write_csv(DS/'financial_budget_actual.csv',['month','department','account','budget','actual','variance','approval_status'],fin)
write_dict(DS/'financial_budget_actual_dictionary.csv',[('financial_budget_actual.csv',h,'number' if h in {'budget','actual','variance'} else 'date-period' if h=='month' else 'text',h.replace('_',' ').title()) for h in ['month','department','account','budget','actual','variance','approval_status']])

# 6 NGO program monitoring
ngo=[]
projects=['Education','Primary Health','Climate Action','Women Empowerment']
for month in range(1,25):
    y=2025+(month-1)//12; m=(month-1)%12+1
    for proj in projects:
        for loc in regions:
            target=rng.randrange(80,420); reached=max(0,round(target*(.65+rng.random()*.55))); budget=round(50000+rng.random()*250000,2); expense=round(budget*(.70+rng.random()*.45),2)
            ngo.append([f'{y}-{m:02d}',proj,loc,target,reached,budget,expense,round(expense/budget,4),rng.randrange(0,8),rng.choice(['On track','At risk','Delayed'])])
write_csv(DS/'ngo_program_monitoring.csv',['month','project','location','beneficiary_target','beneficiary_reached','budget','expense','utilization_rate','quality_issues','status'],ngo)
write_dict(DS/'ngo_program_monitoring_dictionary.csv',[('ngo_program_monitoring.csv',h,'number' if h in {'beneficiary_target','beneficiary_reached','budget','expense','utilization_rate','quality_issues'} else 'date-period' if h=='month' else 'text',h.replace('_',' ').title()) for h in ['month','project','location','beneficiary_target','beneficiary_reached','budget','expense','utilization_rate','quality_issues','status']])

projects = [
    {'id':'retail-sales-360','title_en':'Retail Sales 360° Performance Analysis','title_bn':'Retail Sales 360° Performance Analysis','summary_en':'Analyze revenue, profit, margin, products, regions, channels, customers, and trends across Excel, SQL, Power BI, Python, and Statistics.','summary_bn':'Excel, SQL, Power BI, Python ও Statistics দিয়ে revenue, profit, margin, product, region, channel, customer ও trend analyze করুন।','level':'Intermediate','estimated_hours':28,'tools':['Statistics','Excel','SQL','Power BI','Python'],'files':['retail_sales_360.csv','retail_sales_360_dictionary.csv'],'questions':['Which regions, channels, and products drive revenue and profit?','How do sales and margins change over time?','Where do product mix and discounting create risk?'],'deliverables':['Data-quality audit','Metric dictionary','Excel analysis workbook','SQL analytical query set','Power BI report plan','Python EDA notebook','Executive insight brief']},
    {'id':'customer-retention-cohorts','title_en':'Customer Retention and Cohort Analysis','title_bn':'Customer Retention ও Cohort Analysis','summary_en':'Measure repeat purchase, cohort retention, customer value, segment differences, and churn signals using relational and time-based analysis.','summary_bn':'Relational ও time-based analysis দিয়ে repeat purchase, cohort retention, customer value, segment difference ও churn signal measure করুন।','level':'Intermediate','estimated_hours':32,'tools':['SQL','Power BI','Python','Statistics'],'files':['retention_customers.csv','retention_transactions.csv','customer_retention_dictionary.csv'],'questions':['How does retention vary by signup cohort and acquisition source?','Which segments create the strongest repeat revenue?','Which early behaviors are associated with inactivity?'],'deliverables':['Cohort table','Retention curves','Customer segment summary','SQL query pack','Power BI model plan','Python cohort notebook','Retention recommendation']},
    {'id':'marketing-ab-test','title_en':'Marketing Campaign and A/B Test Evaluation','title_bn':'Marketing Campaign ও A/B Test Evaluation','summary_en':'Evaluate conversion, revenue, segment response, sample balance, uncertainty, effect size, and guardrail metrics for a controlled campaign test.','summary_bn':'Controlled campaign test-এর conversion, revenue, segment response, sample balance, uncertainty, effect size ও guardrail metric evaluate করুন।','level':'Intermediate','estimated_hours':26,'tools':['Statistics','Excel','SQL','Power BI','Python'],'files':['marketing_ab_test.csv','marketing_ab_test_dictionary.csv'],'questions':['Did treatment improve conversion and revenue?','Are results consistent across device and source?','Did complaints or session behavior create a guardrail concern?'],'deliverables':['Experiment audit','Conversion and revenue estimates','Confidence interval and test','Segment analysis','Decision memo','Monitoring plan']},
    {'id':'hr-workforce-analytics','title_en':'HR Workforce and Attrition Analytics','title_bn':'HR Workforce ও Attrition Analytics','summary_en':'Analyze workforce composition, turnover, absence, salary, performance, overtime, and attrition patterns without overstating individual-level causality.','summary_bn':'Individual-level causality overstate না করে workforce composition, turnover, absence, salary, performance, overtime ও attrition pattern analyze করুন।','level':'Intermediate','estimated_hours':28,'tools':['Excel','SQL','Power BI','Python','Statistics'],'files':['hr_workforce.csv','hr_workforce_dictionary.csv'],'questions':['Where is turnover concentrated?','How do overtime, absence, tenure, and role differ between groups?','Which workforce metrics should management monitor?'],'deliverables':['HR metric dictionary','Workforce profile','Attrition segment analysis','Accessible HR dashboard plan','Ethics and privacy note','Management recommendations']},
    {'id':'financial-budget-control','title_en':'Financial Budget vs Actual Control Analysis','title_bn':'Financial Budget vs Actual Control Analysis','summary_en':'Analyze budget, actuals, variance, utilization, approvals, recurring overspend, and forecast risk across departments and accounts.','summary_bn':'Department ও account অনুযায়ী budget, actual, variance, utilization, approval, recurring overspend ও forecast risk analyze করুন।','level':'Intermediate','estimated_hours':24,'tools':['Excel','SQL','Power BI','Python'],'files':['financial_budget_actual.csv','financial_budget_actual_dictionary.csv'],'questions':['Which departments and accounts are over or under budget?','Is overspend recurring or event-specific?','Which approvals and forecasts require management action?'],'deliverables':['Budget-control table','Variance bridge','Monthly trend report','Exception list','Power BI management dashboard plan','Control recommendation']},
    {'id':'ngo-program-monitoring','title_en':'NGO Program Monitoring and Expense Utilization','title_bn':'NGO Program Monitoring ও Expense Utilization','summary_en':'Evaluate beneficiary reach, target achievement, expense utilization, project status, quality issues, and cost efficiency across programs and locations.','summary_bn':'Program ও location অনুযায়ী beneficiary reach, target achievement, expense utilization, project status, quality issue ও cost efficiency evaluate করুন।','level':'Intermediate','estimated_hours':30,'tools':['Excel','SQL','Power BI','Python','Statistics'],'files':['ngo_program_monitoring.csv','ngo_program_monitoring_dictionary.csv'],'questions':['Which projects and locations meet targets within budget?','Where are utilization and delivery misaligned?','Which quality issues require follow-up before donor reporting?'],'deliverables':['Program KPI dictionary','Target-versus-achievement analysis','Expense utilization dashboard plan','Exception and quality log','Donor-ready narrative','Follow-up action plan']},
]

common_workflow = [
    ('01','Frame','Confirm the stakeholder decision, project scope, success criteria, assumptions, and required deliverables.'),
    ('02','Understand','Read the dictionary, state row grain, profile fields, and document source coverage and limitations.'),
    ('03','Prepare','Create reproducible cleaning, type, category, join, and reconciliation steps while preserving raw data.'),
    ('04','Analyze','Build overview metrics, segments, trends, distributions, relationships, and required statistical evaluation.'),
    ('05','Implement','Reproduce agreed metrics in the relevant tools and reconcile totals across implementations.'),
    ('06','Communicate','Create decision-ready visuals, findings, recommendations, limitations, and an executive summary.'),
    ('07','Validate','Complete QA, peer review, refresh instructions, and evidence links before publication.'),
    ('08','Portfolio','Package README, code, queries, report screenshots, data notes, and interview walkthrough.'),
]

for project in projects:
    project['status']='available'; project['url']=f"/projects/{project['id']}/"; project['workflow']=[{'id':a,'title_en':b,'title_bn':b,'summary_en':c,'summary_bn':f'{b} phase-এ {c}'} for a,b,c in common_workflow]
    project['quality_gates']=['Row grain and key uniqueness documented','All metric definitions include filters and denominators','Control totals reconcile across tools','Charts match the stated analytical question','Findings distinguish evidence, interpretation, and limitation','README and reproduction steps are complete']
    project['portfolio_sections']=['Executive summary','Business problem and stakeholders','Data sources and dictionary','Workflow and tool choices','Analysis and evidence','Findings and recommendations','Validation and limitations','Repository structure and reproduction']

# Write project-specific briefs and bundles
for project in projects:
    pdir = DL / project['id']; pdir.mkdir(parents=True, exist_ok=True)
    brief = f"# {project['title_en']}\n\n## Scenario\n{project['summary_en']}\n\n## Analytical questions\n" + ''.join(f'- {q}\n' for q in project['questions']) + '\n## Required deliverables\n' + ''.join(f'- {d}\n' for d in project['deliverables']) + '\n## Workflow\n' + ''.join(f"{w['id']}. **{w['title_en']}** — {w['summary_en']}\n" for w in project['workflow']) + '\n## Quality gates\n' + ''.join(f'- {q}\n' for q in project['quality_gates'])
    (pdir/'project-brief.md').write_text(brief,encoding='utf-8')
    (pdir/'starter-sql.sql').write_text(textwrap.dedent(f'''-- {project['title_en']}\n-- 1. Inspect tables and row grain.\n-- 2. Build quality checks.\n-- 3. Create a validated analytical base.\n-- 4. Calculate project KPIs.\n-- 5. Reconcile totals and document filters.\n'''),encoding='utf-8')
    (pdir/'starter-python.py').write_text(textwrap.dedent(f'''\n"""Starter workflow for {project['title_en']}."""\nfrom pathlib import Path\nimport pandas as pd\n\nDATA = Path('.')\n\n# Load the supplied project files, then complete:\n# 1. data audit\n# 2. cleaning and validation\n# 3. analysis\n# 4. visualization\n# 5. findings and limitations\n''').strip()+"\n",encoding='utf-8')
    (pdir/'power-bi-build-guide.md').write_text(f"# Power BI Build Guide — {project['title_en']}\n\n1. Import the supplied CSV files with Power Query.\n2. Confirm data types, row counts, keys, and missing values.\n3. Build a star schema where multiple tables are supplied.\n4. Create explicit measures for the agreed KPIs.\n5. Design summary, drivers, detail, and definitions pages.\n6. Validate totals against the project control table.\n7. Add accessibility, refresh, and security notes.\n",encoding='utf-8')
    (pdir/'excel-build-guide.md').write_text(f"# Excel Build Guide — {project['title_en']}\n\n1. Keep raw data unchanged.\n2. Convert data to Excel Tables or load with Power Query.\n3. Add a metric dictionary and control sheet.\n4. Use formulas and PivotTables for required analysis.\n5. Build decision-ready charts and an executive summary.\n6. Reconcile totals and document refresh steps.\n",encoding='utf-8')
    zip_path = DL / f"{project['id']}-project-package.zip"
    with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
        for fn in project['files']:
            z.write(DS/fn, f'data/{fn}')
        for asset in pdir.iterdir(): z.write(asset, f'templates/{asset.name}')
        for template in templates: z.write(DL/template, f'portfolio-toolkit/{template}')
        for template in ['project-qa-checklist.csv','metric-dictionary-template.csv','data-quality-audit-template.csv','insight-log-template.csv']:
            z.write(DL/template, f'portfolio-toolkit/{template}')
    project['downloads']=[{'title_en':'Complete project package','title_bn':'Complete project package','url':f'/assets/downloads/portfolio/{project["id"]}-project-package.zip'}]

PROJECT_OUT.write_text(json.dumps(projects,ensure_ascii=False,indent=2),encoding='utf-8')

# Combined portfolio toolkit
with zipfile.ZipFile(DL/'data-analytics-portfolio-toolkit.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in DL.iterdir():
        if p.is_file() and p.name != 'data-analytics-portfolio-toolkit.zip' and not p.name.endswith('-project-package.zip'):
            z.write(p,p.name)

print(f'Built {len(chapters)} workflow chapters, {len(projects)} portfolio projects, and downloadable project packages.')
