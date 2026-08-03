TOPIC_DETAILS = {
    # Foundations
    "Statistics and Data": (
        "Data are recorded values about entities or events; statistics is the discipline of designing data collection, summarizing variation, and making uncertainty-aware conclusions.",
        "ডেটা হলো entity বা event সম্পর্কে রেকর্ড করা মান; statistics হলো data collection ডিজাইন, variation সংক্ষেপ এবং uncertainty বিবেচনায় conclusion তৈরির শাস্ত্র।",
    ),
    "Population and Sample": (
        "A population is the complete target set, while a sample is the observed subset used to learn about that population. Valid generalization depends on how the sample was selected.",
        "Population হলো সম্পূর্ণ target set, আর sample হলো population সম্পর্কে শেখার জন্য observed subset। sample কীভাবে নির্বাচন করা হয়েছে তার ওপর valid generalization নির্ভর করে।",
    ),
    "Variables and Observations": (
        "An observation is one recorded unit or row; a variable is a characteristic measured across observations. Clear unit-of-analysis definitions prevent duplicated or mismatched records.",
        "Observation হলো একটি recorded unit বা row; variable হলো observation জুড়ে measured characteristic। unit of analysis পরিষ্কার না হলে duplicate বা mismatched record তৈরি হয়।",
    ),
    "Measurement Scales": (
        "Nominal, ordinal, interval, and ratio scales describe what comparisons and arithmetic operations are meaningful for a variable.",
        "Nominal, ordinal, interval ও ratio scale নির্ধারণ করে একটি variable-এর জন্য কোন comparison ও arithmetic operation অর্থবহ।",
    ),
    "Categorical and Numerical Data": (
        "Categorical data represent labels or groups; numerical data represent counts or measured quantities. Discrete and continuous numerical variables often require different summaries and models.",
        "Categorical data label বা group প্রকাশ করে; numerical data count বা measured quantity প্রকাশ করে। discrete ও continuous variable-এর summary এবং model প্রায়ই ভিন্ন হয়।",
    ),
    "Data Collection Methods": (
        "Surveys, experiments, observations, sensors, transactions, and administrative systems generate data with different strengths, biases, and error mechanisms.",
        "Survey, experiment, observation, sensor, transaction ও administrative system ভিন্ন strength, bias ও error mechanism-সহ ডেটা তৈরি করে।",
    ),
    "Probability and Non-probability Sampling": (
        "Probability sampling gives units known selection chances and supports design-based inference; non-probability sampling relies on accessibility or judgment and needs stronger assumptions for generalization.",
        "Probability sampling-এ unit-এর selection chance জানা থাকে এবং design-based inference সম্ভব; non-probability sampling accessibility বা judgment-এর ওপর নির্ভর করে এবং generalization-এর জন্য বেশি assumption প্রয়োজন।",
    ),
    "Sampling Bias and Confounding": (
        "Sampling bias occurs when the observed sample systematically differs from the target population. Confounding occurs when a third variable distorts an exposure–outcome relationship.",
        "Observed sample target population থেকে পদ্ধতিগতভাবে ভিন্ন হলে sampling bias হয়। তৃতীয় variable exposure–outcome relationship বিকৃত করলে confounding হয়।",
    ),
    "Data Quality Dimensions": (
        "Accuracy, completeness, consistency, timeliness, validity, and uniqueness are distinct dimensions. A dataset can be complete yet inaccurate, or valid in format yet stale.",
        "Accuracy, completeness, consistency, timeliness, validity ও uniqueness আলাদা dimension। dataset complete হয়েও inaccurate অথবা format-valid হয়েও stale হতে পারে।",
    ),
    "Frequency Tables": (
        "A frequency table counts values or groups and may include proportions and cumulative proportions. It is a first check for distribution, missing categories, and coding errors.",
        "Frequency table value বা group count করে এবং proportion ও cumulative proportion দেখাতে পারে। distribution, missing category ও coding error যাচাইয়ের এটি প্রাথমিক ধাপ।",
    ),
    "Exploratory Data Analysis Workflow": (
        "EDA combines data validation, univariate summaries, relationship checks, visualizations, and anomaly review before formal modeling or reporting.",
        "EDA formal modeling বা reporting-এর আগে data validation, univariate summary, relationship check, visualization ও anomaly review একত্র করে।",
    ),
    "Reproducible Statistical Workflow": (
        "A reproducible workflow preserves raw data, records transformations, fixes random seeds when needed, versions code, and produces outputs that can be regenerated from documented inputs.",
        "Reproducible workflow raw data সংরক্ষণ, transformation record, প্রয়োজনমতো random seed fix, code version এবং documented input থেকে output পুনরায় তৈরি নিশ্চিত করে।",
    ),
    # Descriptive statistics
    "Mean, Median and Mode": (
        "The mean balances all values, the median identifies the ordered midpoint, and the mode identifies the most frequent value. Their usefulness depends on distribution shape and measurement scale.",
        "Mean সব মানের balance point, median ordered midpoint এবং mode সবচেয়ে frequent value দেখায়। কোনটি উপযোগী হবে তা distribution shape ও measurement scale-এর ওপর নির্ভর করে।",
    ),
    "Weighted, Geometric and Harmonic Means": (
        "Weighted means reflect unequal importance; geometric means summarize multiplicative change; harmonic means summarize rates when the numerator is held comparable.",
        "Weighted mean unequal importance, geometric mean multiplicative change এবং harmonic mean comparable numerator-সহ rate সংক্ষেপ করে।",
    ),
    "Quantiles and Percentiles": (
        "Quantiles divide an ordered distribution by cumulative probability. Quartiles are the 25th, 50th, and 75th percentiles, although software may use different interpolation conventions.",
        "Quantile cumulative probability অনুযায়ী ordered distribution ভাগ করে। Quartile হলো 25th, 50th ও 75th percentile; তবে software ভিন্ন interpolation convention ব্যবহার করতে পারে।",
    ),
    "Range and Interquartile Range": (
        "The range uses the two extreme values and is sensitive to outliers. The IQR measures the middle 50% and is more resistant to extreme observations.",
        "Range দুইটি extreme value ব্যবহার করে এবং outlier-sensitive। IQR মাঝের ৫০% spread মাপে এবং extreme observation-এর প্রতি বেশি resistant।",
    ),
    "Variance and Standard Deviation": (
        "Variance averages squared deviations from the mean; standard deviation returns that spread to the original unit. Sample variance commonly uses n−1 to estimate population variance.",
        "Variance mean থেকে squared deviation সংক্ষেপ করে; standard deviation spread-কে original unit-এ ফিরিয়ে আনে। population variance estimate করতে sample variance সাধারণত n−1 ব্যবহার করে।",
    ),
    "Coefficient of Variation": (
        "The coefficient of variation expresses standard deviation relative to the absolute mean, enabling scale-free comparison when a meaningful nonzero ratio-scale mean exists.",
        "Coefficient of variation standard deviation-কে absolute mean-এর তুলনায় প্রকাশ করে; meaningful nonzero ratio-scale mean থাকলে scale-free comparison সম্ভব।",
    ),
    "Skewness": (
        "Skewness describes asymmetry: positive values indicate a longer right tail and negative values a longer left tail. It is sensitive to extreme observations and sample size.",
        "Skewness asymmetry বোঝায়: positive value দীর্ঘ right tail এবং negative value দীর্ঘ left tail নির্দেশ করে। এটি extreme observation ও sample size-sensitive।",
    ),
    "Kurtosis": (
        "Kurtosis summarizes tail weight and outlier-proneness relative to a reference distribution; it should not be interpreted only as peak height.",
        "Kurtosis reference distribution-এর তুলনায় tail weight ও outlier-proneness সংক্ষেপ করে; এটিকে শুধু peak height হিসেবে ব্যাখ্যা করা উচিত নয়।",
    ),
    "Outlier Detection": (
        "Outlier rules flag observations for investigation, not automatic deletion. Unusual values may reflect errors, rare valid events, subgroup structure, or model mismatch.",
        "Outlier rule observation review-এর জন্য flag করে, automatic deletion-এর জন্য নয়। unusual value error, rare valid event, subgroup structure বা model mismatch হতে পারে।",
    ),
    "Histograms": (
        "A histogram groups numerical values into intervals to show shape, center, spread, gaps, and multiple modes. Its appearance changes with bin width and boundary choices.",
        "Histogram numerical value-কে interval-এ group করে shape, center, spread, gap ও multiple mode দেখায়। bin width ও boundary বদলালে appearance বদলায়।",
    ),
    "Box Plots": (
        "A box plot displays quartiles, median, whiskers, and potential outliers, making group comparisons compact while hiding detailed distribution features such as multimodality.",
        "Box plot quartile, median, whisker ও potential outlier দেখায়; group comparison compact হয়, তবে multimodality-এর মতো detail লুকাতে পারে।",
    ),
    "Scatter, Line and Bar Charts": (
        "Scatter plots show relationships between numerical variables, line charts emphasize ordered change over time or sequence, and bar charts compare categorical magnitudes.",
        "Scatter plot numerical variable-এর relationship, line chart time বা sequence অনুযায়ী change এবং bar chart categorical magnitude তুলনা দেখায়।",
    ),
    # Probability
    "Probability Rules": (
        "Probability rules define complements, unions, intersections, and conditional events. Correct use requires a clearly specified sample space and event definitions.",
        "Probability rule complement, union, intersection ও conditional event নির্ধারণ করে। সঠিক ব্যবহারের জন্য sample space ও event definition পরিষ্কার হতে হবে।",
    ),
    "Conditional Probability": (
        "Conditional probability updates the chance of an event after restricting attention to cases where another event occurred. It is generally not symmetric.",
        "Conditional probability অন্য event ঘটেছে এমন case-এ সীমাবদ্ধ হয়ে একটি event-এর chance update করে। এটি সাধারণত symmetric নয়।",
    ),
    "Bayes' Theorem": (
        "Bayes' theorem combines prior probability with evidence likelihood to obtain a posterior probability. Base rates can dominate even when a test appears accurate.",
        "Bayes' theorem prior probability ও evidence likelihood একত্র করে posterior probability দেয়। test accurate মনে হলেও base rate ফলাফলে বড় প্রভাব ফেলতে পারে।",
    ),
    "Random Variables": (
        "A random variable maps outcomes of a random process to numerical values. Its probability distribution describes the values it can take and their probabilities.",
        "Random variable random process-এর outcome-কে numerical value-এ map করে। probability distribution সম্ভাব্য value ও তাদের probability বর্ণনা করে।",
    ),
    "Expected Value and Variance": (
        "Expected value is a probability-weighted long-run average; variance measures expected squared deviation around that mean. Neither guarantees a typical single outcome.",
        "Expected value probability-weighted long-run average; variance mean-এর চারপাশে expected squared deviation মাপে। কোনোটিই একটি single outcome typical হবে তা নিশ্চিত করে না।",
    ),
    "Bernoulli and Binomial Distributions": (
        "A Bernoulli variable records one binary trial. A binomial variable counts successes across a fixed number of independent Bernoulli trials with constant success probability.",
        "Bernoulli variable একটি binary trial record করে। Binomial variable fixed সংখ্যক independent Bernoulli trial-এ constant success probability সহ success count করে।",
    ),
    "Poisson Distribution": (
        "The Poisson distribution models non-negative event counts over fixed exposure when events occur independently at an approximately stable rate.",
        "Poisson distribution fixed exposure-এ non-negative event count model করে, যখন event প্রায় independently এবং stable rate-এ ঘটে।",
    ),
    "Uniform Distribution": (
        "A continuous uniform model assigns equal density across a bounded interval. Equal density does not mean each exact point has positive probability.",
        "Continuous uniform model bounded interval জুড়ে equal density দেয়। equal density মানে প্রতিটি exact point-এর positive probability নয়।",
    ),
    "Normal Distribution": (
        "The normal distribution is a symmetric bell-shaped model determined by mean and standard deviation. Many methods use it as an approximation, not a universal data law.",
        "Normal distribution mean ও standard deviation দ্বারা নির্ধারিত symmetric bell-shaped model। অনেক method এটিকে approximation হিসেবে ব্যবহার করে; এটি universal data law নয়।",
    ),
    "Exponential Distribution": (
        "The exponential distribution models non-negative waiting time between Poisson-process events under a constant rate and has the memoryless property.",
        "Exponential distribution constant rate-সহ Poisson process event-এর মধ্যবর্তী non-negative waiting time model করে এবং memoryless property রাখে।",
    ),
    "Sampling Distributions": (
        "A sampling distribution describes how a statistic varies across repeated samples generated by a defined sampling process. It underlies standard errors and inference.",
        "Sampling distribution নির্ধারিত sampling process-এ repeated sample জুড়ে statistic কীভাবে বদলায় তা বর্ণনা করে; standard error ও inference-এর ভিত্তি এটি।",
    ),
    "Central Limit Theorem": (
        "Under suitable independence and finite-variance conditions, standardized sums or sample means approach a normal distribution as sample size grows.",
        "উপযুক্ত independence ও finite-variance condition-এ sample size বাড়লে standardized sum বা sample mean normal distribution-এর দিকে এগোয়।",
    ),
    # Inference
    "Point Estimation": (
        "A point estimator uses sample data to produce one numerical estimate of a population parameter. Good estimators are evaluated by bias, variance, consistency, and robustness.",
        "Point estimator sample data থেকে population parameter-এর একটি numerical estimate দেয়। estimator bias, variance, consistency ও robustness দিয়ে মূল্যায়িত হয়।",
    ),
    "Confidence Intervals": (
        "A confidence-interval procedure combines an estimate, standard error, and critical value to express sampling uncertainty under stated assumptions.",
        "Confidence interval procedure estimate, standard error ও critical value একত্র করে stated assumption-এর অধীনে sampling uncertainty প্রকাশ করে।",
    ),
    "Hypothesis Testing Framework": (
        "Hypothesis testing compares observed evidence with a reference null model through a prespecified statistic, sampling distribution, decision rule, and alternative.",
        "Hypothesis testing prespecified statistic, sampling distribution, decision rule ও alternative ব্যবহার করে observed evidence-কে reference null model-এর সঙ্গে তুলনা করে।",
    ),
    "p-values and Significance Levels": (
        "A p-value measures how incompatible the data are with a specified null model; alpha is a decision threshold chosen before seeing results. A p-value is not the probability the null is true.",
        "P-value specified null model-এর সঙ্গে data কতটা incompatible তা মাপে; alpha ফল দেখার আগে নির্ধারিত decision threshold। p-value null সত্য হওয়ার probability নয়।",
    ),
    "Type I, Type II Errors and Power": (
        "Type I error is rejecting a true null; Type II error is failing to reject a false null. Power is the probability of detecting a specified effect under the alternative.",
        "True null reject করা Type I error; false null reject করতে ব্যর্থ হওয়া Type II error। alternative-এ নির্দিষ্ট effect detect করার probability হলো power।",
    ),
    "One-sample z and t Tests": (
        "One-sample tests compare a sample mean with a hypothesized population mean. The t test estimates standard error from the sample; a z test needs a justified known standard deviation or approximation.",
        "One-sample test sample mean-কে hypothesized population mean-এর সঙ্গে তুলনা করে। t test sample থেকে standard error estimate করে; z test-এর জন্য justified known standard deviation বা approximation প্রয়োজন।",
    ),
    "Two-sample t Test": (
        "A two-sample t test compares independent group means. Welch's version allows unequal variances and is generally safer than the pooled equal-variance test.",
        "Two-sample t test independent group mean তুলনা করে। Welch version unequal variance অনুমোদন করে এবং pooled equal-variance test-এর তুলনায় সাধারণত নিরাপদ।",
    ),
    "Paired t Test": (
        "A paired t test analyzes within-pair differences, such as before–after measurements or matched units, and requires independence between pairs rather than between individual measurements.",
        "Paired t test before–after measurement বা matched unit-এর within-pair difference বিশ্লেষণ করে; individual measurement নয়, pairগুলোর মধ্যে independence প্রয়োজন।",
    ),
    "Tests for Proportions": (
        "Proportion tests evaluate binary-outcome rates using binomial or large-sample approximations. Validity depends on sampling, independence, and sufficiently informative counts.",
        "Proportion test binary-outcome rate-কে binomial বা large-sample approximation দিয়ে মূল্যায়ন করে। sampling, independence ও পর্যাপ্ত informative count-এর ওপর validity নির্ভর করে।",
    ),
    "Chi-square Tests": (
        "Chi-square tests compare observed categorical counts with expected counts for goodness-of-fit or independence. Small expected cells can invalidate the asymptotic approximation.",
        "Chi-square test goodness-of-fit বা independence-এর জন্য observed categorical count-কে expected count-এর সঙ্গে তুলনা করে। ছোট expected cell asymptotic approximation invalid করতে পারে।",
    ),
    "Analysis of Variance": (
        "ANOVA tests whether group mean variation is larger than expected from within-group variation under a linear-model framework. A significant result does not identify which groups differ.",
        "ANOVA linear-model framework-এ group mean variation within-group variation-এর তুলনায় বেশি কি না test করে। significant result কোন group ভিন্ন তা নিজে বলে না।",
    ),
    "Nonparametric Tests": (
        "Nonparametric and rank-based tests reduce reliance on specific distributional forms, but they still require assumptions about sampling, independence, and what is being compared.",
        "Nonparametric ও rank-based test specific distributional form-এর ওপর নির্ভরতা কমায়; তবুও sampling, independence ও comparison target সম্পর্কে assumption থাকে।",
    ),
    # Regression
    "Covariance and Correlation": (
        "Covariance measures joint variation in product units; correlation standardizes covariance to a −1 to 1 scale for linear association.",
        "Covariance product unit-এ joint variation মাপে; correlation covariance-কে −1 থেকে 1 scale-এ standardize করে linear association দেখায়।",
    ),
    "Pearson and Spearman Correlation": (
        "Pearson correlation measures linear association in original values; Spearman correlation measures monotonic association using ranks and is less sensitive to extreme scale values.",
        "Pearson correlation original value-এ linear association এবং Spearman correlation rank ব্যবহার করে monotonic association মাপে; এটি extreme scale value-এর প্রতি কম sensitive।",
    ),
    "Simple Linear Regression": (
        "Simple linear regression models the conditional mean of an outcome as an intercept plus a slope times one predictor. The slope describes fitted change within the observed range.",
        "Simple linear regression outcome-এর conditional mean-কে intercept ও একটি predictor-এর slope দিয়ে model করে। slope observed range-এর মধ্যে fitted change বোঝায়।",
    ),
    "Ordinary Least Squares": (
        "OLS chooses coefficients that minimize squared residuals. Its estimates and standard errors rely on model specification, independence structure, and variance assumptions.",
        "OLS squared residual সর্বনিম্ন করে coefficient নির্বাচন করে। estimate ও standard error model specification, independence structure ও variance assumption-এর ওপর নির্ভর করে।",
    ),
    "R-squared and Adjusted R-squared": (
        "R-squared compares fitted residual variation with a mean-only baseline. Adjusted R-squared penalizes added predictors, but neither proves causality or out-of-sample usefulness.",
        "R-squared fitted residual variation-কে mean-only baseline-এর সঙ্গে তুলনা করে। adjusted R-squared অতিরিক্ত predictor penalize করে; কোনোটিই causality বা out-of-sample usefulness প্রমাণ করে না।",
    ),
    "Residual Diagnostics": (
        "Residual diagnostics examine nonlinearity, unequal variance, dependence, unusual observations, and distributional assumptions that may make model estimates or uncertainty misleading.",
        "Residual diagnostic nonlinearity, unequal variance, dependence, unusual observation ও distributional assumption যাচাই করে, যেগুলো estimate বা uncertainty misleading করতে পারে।",
    ),
    "Confidence and Prediction Intervals": (
        "A regression confidence interval targets the mean response at a predictor value; a prediction interval targets a new individual response and is therefore wider.",
        "Regression confidence interval predictor value-এ mean response target করে; prediction interval নতুন individual response target করে এবং তাই বেশি wide হয়।",
    ),
    "Multiple Linear Regression": (
        "Multiple regression estimates conditional associations between an outcome and several predictors while holding included predictors fixed, subject to model and data assumptions.",
        "Multiple regression included predictor fixed রেখে outcome ও একাধিক predictor-এর conditional association estimate করে; ফল model ও data assumption-এর ওপর নির্ভরশীল।",
    ),
    "Multicollinearity and VIF": (
        "Multicollinearity occurs when predictors contain overlapping information, inflating coefficient uncertainty. VIF summarizes how much a coefficient variance is amplified by linear dependence.",
        "Predictor-এ overlapping information থাকলে multicollinearity coefficient uncertainty বাড়ায়। VIF linear dependence-এর কারণে coefficient variance কত গুণ বাড়ে তা সংক্ষেপ করে।",
    ),
    "Logistic Regression": (
        "Logistic regression models the log-odds of a binary outcome as a linear predictor. Coefficients are log-odds changes and exponentiated coefficients are conditional odds ratios.",
        "Logistic regression binary outcome-এর log-odds-কে linear predictor হিসেবে model করে। coefficient log-odds change এবং exponentiated coefficient conditional odds ratio।",
    ),
    "Regularization: Ridge and Lasso": (
        "Ridge and lasso add coefficient penalties to reduce variance and manage high-dimensional predictors. Lasso can set coefficients to zero; ridge usually shrinks without exact selection.",
        "Ridge ও lasso coefficient penalty দিয়ে variance কমায় এবং high-dimensional predictor manage করে। lasso coefficient zero করতে পারে; ridge সাধারণত exact selection ছাড়া shrink করে।",
    ),
    "Model Validation": (
        "Model validation evaluates performance on data not used to fit the model, using resampling or holdout designs and metrics aligned with the real decision problem.",
        "Model validation fitting-এ ব্যবহার না করা data-এ performance মূল্যায়ন করে; resampling বা holdout design এবং real decision problem-aligned metric ব্যবহার করে।",
    ),
    # Analytics
    "Data Cleaning": (
        "Data cleaning standardizes types, categories, units, dates, duplicates, and invalid records while preserving an auditable distinction between raw and transformed data.",
        "Data cleaning type, category, unit, date, duplicate ও invalid record standardize করে এবং raw ও transformed data-এর auditable distinction বজায় রাখে।",
    ),
    "Missing Data": (
        "Missingness can be structural, random, or related to observed or unobserved values. Deletion, imputation, or explicit modeling must match the missing-data mechanism and decision context.",
        "Missingness structural, random অথবা observed/unobserved value-এর সঙ্গে related হতে পারে। deletion, imputation বা explicit modeling missing-data mechanism ও decision context-এর সঙ্গে মিলতে হবে।",
    ),
    "Outlier Treatment": (
        "Outlier treatment begins with investigation. Correction, transformation, robust methods, winsorization, segmentation, or exclusion each answer different data-quality and modeling problems.",
        "Outlier treatment investigation দিয়ে শুরু হয়। correction, transformation, robust method, winsorization, segmentation বা exclusion ভিন্ন data-quality ও modeling problem সমাধান করে।",
    ),
    "Exploratory Data Analysis": (
        "EDA profiles distributions, relationships, missingness, anomalies, and business logic to generate questions and detect data problems before confirmatory analysis.",
        "EDA distribution, relationship, missingness, anomaly ও business logic profile করে; confirmatory analysis-এর আগে question তৈরি ও data problem শনাক্ত করে।",
    ),
    "KPI Design": (
        "A KPI needs a clear business objective, formula, grain, population, time window, owner, target, and guardrail. Stable definitions are essential for comparable reporting.",
        "KPI-এর clear business objective, formula, grain, population, time window, owner, target ও guardrail প্রয়োজন। comparable reporting-এর জন্য stable definition জরুরি।",
    ),
    "Cohort Analysis": (
        "Cohort analysis groups entities by a shared starting event or attribute and compares their behavior over aligned lifecycle periods, separating age effects from calendar effects.",
        "Cohort analysis shared starting event বা attribute অনুযায়ী entity group করে এবং aligned lifecycle period-এ behavior তুলনা করে; age effect ও calendar effect আলাদা করে।",
    ),
    "Funnel Analysis": (
        "Funnel analysis measures progression through ordered stages. Valid funnels require consistent eligibility, event identity, sequence rules, time windows, and deduplication.",
        "Funnel analysis ordered stage-এর progression মাপে। valid funnel-এর জন্য consistent eligibility, event identity, sequence rule, time window ও deduplication প্রয়োজন।",
    ),
    "A/B Testing": (
        "A/B testing randomly assigns eligible units to variants to estimate causal effects under controlled exposure, prespecified outcomes, and appropriate analysis plans.",
        "A/B testing eligible unit-কে randomভাবে variant-এ assign করে controlled exposure, prespecified outcome ও appropriate analysis plan-এর অধীনে causal effect estimate করে।",
    ),
    "Time-series Components": (
        "Time series may contain trend, seasonality, cycles, interventions, and irregular variation. Time order creates dependence that ordinary independent-sample methods may ignore.",
        "Time series-এ trend, seasonality, cycle, intervention ও irregular variation থাকতে পারে। time order dependence তৈরি করে, যা ordinary independent-sample method উপেক্ষা করতে পারে।",
    ),
    "Moving Averages and Smoothing": (
        "Moving averages and exponential smoothing reduce short-term noise to reveal level and trend. Smoothing choices trade responsiveness against stability.",
        "Moving average ও exponential smoothing short-term noise কমিয়ে level ও trend দেখায়। smoothing choice responsiveness ও stability-এর মধ্যে trade-off তৈরি করে।",
    ),
    "Forecast Evaluation": (
        "Forecasts must be evaluated on future-like holdout periods with scale-appropriate metrics, naive baselines, time-aware validation, and checks for bias and interval coverage.",
        "Forecast future-like holdout period-এ scale-appropriate metric, naive baseline, time-aware validation এবং bias ও interval coverage check দিয়ে মূল্যায়ন করতে হয়।",
    ),
    "Data Storytelling": (
        "Data storytelling connects a decision question, credible evidence, visual hierarchy, uncertainty, and a recommended action without hiding limitations or alternative explanations.",
        "Data storytelling decision question, credible evidence, visual hierarchy, uncertainty ও recommended action যুক্ত করে; limitation বা alternative explanation লুকায় না।",
    ),
    # Data science
    "Bootstrap": (
        "The bootstrap repeatedly resamples observed units with replacement to approximate the sampling distribution of a statistic when the empirical sample is a defensible stand-in for the population.",
        "Bootstrap observed unit replacement-সহ বারবার resample করে statistic-এর sampling distribution approximate করে, যখন empirical sample population-এর গ্রহণযোগ্য stand-in।",
    ),
    "Cross-validation": (
        "Cross-validation repeatedly separates training and validation folds to estimate generalization performance and tune models without using the final test set.",
        "Cross-validation training ও validation fold বারবার আলাদা করে generalization performance estimate ও model tune করে; final test set ব্যবহার করে না।",
    ),
    "Bias-Variance Trade-off": (
        "Prediction error can arise from systematic underfitting, sensitivity to training samples, and irreducible noise. Model complexity often reduces bias while increasing variance.",
        "Prediction error systematic underfitting, training sample sensitivity ও irreducible noise থেকে আসে। model complexity বাড়লে সাধারণত bias কমে এবং variance বাড়ে।",
    ),
    "Feature Engineering": (
        "Feature engineering transforms raw variables into representations aligned with the prediction task while preventing target leakage and preserving availability at prediction time.",
        "Feature engineering raw variable-কে prediction task-aligned representation-এ transform করে; target leakage এড়ায় এবং prediction time-এ availability নিশ্চিত করে।",
    ),
    "Scaling and Encoding": (
        "Scaling changes numerical magnitudes; encoding represents categories numerically. Both must be learned from training data and applied consistently to validation and production data.",
        "Scaling numerical magnitude বদলায়; encoding category-কে numericalভাবে represent করে। উভয়টি training data থেকে শিখে validation ও production data-এ consistentভাবে apply করতে হয়।",
    ),
    "Principal Component Analysis": (
        "PCA creates orthogonal linear combinations that capture descending variance. It is sensitive to scaling and does not necessarily preserve predictive or causal meaning.",
        "PCA descending variance capture করা orthogonal linear combination তৈরি করে। এটি scaling-sensitive এবং predictive বা causal meaning নিশ্চিত করে না।",
    ),
    "K-means Clustering": (
        "K-means partitions observations into k groups by minimizing squared distance to centroids. Results depend on scaling, initialization, k, and roughly spherical cluster geometry.",
        "K-means centroid থেকে squared distance কমিয়ে observation-কে k group-এ ভাগ করে। ফল scaling, initialization, k ও প্রায় spherical cluster geometry-এর ওপর নির্ভর করে।",
    ),
    "Hierarchical Clustering and DBSCAN": (
        "Hierarchical clustering builds nested groups from a distance and linkage rule; DBSCAN finds dense regions and labels sparse observations as noise without requiring k in advance.",
        "Hierarchical clustering distance ও linkage rule থেকে nested group তৈরি করে; DBSCAN আগে k না দিয়েই dense region খুঁজে এবং sparse observation-কে noise label দেয়।",
    ),
    "Classification Metrics": (
        "Accuracy, precision, recall, specificity, F1, ROC AUC, and PR AUC answer different questions. Metric choice must reflect class prevalence and error costs.",
        "Accuracy, precision, recall, specificity, F1, ROC AUC ও PR AUC ভিন্ন প্রশ্নের উত্তর দেয়। metric choice class prevalence ও error cost অনুযায়ী হতে হবে।",
    ),
    "Probability Calibration and Thresholds": (
        "Calibration asks whether predicted probabilities match observed frequencies; thresholds convert probabilities to actions and should reflect costs, capacity, and risk tolerance.",
        "Calibration predicted probability observed frequency-এর সঙ্গে মেলে কি না দেখে; threshold probability-কে action-এ রূপ দেয় এবং cost, capacity ও risk tolerance অনুযায়ী হওয়া উচিত।",
    ),
    "Bayesian Inference": (
        "Bayesian inference combines a prior distribution and likelihood to produce a posterior distribution, making assumptions explicit and expressing uncertainty over parameters and predictions.",
        "Bayesian inference prior distribution ও likelihood একত্র করে posterior distribution তৈরি করে; assumption explicit এবং parameter ও prediction uncertainty প্রকাশ করে।",
    ),
    "Causal Inference": (
        "Causal inference estimates outcomes under alternative interventions using designs and assumptions that address confounding, selection, timing, interference, and counterfactual identification.",
        "Causal inference confounding, selection, timing, interference ও counterfactual identification address করা design ও assumption দিয়ে alternative intervention-এর outcome estimate করে।",
    ),
    # Data engineering
    "Data Formats: CSV, JSON and Parquet": (
        "CSV is simple row-oriented text, JSON represents nested structures, and Parquet is a typed columnar format optimized for analytical scans and compression.",
        "CSV simple row-oriented text, JSON nested structure এবং Parquet analytical scan ও compression-এর জন্য optimized typed columnar format।",
    ),
    "Relational Data Modeling": (
        "Relational modeling organizes entities, attributes, keys, and relationships into tables with constraints that preserve identity and referential integrity.",
        "Relational modeling entity, attribute, key ও relationship-কে table-এ সংগঠিত করে এবং constraint দিয়ে identity ও referential integrity বজায় রাখে।",
    ),
    "SQL for Analytics": (
        "Analytical SQL filters, joins, aggregates, windows, and reshapes data at an explicit grain. Correct results require careful handling of join multiplicity, nulls, and time.",
        "Analytical SQL explicit grain-এ filter, join, aggregate, window ও reshape করে। সঠিক ফলের জন্য join multiplicity, null ও time সাবধানে handle করতে হয়।",
    ),
    "Normalization and Denormalization": (
        "Normalization reduces redundancy and update anomalies in transactional models; denormalization duplicates selected data to simplify or accelerate analytical access.",
        "Normalization transactional model-এ redundancy ও update anomaly কমায়; denormalization analytical access সহজ বা দ্রুত করতে selected data duplicate করে।",
    ),
    "ETL and ELT": (
        "ETL transforms before loading into the target; ELT loads raw data first and transforms within the analytical platform. Governance and testing matter more than the acronym alone.",
        "ETL target-এ load করার আগে transform করে; ELT raw data আগে load করে এবং analytical platform-এর ভেতরে transform করে। acronym-এর চেয়ে governance ও testing বেশি গুরুত্বপূর্ণ।",
    ),
    "Batch and Streaming Data": (
        "Batch systems process bounded collections on a schedule; streaming systems process continuing events with explicit event time, ordering, lateness, state, and delivery semantics.",
        "Batch system schedule অনুযায়ী bounded collection process করে; streaming system event time, ordering, lateness, state ও delivery semantic-সহ continuous event process করে।",
    ),
    "Warehouse, Lake and Lakehouse": (
        "Warehouses emphasize governed analytical tables, lakes store flexible files at scale, and lakehouse architectures add transactional and governance capabilities over lake storage.",
        "Warehouse governed analytical table, lake scale-এ flexible file এবং lakehouse lake storage-এর ওপর transactional ও governance capability যোগ করে।",
    ),
    "Dimensional Modeling and Star Schemas": (
        "Dimensional models separate measurable business events in fact tables from descriptive context in dimension tables at a declared grain.",
        "Dimensional model declared grain-এ measurable business event-কে fact table এবং descriptive context-কে dimension table-এ আলাদা করে।",
    ),
    "Data Quality Testing": (
        "Data tests encode expectations for schema, freshness, uniqueness, referential integrity, accepted values, distributions, and business rules, with ownership and incident response.",
        "Data test schema, freshness, uniqueness, referential integrity, accepted value, distribution ও business rule-এর expectation encode করে; ownership ও incident response প্রয়োজন।",
    ),
    "Pipeline Orchestration": (
        "Orchestration coordinates dependencies, schedules, retries, backfills, parameters, observability, and failure handling across data tasks; it does not replace idempotent task design.",
        "Orchestration data task জুড়ে dependency, schedule, retry, backfill, parameter, observability ও failure handling coordinate করে; idempotent task design-এর বিকল্প নয়।",
    ),
    "Data Lineage and Governance": (
        "Lineage traces data origins and transformations; governance defines ownership, access, classification, quality, retention, and acceptable use throughout the data lifecycle.",
        "Lineage data origin ও transformation trace করে; governance data lifecycle জুড়ে ownership, access, classification, quality, retention ও acceptable use নির্ধারণ করে।",
    ),
    "Analytics Engineering and Semantic Layers": (
        "Analytics engineering applies software practices to tested transformations and documented models; a semantic layer centralizes metric logic, dimensions, and access rules.",
        "Analytics engineering tested transformation ও documented model-এ software practice প্রয়োগ করে; semantic layer metric logic, dimension ও access rule centralize করে।",
    ),
    # Advanced
    "Experimental Design": (
        "Experimental design uses randomization, control, replication, and blocking to estimate effects while reducing bias and separating treatment variation from noise.",
        "Experimental design randomization, control, replication ও blocking দিয়ে effect estimate করে; bias কমায় এবং treatment variation-কে noise থেকে আলাদা করে।",
    ),
    "Factorial Designs": (
        "Factorial designs vary two or more factors together to estimate main effects and interactions efficiently, provided treatment combinations and replication are planned appropriately.",
        "Factorial design দুই বা ততোধিক factor একসঙ্গে পরিবর্তন করে main effect ও interaction efficiently estimate করে, যদি treatment combination ও replication সঠিকভাবে পরিকল্পিত হয়।",
    ),
    "Repeated Measures": (
        "Repeated-measures data contain multiple outcomes from the same unit, creating within-unit dependence that requires paired, mixed, generalized estimating, or longitudinal methods.",
        "Repeated-measures data-এ একই unit থেকে multiple outcome থাকে; within-unit dependence-এর জন্য paired, mixed, generalized estimating বা longitudinal method প্রয়োজন।",
    ),
    "Survival Analysis": (
        "Survival analysis models time to an event while handling censoring and time-dependent risk. Ordinary averages can be biased when follow-up is incomplete.",
        "Survival analysis censoring ও time-dependent risk handle করে event পর্যন্ত সময় model করে। follow-up incomplete হলে ordinary average biased হতে পারে।",
    ),
    "Kaplan-Meier Estimation": (
        "The Kaplan–Meier estimator multiplies conditional survival probabilities at observed event times to estimate a stepwise survival curve under non-informative censoring.",
        "Kaplan–Meier estimator observed event time-এ conditional survival probability multiply করে stepwise survival curve estimate করে; non-informative censoring ধরে।",
    ),
    "Cox Proportional Hazards Model": (
        "The Cox model relates covariates to the hazard through proportional hazard ratios without specifying the baseline hazard shape. Proportionality must be assessed.",
        "Cox model baseline hazard shape specify না করে covariate-কে proportional hazard ratio-এর মাধ্যমে hazard-এর সঙ্গে যুক্ত করে। proportionality যাচাই করতে হয়।",
    ),
    "Multivariate Normal Distribution": (
        "A multivariate normal model describes jointly normal variables through a mean vector and covariance matrix, with elliptical contours and normal linear combinations.",
        "Multivariate normal model mean vector ও covariance matrix দিয়ে jointly normal variable বর্ণনা করে; elliptical contour এবং normal linear combination থাকে।",
    ),
    "MANOVA": (
        "MANOVA tests group differences across a vector of correlated outcomes, accounting for their joint covariance structure. Interpretation usually requires follow-up analysis.",
        "MANOVA correlated outcome vector জুড়ে group difference test করে এবং joint covariance structure বিবেচনা করে। interpretation-এর জন্য সাধারণত follow-up analysis প্রয়োজন।",
    ),
    "Factor Analysis": (
        "Factor analysis models correlations among observed variables using fewer latent factors plus unique variation. Factor number, rotation, scale, and identifiability affect interpretation.",
        "Factor analysis observed variable-এর correlation-কে কম সংখ্যক latent factor ও unique variation দিয়ে model করে। factor number, rotation, scale ও identifiability interpretation প্রভাবিত করে।",
    ),
    "Monte Carlo Simulation": (
        "Monte Carlo simulation propagates uncertainty by repeatedly sampling from specified input models and summarizing the resulting output distribution.",
        "Monte Carlo simulation specified input model থেকে বারবার sample নিয়ে uncertainty propagate করে এবং resulting output distribution সংক্ষেপ করে।",
    ),
    "Markov Chains and MCMC": (
        "A Markov chain moves between states using transition probabilities that depend on the current state. MCMC constructs a chain whose stationary distribution targets a difficult probability distribution.",
        "Markov chain current state-এর ওপর নির্ভর transition probability দিয়ে state বদলায়। MCMC এমন chain তৈরি করে যার stationary distribution একটি কঠিন target distribution approximate করে।",
    ),
    "Spatial Statistics": (
        "Spatial statistics analyzes location-linked data where nearby observations may be dependent, requiring attention to coordinate systems, scale, neighborhood definitions, and spatial autocorrelation.",
        "Spatial statistics location-linked data বিশ্লেষণ করে, যেখানে কাছাকাছি observation dependent হতে পারে; coordinate system, scale, neighborhood ও spatial autocorrelation গুরুত্বপূর্ণ।",
    ),
}
