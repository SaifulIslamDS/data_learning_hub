"""Topic-specific lesson enrichment for v1.2.0.

The generator stays static: this module only returns JSON-serialisable content.
English is the primary language and every learner-facing field has a Bangla pair.
"""
from __future__ import annotations

REFERENCES = {
    "foundations": [
        {"label": "OpenStax Introductory Statistics 2e", "url": "https://openstax.org/details/books/introductory-statistics-2e"},
        {"label": "NIST/SEMATECH Engineering Statistics Handbook", "url": "https://www.itl.nist.gov/div898/handbook/"},
    ],
    "descriptive": [
        {"label": "OpenStax Introductory Statistics 2e", "url": "https://openstax.org/details/books/introductory-statistics-2e"},
        {"label": "NIST Exploratory Data Analysis", "url": "https://www.itl.nist.gov/div898/handbook/eda/eda.htm"},
    ],
    "probability": [
        {"label": "OpenStax Introductory Statistics 2e", "url": "https://openstax.org/details/books/introductory-statistics-2e"},
        {"label": "NIST Probability Distributions", "url": "https://www.itl.nist.gov/div898/handbook/eda/section3/eda36.htm"},
    ],
    "inference": [
        {"label": "NIST Process Comparisons", "url": "https://www.itl.nist.gov/div898/handbook/prc/prc.htm"},
        {"label": "OpenStax Introductory Statistics 2e", "url": "https://openstax.org/details/books/introductory-statistics-2e"},
    ],
    "regression": [
        {"label": "NIST Process Modeling", "url": "https://www.itl.nist.gov/div898/handbook/pmd/pmd.htm"},
        {"label": "scikit-learn Model Selection and Evaluation", "url": "https://scikit-learn.org/stable/model_selection.html"},
    ],
    "analytics": [
        {"label": "OpenStax Introductory Business Statistics 2e", "url": "https://openstax.org/details/books/introductory-business-statistics-2e"},
        {"label": "NIST Exploratory Data Analysis", "url": "https://www.itl.nist.gov/div898/handbook/eda/eda.htm"},
    ],
    "data-science": [
        {"label": "scikit-learn User Guide", "url": "https://scikit-learn.org/stable/user_guide.html"},
        {"label": "scikit-learn Model Selection and Evaluation", "url": "https://scikit-learn.org/stable/model_selection.html"},
    ],
    "data-engineering": [
        {"label": "Apache Parquet Documentation", "url": "https://parquet.apache.org/docs/"},
        {"label": "PostgreSQL Documentation", "url": "https://www.postgresql.org/docs/"},
        {"label": "dbt Documentation", "url": "https://docs.getdbt.com/docs/introduction"},
    ],
    "advanced": [
        {"label": "NIST/SEMATECH Engineering Statistics Handbook", "url": "https://www.itl.nist.gov/div898/handbook/"},
        {"label": "scikit-learn User Guide", "url": "https://scikit-learn.org/stable/user_guide.html"},
    ],
}

# label_en, label_bn, context_en, context_bn, learner_question_en, learner_question_bn
SCENARIO_SEEDS = {
    # Foundations
    "Statistics and Data": ("A week of shop sales", "এক সপ্তাহের দোকান বিক্রি", "A small shop records daily sales, product category, quantity and payment method.", "একটি ছোট দোকান প্রতিদিনের বিক্রি, পণ্যের ক্যাটাগরি, পরিমাণ ও payment method রেকর্ড করে।", "Which recorded values are data, and how can statistics turn them into a decision?", "কোন recorded value-গুলো data, এবং statistics কীভাবে এগুলোকে decision-এ রূপ দিতে পারে?"),
    "Population and Sample": ("Customer satisfaction survey", "কাস্টমার সন্তুষ্টি survey", "A company has 12,000 customers but interviews 400 of them.", "একটি প্রতিষ্ঠানের ১২,০০০ customer আছে, কিন্তু ৪০০ জনকে interview করা হয়।", "When can the 400 responses represent all 12,000 customers?", "কখন ৪০০টি response পুরো ১২,০০০ customer-কে প্রতিনিধিত্ব করতে পারে?"),
    "Variables and Observations": ("Student result table", "শিক্ষার্থীর ফলাফল টেবিল", "Each row contains one student and columns contain age, class, attendance and marks.", "প্রতিটি row-তে একজন শিক্ষার্থী এবং column-এ age, class, attendance ও marks আছে।", "What is one observation, what are the variables, and what is the unit of analysis?", "একটি observation কী, variable কোনগুলো, এবং unit of analysis কী?"),
    "Measurement Scales": ("Survey response design", "survey response design", "A survey records district, satisfaction level, temperature and monthly income.", "একটি survey district, satisfaction level, temperature ও monthly income রেকর্ড করে।", "Which arithmetic and comparison operations are meaningful for each variable?", "প্রতিটি variable-এর জন্য কোন arithmetic ও comparison অর্থবহ?"),
    "Categorical and Numerical Data": ("Hospital visit records", "হাসপাতাল visit record", "A clinic records diagnosis group, visit type, patient age and waiting time.", "একটি clinic diagnosis group, visit type, patient age ও waiting time রেকর্ড করে।", "Which variables are categorical, discrete numerical or continuous numerical?", "কোন variable categorical, discrete numerical অথবা continuous numerical?"),
    "Data Collection Methods": ("Measuring delivery service quality", "delivery service quality মাপা", "A delivery company can use customer surveys, GPS logs, transaction records and controlled trials.", "একটি delivery company customer survey, GPS log, transaction record ও controlled trial ব্যবহার করতে পারে।", "Which method answers the question with the least avoidable bias and cost?", "কোন method সবচেয়ে কম avoidable bias ও cost-এ প্রশ্নের উত্তর দেয়?"),
    "Probability and Non-probability Sampling": ("Selecting households", "household নির্বাচন", "A researcher compares random household selection with interviewing people who are easiest to reach.", "একজন researcher random household selection-এর সঙ্গে সহজে পাওয়া মানুষকে interview করার পদ্ধতি তুলনা করেন।", "What can be generalized from each sample and what assumptions are required?", "প্রতিটি sample থেকে কী generalize করা যায় এবং কী assumption দরকার?"),
    "Sampling Bias and Confounding": ("Online training evaluation", "online training evaluation", "Training participants volunteer for an online survey, and more experienced staff are also more likely to complete the course.", "training participant-রা voluntary online survey দেয়, এবং বেশি experienced staff course সম্পন্ন করার সম্ভাবনাও বেশি।", "Is the observed improvement caused by training, selection bias, experience or a mixture?", "দেখা improvement training, selection bias, experience নাকি মিশ্র প্রভাব?"),
    "Data Quality Dimensions": ("Monthly donor report", "মাসিক donor report", "A report has every required row, but several amounts use the wrong currency and some records arrive late.", "একটি report-এ সব required row আছে, কিন্তু কিছু amount ভুল currency-তে এবং কিছু record দেরিতে এসেছে।", "Which quality dimensions fail even though the file is complete?", "file complete হলেও কোন quality dimension ব্যর্থ হয়েছে?"),
    "Frequency Tables": ("Support ticket categories", "support ticket category", "A help desk groups 500 tickets by issue type and resolution status.", "একটি help desk ৫০০ ticket-কে issue type ও resolution status অনুযায়ী group করে।", "Which categories dominate, which are rare, and are any codes unexpected?", "কোন category বেশি, কোনগুলো rare, এবং কোনো code অপ্রত্যাশিত কি না?"),
    "Exploratory Data Analysis Workflow": ("First look at sales data", "sales data-র প্রথম পর্যালোচনা", "An analyst receives a new sales file with unknown missing values, duplicate rows and unusual amounts.", "একজন analyst নতুন sales file পান যেখানে missing value, duplicate row ও unusual amount সম্পর্কে জানা নেই।", "What should be checked before calculating KPIs or building a model?", "KPI calculate বা model বানানোর আগে কী কী যাচাই করা উচিত?"),
    "Reproducible Statistical Workflow": ("Repeatable monthly report", "repeatable monthly report", "A monthly analysis must be regenerated when corrected source files arrive.", "corrected source file এলে একটি monthly analysis আবার generate করতে হয়।", "Can another analyst reproduce the same output from documented inputs and code?", "documented input ও code থেকে অন্য analyst কি একই output reproduce করতে পারবেন?"),
    # Descriptive
    "Mean, Median and Mode": ("Employee salary summary", "employee salary summary", "Most salaries are close together but one executive salary is much larger.", "বেশিরভাগ salary কাছাকাছি, কিন্তু একজন executive-এর salary অনেক বেশি।", "Which measure best describes a typical salary, and why?", "কোন measure typical salary ভালোভাবে বোঝায় এবং কেন?"),
    "Weighted, Geometric and Harmonic Means": ("Grades, growth and speed", "grade, growth ও speed", "A learner combines course grades, annual growth rates and travel speeds from equal distances.", "একজন learner course grade, annual growth rate ও equal distance-এর travel speed একত্র করেন।", "Why do these three situations require different kinds of averages?", "এই তিন পরিস্থিতিতে ভিন্ন average কেন দরকার?"),
    "Quantiles and Percentiles": ("Delivery time service level", "delivery time service level", "A company wants to know the time below which 90% of deliveries finish.", "একটি company জানতে চায় কত সময়ের মধ্যে ৯০% delivery শেষ হয়।", "How does the 90th percentile differ from the average delivery time?", "90th percentile average delivery time থেকে কীভাবে ভিন্ন?"),
    "Range and Interquartile Range": ("Comparing machine consistency", "machine consistency তুলনা", "Two machines have similar centers, but one has occasional extreme measurements.", "দুই machine-এর center কাছাকাছি, কিন্তু একটিতে মাঝে মাঝে extreme measurement হয়।", "Why might IQR describe routine variation better than range?", "কেন IQR routine variation-কে range-এর চেয়ে ভালো বোঝাতে পারে?"),
    "Variance and Standard Deviation": ("Daily demand variability", "দৈনিক demand variability", "Two products have the same average demand but very different day-to-day fluctuation.", "দুই product-এর average demand একই, কিন্তু day-to-day fluctuation ভিন্ন।", "Which product is harder to plan inventory for?", "কোন product-এর inventory plan করা বেশি কঠিন?"),
    "Coefficient of Variation": ("Comparing relative risk", "relative risk তুলনা", "Two products have very different average sales and standard deviations.", "দুই product-এর average sales ও standard deviation অনেক ভিন্ন।", "How can variability be compared relative to each product's scale?", "প্রতিটি product-এর scale অনুযায়ী variability কীভাবে তুলনা করা যায়?"),
    "Skewness": ("Household income distribution", "household income distribution", "Most households have moderate income while a few have very high income.", "বেশিরভাগ household-এর income মাঝারি, কিন্তু অল্প কয়েকটির খুব বেশি।", "What does a long right tail imply for the mean and median?", "দীর্ঘ right tail mean ও median সম্পর্কে কী বোঝায়?"),
    "Kurtosis": ("Rare extreme losses", "দুর্লভ extreme loss", "Two return series look similarly centered, but one produces extreme losses more often.", "দুই return series-এর center কাছাকাছি, কিন্তু একটিতে extreme loss বেশি ঘটে।", "How can tail behaviour matter even when the means and variances look similar?", "mean ও variance কাছাকাছি হলেও tail behaviour কেন গুরুত্বপূর্ণ?"),
    "Outlier Detection": ("Unusual invoice amount", "অস্বাভাবিক invoice amount", "One invoice is ten times larger than the usual range.", "একটি invoice সাধারণ range-এর চেয়ে দশ গুণ বড়।", "Is it a data error, a valid large purchase, or evidence of a different process?", "এটি data error, valid large purchase নাকি ভিন্ন process-এর evidence?"),
    "Histograms": ("Call handling times", "call handling time", "A call center plots thousands of handling times using different bin widths.", "একটি call center বিভিন্ন bin width ব্যবহার করে হাজারো handling time plot করে।", "Which distribution features remain stable and which are created by bin choices?", "কোন distribution feature স্থিতিশীল এবং কোনটি bin choice-এর কারণে তৈরি?"),
    "Box Plots": ("Branch performance comparison", "branch performance তুলনা", "A retailer compares monthly sales distributions across six branches.", "একটি retailer ছয় branch-এর monthly sales distribution তুলনা করে।", "Which branches differ in median, spread and potential outliers?", "কোন branch median, spread ও potential outlier-এ ভিন্ন?"),
    "Scatter, Line and Bar Charts": ("Choosing the right visual", "সঠিক visual নির্বাচন", "An analyst must show advertising versus sales, monthly revenue, and sales by category.", "একজন analyst advertising বনাম sales, monthly revenue এবং category অনুযায়ী sales দেখাতে চান।", "Which chart matches each analytical question?", "প্রতিটি analytical question-এর জন্য কোন chart উপযুক্ত?"),
    # Probability
    "Probability Rules": ("Quality inspection outcomes", "quality inspection outcome", "A garment can have a stitching defect, a shade defect, both, or neither.", "একটি garment-এ stitching defect, shade defect, দুটিই অথবা কোনোটিই না থাকতে পারে।", "How are union, intersection and complement probabilities calculated?", "union, intersection ও complement probability কীভাবে হিসাব হয়?"),
    "Conditional Probability": ("Late delivery after rain", "বৃষ্টির পর late delivery", "A courier compares late-delivery rates on rainy and non-rainy days.", "একটি courier rainy ও non-rainy day-এ late-delivery rate তুলনা করে।", "How does knowing that it rained change the probability of delay?", "বৃষ্টি হয়েছে জানা delay-এর probability কীভাবে বদলায়?"),
    "Bayes' Theorem": ("Screening test result", "screening test result", "A screening test is accurate but the condition is rare.", "একটি screening test accurate, কিন্তু condition rare।", "What is the probability of actually having the condition after a positive result?", "positive result-এর পর condition সত্যিই থাকার probability কত?"),
    "Random Variables": ("Daily order count", "দৈনিক order count", "The number of orders tomorrow is unknown but possible values and probabilities can be described.", "আগামীকালের order count অজানা, কিন্তু possible value ও probability বর্ণনা করা যায়।", "How do outcomes become numerical variables suitable for analysis?", "outcome কীভাবে analysis-এর জন্য numerical variable হয়?"),
    "Expected Value and Variance": ("Warranty cost planning", "warranty cost planning", "A company faces several possible warranty costs with different probabilities.", "একটি company বিভিন্ন probability-সহ কয়েকটি possible warranty cost-এর মুখোমুখি।", "What is the long-run average cost and how uncertain is a single period?", "long-run average cost কত এবং একটি period কতটা uncertain?"),
    "Bernoulli and Binomial Distributions": ("Email conversion experiment", "email conversion experiment", "Each recipient either converts or does not, and the analyst counts conversions among 200 recipients.", "প্রতিটি recipient convert করে অথবা করে না, এবং analyst ২০০ recipient-এর conversion count করেন।", "When is a binomial model reasonable for the total conversions?", "total conversion-এর জন্য binomial model কখন যুক্তিসঙ্গত?"),
    "Poisson Distribution": ("Calls per minute", "প্রতি মিনিটে call", "A service desk counts incoming calls during equal one-minute intervals.", "একটি service desk সমান এক মিনিট interval-এ incoming call count করে।", "Can a stable-rate count model describe the observed call volume?", "stable-rate count model কি observed call volume বর্ণনা করতে পারে?"),
    "Uniform Distribution": ("Random arrival within an interval", "একটি interval-এ random arrival", "A simulated arrival time is equally likely anywhere between 0 and 10 minutes.", "একটি simulated arrival time ০ থেকে ১০ মিনিটের যেকোনো স্থানে equally likely।", "What probabilities correspond to subinterval lengths?", "subinterval length-এর সঙ্গে probability কীভাবে সম্পর্কিত?"),
    "Normal Distribution": ("Manufacturing measurements", "manufacturing measurement", "A stable process produces measurements clustered around a target with roughly symmetric variation.", "একটি stable process target-এর চারপাশে roughly symmetric variation-সহ measurement তৈরি করে।", "How can standardized distance from the mean estimate tail probabilities?", "mean থেকে standardized distance কীভাবে tail probability estimate করে?"),
    "Exponential Distribution": ("Waiting time between events", "event-এর মধ্যবর্তী waiting time", "A system receives events at an approximately constant average rate.", "একটি system প্রায় constant average rate-এ event পায়।", "What model describes time until the next event under a memoryless process?", "memoryless process-এ next event পর্যন্ত সময় কোন model বর্ণনা করে?"),
    "Sampling Distributions": ("Repeated sample averages", "repeated sample average", "Many random samples of the same size are drawn from one population.", "একটি population থেকে একই size-এর অনেক random sample নেওয়া হয়।", "How much does the sample mean vary from sample to sample?", "sample mean sample-to-sample কতটা বদলায়?"),
    "Central Limit Theorem": ("Average transaction value", "average transaction value", "Individual transactions are skewed, but averages from increasingly large samples are compared.", "individual transaction skewed, কিন্তু বড় হতে থাকা sample-এর average তুলনা করা হয়।", "When and why does the distribution of sample means become approximately normal?", "কখন এবং কেন sample mean-এর distribution approximately normal হয়?"),
    # Inference
    "Point Estimation": ("Estimating average waiting time", "average waiting time estimate", "A clinic uses one sample to estimate the population mean waiting time.", "একটি clinic একটি sample ব্যবহার করে population mean waiting time estimate করে।", "What makes an estimator precise, unbiased or robust?", "কোন বিষয় estimator-কে precise, unbiased বা robust করে?"),
    "Confidence Intervals": ("Customer satisfaction estimate", "customer satisfaction estimate", "A sample mean is reported with a range reflecting sampling uncertainty.", "একটি sample mean sampling uncertainty-সহ একটি range দিয়ে report করা হয়।", "What does a 95% confidence procedure guarantee over repeated samples?", "repeated sample-এ 95% confidence procedure কী guarantee করে?"),
    "Hypothesis Testing Framework": ("Checking a filling machine", "filling machine যাচাই", "A factory asks whether the average fill differs from the target value.", "একটি factory average fill target value থেকে ভিন্ন কি না জানতে চায়।", "What null model, statistic, evidence rule and alternative should be specified?", "কোন null model, statistic, evidence rule ও alternative specify করা উচিত?"),
    "p-values and Significance Levels": ("Interpreting a test result", "test result ব্যাখ্যা", "A test produces p = 0.03 with alpha = 0.05.", "একটি test-এ p = 0.03 এবং alpha = 0.05 পাওয়া যায়।", "What can be concluded, and what cannot be concluded, from this comparison?", "এই comparison থেকে কী conclusion নেওয়া যায় এবং কী যায় না?"),
    "Type I, Type II Errors and Power": ("Detecting a harmful defect rate", "ক্ষতিকর defect rate detect করা", "A quality team balances false alarms against missing a real increase in defects.", "একটি quality team false alarm ও প্রকৃত defect increase miss করার মধ্যে balance করে।", "How do effect size, sample size, alpha and variability affect power?", "effect size, sample size, alpha ও variability power-কে কীভাবে প্রভাবিত করে?"),
    "One-sample z and t Tests": ("Average delivery promise", "average delivery promise", "A company compares sample delivery time with a promised population target.", "একটি company sample delivery time-কে promised population target-এর সঙ্গে তুলনা করে।", "When is a t test appropriate and when is a z approximation justified?", "কখন t test উপযুক্ত এবং কখন z approximation justified?"),
    "Two-sample t Test": ("Comparing two training programs", "দুই training program তুলনা", "Independent groups receive two different training programs and their scores are compared.", "independent group দুইটি ভিন্ন training program পায় এবং score তুলনা করা হয়।", "How large is the mean difference relative to its uncertainty?", "mean difference uncertainty-এর তুলনায় কত বড়?"),
    "Paired t Test": ("Before-and-after blood pressure", "before-and-after blood pressure", "The same patients are measured before and after an intervention.", "একই patient-কে intervention-এর আগে ও পরে measure করা হয়।", "Why should within-person differences be analyzed instead of treating measurements as independent?", "measurement-কে independent না ধরে within-person difference কেন analyze করা উচিত?"),
    "Tests for Proportions": ("Defect-rate comparison", "defect-rate comparison", "Two production lines produce pass/fail outcomes.", "দুই production line pass/fail outcome তৈরি করে।", "Is the observed difference in proportions larger than expected from sampling variation?", "observed proportion difference sampling variation-এর চেয়ে বড় কি না?"),
    "Chi-square Tests": ("Device type and conversion", "device type ও conversion", "A table records conversion counts across mobile, tablet and desktop users.", "একটি table mobile, tablet ও desktop user-এর conversion count রেকর্ড করে।", "Are device type and conversion independent in the sampled data?", "sampled data-তে device type ও conversion independent কি না?"),
    "Analysis of Variance": ("Comparing four teaching methods", "চার teaching method তুলনা", "Four independent groups have different average exam scores.", "চার independent group-এর average exam score ভিন্ন।", "Is between-group variation large relative to within-group variation?", "between-group variation within-group variation-এর তুলনায় বড় কি না?"),
    "Nonparametric Tests": ("Ordinal satisfaction scores", "ordinal satisfaction score", "Small groups provide highly skewed or ordinal ratings.", "ছোট group highly skewed অথবা ordinal rating দেয়।", "Which rank-based comparison matches the design and target question?", "design ও target question-এর সঙ্গে কোন rank-based comparison মেলে?"),
    # Regression
    "Covariance and Correlation": ("Advertising and sales", "advertising ও sales", "Monthly advertising spend and sales move together to varying degrees.", "monthly advertising spend ও sales বিভিন্ন মাত্রায় একসঙ্গে বদলায়।", "How can joint variation be summarized without confusing association with causation?", "association-কে causation না ধরে joint variation কীভাবে summarize করা যায়?"),
    "Pearson and Spearman Correlation": ("Relationship with an extreme value", "extreme value-সহ relationship", "Two variables have a monotonic relationship but one observation is extreme.", "দুই variable-এর monotonic relationship আছে, কিন্তু একটি observation extreme।", "How do value-based and rank-based correlations respond differently?", "value-based ও rank-based correlation কীভাবে ভিন্ন response দেয়?"),
    "Simple Linear Regression": ("Predicting sales from advertising", "advertising থেকে sales predict", "An analyst fits a straight line between advertising spend and sales.", "একজন analyst advertising spend ও sales-এর মধ্যে straight line fit করেন।", "What do the slope, intercept, residuals and prediction range mean?", "slope, intercept, residual ও prediction range কী বোঝায়?"),
    "Ordinary Least Squares": ("Choosing the best-fitting line", "best-fitting line নির্বাচন", "Many possible lines could describe the same scatter plot.", "একই scatter plot অনেক possible line দিয়ে বর্ণনা করা যায়।", "Why does minimizing squared residuals identify the OLS coefficients?", "squared residual minimize করলে OLS coefficient কেন পাওয়া যায়?"),
    "R-squared and Adjusted R-squared": ("Adding more predictors", "আরও predictor যোগ", "A model's R-squared increases after adding weak predictors.", "weak predictor যোগ করার পর model-এর R-squared বাড়ে।", "Does the larger value mean the model predicts new data better?", "বড় value কি new data ভালো predict করার অর্থ?"),
    "Residual Diagnostics": ("Checking model failures", "model failure যাচাই", "A fitted regression shows curved residuals and increasing spread.", "একটি fitted regression-এ curved residual ও increasing spread দেখা যায়।", "Which assumptions are questionable and what changes might be needed?", "কোন assumption questionable এবং কী change দরকার হতে পারে?"),
    "Confidence and Prediction Intervals": ("Average response versus one future case", "average response বনাম future case", "A model estimates the mean sales response and predicts one future month's sales.", "একটি model mean sales response estimate করে এবং একটি future month-এর sales predict করে।", "Why is a prediction interval usually wider than a confidence interval for the mean?", "prediction interval mean-এর confidence interval-এর চেয়ে সাধারণত wider কেন?"),
    "Multiple Linear Regression": ("Sales with several drivers", "একাধিক driver-সহ sales", "Sales are modeled using price, advertising, season and store size.", "sales-কে price, advertising, season ও store size দিয়ে model করা হয়।", "How should each coefficient be interpreted while holding other predictors constant?", "অন্য predictor constant ধরে প্রতিটি coefficient কীভাবে interpret করা উচিত?"),
    "Multicollinearity and VIF": ("Overlapping predictors", "overlapping predictor", "Advertising spend and campaign impressions carry very similar information.", "advertising spend ও campaign impression খুব similar information বহন করে।", "How can redundancy inflate uncertainty without necessarily harming prediction?", "redundancy কীভাবে uncertainty বাড়ায় কিন্তু prediction সবসময় নষ্ট করে না?"),
    "Logistic Regression": ("Predicting churn", "churn predict", "Customer attributes are used to estimate the probability of churn.", "customer attribute ব্যবহার করে churn probability estimate করা হয়।", "How do log-odds coefficients translate into probability changes and classification decisions?", "log-odds coefficient probability change ও classification decision-এ কীভাবে translate হয়?"),
    "Regularization: Ridge and Lasso": ("Many correlated features", "অনেক correlated feature", "A model has many predictors relative to the available observations.", "available observation-এর তুলনায় model-এ অনেক predictor আছে।", "How do coefficient penalties trade bias for stability and feature selection?", "coefficient penalty bias-এর বিনিময়ে stability ও feature selection কীভাবে দেয়?"),
    "Model Validation": ("Estimating future performance", "future performance estimate", "A model performs well on the same data used for fitting.", "একটি model fitting-এ ব্যবহৃত একই data-তে ভালো perform করে।", "What evaluation design estimates performance on genuinely unseen data?", "কোন evaluation design genuinely unseen data-তে performance estimate করে?"),
    # Analytics
    "Data Cleaning": ("Messy customer file", "messy customer file", "Names, dates, categories and amounts use inconsistent formats and duplicate records exist.", "name, date, category ও amount inconsistent format-এ আছে এবং duplicate record আছে।", "Which cleaning rules are necessary, documented and reversible?", "কোন cleaning rule প্রয়োজনীয়, documented ও reversible?"),
    "Missing Data": ("Incomplete survey answers", "অসম্পূর্ণ survey answer", "Some respondents skip income questions and missingness differs by age group.", "কিছু respondent income question skip করে এবং age group অনুযায়ী missingness ভিন্ন।", "Is deletion, imputation or explicit missing-category treatment defensible?", "deletion, imputation নাকি explicit missing-category treatment defensible?"),
    "Outlier Treatment": ("Extreme transaction values", "extreme transaction value", "Several very large transactions may be errors, fraud or valid enterprise purchases.", "কিছু খুব বড় transaction error, fraud অথবা valid enterprise purchase হতে পারে।", "Should values be corrected, segmented, transformed, winsorized or retained?", "value correct, segment, transform, winsorize নাকি retain করা উচিত?"),
    "Exploratory Data Analysis": ("Understanding a new dataset", "নতুন dataset বোঝা", "An analyst must learn the dataset's shape, quality, distributions and relationships before modeling.", "modeling-এর আগে analyst-কে dataset-এর shape, quality, distribution ও relationship বুঝতে হয়।", "What evidence should be collected before choosing a formal method?", "formal method বাছাইয়ের আগে কী evidence সংগ্রহ করা উচিত?"),
    "KPI Design": ("Defining customer retention", "customer retention define করা", "Different teams calculate retention using different populations, windows and exclusions.", "ভিন্ন team ভিন্ন population, window ও exclusion দিয়ে retention calculate করে।", "What precise definition makes the KPI comparable and decision-useful?", "কোন precise definition KPI-কে comparable ও decision-useful করে?"),
    "Cohort Analysis": ("Retention by signup month", "signup month অনুযায়ী retention", "Users are grouped by the month they first joined and followed over time.", "user-কে first join month অনুযায়ী group করে সময়ের সঙ্গে follow করা হয়।", "How do lifecycle differences appear after aligning users by cohort age?", "cohort age অনুযায়ী align করলে lifecycle difference কীভাবে দেখা যায়?"),
    "Funnel Analysis": ("Checkout conversion funnel", "checkout conversion funnel", "Visitors move through product view, cart, checkout and purchase stages.", "visitor product view, cart, checkout ও purchase stage দিয়ে যায়।", "Where is the largest meaningful drop-off and how should denominator rules be defined?", "সবচেয়ে বড় meaningful drop-off কোথায় এবং denominator rule কীভাবে define হবে?"),
    "A/B Testing": ("New landing page", "নতুন landing page", "Visitors are randomly assigned to two page versions and conversion is measured.", "visitor-কে randomভাবে দুই page version-এ assign করে conversion মাপা হয়।", "Is the observed lift statistically and practically important under the planned design?", "planned design-এ observed lift statistically ও practically important কি না?"),
    "Time-series Components": ("Monthly sales pattern", "monthly sales pattern", "Sales contain trend, recurring seasonal peaks and irregular shocks.", "sales-এ trend, recurring seasonal peak ও irregular shock আছে।", "Which components should be separated before forecasting?", "forecasting-এর আগে কোন component আলাদা করা উচিত?"),
    "Moving Averages and Smoothing": ("Reducing weekly noise", "weekly noise কমানো", "Daily demand is noisy but the business needs a clearer short-term signal.", "daily demand noisy, কিন্তু business-এর clearer short-term signal দরকার।", "How does the smoothing window trade responsiveness for stability?", "smoothing window responsiveness ও stability-এর মধ্যে কী trade-off করে?"),
    "Forecast Evaluation": ("Choosing a demand forecast", "demand forecast নির্বাচন", "Several models are compared on future periods not used for fitting.", "কয়েকটি model fitting-এ ব্যবহৃত নয় এমন future period-এ তুলনা করা হয়।", "Which metric and backtesting design match the business cost of errors?", "কোন metric ও backtesting design business error cost-এর সঙ্গে মেলে?"),
    "Data Storytelling": ("Executive performance review", "executive performance review", "An analyst must explain a KPI change, its drivers, uncertainty and recommended action.", "একজন analyst KPI change, driver, uncertainty ও recommended action ব্যাখ্যা করেন।", "How can evidence be structured without hiding limitations or overstating causality?", "limitation লুকানো বা causality overstating না করে evidence কীভাবে structure করা যায়?"),
    # Data science
    "Bootstrap": ("Uncertain median estimate", "uncertain median estimate", "A sample median has no convenient simple standard-error formula for the dataset.", "dataset-এর sample median-এর convenient simple standard-error formula নেই।", "How can resampling approximate the estimator's sampling distribution?", "resampling কীভাবে estimator-এর sampling distribution approximate করে?"),
    "Cross-validation": ("Comparing predictive models", "predictive model তুলনা", "Several models must be compared without using the test set repeatedly.", "test set বারবার ব্যবহার না করে কয়েকটি model তুলনা করতে হয়।", "How can repeated training and validation splits estimate generalization?", "repeated training ও validation split generalization কীভাবে estimate করে?"),
    "Bias-Variance Trade-off": ("Simple versus flexible model", "simple বনাম flexible model", "A simple model underfits while a highly flexible model changes greatly across samples.", "একটি simple model underfit করে, আর highly flexible model sample অনুযায়ী অনেক বদলায়।", "How should complexity be chosen to minimize expected prediction error?", "expected prediction error minimize করতে complexity কীভাবে বাছাই করা উচিত?"),
    "Feature Engineering": ("Turning raw timestamps into signals", "raw timestamp থেকে signal", "A model receives transaction timestamps, text categories and historical behaviour.", "একটি model transaction timestamp, text category ও historical behaviour পায়।", "Which transformations encode useful information without leaking the future?", "কোন transformation future leak না করে useful information encode করে?"),
    "Scaling and Encoding": ("Preparing mixed features", "mixed feature প্রস্তুত", "A dataset contains income, age, city and product category for a distance-based model.", "একটি dataset distance-based model-এর জন্য income, age, city ও product category ধারণ করে।", "Which variables require scaling or encoding, and which transformations must be learned only from training data?", "কোন variable scaling বা encoding চায় এবং কোন transformation শুধু training data থেকে শেখা উচিত?"),
    "Principal Component Analysis": ("Compressing correlated measurements", "correlated measurement compress করা", "Dozens of correlated sensor measurements are difficult to visualize and model.", "অনেক correlated sensor measurement visualize ও model করা কঠিন।", "Can orthogonal components preserve most variation with fewer dimensions?", "কম dimension-এ orthogonal component কি অধিকাংশ variation preserve করতে পারে?"),
    "K-means Clustering": ("Customer segmentation", "customer segmentation", "Customers are represented by scaled behavioural features and grouped into k clusters.", "customer-কে scaled behavioural feature দিয়ে represent করে k cluster-এ group করা হয়।", "Are spherical distance-based groups meaningful and stable for this data?", "এই data-তে spherical distance-based group meaningful ও stable কি না?"),
    "Hierarchical Clustering and DBSCAN": ("Irregular customer groups", "irregular customer group", "The data may contain nested groups, irregular shapes and isolated noise points.", "data-তে nested group, irregular shape ও isolated noise point থাকতে পারে।", "Which clustering approach matches the geometry and noise structure?", "কোন clustering approach geometry ও noise structure-এর সঙ্গে মেলে?"),
    "Classification Metrics": ("Fraud detection", "fraud detection", "Fraud is rare and false negatives are much more costly than false positives.", "fraud rare এবং false negative false positive-এর চেয়ে অনেক costly।", "Which metrics reflect class imbalance and the real decision cost?", "কোন metric class imbalance ও real decision cost reflect করে?"),
    "Probability Calibration and Thresholds": ("Risk score decisions", "risk score decision", "A model ranks customers well but predicted probabilities are too high.", "একটি model customer rank ভালো করে, কিন্তু predicted probability বেশি।", "How can probability calibration and threshold choice be evaluated separately?", "probability calibration ও threshold choice আলাদাভাবে কীভাবে evaluate করা যায়?"),
    "Bayesian Inference": ("Updating defect-rate belief", "defect-rate belief update", "A quality team combines prior knowledge with new inspection results.", "একটি quality team prior knowledge-এর সঙ্গে new inspection result combine করে।", "How does the posterior balance prior information and likelihood evidence?", "posterior prior information ও likelihood evidence কীভাবে balance করে?"),
    "Causal Inference": ("Training impact without randomization", "randomization ছাড়া training impact", "Employees who choose training differ from those who do not.", "training বেছে নেওয়া employee অন্যদের থেকে ভিন্ন।", "What assumptions or design strategies are needed to estimate a causal effect?", "causal effect estimate করতে কোন assumption বা design strategy দরকার?"),
    # Data engineering
    "Data Formats: CSV, JSON and Parquet": ("Choosing a storage format", "storage format নির্বাচন", "An analytics pipeline handles flat extracts, nested events and large columnar tables.", "একটি analytics pipeline flat extract, nested event ও বড় columnar table handle করে।", "Which format best matches structure, interoperability, compression and query pattern?", "কোন format structure, interoperability, compression ও query pattern-এর সঙ্গে সবচেয়ে ভালো মেলে?"),
    "Relational Data Modeling": ("Customers, orders and products", "customer, order ও product", "A transactional system must connect customers, orders, order lines and products without ambiguity.", "একটি transactional system customer, order, order line ও product-কে ambiguity ছাড়া connect করে।", "What entities, keys and relationships preserve business meaning?", "কোন entity, key ও relationship business meaning preserve করে?"),
    "SQL for Analytics": ("Monthly revenue by segment", "segment অনুযায়ী monthly revenue", "An analyst must filter, join, aggregate and window transaction data.", "একজন analyst transaction data filter, join, aggregate ও window করেন।", "How can SQL express the metric grain and avoid double counting?", "SQL কীভাবে metric grain প্রকাশ করে এবং double counting এড়ায়?"),
    "Normalization and Denormalization": ("Operational versus analytical tables", "operational বনাম analytical table", "A normalized order system is reliable for updates but cumbersome for repeated reporting queries.", "normalized order system update-এর জন্য reliable, কিন্তু repeated reporting query-তে cumbersome।", "Where should redundancy be reduced, and where can controlled duplication improve analysis?", "কোথায় redundancy কমানো উচিত এবং কোথায় controlled duplication analysis উন্নত করে?"),
    "ETL and ELT": ("Building a governed transformation flow", "governed transformation flow", "Raw files must become tested analytical tables in a warehouse.", "raw file-কে warehouse-এ tested analytical table করতে হয়।", "Should transformation occur before or after loading, and how will quality be verified?", "transformation load-এর আগে নাকি পরে হবে এবং quality কীভাবে verify হবে?"),
    "Batch and Streaming Data": ("Daily report and live alerts", "daily report ও live alert", "The same platform needs a nightly summary and near-real-time fraud alerts.", "একই platform-এর nightly summary ও near-real-time fraud alert দরকার।", "Which latency, ordering and delivery guarantees are required for each workload?", "প্রতিটি workload-এর জন্য কোন latency, ordering ও delivery guarantee দরকার?"),
    "Warehouse, Lake and Lakehouse": ("Enterprise analytics storage", "enterprise analytics storage", "An organization stores governed BI tables, raw files, machine-learning features and large histories.", "একটি organization governed BI table, raw file, machine-learning feature ও বড় history store করে।", "Which architecture balances flexibility, governance, performance and cost?", "কোন architecture flexibility, governance, performance ও cost balance করে?"),
    "Dimensional Modeling and Star Schemas": ("Sales reporting model", "sales reporting model", "Business users need consistent sales measures sliced by date, product, customer and region.", "business user date, product, customer ও region অনুযায়ী consistent sales measure চান।", "What fact-table grain and dimensions support reliable analysis?", "কোন fact-table grain ও dimension reliable analysis support করে?"),
    "Data Quality Testing": ("Preventing broken dashboards", "broken dashboard প্রতিরোধ", "A dashboard depends on fresh, unique orders with valid statuses and customer keys.", "একটি dashboard fresh, unique order, valid status ও customer key-এর ওপর নির্ভর করে।", "Which automated tests detect failures before users see incorrect metrics?", "user incorrect metric দেখার আগে কোন automated test failure detect করে?"),
    "Pipeline Orchestration": ("Coordinating dependent jobs", "dependent job coordinate", "Extraction, transformation, testing and publishing jobs have dependencies and may fail.", "extraction, transformation, testing ও publishing job-এর dependency আছে এবং fail করতে পারে।", "How should schedules, retries, backfills and alerts be coordinated safely?", "schedule, retry, backfill ও alert safely কীভাবে coordinate করা উচিত?"),
    "Data Lineage and Governance": ("Tracing a board metric", "board metric trace করা", "Leadership asks where a reported metric came from and who may access its source data.", "leadership জানতে চান reported metric কোথা থেকে এসেছে এবং source data কে access করতে পারে।", "Can the organization trace transformations, ownership, classification and retention rules?", "organization কি transformation, ownership, classification ও retention rule trace করতে পারে?"),
    "Analytics Engineering and Semantic Layers": ("One definition of revenue", "revenue-এর একটি definition", "Different dashboards calculate revenue differently across teams.", "ভিন্ন dashboard ও team revenue ভিন্নভাবে calculate করে।", "How can tested models and centralized metric logic create consistent self-service analytics?", "tested model ও centralized metric logic consistent self-service analytics কীভাবে তৈরি করে?"),
    # Advanced
    "Experimental Design": ("Testing a process change", "process change test", "A factory compares a new method with a control while controlling shift and machine differences.", "একটি factory shift ও machine difference control করে new method-কে control-এর সঙ্গে তুলনা করে।", "How do randomization, replication and blocking support an unbiased effect estimate?", "randomization, replication ও blocking unbiased effect estimate কীভাবে support করে?"),
    "Factorial Designs": ("Temperature and pressure experiment", "temperature ও pressure experiment", "A process outcome may depend on two settings and their interaction.", "একটি process outcome দুই setting ও তাদের interaction-এর ওপর নির্ভর করতে পারে।", "How can all factor combinations estimate main effects and interactions efficiently?", "সব factor combination main effect ও interaction efficiently কীভাবে estimate করে?"),
    "Repeated Measures": ("Monthly measurements per patient", "প্রতি patient-এর monthly measurement", "Each patient contributes several correlated measurements over time.", "প্রতিটি patient সময়ের সঙ্গে কয়েকটি correlated measurement দেয়।", "Which model accounts for within-person dependence and changing time effects?", "কোন model within-person dependence ও changing time effect account করে?"),
    "Survival Analysis": ("Time until customer churn", "customer churn পর্যন্ত সময়", "Some customers churn during observation while others remain active when follow-up ends.", "কিছু customer observation-এর মধ্যে churn করে, অন্যরা follow-up শেষে active থাকে।", "How can event times be analyzed without treating censored observations as complete failures?", "censored observation-কে complete failure না ধরে event time কীভাবে analyze করা যায়?"),
    "Kaplan-Meier Estimation": ("Comparing retention curves", "retention curve তুলনা", "Two customer groups are followed for different lengths of time with censoring.", "দুই customer group-কে censoring-সহ ভিন্ন সময় follow করা হয়।", "How is a stepwise survival probability estimated at each event time?", "প্রতিটি event time-এ stepwise survival probability কীভাবে estimate হয়?"),
    "Cox Proportional Hazards Model": ("Churn risk with covariates", "covariate-সহ churn risk", "Customer age, plan and usage are related to time until churn.", "customer age, plan ও usage churn পর্যন্ত সময়ের সঙ্গে related।", "How are hazard ratios interpreted and how is proportionality checked?", "hazard ratio কীভাবে interpret এবং proportionality কীভাবে check করা হয়?"),
    "Multivariate Normal Distribution": ("Joint sensor measurements", "joint sensor measurement", "Several correlated sensor variables are modeled together.", "কয়েকটি correlated sensor variable একসঙ্গে model করা হয়।", "How do the mean vector and covariance matrix determine joint elliptical variation?", "mean vector ও covariance matrix joint elliptical variation কীভাবে নির্ধারণ করে?"),
    "MANOVA": ("Multiple student outcomes", "multiple student outcome", "Teaching methods are compared on mathematics, language and science scores together.", "teaching method-কে mathematics, language ও science score একসঙ্গে দিয়ে তুলনা করা হয়।", "Is there a group difference in the joint outcome profile?", "joint outcome profile-এ group difference আছে কি না?"),
    "Factor Analysis": ("Finding latent survey dimensions", "latent survey dimension খোঁজা", "Many survey questions may reflect a smaller set of unobserved constructs.", "অনেক survey question কম সংখ্যক unobserved construct reflect করতে পারে।", "Can shared correlations be explained by interpretable latent factors?", "shared correlation কি interpretable latent factor দিয়ে explain করা যায়?"),
    "Monte Carlo Simulation": ("Project cost uncertainty", "project cost uncertainty", "Cost, duration and demand inputs are uncertain and interact in a financial outcome.", "cost, duration ও demand input uncertain এবং financial outcome-এ interact করে।", "What output distribution appears after repeatedly sampling credible input models?", "credible input model বারবার sample করলে কী output distribution পাওয়া যায়?"),
    "Markov Chains and MCMC": ("Customer state transitions", "customer state transition", "Customers move among active, dormant and churned states over time.", "customer সময়ের সঙ্গে active, dormant ও churned state-এ move করে।", "How do transition probabilities describe state evolution, and when is MCMC needed for inference?", "transition probability state evolution কীভাবে describe করে এবং inference-এ MCMC কখন দরকার?"),
    "Spatial Statistics": ("Disease rates by location", "location অনুযায়ী disease rate", "Nearby areas may have similar risk because geography creates dependence.", "geography dependence তৈরি করায় nearby area-এর risk similar হতে পারে।", "How should spatial autocorrelation, scale and neighborhood definitions change the analysis?", "spatial autocorrelation, scale ও neighborhood definition analysis কীভাবে বদলায়?"),
}

CUSTOM_CONCEPTS = {
    "Statistics and Data": [
        ("Data", "ডেটা", "Recorded facts, measurements, labels or observations about people, objects, processes or events.", "মানুষ, বস্তু, process বা event সম্পর্কে recorded fact, measurement, label অথবা observation।"),
        ("Statistics", "পরিসংখ্যান", "Methods for collecting, organizing, summarizing, analysing and interpreting data while accounting for uncertainty.", "uncertainty বিবেচনায় data collect, organize, summarize, analyse ও interpret করার method।"),
        ("Descriptive statistics", "বর্ণনামূলক পরিসংখ্যান", "Methods that describe the data you observed, such as tables, charts, averages and measures of spread.", "observed data-কে table, chart, average ও spread measure দিয়ে describe করার method।"),
        ("Inferential statistics", "অনুমানমূলক পরিসংখ্যান", "Methods that use a sample to estimate, compare or test claims about a wider population.", "sample ব্যবহার করে wider population সম্পর্কে estimate, comparison বা claim test করার method।"),
    ],
    "Population and Sample": [
        ("Population", "পপুলেশন", "The complete group, set of events or process outcomes that the question is about.", "যে complete group, event set বা process outcome সম্পর্কে প্রশ্ন করা হচ্ছে।"),
        ("Sample", "স্যাম্পল", "The subset actually observed or measured.", "যে subset বাস্তবে observe বা measure করা হয়েছে।"),
        ("Parameter", "প্যারামিটার", "A numerical property of the population, usually unknown.", "population-এর numerical property, যা সাধারণত unknown।"),
        ("Statistic", "স্ট্যাটিস্টিক", "A numerical value calculated from the sample and used to learn about a parameter.", "sample থেকে calculated numerical value, যা parameter সম্পর্কে শেখায়।"),
    ],
    "Variables and Observations": [
        ("Observation", "অবজারভেশন", "One unit recorded in the data, commonly represented by one row.", "data-তে recorded একটি unit, সাধারণত একটি row।"),
        ("Variable", "ভেরিয়েবল", "A characteristic that can take different values across observations.", "observation অনুযায়ী ভিন্ন value নিতে পারে এমন characteristic।"),
        ("Unit of analysis", "unit of analysis", "The entity each row is intended to represent.", "প্রতিটি row যে entity-কে represent করার কথা।"),
    ],
    "Measurement Scales": [
        ("Nominal", "নমিনাল", "Categories with no inherent order, such as district or blood group.", "inherent order ছাড়া category, যেমন district বা blood group।"),
        ("Ordinal", "অর্ডিনাল", "Ordered categories whose gaps are not guaranteed equal, such as satisfaction levels.", "ordered category যেখানে gap equal হওয়ার guarantee নেই, যেমন satisfaction level।"),
        ("Interval", "ইন্টারভ্যাল", "Equal numerical differences but no meaningful absolute zero, such as Celsius temperature.", "equal numerical difference আছে, কিন্তু meaningful absolute zero নেই, যেমন Celsius temperature।"),
        ("Ratio", "রেশিও", "Equal differences and a meaningful zero, allowing ratio comparisons, such as weight or income.", "equal difference ও meaningful zero আছে, তাই ratio comparison সম্ভব, যেমন weight বা income।"),
    ],
    "Categorical and Numerical Data": [
        ("Categorical", "ক্যাটেগরিক্যাল", "Labels or groups such as product type, region or pass/fail.", "product type, region বা pass/fail-এর মতো label বা group।"),
        ("Discrete numerical", "ডিসক্রিট নিউমেরিক্যাল", "Countable values such as number of orders or defects.", "order বা defect count-এর মতো countable value।"),
        ("Continuous numerical", "কন্টিনিউয়াস নিউমেরিক্যাল", "Measurements that can take any value in a range, such as time, length or temperature.", "time, length বা temperature-এর মতো range-এর মধ্যে যেকোনো value নিতে পারে এমন measurement।"),
    ],
    "Mean, Median and Mode": [
        ("Mean", "মিন", "Add all values and divide by the number of values; it uses every observation and is sensitive to extremes.", "সব value যোগ করে count দিয়ে ভাগ; সব observation ব্যবহার করে এবং extreme value-sensitive।"),
        ("Median", "মিডিয়ান", "The middle ordered value; it is resistant to a small number of extreme values.", "ordered data-এর middle value; অল্প কিছু extreme value-এর প্রতি resistant।"),
        ("Mode", "মোড", "The most frequent value or category; there may be none or more than one.", "সবচেয়ে frequent value বা category; কোনো mode নাও থাকতে পারে বা একাধিক হতে পারে।"),
    ],
    "Variance and Standard Deviation": [
        ("Deviation", "ডেভিয়েশন", "The difference between an observation and the mean.", "একটি observation ও mean-এর difference।"),
        ("Variance", "ভ্যারিয়েন্স", "The average squared deviation; sample variance commonly divides by n−1.", "squared deviation-এর average; sample variance সাধারণত n−1 দিয়ে divide করে।"),
        ("Standard deviation", "স্ট্যান্ডার্ড ডেভিয়েশন", "The square root of variance, expressed in the original measurement unit.", "variance-এর square root, original measurement unit-এ প্রকাশিত।"),
    ],
    "Probability Rules": [
        ("Sample space", "sample space", "The set of all possible outcomes under the defined experiment.", "defined experiment-এর সব possible outcome-এর set।"),
        ("Event", "event", "A subset of outcomes of interest.", "interest-এর outcome subset।"),
        ("Union and intersection", "union ও intersection", "Union means either event occurs; intersection means both occur.", "union মানে যেকোনো event ঘটে; intersection মানে দুটিই ঘটে।"),
        ("Complement", "complement", "The event that the specified event does not occur.", "specified event না ঘটার event।"),
    ],
    "Confidence Intervals": [
        ("Estimate", "estimate", "The sample-based value at the centre of the interval.", "interval-এর centre-এ sample-based value।"),
        ("Standard error", "standard error", "The estimated sample-to-sample variability of the estimator.", "estimator-এর estimated sample-to-sample variability।"),
        ("Critical value", "critical value", "A multiplier determined by the confidence procedure and reference distribution.", "confidence procedure ও reference distribution দ্বারা নির্ধারিত multiplier।"),
        ("Confidence level", "confidence level", "The long-run coverage rate of intervals produced by the procedure under its assumptions.", "assumption-এর অধীনে procedure দ্বারা তৈরি interval-এর long-run coverage rate।"),
    ],
    "Hypothesis Testing Framework": [
        ("Null hypothesis", "null hypothesis", "The reference claim or model used to calculate expected evidence.", "expected evidence calculate করার reference claim বা model।"),
        ("Alternative hypothesis", "alternative hypothesis", "The competing direction or set of values the study is designed to detect.", "study যে competing direction বা value set detect করতে design করা।"),
        ("Test statistic", "test statistic", "A standardized summary of how far the data are from the null expectation.", "data null expectation থেকে কত দূরে তার standardized summary।"),
        ("Decision rule", "decision rule", "A prespecified rule linking evidence to reject or fail-to-reject language.", "evidence-কে reject বা fail-to-reject language-এর সঙ্গে যুক্ত prespecified rule।"),
    ],
    "Simple Linear Regression": [
        ("Outcome", "outcome", "The numerical response the model aims to explain or predict.", "model যে numerical response explain বা predict করতে চায়।"),
        ("Predictor", "predictor", "The explanatory variable used to model changes in the outcome.", "outcome change model করতে ব্যবহৃত explanatory variable।"),
        ("Slope", "slope", "The fitted change in the outcome for a one-unit predictor increase within the data range.", "data range-এর মধ্যে predictor এক unit বাড়লে fitted outcome change।"),
        ("Residual", "residual", "Observed outcome minus fitted outcome for one observation.", "একটি observation-এর observed outcome minus fitted outcome।"),
    ],
    "Data Cleaning": [
        ("Validation", "validation", "Checking whether values follow expected type, range, format and business rules.", "value expected type, range, format ও business rule follow করে কি না যাচাই।"),
        ("Standardization", "standardization", "Making equivalent values use consistent formats and labels.", "equivalent value-কে consistent format ও label-এ আনা।"),
        ("Deduplication", "deduplication", "Identifying repeated records according to a declared business key.", "declared business key অনুযায়ী repeated record শনাক্ত করা।"),
        ("Audit trail", "audit trail", "Recording what changed, why it changed and how the original can be recovered.", "কী change হয়েছে, কেন এবং original কীভাবে recover হবে তা record করা।"),
    ],
    "Data Formats: CSV, JSON and Parquet": [
        ("CSV", "CSV", "A simple text table with rows and delimited columns; portable but weakly typed.", "row ও delimited column-সহ simple text table; portable কিন্তু weakly typed।"),
        ("JSON", "JSON", "A text format for nested objects and arrays; flexible but often verbose for analytics.", "nested object ও array-এর text format; flexible কিন্তু analytics-এর জন্য অনেক সময় verbose।"),
        ("Parquet", "Parquet", "A typed column-oriented binary format designed for efficient analytical storage and retrieval.", "efficient analytical storage ও retrieval-এর জন্য typed column-oriented binary format।"),
    ],
}

MODULE_PURPOSE = {
    "foundations": ("It prevents category mistakes, weak sampling claims and unreliable analysis before calculations begin.", "calculation শুরু হওয়ার আগে category mistake, weak sampling claim ও unreliable analysis প্রতিরোধ করে।"),
    "descriptive": ("It helps you describe what the observed data look like before making broader claims.", "broader claim করার আগে observed data কেমন তা describe করতে সাহায্য করে।"),
    "probability": ("It provides a mathematical language for uncertainty, repeated events and random variation.", "uncertainty, repeated event ও random variation-এর mathematical language দেয়।"),
    "inference": ("It separates real evidence from changes that could plausibly arise through sampling variation.", "sampling variation-এর মাধ্যমে ঘটতে পারে এমন change থেকে real evidence আলাদা করে।"),
    "regression": ("It helps quantify relationships, make conditional predictions and diagnose model limitations.", "relationship quantify, conditional prediction ও model limitation diagnose করতে সাহায্য করে।"),
    "analytics": ("It connects reliable metrics and analysis to practical business decisions.", "reliable metric ও analysis-কে practical business decision-এর সঙ্গে যুক্ত করে।"),
    "data-science": ("It supports models that generalize, avoid leakage and align evaluation with the real decision.", "generalize করা model, leakage avoidance ও real decision-এর সঙ্গে evaluation align করতে সাহায্য করে।"),
    "data-engineering": ("It makes data trustworthy, traceable and usable across repeatable analytical systems.", "repeatable analytical system জুড়ে data-কে trustworthy, traceable ও usable করে।"),
    "advanced": ("It handles designs, dependencies and uncertainty patterns that simpler methods cannot represent well.", "simple method ভালোভাবে represent করতে পারে না এমন design, dependency ও uncertainty pattern handle করে।"),
}

TYPE_BY_MODULE = {
    "foundations": "concept",
    "descriptive": "formula",
    "probability": "formula",
    "inference": "method",
    "regression": "method",
    "analytics": "workflow",
    "data-science": "method",
    "data-engineering": "workflow",
    "advanced": "method",
}

FORMULA_TOPICS = {
    "Mean, Median and Mode", "Weighted, Geometric and Harmonic Means", "Quantiles and Percentiles",
    "Range and Interquartile Range", "Variance and Standard Deviation", "Coefficient of Variation", "Skewness",
    "Kurtosis", "Probability Rules", "Conditional Probability", "Bayes' Theorem", "Expected Value and Variance",
    "Bernoulli and Binomial Distributions", "Poisson Distribution", "Uniform Distribution", "Normal Distribution",
    "Exponential Distribution", "Point Estimation", "Confidence Intervals", "One-sample z and t Tests",
    "Two-sample t Test", "Paired t Test", "Tests for Proportions", "Chi-square Tests", "Analysis of Variance",
    "Covariance and Correlation", "Pearson and Spearman Correlation", "Simple Linear Regression", "Ordinary Least Squares",
    "R-squared and Adjusted R-squared", "Multicollinearity and VIF", "Logistic Regression", "Moving Averages and Smoothing",
    "Classification Metrics", "Kaplan-Meier Estimation", "Cox Proportional Hazards Model", "Monte Carlo Simulation",
}

IMPLEMENTATION_GUIDES = {
    "foundations": [
        ("Spreadsheet", "স্প্রেডশিট", ["Put one observation on each row and one variable in each column.", "Create a data dictionary with name, meaning, type, unit and allowed values.", "Use filters and frequency tables to inspect missing or unexpected codes."], ["প্রতি row-তে একটি observation এবং প্রতি column-এ একটি variable রাখুন।", "name, meaning, type, unit ও allowed value-সহ data dictionary তৈরি করুন।", "missing বা unexpected code দেখতে filter ও frequency table ব্যবহার করুন।"]),
        ("SQL", "SQL", ["Declare the table grain before writing joins or aggregations.", "Inspect row counts, null counts and distinct keys.", "Document filters so that the analysed population is explicit."], ["join বা aggregation-এর আগে table grain declare করুন।", "row count, null count ও distinct key inspect করুন।", "analysed population explicit রাখতে filter document করুন।"]),
    ],
    "descriptive": [
        ("Excel / Sheets", "Excel / Sheets", ["Keep raw values in one clean column or table.", "Use appropriate summary functions and state the convention used.", "Pair numerical summaries with a chart before interpreting."], ["raw value একটি clean column বা table-এ রাখুন।", "উপযুক্ত summary function ব্যবহার করে convention উল্লেখ করুন।", "interpret করার আগে numerical summary-এর সঙ্গে chart দেখুন।"]),
        ("Python", "Python", ["Load data into pandas and inspect dtype and missing values.", "Use describe(), value_counts(), quantile() or the relevant method.", "Plot the distribution and verify results with a small hand-checkable example."], ["pandas-এ data load করে dtype ও missing value inspect করুন।", "describe(), value_counts(), quantile() অথবা relevant method ব্যবহার করুন।", "distribution plot করুন এবং ছোট hand-checkable example দিয়ে result verify করুন।"]),
    ],
    "probability": [
        ("Manual model", "ম্যানুয়াল model", ["Define the experiment, sample space and event clearly.", "List assumptions such as independence, constant rate or fixed probability.", "Calculate probability and check that the result remains between 0 and 1."], ["experiment, sample space ও event পরিষ্কারভাবে define করুন।", "independence, constant rate বা fixed probability-এর মতো assumption list করুন।", "probability calculate করে result 0 ও 1-এর মধ্যে আছে কি না check করুন।"]),
        ("Python", "Python", ["Represent parameters explicitly and use a tested distribution function when available.", "Compare analytical results with simulation for a small example.", "Set a random seed only when reproducible simulation is required."], ["parameter explicitভাবে represent করুন এবং available হলে tested distribution function ব্যবহার করুন।", "ছোট example-এ analytical result simulation-এর সঙ্গে তুলনা করুন।", "reproducible simulation দরকার হলেই random seed set করুন।"]),
    ],
    "inference": [
        ("Analysis plan", "analysis plan", ["State the estimand, null hypothesis, alternative, alpha and test before viewing results.", "Check design, independence, sample size and method-specific assumptions.", "Report effect size and interval alongside the p-value."], ["result দেখার আগে estimand, null hypothesis, alternative, alpha ও test state করুন।", "design, independence, sample size ও method-specific assumption check করুন।", "p-value-এর সঙ্গে effect size ও interval report করুন।"]),
        ("Software", "software", ["Use a validated statistical function rather than rewriting distribution algorithms casually.", "Confirm defaults such as equal-variance assumptions, tail direction and confidence level.", "Save code, inputs and output needed to reproduce the result."], ["distribution algorithm casually rewrite না করে validated statistical function ব্যবহার করুন।", "equal-variance assumption, tail direction ও confidence level-এর default confirm করুন।", "result reproduce করতে প্রয়োজনীয় code, input ও output save করুন।"]),
    ],
    "regression": [
        ("Model workflow", "model workflow", ["Define outcome, predictors, unit of analysis and prediction target.", "Split validation data before feature decisions that could leak information.", "Inspect coefficients, residuals, uncertainty and out-of-sample performance together."], ["outcome, predictor, unit of analysis ও prediction target define করুন।", "information leak করতে পারে এমন feature decision-এর আগে validation data split করুন।", "coefficient, residual, uncertainty ও out-of-sample performance একসঙ্গে inspect করুন।"]),
        ("Python / R", "Python / R", ["Use a transparent model specification and documented preprocessing pipeline.", "Retain a baseline model for comparison.", "Check diagnostics and avoid extrapolating far beyond observed predictor ranges."], ["transparent model specification ও documented preprocessing pipeline ব্যবহার করুন।", "comparison-এর জন্য baseline model রাখুন।", "diagnostic check করুন এবং observed predictor range-এর অনেক বাইরে extrapolate করবেন না।"]),
    ],
    "analytics": [
        ("SQL", "SQL", ["Define metric grain, eligible population, time window and exclusions.", "Build auditable intermediate queries before the final aggregation.", "Reconcile totals against a trusted source or control report."], ["metric grain, eligible population, time window ও exclusion define করুন।", "final aggregation-এর আগে auditable intermediate query বানান।", "trusted source বা control report-এর সঙ্গে total reconcile করুন।"]),
        ("Power BI / BI", "Power BI / BI", ["Create a documented semantic measure instead of repeating logic in visuals.", "Use visuals that match the question and expose denominator or filter context.", "Add a note for uncertainty, incomplete data or non-causal interpretation."], ["visual-এ logic repeat না করে documented semantic measure তৈরি করুন।", "question-এর সঙ্গে matching visual ব্যবহার করে denominator বা filter context expose করুন।", "uncertainty, incomplete data বা non-causal interpretation-এর note যোগ করুন।"]),
    ],
    "data-science": [
        ("Python pipeline", "Python pipeline", ["Separate training, validation and test roles before learning transformations.", "Place preprocessing and modelling in one reproducible pipeline.", "Evaluate with metrics and thresholds aligned to the real cost of errors."], ["transformation শেখার আগে training, validation ও test role আলাদা করুন।", "preprocessing ও modelling একটি reproducible pipeline-এ রাখুন।", "real error cost-এর সঙ্গে aligned metric ও threshold দিয়ে evaluate করুন।"]),
        ("Experiment log", "experiment log", ["Record data version, feature set, random seed, model settings and evaluation protocol.", "Compare against a simple baseline.", "Investigate subgroup performance and failure cases before deployment."], ["data version, feature set, random seed, model setting ও evaluation protocol record করুন।", "simple baseline-এর সঙ্গে compare করুন।", "deployment-এর আগে subgroup performance ও failure case investigate করুন।"]),
    ],
    "data-engineering": [
        ("Design", "design", ["Declare source, target, grain, ownership, freshness and failure expectations.", "Choose formats and models based on access pattern, scale and governance requirements.", "Design idempotent transformations so reruns do not corrupt results."], ["source, target, grain, ownership, freshness ও failure expectation declare করুন।", "access pattern, scale ও governance requirement অনুযায়ী format ও model বাছাই করুন।", "rerun যেন result corrupt না করে এমন idempotent transformation design করুন।"]),
        ("Testing and operations", "testing ও operations", ["Test schema, uniqueness, relationships, accepted values and freshness.", "Track lineage and publish clear metric or dataset contracts.", "Monitor failures with actionable alerts, retries and backfill procedures."], ["schema, uniqueness, relationship, accepted value ও freshness test করুন।", "lineage track করুন এবং clear metric বা dataset contract publish করুন।", "actionable alert, retry ও backfill procedure দিয়ে failure monitor করুন।"]),
    ],
    "advanced": [
        ("Study design", "study design", ["Define the scientific question, data-generating process and dependency structure.", "Select a method whose assumptions match censoring, repeated measures, multivariate or spatial structure.", "Plan diagnostics and sensitivity analyses before interpreting results."], ["scientific question, data-generating process ও dependency structure define করুন।", "censoring, repeated measure, multivariate বা spatial structure-এর সঙ্গে matching assumption-এর method বাছাই করুন।", "result interpret করার আগে diagnostic ও sensitivity analysis plan করুন।"]),
        ("Computation", "computation", ["Use established libraries and validate with simulated or known examples.", "Assess convergence, numerical stability or identifiability where relevant.", "Report uncertainty and model dependence, not only a point result."], ["established library ব্যবহার করে simulated বা known example দিয়ে validate করুন।", "relevant হলে convergence, numerical stability বা identifiability assess করুন।", "শুধু point result নয়, uncertainty ও model dependence report করুন।"]),
    ],
}

WORKFLOW_LABELS = {
    "concept": [
        ("Define the question", "প্রশ্ন define করুন"),
        ("Identify the unit and variables", "unit ও variable শনাক্ত করুন"),
        ("Classify the data correctly", "data সঠিকভাবে classify করুন"),
        ("Choose a suitable summary or method", "উপযুক্ত summary বা method বাছাই করুন"),
        ("Interpret with context and limitations", "context ও limitation-সহ interpret করুন"),
    ],
    "formula": [
        ("State the quantity and convention", "quantity ও convention state করুন"),
        ("Check the required data type and assumptions", "required data type ও assumption check করুন"),
        ("Calculate with a small verifiable example", "ছোট verifiable example-এ calculate করুন"),
        ("Compare the result with a visual or alternative summary", "result-কে visual বা alternative summary-এর সঙ্গে compare করুন"),
        ("Explain units, magnitude and sensitivity", "unit, magnitude ও sensitivity explain করুন"),
    ],
    "method": [
        ("Translate the practical question into an estimand or model", "practical question-কে estimand বা model-এ translate করুন"),
        ("Check design and assumptions", "design ও assumption check করুন"),
        ("Fit or calculate using a validated procedure", "validated procedure দিয়ে fit বা calculate করুন"),
        ("Diagnose uncertainty and failure modes", "uncertainty ও failure mode diagnose করুন"),
        ("Report effect, uncertainty and limitations", "effect, uncertainty ও limitation report করুন"),
    ],
    "workflow": [
        ("Define the business or system outcome", "business বা system outcome define করুন"),
        ("Map source data, grain and ownership", "source data, grain ও ownership map করুন"),
        ("Apply documented transformations or rules", "documented transformation বা rule apply করুন"),
        ("Validate quality and reconcile results", "quality validate ও result reconcile করুন"),
        ("Publish, monitor and improve", "publish, monitor ও improve করুন"),
    ],
}


def _generic_concepts(title: str, title_bn: str, summary_en: str, summary_bn: str, why_en: str, why_bn: str, formula_en: str, formula_bn: str):
    return [
        (title, title_bn, summary_en, summary_bn),
        ("When it is useful", "কখন কাজে লাগে", why_en, why_bn),
        ("Calculation or decision rule", "calculation বা decision rule", formula_en, formula_bn),
    ]


def build_lesson_content(topic: dict, module: dict) -> dict:
    title = topic["title_en"]
    title_bn = topic["title_bn"]
    scenario = SCENARIO_SEEDS[title]
    label_en, label_bn, context_en, context_bn, question_en, question_bn = scenario
    lesson_type = "formula" if title in FORMULA_TOPICS else TYPE_BY_MODULE[module["id"]]
    module_why_en, module_why_bn = MODULE_PURPOSE[module["id"]]
    why_en = f"{title} matters because {module_why_en[0].lower() + module_why_en[1:]} In practice, it helps answer: {question_en}"
    why_bn = f"{title_bn} গুরুত্বপূর্ণ কারণ {module_why_bn} Practical question: {question_bn}"
    concepts = CUSTOM_CONCEPTS.get(title) or _generic_concepts(
        title, title_bn, topic["summary_en"], topic["summary_bn"], why_en, why_bn,
        topic["formula_en"], topic["formula_bn"],
    )
    worked_steps_en = [
        f"Start with the situation: {context_en}",
        f"Write the exact question: {question_en}",
        f"Identify the relevant observations, variables, units and time window for {title.lower()}.",
        "Apply the stated definition, formula or workflow and keep intermediate decisions visible.",
        "Explain what the result supports, what remains uncertain and one practical next action.",
    ]
    worked_steps_bn = [
        f"পরিস্থিতি দিয়ে শুরু করুন: {context_bn}",
        f"exact question লিখুন: {question_bn}",
        f"{title_bn}-এর relevant observation, variable, unit ও time window শনাক্ত করুন।",
        "stated definition, formula বা workflow apply করুন এবং intermediate decision visible রাখুন।",
        "result কী support করে, কী uncertain এবং একটি practical next action ব্যাখ্যা করুন।",
    ]
    correct_en = f"A careful interpretation names the data and population, explains the {title.lower()} result in its unit or decision context, and states the assumptions or limitations that affect the conclusion."
    correct_bn = f"careful interpretation data ও population উল্লেখ করে, {title_bn} result-কে unit বা decision context-এ explain করে এবং conclusion-কে প্রভাবিত করা assumption বা limitation state করে।"
    wrong_en = f"Avoid saying that {title.lower()} automatically proves causation, guarantees a future outcome, or remains valid when its data requirements are violated."
    wrong_bn = f"{title_bn} automatically causation prove করে, future outcome guarantee করে অথবা data requirement ভাঙলেও valid থাকে—এমন কথা বলবেন না।"
    quiz_question_en = f"Which statement best demonstrates responsible use of {title}?"
    quiz_question_bn = f"কোন statement {title_bn}-এর responsible use সবচেয়ে ভালো দেখায়?"
    quiz_options = [
        (correct_en, correct_bn),
        (f"Use the result alone and ignore how the data were collected because {title.lower()} is objective.", f"data কীভাবে collect হয়েছে তা ignore করে শুধু result ব্যবহার করুন, কারণ {title_bn} objective।"),
        (f"Treat any numerical output from {title.lower()} as proof of a causal relationship.", f"{title_bn}-এর যেকোনো numerical output-কে causal relationship-এর proof ধরুন।"),
    ]
    recap = [
        (topic["summary_en"], topic["summary_bn"]),
        (why_en, why_bn),
        (f"The key practical question is: {question_en}", f"মূল practical question: {question_bn}"),
        (f"A valid use of {title.lower()} depends on suitable data, transparent conventions and cautious interpretation.", f"{title_bn}-এর valid use suitable data, transparent convention ও cautious interpretation-এর ওপর নির্ভর করে।"),
    ]
    practice_en = f"Create a small example for “{label_en}”. Record 5–10 observations, identify the variables or parameters needed for {title.lower()}, apply the method, and write a two-sentence interpretation containing one limitation."
    practice_bn = f"“{label_bn}” নিয়ে ছোট example তৈরি করুন। ৫–১০টি observation record করে {title_bn}-এর প্রয়োজনীয় variable বা parameter শনাক্ত করুন, method apply করুন এবং একটি limitation-সহ দুই sentence interpretation লিখুন।"
    return {
        "lesson_type": lesson_type,
        "plain_en": topic["summary_en"],
        "plain_bn": topic["summary_bn"],
        "why_en": why_en,
        "why_bn": why_bn,
        "concepts": [
            {"term_en": a, "term_bn": b, "definition_en": c, "definition_bn": d}
            for a, b, c, d in concepts
        ],
        "scenario": {
            "title_en": label_en,
            "title_bn": label_bn,
            "context_en": context_en,
            "context_bn": context_bn,
            "question_en": question_en,
            "question_bn": question_bn,
            "steps_en": worked_steps_en,
            "steps_bn": worked_steps_bn,
        },
        "workflow": [
            {"en": en, "bn": bn} for en, bn in WORKFLOW_LABELS[lesson_type]
        ],
        "implementations": [
            {"tool_en": a, "tool_bn": b, "steps_en": c, "steps_bn": d}
            for a, b, c, d in IMPLEMENTATION_GUIDES[module["id"]]
        ],
        "interpretation": {
            "good_en": correct_en,
            "good_bn": correct_bn,
            "caution_en": wrong_en,
            "caution_bn": wrong_bn,
        },
        "practice_en": practice_en,
        "practice_bn": practice_bn,
        "quiz": {
            "question_en": quiz_question_en,
            "question_bn": quiz_question_bn,
            "options": [{"en": en, "bn": bn} for en, bn in quiz_options],
            "answer": 0,
            "explanation_en": f"The first statement keeps the result tied to its data, context, assumptions and uncertainty. That is the standard required for {title.lower()}.",
            "explanation_bn": f"প্রথম statement result-কে data, context, assumption ও uncertainty-এর সঙ্গে যুক্ত রাখে। {title_bn}-এর জন্য এটাই প্রয়োজনীয় standard।",
        },
        "recap": [{"en": en, "bn": bn} for en, bn in recap],
        "references": REFERENCES[module["id"]],
    }
