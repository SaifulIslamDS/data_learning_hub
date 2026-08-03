from __future__ import annotations

import json
import re
from pathlib import Path
from html import escape

from topic_details import TOPIC_DETAILS

ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://statistics-learning-hub.netlify.app"


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = value.replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


MODULES = [
    {
        "id": "foundations",
        "title_en": "Data & Statistics Foundations",
        "title_bn": "ডেটা ও পরিসংখ্যানের ভিত্তি",
        "description_en": "Build the vocabulary, data literacy, sampling awareness, and workflow habits needed before formal analysis.",
        "description_bn": "আনুষ্ঠানিক বিশ্লেষণের আগে প্রয়োজনীয় পরিভাষা, ডেটা লিটারেসি, স্যাম্পলিং ধারণা ও সুশৃঙ্খল কাজের ধারা তৈরি করুন।",
        "accent": "violet",
        "icon": "database",
        "topics": [
            ("Statistics and Data", "পরিসংখ্যান ও ডেটা", "Beginner", "lesson"),
            ("Population and Sample", "পপুলেশন ও স্যাম্পল", "Beginner", "lesson"),
            ("Variables and Observations", "ভেরিয়েবল ও অবজারভেশন", "Beginner", "lesson"),
            ("Measurement Scales", "পরিমাপের স্কেল", "Beginner", "lesson"),
            ("Categorical and Numerical Data", "ক্যাটেগরিক্যাল ও নিউমেরিক্যাল ডেটা", "Beginner", "lesson"),
            ("Data Collection Methods", "ডেটা সংগ্রহের পদ্ধতি", "Beginner", "lesson"),
            ("Probability and Non-probability Sampling", "প্রবাবিলিটি ও নন-প্রবাবিলিটি স্যাম্পলিং", "Intermediate", "lesson"),
            ("Sampling Bias and Confounding", "স্যাম্পলিং বায়াস ও কনফাউন্ডিং", "Intermediate", "lesson"),
            ("Data Quality Dimensions", "ডেটা কোয়ালিটির মাত্রা", "Intermediate", "lesson"),
            ("Frequency Tables", "ফ্রিকোয়েন্সি টেবিল", "Beginner", "practice"),
            ("Exploratory Data Analysis Workflow", "এক্সপ্লোরেটরি ডেটা অ্যানালাইসিস ওয়ার্কফ্লো", "Intermediate", "practice"),
            ("Reproducible Statistical Workflow", "পুনরুৎপাদনযোগ্য পরিসংখ্যান ওয়ার্কফ্লো", "Intermediate", "lesson"),
        ],
    },
    {
        "id": "descriptive",
        "title_en": "Descriptive Statistics & Visualization",
        "title_bn": "বর্ণনামূলক পরিসংখ্যান ও ভিজ্যুয়ালাইজেশন",
        "description_en": "Summarize distributions, compare groups, detect unusual values, and communicate patterns with appropriate charts.",
        "description_bn": "ডিস্ট্রিবিউশন সংক্ষেপ করুন, গ্রুপ তুলনা করুন, অস্বাভাবিক মান শনাক্ত করুন এবং উপযুক্ত চার্টে প্যাটার্ন ব্যাখ্যা করুন।",
        "accent": "cyan",
        "icon": "chart",
        "topics": [
            ("Mean, Median and Mode", "মিন, মিডিয়ান ও মোড", "Beginner", "lab", "summary-statistics"),
            ("Weighted, Geometric and Harmonic Means", "ওয়েটেড, জ্যামিতিক ও হারমোনিক গড়", "Intermediate", "lab", "weighted-mean"),
            ("Quantiles and Percentiles", "কোয়ান্টাইল ও পার্সেন্টাইল", "Beginner", "lab", "percentile-quartile"),
            ("Range and Interquartile Range", "রেঞ্জ ও ইন্টারকোয়ার্টাইল রেঞ্জ", "Beginner", "lab", "summary-statistics"),
            ("Variance and Standard Deviation", "ভ্যারিয়েন্স ও স্ট্যান্ডার্ড ডেভিয়েশন", "Beginner", "lab", "summary-statistics"),
            ("Coefficient of Variation", "কো-এফিশিয়েন্ট অব ভ্যারিয়েশন", "Intermediate", "lesson"),
            ("Skewness", "স্কিউনেস", "Intermediate", "lesson"),
            ("Kurtosis", "কার্টোসিস", "Intermediate", "lesson"),
            ("Outlier Detection", "আউটলায়ার শনাক্তকরণ", "Intermediate", "lab", "box-plot"),
            ("Histograms", "হিস্টোগ্রাম", "Beginner", "lab", "histogram"),
            ("Box Plots", "বক্স প্লট", "Beginner", "lab", "box-plot"),
            ("Scatter, Line and Bar Charts", "স্ক্যাটার, লাইন ও বার চার্ট", "Beginner", "practice"),
        ],
    },
    {
        "id": "probability",
        "title_en": "Probability & Distributions",
        "title_bn": "প্রবাবিলিটি ও ডিস্ট্রিবিউশন",
        "description_en": "Model uncertainty with probability rules, random variables, common distributions, sampling distributions, and the CLT.",
        "description_bn": "প্রবাবিলিটি রুল, র‍্যান্ডম ভেরিয়েবল, প্রচলিত ডিস্ট্রিবিউশন, স্যাম্পলিং ডিস্ট্রিবিউশন ও CLT দিয়ে অনিশ্চয়তা মডেল করুন।",
        "accent": "blue",
        "icon": "dice",
        "topics": [
            ("Probability Rules", "প্রবাবিলিটির নিয়ম", "Beginner", "lesson"),
            ("Conditional Probability", "শর্তাধীন প্রবাবিলিটি", "Intermediate", "lesson"),
            ("Bayes' Theorem", "বেইজের উপপাদ্য", "Intermediate", "lesson"),
            ("Random Variables", "র‍্যান্ডম ভেরিয়েবল", "Beginner", "lesson"),
            ("Expected Value and Variance", "এক্সপেক্টেড ভ্যালু ও ভ্যারিয়েন্স", "Intermediate", "lesson"),
            ("Bernoulli and Binomial Distributions", "বার্নুলি ও বাইনোমিয়াল ডিস্ট্রিবিউশন", "Intermediate", "lab", "binomial-probability"),
            ("Poisson Distribution", "পয়সন ডিস্ট্রিবিউশন", "Intermediate", "lab", "poisson-probability"),
            ("Uniform Distribution", "ইউনিফর্ম ডিস্ট্রিবিউশন", "Beginner", "lesson"),
            ("Normal Distribution", "নরমাল ডিস্ট্রিবিউশন", "Intermediate", "lab", "normal-probability"),
            ("Exponential Distribution", "এক্সপোনেনশিয়াল ডিস্ট্রিবিউশন", "Intermediate", "lesson"),
            ("Sampling Distributions", "স্যাম্পলিং ডিস্ট্রিবিউশন", "Intermediate", "lesson"),
            ("Central Limit Theorem", "সেন্ট্রাল লিমিট থিওরেম", "Intermediate", "lab", "clt-simulator"),
        ],
    },
    {
        "id": "inference",
        "title_en": "Statistical Inference & Experimentation",
        "title_bn": "স্ট্যাটিস্টিক্যাল ইনফারেন্স ও এক্সপেরিমেন্টেশন",
        "description_en": "Estimate unknown quantities, test evidence, quantify uncertainty, compare groups, and design defensible experiments.",
        "description_bn": "অজানা প্যারামিটার অনুমান, প্রমাণ যাচাই, অনিশ্চয়তা পরিমাপ, গ্রুপ তুলনা এবং গ্রহণযোগ্য এক্সপেরিমেন্ট ডিজাইন শিখুন।",
        "accent": "emerald",
        "icon": "flask",
        "topics": [
            ("Point Estimation", "পয়েন্ট এস্টিমেশন", "Intermediate", "lesson"),
            ("Confidence Intervals", "কনফিডেন্স ইন্টারভ্যাল", "Intermediate", "lab", "mean-confidence-interval"),
            ("Hypothesis Testing Framework", "হাইপোথিসিস টেস্টিং ফ্রেমওয়ার্ক", "Intermediate", "lesson"),
            ("p-values and Significance Levels", "পি-ভ্যালু ও সিগনিফিক্যান্স লেভেল", "Intermediate", "lesson"),
            ("Type I, Type II Errors and Power", "টাইপ I, টাইপ II এরর ও পাওয়ার", "Intermediate", "lesson"),
            ("One-sample z and t Tests", "ওয়ান-স্যাম্পল z ও t টেস্ট", "Intermediate", "lab", "one-sample-t-test"),
            ("Two-sample t Test", "টু-স্যাম্পল t টেস্ট", "Intermediate", "lab", "two-sample-t-test"),
            ("Paired t Test", "পেয়ার্ড t টেস্ট", "Intermediate", "lesson"),
            ("Tests for Proportions", "প্রপোরশনের টেস্ট", "Intermediate", "lab", "ab-test"),
            ("Chi-square Tests", "কাই-স্কয়ার টেস্ট", "Intermediate", "lab", "chi-square-independence"),
            ("Analysis of Variance", "অ্যানালাইসিস অব ভ্যারিয়েন্স", "Advanced", "lesson"),
            ("Nonparametric Tests", "ননপ্যারামেট্রিক টেস্ট", "Advanced", "lesson"),
        ],
    },
    {
        "id": "regression",
        "title_en": "Correlation & Regression Modeling",
        "title_bn": "কোরিলেশন ও রিগ্রেশন মডেলিং",
        "description_en": "Measure relationships, build predictive models, diagnose assumptions, and evaluate out-of-sample performance.",
        "description_bn": "সম্পর্ক পরিমাপ, প্রেডিক্টিভ মডেল তৈরি, অ্যাসাম্পশন যাচাই এবং নতুন ডেটায় পারফরম্যান্স মূল্যায়ন করুন।",
        "accent": "orange",
        "icon": "trend",
        "topics": [
            ("Covariance and Correlation", "কোভ্যারিয়েন্স ও কোরিলেশন", "Intermediate", "lesson"),
            ("Pearson and Spearman Correlation", "পিয়ারসন ও স্পিয়ারম্যান কোরিলেশন", "Intermediate", "lab", "pearson-correlation"),
            ("Simple Linear Regression", "সিম্পল লিনিয়ার রিগ্রেশন", "Intermediate", "lab", "linear-regression"),
            ("Ordinary Least Squares", "অর্ডিনারি লিস্ট স্কয়ারস", "Intermediate", "lesson"),
            ("R-squared and Adjusted R-squared", "R-squared ও Adjusted R-squared", "Intermediate", "lesson"),
            ("Residual Diagnostics", "রেসিডুয়াল ডায়াগনস্টিকস", "Advanced", "lesson"),
            ("Confidence and Prediction Intervals", "কনফিডেন্স ও প্রেডিকশন ইন্টারভ্যাল", "Advanced", "lesson"),
            ("Multiple Linear Regression", "মাল্টিপল লিনিয়ার রিগ্রেশন", "Advanced", "lesson"),
            ("Multicollinearity and VIF", "মাল্টিকোলিনিয়ারিটি ও VIF", "Advanced", "lesson"),
            ("Logistic Regression", "লজিস্টিক রিগ্রেশন", "Advanced", "lesson"),
            ("Regularization: Ridge and Lasso", "রেগুলারাইজেশন: রিজ ও লাসো", "Advanced", "lesson"),
            ("Model Validation", "মডেল ভ্যালিডেশন", "Advanced", "practice"),
        ],
    },
    {
        "id": "analytics",
        "title_en": "Data Analytics & Business Statistics",
        "title_bn": "ডেটা অ্যানালিটিক্স ও বিজনেস স্ট্যাটিস্টিকস",
        "description_en": "Turn raw business data into reliable metrics, experiments, forecasts, and decision-ready narratives.",
        "description_bn": "কাঁচা ব্যবসায়িক ডেটাকে নির্ভরযোগ্য মেট্রিক, এক্সপেরিমেন্ট, ফোরকাস্ট ও সিদ্ধান্তযোগ্য গল্পে রূপ দিন।",
        "accent": "pink",
        "icon": "briefcase",
        "topics": [
            ("Data Cleaning", "ডেটা ক্লিনিং", "Beginner", "practice"),
            ("Missing Data", "মিসিং ডেটা", "Intermediate", "lesson"),
            ("Outlier Treatment", "আউটলায়ার ট্রিটমেন্ট", "Intermediate", "lesson"),
            ("Exploratory Data Analysis", "এক্সপ্লোরেটরি ডেটা অ্যানালাইসিস", "Intermediate", "practice"),
            ("KPI Design", "KPI ডিজাইন", "Intermediate", "lesson"),
            ("Cohort Analysis", "কোহর্ট অ্যানালাইসিস", "Intermediate", "lesson"),
            ("Funnel Analysis", "ফানেল অ্যানালাইসিস", "Intermediate", "lesson"),
            ("A/B Testing", "A/B টেস্টিং", "Intermediate", "lab", "ab-test"),
            ("Time-series Components", "টাইম সিরিজ কম্পোনেন্ট", "Intermediate", "lesson"),
            ("Moving Averages and Smoothing", "মুভিং এভারেজ ও স্মুথিং", "Intermediate", "lab", "moving-average"),
            ("Forecast Evaluation", "ফোরকাস্ট মূল্যায়ন", "Advanced", "lesson"),
            ("Data Storytelling", "ডেটা স্টোরিটেলিং", "Intermediate", "practice"),
        ],
    },
    {
        "id": "data-science",
        "title_en": "Data Science Statistics",
        "title_bn": "ডেটা সায়েন্স স্ট্যাটিস্টিকস",
        "description_en": "Connect statistical reasoning to feature preparation, resampling, unsupervised learning, and model evaluation.",
        "description_bn": "ফিচার প্রস্তুতি, রিস্যাম্পলিং, আনসুপারভাইজড লার্নিং ও মডেল মূল্যায়নের সঙ্গে পরিসংখ্যানগত যুক্তি যুক্ত করুন।",
        "accent": "indigo",
        "icon": "brain",
        "topics": [
            ("Bootstrap", "বুটস্ট্র্যাপ", "Advanced", "lesson"),
            ("Cross-validation", "ক্রস-ভ্যালিডেশন", "Intermediate", "lesson"),
            ("Bias-Variance Trade-off", "বায়াস-ভ্যারিয়েন্স ট্রেড-অফ", "Advanced", "lesson"),
            ("Feature Engineering", "ফিচার ইঞ্জিনিয়ারিং", "Intermediate", "practice"),
            ("Scaling and Encoding", "স্কেলিং ও এনকোডিং", "Intermediate", "practice"),
            ("Principal Component Analysis", "প্রিন্সিপাল কম্পোনেন্ট অ্যানালাইসিস", "Advanced", "lesson"),
            ("K-means Clustering", "K-means ক্লাস্টারিং", "Intermediate", "lesson"),
            ("Hierarchical Clustering and DBSCAN", "হায়ারার্কিক্যাল ক্লাস্টারিং ও DBSCAN", "Advanced", "lesson"),
            ("Classification Metrics", "ক্লাসিফিকেশন মেট্রিক", "Intermediate", "lesson"),
            ("Probability Calibration and Thresholds", "প্রবাবিলিটি ক্যালিব্রেশন ও থ্রেশহোল্ড", "Advanced", "lesson"),
            ("Bayesian Inference", "বেইজিয়ান ইনফারেন্স", "Advanced", "lesson"),
            ("Causal Inference", "কজাল ইনফারেন্স", "Advanced", "lesson"),
        ],
    },
    {
        "id": "data-engineering",
        "title_en": "Data Engineering Foundations",
        "title_bn": "ডেটা ইঞ্জিনিয়ারিংয়ের ভিত্তি",
        "description_en": "Learn how reliable analytical data is represented, modeled, transformed, tested, orchestrated, and governed.",
        "description_bn": "নির্ভরযোগ্য অ্যানালিটিক্যাল ডেটা কীভাবে উপস্থাপন, মডেল, ট্রান্সফর্ম, টেস্ট, অর্কেস্ট্রেট ও গভর্ন করা হয় তা শিখুন।",
        "accent": "teal",
        "icon": "pipeline",
        "topics": [
            ("Data Formats: CSV, JSON and Parquet", "ডেটা ফরম্যাট: CSV, JSON ও Parquet", "Beginner", "lesson"),
            ("Relational Data Modeling", "রিলেশনাল ডেটা মডেলিং", "Intermediate", "lesson"),
            ("SQL for Analytics", "অ্যানালিটিক্সের জন্য SQL", "Intermediate", "practice"),
            ("Normalization and Denormalization", "নরমালাইজেশন ও ডিনরমালাইজেশন", "Intermediate", "lesson"),
            ("ETL and ELT", "ETL ও ELT", "Intermediate", "lesson"),
            ("Batch and Streaming Data", "ব্যাচ ও স্ট্রিমিং ডেটা", "Intermediate", "lesson"),
            ("Warehouse, Lake and Lakehouse", "ডেটা ওয়্যারহাউস, লেক ও লেকহাউস", "Intermediate", "lesson"),
            ("Dimensional Modeling and Star Schemas", "ডাইমেনশনাল মডেলিং ও স্টার স্কিমা", "Advanced", "lesson"),
            ("Data Quality Testing", "ডেটা কোয়ালিটি টেস্টিং", "Intermediate", "practice"),
            ("Pipeline Orchestration", "পাইপলাইন অর্কেস্ট্রেশন", "Advanced", "lesson"),
            ("Data Lineage and Governance", "ডেটা লিনিয়েজ ও গভর্ন্যান্স", "Advanced", "lesson"),
            ("Analytics Engineering and Semantic Layers", "অ্যানালিটিক্স ইঞ্জিনিয়ারিং ও সেমান্টিক লেয়ার", "Advanced", "lesson"),
        ],
    },
    {
        "id": "advanced",
        "title_en": "Advanced Statistical Methods",
        "title_bn": "অ্যাডভান্সড স্ট্যাটিস্টিক্যাল মেথড",
        "description_en": "Study experimental design, survival and multivariate methods, simulation, Markov processes, and spatial reasoning.",
        "description_bn": "এক্সপেরিমেন্টাল ডিজাইন, সারভাইভাল ও মাল্টিভ্যারিয়েট মেথড, সিমুলেশন, মার্কভ প্রসেস এবং স্পেশাল বিশ্লেষণ শিখুন।",
        "accent": "amber",
        "icon": "atom",
        "topics": [
            ("Experimental Design", "এক্সপেরিমেন্টাল ডিজাইন", "Advanced", "lesson"),
            ("Factorial Designs", "ফ্যাক্টোরিয়াল ডিজাইন", "Advanced", "lesson"),
            ("Repeated Measures", "রিপিটেড মেজারস", "Advanced", "lesson"),
            ("Survival Analysis", "সারভাইভাল অ্যানালাইসিস", "Advanced", "lesson"),
            ("Kaplan-Meier Estimation", "ক্যাপলান-মায়ার এস্টিমেশন", "Advanced", "lesson"),
            ("Cox Proportional Hazards Model", "কক্স প্রপোরশনাল হ্যাজার্ডস মডেল", "Advanced", "lesson"),
            ("Multivariate Normal Distribution", "মাল্টিভ্যারিয়েট নরমাল ডিস্ট্রিবিউশন", "Advanced", "lesson"),
            ("MANOVA", "MANOVA", "Advanced", "lesson"),
            ("Factor Analysis", "ফ্যাক্টর অ্যানালাইসিস", "Advanced", "lesson"),
            ("Monte Carlo Simulation", "মন্টে কার্লো সিমুলেশন", "Advanced", "lab", "monte-carlo-pi"),
            ("Markov Chains and MCMC", "মার্কভ চেইন ও MCMC", "Advanced", "lesson"),
            ("Spatial Statistics", "স্পেশাল স্ট্যাটিস্টিকস", "Advanced", "lesson"),
        ],
    },
]

TOOLS = [
    ("summary-statistics", "Summary Statistics Lab", "সামারি স্ট্যাটিস্টিকস ল্যাব", "descriptive", "Calculate center, spread, quartiles, shape indicators, and a histogram from a numeric dataset.", "নিউমেরিক ডেটাসেট থেকে কেন্দ্র, বিস্তার, কোয়ার্টাইল, শেপ ইন্ডিকেটর ও হিস্টোগ্রাম হিসাব করুন।"),
    ("weighted-mean", "Weighted Mean Lab", "ওয়েটেড মিন ল্যাব", "descriptive", "Calculate weighted, geometric, and harmonic means with validation and interpretation.", "ভ্যালিডেশন ও ব্যাখ্যাসহ ওয়েটেড, জ্যামিতিক ও হারমোনিক গড় হিসাব করুন।"),
    ("z-score", "Z-score Calculator", "Z-score ক্যালকুলেটর", "descriptive", "Standardize a value and interpret its distance from the mean in standard-deviation units.", "একটি মানকে স্ট্যান্ডার্ডাইজ করুন এবং গড় থেকে স্ট্যান্ডার্ড ডেভিয়েশন এককে দূরত্ব ব্যাখ্যা করুন।"),
    ("percentile-quartile", "Percentile & Quartile Lab", "পার্সেন্টাইল ও কোয়ার্টাইল ল্যাব", "descriptive", "Find percentiles, quartiles, IQR, and percentile ranks using a documented interpolation rule.", "নির্ধারিত ইন্টারপোলেশন নিয়মে পার্সেন্টাইল, কোয়ার্টাইল, IQR ও পার্সেন্টাইল র‍্যাঙ্ক বের করুন।"),
    ("histogram", "Histogram Builder", "হিস্টোগ্রাম বিল্ডার", "descriptive", "Group numeric observations into bins and inspect the distribution shape.", "নিউমেরিক অবজারভেশনকে বিনে ভাগ করে ডিস্ট্রিবিউশনের শেপ দেখুন।"),
    ("box-plot", "Box Plot & Outlier Lab", "বক্স প্লট ও আউটলায়ার ল্যাব", "descriptive", "Compute the five-number summary and flag Tukey 1.5×IQR outliers.", "ফাইভ-নাম্বার সামারি হিসাব করুন এবং Tukey 1.5×IQR নিয়মে আউটলায়ার শনাক্ত করুন।"),
    ("pearson-correlation", "Pearson Correlation Lab", "পিয়ারসন কোরিলেশন ল্যাব", "regression", "Measure linear association between two numeric variables and inspect a scatter plot.", "দুইটি নিউমেরিক ভেরিয়েবলের লিনিয়ার সম্পর্ক পরিমাপ করুন এবং স্ক্যাটার প্লট দেখুন।"),
    ("linear-regression", "Simple Linear Regression Lab", "সিম্পল লিনিয়ার রিগ্রেশন ল্যাব", "regression", "Fit an ordinary least-squares line, inspect R² and residual error, and make a prediction.", "অর্ডিনারি লিস্ট-স্কয়ারস লাইন ফিট করুন, R² ও রেসিডুয়াল এরর দেখুন এবং প্রেডিকশন করুন।"),
    ("normal-probability", "Normal Probability Lab", "নরমাল প্রবাবিলিটি ল্যাব", "probability", "Calculate normal probabilities between bounds and visualize the density curve.", "দুই সীমার মধ্যবর্তী নরমাল প্রবাবিলিটি হিসাব করুন এবং ডেনসিটি কার্ভ দেখুন।"),
    ("binomial-probability", "Binomial Probability Lab", "বাইনোমিয়াল প্রবাবিলিটি ল্যাব", "probability", "Calculate exact, cumulative, and upper-tail binomial probabilities.", "বাইনোমিয়াল ডিস্ট্রিবিউশনের exact, cumulative ও upper-tail প্রবাবিলিটি হিসাব করুন।"),
    ("poisson-probability", "Poisson Probability Lab", "পয়সন প্রবাবিলিটি ল্যাব", "probability", "Calculate event-count probabilities from an expected rate.", "প্রত্যাশিত রেট থেকে event-count প্রবাবিলিটি হিসাব করুন।"),
    ("mean-confidence-interval", "Mean Confidence Interval Lab", "মিন কনফিডেন্স ইন্টারভ্যাল ল্যাব", "inference", "Estimate a population mean with a Student-t confidence interval.", "Student-t কনফিডেন্স ইন্টারভ্যাল দিয়ে পপুলেশন মিন অনুমান করুন।"),
    ("one-sample-t-test", "One-sample t Test Lab", "ওয়ান-স্যাম্পল t টেস্ট ল্যাব", "inference", "Test a sample mean against a hypothesized value and report the two-sided p-value.", "স্যাম্পল মিনকে একটি অনুমিত মানের সঙ্গে টেস্ট করুন এবং two-sided p-value দেখুন।"),
    ("two-sample-t-test", "Welch Two-sample t Test Lab", "Welch টু-স্যাম্পল t টেস্ট ল্যাব", "inference", "Compare two independent means without assuming equal variances.", "সমান ভ্যারিয়েন্স না ধরে দুইটি independent mean তুলনা করুন।"),
    ("chi-square-independence", "Chi-square Independence Lab", "কাই-স্কয়ার ইন্ডিপেনডেন্স ল্যাব", "inference", "Test association in a contingency table and inspect expected counts.", "কন্টিনজেন্সি টেবিলে সম্পর্ক টেস্ট করুন এবং expected count দেখুন।"),
    ("ab-test", "A/B Test for Proportions", "প্রপোরশনের A/B টেস্ট", "analytics", "Compare conversion rates with a pooled two-proportion z test and confidence interval.", "pooled two-proportion z test ও confidence interval দিয়ে conversion rate তুলনা করুন।"),
    ("clt-simulator", "Central Limit Theorem Simulator", "সেন্ট্রাল লিমিট থিওরেম সিমুলেটর", "probability", "Generate sample means and observe convergence toward an approximately normal sampling distribution.", "স্যাম্পল মিন তৈরি করে প্রায় নরমাল স্যাম্পলিং ডিস্ট্রিবিউশনের দিকে কনভার্জেন্স দেখুন।"),
    ("monte-carlo-pi", "Monte Carlo Pi Estimator", "মন্টে কার্লো Pi এস্টিমেটর", "advanced", "Estimate π by random sampling inside a unit square and inspect convergence.", "ইউনিট স্কয়ারে র‍্যান্ডম স্যাম্পলিং দিয়ে π অনুমান করুন এবং কনভার্জেন্স দেখুন।"),
    ("moving-average", "Moving Average Lab", "মুভিং এভারেজ ল্যাব", "analytics", "Smooth a time series with a configurable simple moving-average window.", "কনফিগারযোগ্য simple moving-average window দিয়ে টাইম সিরিজ স্মুথ করুন।"),
    ("sample-size-estimator", "Sample Size Estimator", "স্যাম্পল সাইজ এস্টিমেটর", "inference", "Estimate sample size for a proportion or mean at a chosen confidence and margin of error.", "নির্বাচিত confidence ও margin of error অনুযায়ী proportion বা mean-এর sample size অনুমান করুন।"),
]

FORMULAS = {
    "mean-median-and-mode": ("Mean: x̄ = Σxᵢ / n", "মিন: x̄ = Σxᵢ / n"),
    "weighted-geometric-and-harmonic-means": ("Weighted mean: x̄w = Σ(wᵢxᵢ) / Σwᵢ", "ওয়েটেড মিন: x̄w = Σ(wᵢxᵢ) / Σwᵢ"),
    "quantiles-and-percentiles": ("Linear-interpolation position: h = (n − 1)p", "লিনিয়ার ইন্টারপোলেশন পজিশন: h = (n − 1)p"),
    "range-and-interquartile-range": ("Range = max − min; IQR = Q₃ − Q₁", "রেঞ্জ = সর্বোচ্চ − সর্বনিম্ন; IQR = Q₃ − Q₁"),
    "variance-and-standard-deviation": ("Sample variance: s² = Σ(xᵢ − x̄)² / (n − 1); s = √s²", "স্যাম্পল ভ্যারিয়েন্স: s² = Σ(xᵢ − x̄)² / (n − 1); s = √s²"),
    "coefficient-of-variation": ("CV = s / |x̄| × 100%", "CV = s / |x̄| × 100%"),
    "probability-rules": ("P(A ∪ B) = P(A) + P(B) − P(A ∩ B)", "P(A ∪ B) = P(A) + P(B) − P(A ∩ B)"),
    "conditional-probability": ("P(A | B) = P(A ∩ B) / P(B), when P(B) > 0", "P(A | B) = P(A ∩ B) / P(B), যেখানে P(B) > 0"),
    "bayes-theorem": ("P(A | B) = P(B | A)P(A) / P(B)", "P(A | B) = P(B | A)P(A) / P(B)"),
    "expected-value-and-variance": ("E[X] = ΣxP(X=x); Var(X) = E[(X − μ)²]", "E[X] = ΣxP(X=x); Var(X) = E[(X − μ)²]"),
    "bernoulli-and-binomial-distributions": ("P(X=k) = C(n,k)pᵏ(1−p)ⁿ⁻ᵏ", "P(X=k) = C(n,k)pᵏ(1−p)ⁿ⁻ᵏ"),
    "poisson-distribution": ("P(X=k) = e⁻λ λᵏ / k!", "P(X=k) = e⁻λ λᵏ / k!"),
    "normal-distribution": ("f(x)=1/(σ√(2π)) · exp(−(x−μ)²/(2σ²))", "f(x)=1/(σ√(2π)) · exp(−(x−μ)²/(2σ²))"),
    "central-limit-theorem": ("For large n, (x̄ − μ)/(σ/√n) is approximately standard normal under regularity conditions.", "উপযুক্ত শর্তে বড় n-এর জন্য (x̄ − μ)/(σ/√n) প্রায় standard normal হয়।"),
    "confidence-intervals": ("Estimate ± critical value × standard error", "Estimate ± critical value × standard error"),
    "one-sample-z-and-t-tests": ("t = (x̄ − μ₀)/(s/√n), df = n − 1", "t = (x̄ − μ₀)/(s/√n), df = n − 1"),
    "two-sample-t-test": ("Welch t = (x̄₁ − x̄₂)/√(s₁²/n₁ + s₂²/n₂)", "Welch t = (x̄₁ − x̄₂)/√(s₁²/n₁ + s₂²/n₂)"),
    "chi-square-tests": ("χ² = Σ (Observed − Expected)² / Expected", "χ² = Σ (Observed − Expected)² / Expected"),
    "analysis-of-variance": ("F = variance between groups / variance within groups", "F = গ্রুপগুলোর মধ্যকার ভ্যারিয়েন্স / গ্রুপের ভেতরের ভ্যারিয়েন্স"),
    "covariance-and-correlation": ("r = cov(X,Y)/(sₓsᵧ)", "r = cov(X,Y)/(sₓsᵧ)"),
    "simple-linear-regression": ("ŷ = b₀ + b₁x", "ŷ = b₀ + b₁x"),
    "ordinary-least-squares": ("Choose coefficients that minimize Σ(yᵢ − ŷᵢ)²", "যে coefficient-এ Σ(yᵢ − ŷᵢ)² সর্বনিম্ন হয় সেটি নির্বাচন করা হয়।"),
    "r-squared-and-adjusted-r-squared": ("R² = 1 − SSE/SST", "R² = 1 − SSE/SST"),
    "logistic-regression": ("log(p/(1−p)) = β₀ + β₁x₁ + … + βₖxₖ", "log(p/(1−p)) = β₀ + β₁x₁ + … + βₖxₖ"),
    "moving-averages-and-smoothing": ("SMAₜ = (yₜ + … + yₜ₋w₊₁)/w", "SMAₜ = (yₜ + … + yₜ₋w₊₁)/w"),
    "bootstrap": ("Repeatedly resample n observations with replacement and summarize the resampled statistic.", "replacement সহ n observation বারবার resample করে statistic-এর distribution তৈরি করা হয়।"),
    "principal-component-analysis": ("Principal components are eigenvector directions of the covariance/correlation matrix.", "Principal component হলো covariance/correlation matrix-এর eigenvector direction।"),
    "k-means-clustering": ("Minimize within-cluster sum of squared distances to cluster centroids.", "ক্লাস্টার centroid থেকে within-cluster squared distance-এর যোগফল সর্বনিম্ন করা হয়।"),
    "monte-carlo-simulation": ("Approximate an expectation or probability by repeated random sampling.", "বারবার random sampling করে expectation বা probability আনুমানিক হিসাব করা হয়।"),
    "kaplan-meier-estimation": ("Ŝ(t) = ∏(1 − dᵢ/nᵢ) over event times tᵢ ≤ t", "Ŝ(t) = ∏(1 − dᵢ/nᵢ), যেখানে event time tᵢ ≤ t"),
    "cox-proportional-hazards-model": ("h(t|x)=h₀(t)exp(βᵀx)", "h(t|x)=h₀(t)exp(βᵀx)"),
}

MODULE_CONTEXT = {
    "foundations": ("survey and operational data", "সার্ভে ও অপারেশনাল ডেটা"),
    "descriptive": ("sales, quality, and performance datasets", "সেলস, কোয়ালিটি ও পারফরম্যান্স ডেটাসেট"),
    "probability": ("uncertain events, counts, and waiting times", "অনিশ্চিত ঘটনা, কাউন্ট ও অপেক্ষার সময়"),
    "inference": ("samples, experiments, and evidence-based decisions", "স্যাম্পল, এক্সপেরিমেন্ট ও প্রমাণভিত্তিক সিদ্ধান্ত"),
    "regression": ("relationships and prediction problems", "সম্পর্ক ও প্রেডিকশন সমস্যা"),
    "analytics": ("business performance and customer behavior", "ব্যবসায়িক পারফরম্যান্স ও কাস্টমার আচরণ"),
    "data-science": ("machine-learning datasets and model evaluation", "মেশিন লার্নিং ডেটাসেট ও মডেল মূল্যায়ন"),
    "data-engineering": ("reliable analytical data pipelines", "নির্ভরযোগ্য অ্যানালিটিক্যাল ডেটা পাইপলাইন"),
    "advanced": ("research, experimentation, and complex data structures", "গবেষণা, এক্সপেরিমেন্ট ও জটিল ডেটা স্ট্রাকচার"),
}

COMMON_MISTAKES = {
    "foundations": ("Treating a convenient sample as representative; mixing measurement scales; ignoring how data was generated.", "সুবিধাজনক স্যাম্পলকে প্রতিনিধিত্বশীল ধরা, measurement scale গুলিয়ে ফেলা এবং ডেটা কীভাবে তৈরি হয়েছে তা উপেক্ষা করা।"),
    "descriptive": ("Reporting only an average; hiding distribution shape; comparing spreads without considering scale.", "শুধু গড় রিপোর্ট করা, ডিস্ট্রিবিউশনের শেপ লুকিয়ে ফেলা এবং স্কেল বিবেচনা না করে বিস্তার তুলনা করা।"),
    "probability": ("Confusing independence with mutual exclusivity; using the wrong distribution; interpreting probability as certainty.", "independence ও mutual exclusivity গুলিয়ে ফেলা, ভুল distribution ব্যবহার এবং probability-কে নিশ্চয়তা হিসেবে ধরা।"),
    "inference": ("Equating non-significance with no effect; ignoring assumptions; focusing on p-values without effect size and uncertainty.", "non-significance-কে effect নেই বলা, assumption উপেক্ষা এবং effect size ও uncertainty বাদ দিয়ে শুধু p-value দেখা।"),
    "regression": ("Interpreting association as causation; extrapolating beyond observed data; ignoring residuals and leakage.", "association-কে causation বলা, observed range-এর বাইরে extrapolate করা এবং residual ও leakage উপেক্ষা করা।"),
    "analytics": ("Using unstable KPI definitions; changing experiment rules after seeing results; reporting charts without decisions.", "অস্থিতিশীল KPI definition ব্যবহার, ফল দেখার পর experiment rule বদলানো এবং সিদ্ধান্ত ছাড়া chart রিপোর্ট করা।"),
    "data-science": ("Fitting preprocessing on the full dataset; optimizing only one metric; ignoring class imbalance and calibration.", "পুরো dataset-এ preprocessing fit করা, শুধু একটি metric optimize এবং class imbalance ও calibration উপেক্ষা করা।"),
    "data-engineering": ("Treating schema changes as harmless; skipping data tests; building pipelines without ownership, lineage, or recovery plans.", "schema change-কে harmless ধরা, data test বাদ দেওয়া এবং ownership, lineage বা recovery plan ছাড়া pipeline তৈরি করা।"),
    "advanced": ("Using complex methods without checking identifiability, assumptions, censoring, dependence, or model diagnostics.", "identifiability, assumption, censoring, dependence বা model diagnostic যাচাই ছাড়া complex method ব্যবহার করা।"),
}

GLOSSARY = [
    ("Accuracy", "অ্যাকিউরেসি", "The proportion of all predictions that are correct.", "সব prediction-এর মধ্যে সঠিক prediction-এর অনুপাত।"),
    ("Alternative hypothesis", "অল্টারনেটিভ হাইপোথিসিস", "The claim considered when evidence is inconsistent with the null hypothesis.", "null hypothesis-এর সঙ্গে evidence অসামঞ্জস্য হলে যে claim বিবেচনা করা হয়।"),
    ("Bias", "বায়াস", "A systematic tendency for an estimate or process to differ from the target.", "কোনো estimate বা process-এর target থেকে পদ্ধতিগতভাবে সরে যাওয়ার প্রবণতা।"),
    ("Categorical variable", "ক্যাটেগরিক্যাল ভেরিয়েবল", "A variable whose values represent groups or labels.", "যে ভেরিয়েবলের মান group বা label প্রকাশ করে।"),
    ("Central limit theorem", "সেন্ট্রাল লিমিট থিওরেম", "A result describing when standardized sample means are approximately normal.", "কখন standardized sample mean প্রায় normal হয় তা ব্যাখ্যা করা ফলাফল।"),
    ("Confidence interval", "কনফিডেন্স ইন্টারভ্যাল", "A procedure that produces a range of plausible parameter values at a stated confidence level.", "নির্দিষ্ট confidence level-এ plausible parameter value-এর range তৈরির procedure।"),
    ("Confounder", "কনফাউন্ডার", "A variable related to both an exposure and an outcome that can distort their association.", "exposure ও outcome উভয়ের সঙ্গে সম্পর্কিত variable, যা তাদের association বিকৃত করতে পারে।"),
    ("Correlation", "কোরিলেশন", "A standardized measure of association; it does not by itself establish causation.", "association-এর standardized measure; এটি নিজে causation প্রমাণ করে না।"),
    ("Covariance", "কোভ্যারিয়েন্স", "A measure of how two variables vary together, expressed in product units.", "দুই variable একসঙ্গে কীভাবে পরিবর্তিত হয় তার measure, product unit-এ প্রকাশিত।"),
    ("Cross-validation", "ক্রস-ভ্যালিডেশন", "A resampling method for estimating out-of-sample model performance.", "out-of-sample model performance অনুমানের resampling method।"),
    ("Data lineage", "ডেটা লিনিয়েজ", "A record of where data came from, how it changed, and where it is used.", "ডেটা কোথা থেকে এসেছে, কীভাবে বদলেছে এবং কোথায় ব্যবহৃত হয়েছে তার রেকর্ড।"),
    ("Distribution", "ডিস্ট্রিবিউশন", "The pattern of possible values and their frequencies or probabilities.", "সম্ভাব্য মান এবং তাদের frequency বা probability-এর pattern।"),
    ("Effect size", "ইফেক্ট সাইজ", "A quantitative measure of the magnitude of a difference or relationship.", "difference বা relationship-এর magnitude-এর quantitative measure।"),
    ("ELT", "ELT", "Extract, load, then transform data inside the target analytical system.", "ডেটা extract ও load করার পর target analytical system-এর ভেতরে transform করা।"),
    ("ETL", "ETL", "Extract, transform, then load data into a target system.", "ডেটা extract, transform এবং পরে target system-এ load করা।"),
    ("Expected value", "এক্সপেক্টেড ভ্যালু", "The probability-weighted long-run average of a random variable.", "random variable-এর probability-weighted long-run average।"),
    ("Feature", "ফিচার", "An input variable used by an analytical or machine-learning model.", "analytical বা machine-learning model-এ ব্যবহৃত input variable।"),
    ("Hypothesis test", "হাইপোথিসিস টেস্ট", "A rule-based procedure for evaluating evidence about a population claim.", "population claim সম্পর্কে evidence মূল্যায়নের rule-based procedure।"),
    ("Interquartile range", "ইন্টারকোয়ার্টাইল রেঞ্জ", "Q3 minus Q1; the spread of the middle 50% of observations.", "Q3 − Q1; মাঝের ৫০% observation-এর spread।"),
    ("Mean", "মিন", "The arithmetic average of numeric observations.", "নিউমেরিক observation-এর arithmetic average।"),
    ("Median", "মিডিয়ান", "The middle value after sorting, or the average of two middle values for even n.", "sort করার পর মাঝের মান; even n হলে দুই মাঝের মানের average।"),
    ("Null hypothesis", "নাল হাইপোথিসিস", "The reference claim tested by a statistical procedure.", "statistical procedure দিয়ে test করা reference claim।"),
    ("Outlier", "আউটলায়ার", "An observation unusually far from the main body of data; it is not automatically an error.", "ডেটার মূল অংশ থেকে অস্বাভাবিক দূরের observation; এটি স্বয়ংক্রিয়ভাবে error নয়।"),
    ("p-value", "পি-ভ্যালু", "Under the null model, the probability of a result at least as incompatible with the null as the observed result.", "null model সত্য ধরে observed result-এর মতো বা তার চেয়ে বেশি incompatible result পাওয়ার probability।"),
    ("Parameter", "প্যারামিটার", "A fixed but usually unknown numerical characteristic of a population or model.", "population বা model-এর fixed কিন্তু সাধারণত unknown numerical characteristic।"),
    ("Population", "পপুলেশন", "The complete set of units or outcomes targeted by an analysis.", "analysis যে সম্পূর্ণ set of units বা outcomes-কে target করে।"),
    ("Precision", "প্রিসিশন", "For classification, the proportion of positive predictions that are truly positive.", "classification-এ positive prediction-এর মধ্যে সত্যিকারের positive-এর অনুপাত।"),
    ("Probability", "প্রবাবিলিটি", "A number from 0 to 1 representing uncertainty under a specified model.", "নির্দিষ্ট model-এ uncertainty প্রকাশকারী ০ থেকে ১-এর একটি সংখ্যা।"),
    ("Quantile", "কোয়ান্টাইল", "A cut point that divides an ordered distribution at a chosen cumulative probability.", "ordered distribution-কে নির্দিষ্ট cumulative probability-এ ভাগ করা cut point।"),
    ("R-squared", "R-squared", "The proportion of outcome variation explained by a fitted regression model relative to a baseline mean model.", "baseline mean model-এর তুলনায় fitted regression model outcome variation-এর যে অনুপাত ব্যাখ্যা করে।"),
    ("Recall", "রিকল", "The proportion of actual positive cases correctly identified.", "actual positive case-এর মধ্যে সঠিকভাবে শনাক্ত positive-এর অনুপাত।"),
    ("Regression", "রিগ্রেশন", "A family of models for describing conditional relationships between outcomes and predictors.", "outcome ও predictor-এর conditional relationship বর্ণনার model family।"),
    ("Residual", "রেসিডুয়াল", "Observed outcome minus the model's fitted value.", "observed outcome − model-এর fitted value।"),
    ("Sample", "স্যাম্পল", "A subset of units observed from a target population.", "target population থেকে observed unit-এর subset।"),
    ("Sampling distribution", "স্যাম্পলিং ডিস্ট্রিবিউশন", "The distribution of a statistic across repeated samples under a sampling process.", "sampling process-এ repeated sample জুড়ে একটি statistic-এর distribution।"),
    ("Standard deviation", "স্ট্যান্ডার্ড ডেভিয়েশন", "The square root of variance, expressed in the original measurement unit.", "variance-এর square root, original measurement unit-এ প্রকাশিত।"),
    ("Standard error", "স্ট্যান্ডার্ড এরর", "The standard deviation of an estimator's sampling distribution.", "একটি estimator-এর sampling distribution-এর standard deviation।"),
    ("Statistic", "স্ট্যাটিস্টিক", "A numerical summary calculated from sample data.", "sample data থেকে হিসাব করা numerical summary।"),
    ("Variance", "ভ্যারিয়েন্স", "The average squared deviation from a mean, with population or sample conventions.", "mean থেকে squared deviation-এর average, population বা sample convention অনুযায়ী।"),
    ("Warehouse", "ডেটা ওয়্যারহাউস", "A managed analytical store optimized for structured querying and reporting.", "structured query ও reporting-এর জন্য optimized managed analytical store।"),
]

PATHS = [
    {
        "id": "data-analyst",
        "title_en": "Data Analyst Path",
        "title_bn": "ডেটা অ্যানালিস্ট পাথ",
        "description_en": "From data literacy to EDA, inference, regression, business metrics, experiments, and storytelling.",
        "description_bn": "ডেটা লিটারেসি থেকে EDA, inference, regression, business metric, experiment ও storytelling পর্যন্ত।",
        "topics": [
            "statistics-and-data", "categorical-and-numerical-data", "frequency-tables", "mean-median-and-mode",
            "variance-and-standard-deviation", "histograms", "box-plots", "exploratory-data-analysis",
            "confidence-intervals", "hypothesis-testing-framework", "pearson-and-spearman-correlation",
            "simple-linear-regression", "kpi-design", "cohort-analysis", "funnel-analysis", "a-b-testing",
            "moving-averages-and-smoothing", "data-storytelling"
        ],
    },
    {
        "id": "data-scientist",
        "title_en": "Data Scientist Path",
        "title_bn": "ডেটা সায়েন্টিস্ট পাথ",
        "description_en": "Probability, inference, modeling, resampling, feature preparation, clustering, Bayesian and causal reasoning.",
        "description_bn": "probability, inference, modeling, resampling, feature preparation, clustering, Bayesian ও causal reasoning।",
        "topics": [
            "probability-rules", "conditional-probability", "random-variables", "normal-distribution",
            "central-limit-theorem", "confidence-intervals", "type-i-type-ii-errors-and-power",
            "simple-linear-regression", "multiple-linear-regression", "logistic-regression",
            "model-validation", "bootstrap", "cross-validation", "bias-variance-trade-off",
            "feature-engineering", "principal-component-analysis", "k-means-clustering",
            "classification-metrics", "bayesian-inference", "causal-inference"
        ],
    },
    {
        "id": "data-engineer",
        "title_en": "Data Engineer Path",
        "title_bn": "ডেটা ইঞ্জিনিয়ার পাথ",
        "description_en": "Build statistical literacy, then focus on data modeling, SQL, transformations, quality, orchestration, lineage, and semantic layers.",
        "description_bn": "statistical literacy তৈরি করে data modeling, SQL, transformation, quality, orchestration, lineage ও semantic layer-এ এগিয়ে যান।",
        "topics": [
            "statistics-and-data", "data-quality-dimensions", "reproducible-statistical-workflow",
            "data-formats-csv-json-and-parquet", "relational-data-modeling", "sql-for-analytics",
            "normalization-and-denormalization", "etl-and-elt", "batch-and-streaming-data",
            "warehouse-lake-and-lakehouse", "dimensional-modeling-and-star-schemas",
            "data-quality-testing", "pipeline-orchestration", "data-lineage-and-governance",
            "analytics-engineering-and-semantic-layers"
        ],
    },
    {
        "id": "research-business",
        "title_en": "Research & Business Decision Path",
        "title_bn": "রিসার্চ ও বিজনেস ডিসিশন পাথ",
        "description_en": "Sampling, measurement, uncertainty, experiments, group comparisons, regression, forecasting, and defensible communication.",
        "description_bn": "sampling, measurement, uncertainty, experiment, group comparison, regression, forecasting ও defensible communication।",
        "topics": [
            "population-and-sample", "measurement-scales", "data-collection-methods",
            "probability-and-non-probability-sampling", "sampling-bias-and-confounding",
            "exploratory-data-analysis-workflow", "confidence-intervals", "hypothesis-testing-framework",
            "tests-for-proportions", "chi-square-tests", "analysis-of-variance",
            "simple-linear-regression", "a-b-testing", "forecast-evaluation", "data-storytelling",
            "experimental-design", "causal-inference"
        ],
    },
]


def build_content() -> dict:
    modules = []
    topics = []
    order = 1
    for module in MODULES:
        module_topics = []
        context_en, context_bn = MODULE_CONTEXT[module["id"]]
        for item in module["topics"]:
            title_en, title_bn, difficulty, kind, *rest = item
            lab = rest[0] if rest else None
            slug = slugify(title_en)
            formula_en, formula_bn = FORMULAS.get(
                slug,
                (
                    "This topic is primarily conceptual or procedural; no single universal equation defines it.",
                    "এটি প্রধানত conceptual বা procedural topic; একক কোনো universal equation দিয়ে পুরো বিষয়টি সংজ্ঞায়িত হয় না।",
                ),
            )
            summary_en, summary_bn = TOPIC_DETAILS[title_en]
            example_en = f"A practitioner uses {title_en.lower()} to examine a small {context_en} example, checks the method's assumptions, calculates or organizes the required quantities, and explains what the result supports—and what it does not support."
            example_bn = f"একজন practitioner একটি ছোট {context_bn} উদাহরণে {title_bn} ব্যবহার করেন, method-এর assumption যাচাই করেন, প্রয়োজনীয় quantity হিসাব বা সংগঠিত করেন এবং ফলাফল কী সমর্থন করে ও কী করে না তা ব্যাখ্যা করেন।"
            topic = {
                "id": slug,
                "order": order,
                "module": module["id"],
                "title_en": title_en,
                "title_bn": title_bn,
                "summary_en": summary_en,
                "summary_bn": summary_bn,
                "difficulty": difficulty,
                "kind": kind,
                "minutes": 20 if difficulty == "Beginner" else 35 if difficulty == "Intermediate" else 50,
                "formula_en": formula_en,
                "formula_bn": formula_bn,
                "example_en": example_en,
                "example_bn": example_bn,
                "mistakes_en": COMMON_MISTAKES[module["id"]][0],
                "mistakes_bn": COMMON_MISTAKES[module["id"]][1],
                "lab": lab,
                "url": f"topics/{slug}/",
            }
            topics.append(topic)
            module_topics.append(slug)
            order += 1
        modules.append({k: v for k, v in module.items() if k != "topics"} | {"topics": module_topics})

    tools = [
        {
            "id": slug,
            "title_en": en,
            "title_bn": bn,
            "module": module,
            "description_en": desc_en,
            "description_bn": desc_bn,
            "url": f"tools/{slug}/",
        }
        for slug, en, bn, module, desc_en, desc_bn in TOOLS
    ]
    return {"modules": modules, "topics": topics, "tools": tools, "paths": PATHS, "glossary": [
        {"term_en": a, "term_bn": b, "definition_en": c, "definition_bn": d} for a,b,c,d in GLOSSARY
    ]}


def icon_svg(name: str) -> str:
    # Kept intentionally simple; interface icons are rendered by site.js.
    return ""


def html_shell(*, title: str, description: str, page: str, base: str = "", body_attrs: str = "", extra_scripts: str = "", main_html: str = "") -> str:
    canonical = f"{SITE_URL}/{base}" if base else f"{SITE_URL}/"
    return f"""<!doctype html>
<html lang="en" data-theme="light">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{escape(description)}">
  <meta name="theme-color" content="#6d5dfc">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:image" content="{SITE_URL}/assets/icons/social-card.svg">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" href="/assets/icons/favicon.svg" type="image/svg+xml">
  <link rel="manifest" href="/manifest.webmanifest">
  <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
  <script src="/assets/js/theme-init.js"></script>
  <link rel="stylesheet" href="/assets/css/main.css">
  <title>{escape(title)}</title>
</head>
<body data-page="{page}" {body_attrs}>
  <a class="skip-link" href="#main-content">Skip to content</a>
  <div id="site-header"></div>
  <main id="main-content" tabindex="-1">{main_html}</main>
  <div id="site-footer"></div>
  <div id="search-root"></div>
  <button class="scroll-top" id="scroll-top" type="button" aria-label="Scroll to top" title="Scroll to top">↑</button>
  <script src="/assets/js/content.js"></script>
  <script src="/assets/js/site.js" defer></script>
  {extra_scripts}
</body>
</html>
"""


def write_pages(data: dict) -> None:
    # Home
    home_main = """
<section class="hero home-hero">
  <div class="container hero-grid">
    <div class="hero-copy reveal">
      <span class="eyebrow" data-en="Free, bilingual and browser-based" data-bn="বিনামূল্যে, দ্বিভাষিক ও ব্রাউজারভিত্তিক">Free, bilingual and browser-based</span>
      <h1 data-en="Learn statistics by understanding, calculating and experimenting." data-bn="বোঝা, হিসাব ও এক্সপেরিমেন্টের মাধ্যমে পরিসংখ্যান শিখুন।">Learn statistics by understanding, calculating and experimenting.</h1>
      <p data-en="A complete static learning hub for future data analysts, data scientists, data engineers, researchers and evidence-driven professionals." data-bn="ভবিষ্যৎ ডেটা অ্যানালিস্ট, ডেটা সায়েন্টিস্ট, ডেটা ইঞ্জিনিয়ার, গবেষক ও প্রমাণভিত্তিক পেশাজীবীদের জন্য একটি পূর্ণাঙ্গ স্ট্যাটিক লার্নিং হাব।">A complete static learning hub for future data analysts, data scientists, data engineers, researchers and evidence-driven professionals.</p>
      <div class="hero-actions">
        <a class="button primary" href="/paths/" data-en="Choose a learning path" data-bn="লার্নিং পাথ বেছে নিন">Choose a learning path</a>
        <a class="button ghost" href="/tools/" data-en="Open interactive labs" data-bn="ইন্টারঅ্যাকটিভ ল্যাব খুলুন">Open interactive labs</a>
      </div>
      <div class="hero-proof" id="hero-stats"></div>
    </div>
    <div class="hero-visual reveal" aria-label="Statistics learning dashboard preview">
      <div class="visual-orbit orbit-one"></div><div class="visual-orbit orbit-two"></div>
      <div class="preview-card preview-main"><span>μ</span><strong data-en="From data to decisions" data-bn="ডেটা থেকে সিদ্ধান্ত">From data to decisions</strong><small data-en="Theory · labs · practice · career paths" data-bn="থিওরি · ল্যাব · প্র্যাকটিস · ক্যারিয়ার পাথ">Theory · labs · practice · career paths</small></div>
      <div class="preview-card preview-float a"><span>σ</span><small>Spread</small></div>
      <div class="preview-card preview-float b"><span>r</span><small>Relation</small></div>
      <div class="preview-card preview-float c"><span>p</span><small>Evidence</small></div>
    </div>
  </div>
</section>
<section class="section"><div class="container"><div class="section-heading"><div><span class="eyebrow" data-en="Structured curriculum" data-bn="স্ট্রাকচার্ড কারিকুলাম">Structured curriculum</span><h2 data-en="Nine modules from first principles to advanced methods" data-bn="প্রাথমিক ধারণা থেকে অ্যাডভান্সড মেথড পর্যন্ত নয়টি মডিউল">Nine modules from first principles to advanced methods</h2></div><a href="/catalog/" class="text-link" data-en="Browse all lessons →" data-bn="সব লেসন দেখুন →">Browse all lessons →</a></div><div id="module-grid" class="card-grid modules-grid"></div></div></section>
<section class="section section-muted"><div class="container"><div class="section-heading"><div><span class="eyebrow" data-en="Practice in the browser" data-bn="ব্রাউজারেই প্র্যাকটিস">Practice in the browser</span><h2 data-en="Interactive statistical labs with transparent methods" data-bn="স্বচ্ছ পদ্ধতিসহ ইন্টারঅ্যাকটিভ স্ট্যাটিস্টিক্যাল ল্যাব">Interactive statistical labs with transparent methods</h2></div><a href="/tools/" class="text-link" data-en="View every lab →" data-bn="সব ল্যাব দেখুন →">View every lab →</a></div><div id="featured-tools" class="card-grid tool-grid"></div></div></section>
<section class="section"><div class="container"><div class="section-heading center"><div><span class="eyebrow" data-en="Career-oriented learning" data-bn="ক্যারিয়ারভিত্তিক শেখা">Career-oriented learning</span><h2 data-en="Follow a path built around your goal" data-bn="আপনার লক্ষ্য অনুযায়ী তৈরি পাথ অনুসরণ করুন">Follow a path built around your goal</h2></div></div><div id="featured-paths" class="path-grid"></div></div></section>
<section class="section final-cta"><div class="container cta-card"><div><span class="eyebrow" data-en="Private by design" data-bn="ডিজাইনেই প্রাইভেট">Private by design</span><h2 data-en="Your inputs and progress stay in your browser." data-bn="আপনার ইনপুট ও অগ্রগতি আপনার ব্রাউজারেই থাকে।">Your inputs and progress stay in your browser.</h2><p data-en="The site has no account, backend, database or tracking API. Calculator inputs are processed locally, and optional progress is saved with localStorage." data-bn="সাইটে account, backend, database বা tracking API নেই। Calculator input locally process হয় এবং optional progress localStorage-এ সংরক্ষিত থাকে।">The site has no account, backend, database or tracking API. Calculator inputs are processed locally, and optional progress is saved with localStorage.</p></div><a class="button primary" href="/about/" data-en="How the hub works" data-bn="হাব কীভাবে কাজ করে">How the hub works</a></div></section>
"""
    (ROOT / "index.html").write_text(html_shell(title="Statistics Learning Hub", description="A modern English-first, bilingual statistics, data analytics, data science and data engineering learning hub.", page="home", main_html=home_main), encoding="utf-8")

    catalog_main = """
<section class="page-hero compact"><div class="container"><span class="eyebrow" data-en="Curriculum catalog" data-bn="কারিকুলাম ক্যাটালগ">Curriculum catalog</span><h1 data-en="Explore every lesson" data-bn="সব লেসন এক্সপ্লোর করুন">Explore every lesson</h1><p data-en="Filter by module, level and learning format. Every published card opens a complete page." data-bn="মডিউল, লেভেল ও শেখার ধরন অনুযায়ী ফিল্টার করুন। প্রতিটি প্রকাশিত কার্ড একটি পূর্ণাঙ্গ পেজ খুলবে।">Filter by module, level and learning format. Every published card opens a complete page.</p></div></section>
<section class="section"><div class="container"><div class="filter-panel"><label class="search-field"><span class="sr-only">Search lessons</span><input id="catalog-search" type="search" placeholder="Search lessons, formulas or topics…" data-placeholder-en="Search lessons, formulas or topics…" data-placeholder-bn="লেসন, ফর্মুলা বা টপিক খুঁজুন…"><span>⌕</span></label><select id="module-filter" aria-label="Filter by module"></select><select id="difficulty-filter" aria-label="Filter by difficulty"><option value="all">All levels</option><option>Beginner</option><option>Intermediate</option><option>Advanced</option></select><select id="kind-filter" aria-label="Filter by format"><option value="all">All formats</option><option value="lesson">Lesson</option><option value="lab">Lab-linked</option><option value="practice">Practice</option></select></div><div class="result-line"><strong id="catalog-count"></strong><button class="button small ghost" id="clear-filters" type="button" data-en="Clear filters" data-bn="ফিল্টার মুছুন">Clear filters</button></div><div id="catalog-grid" class="card-grid lesson-grid"></div></div></section>
"""
    (ROOT / "catalog" / "index.html").write_text(html_shell(title="Lesson Catalog | Statistics Learning Hub", description="Browse all statistics, analytics, data science and data engineering lessons.", page="catalog", base="catalog/", main_html=catalog_main, extra_scripts='<script src="/assets/js/catalog.js" defer></script>'), encoding="utf-8")

    paths_main = """
<section class="page-hero compact"><div class="container"><span class="eyebrow" data-en="Career learning paths" data-bn="ক্যারিয়ার লার্নিং পাথ">Career learning paths</span><h1 data-en="Learn in the order your goal requires" data-bn="আপনার লক্ষ্য অনুযায়ী প্রয়োজনীয় ক্রমে শিখুন">Learn in the order your goal requires</h1><p data-en="Each path is a curated sequence. Progress is stored only in your browser and can be reset at any time." data-bn="প্রতিটি পাথ একটি curated sequence। progress শুধু আপনার browser-এ থাকে এবং যেকোনো সময় reset করা যায়।">Each path is a curated sequence. Progress is stored only in your browser and can be reset at any time.</p></div></section>
<section class="section"><div class="container"><div id="paths-grid" class="paths-stack"></div></div></section>
"""
    (ROOT / "paths" / "index.html").write_text(html_shell(title="Learning Paths | Statistics Learning Hub", description="Career-oriented learning paths for data analysts, data scientists, data engineers and researchers.", page="paths", base="paths/", main_html=paths_main, extra_scripts='<script src="/assets/js/paths.js" defer></script>'), encoding="utf-8")

    tools_main = """
<section class="page-hero compact"><div class="container"><span class="eyebrow" data-en="Interactive labs" data-bn="ইন্টারঅ্যাকটিভ ল্যাব">Interactive labs</span><h1 data-en="Calculate, visualize and interpret" data-bn="হিসাব, ভিজ্যুয়ালাইজ ও ব্যাখ্যা করুন">Calculate, visualize and interpret</h1><p data-en="Every lab runs locally in your browser. Inputs are validated, methods are stated, and results include interpretation guidance." data-bn="প্রতিটি ল্যাব আপনার browser-এ locally run করে। input validate করা হয়, method উল্লেখ থাকে এবং result-এর সঙ্গে interpretation guidance দেওয়া হয়।">Every lab runs locally in your browser. Inputs are validated, methods are stated, and results include interpretation guidance.</p></div></section>
<section class="section"><div class="container"><div class="filter-panel"><label class="search-field"><span class="sr-only">Search labs</span><input id="tool-search" type="search" placeholder="Search interactive labs…" data-placeholder-en="Search interactive labs…" data-placeholder-bn="ইন্টারঅ্যাকটিভ ল্যাব খুঁজুন…"><span>⌕</span></label><select id="tool-module-filter" aria-label="Filter labs by module"></select></div><div id="tools-grid" class="card-grid tool-grid"></div></div></section>
"""
    (ROOT / "tools" / "index.html").write_text(html_shell(title="Interactive Labs | Statistics Learning Hub", description="Browser-based statistics calculators, simulations and visualizers.", page="tools", base="tools/", main_html=tools_main, extra_scripts='<script src="/assets/js/tools-index.js" defer></script>'), encoding="utf-8")

    glossary_main = """
<section class="page-hero compact"><div class="container"><span class="eyebrow" data-en="Bilingual glossary" data-bn="দ্বিভাষিক গ্লসারি">Bilingual glossary</span><h1 data-en="Essential statistics and data terms" data-bn="পরিসংখ্যান ও ডেটার প্রয়োজনীয় পরিভাষা">Essential statistics and data terms</h1><p data-en="Concise definitions for study and revision. Technical terms retain their standard meaning across both languages." data-bn="পড়া ও রিভিশনের জন্য সংক্ষিপ্ত সংজ্ঞা। দুই ভাষাতেই technical term-এর standard meaning বজায় রাখা হয়েছে।">Concise definitions for study and revision. Technical terms retain their standard meaning across both languages.</p></div></section>
<section class="section"><div class="container"><label class="search-field glossary-search"><span class="sr-only">Search glossary</span><input id="glossary-search" type="search" placeholder="Search a term…" data-placeholder-en="Search a term…" data-placeholder-bn="একটি term খুঁজুন…"><span>⌕</span></label><div id="glossary-list" class="glossary-list"></div></div></section>
"""
    (ROOT / "glossary" / "index.html").write_text(html_shell(title="Glossary | Statistics Learning Hub", description="A bilingual glossary of essential statistics, analytics, data science and data engineering terms.", page="glossary", base="glossary/", main_html=glossary_main, extra_scripts='<script src="/assets/js/glossary.js" defer></script>'), encoding="utf-8")

    about_main = """
<section class="page-hero compact"><div class="container"><span class="eyebrow" data-en="About the project" data-bn="প্রজেক্ট সম্পর্কে">About the project</span><h1 data-en="An original static learning product" data-bn="একটি original static learning product">An original static learning product</h1><p data-en="Designed for learners who need clear theory, transparent calculations, practical context, and a route toward data careers." data-bn="যেসব learner-এর clear theory, transparent calculation, practical context এবং data career-এর route প্রয়োজন তাদের জন্য ডিজাইন করা।">Designed for learners who need clear theory, transparent calculations, practical context, and a route toward data careers.</p></div></section>
<section class="section"><div class="container prose-layout"><article class="prose-card"><h2 data-en="What this hub provides" data-bn="এই হাব কী দেয়">What this hub provides</h2><p data-en="The hub combines a structured curriculum, bilingual lesson pages, interactive browser-based labs, career paths, a glossary, search, bookmarks and local progress. It uses no backend, database or external data API." data-bn="এই হাব structured curriculum, bilingual lesson page, interactive browser-based lab, career path, glossary, search, bookmark ও local progress একত্র করেছে। এতে backend, database বা external data API নেই।">The hub combines a structured curriculum, bilingual lesson pages, interactive browser-based labs, career paths, a glossary, search, bookmarks and local progress. It uses no backend, database or external data API.</p><h2 data-en="Content standard" data-bn="কন্টেন্ট স্ট্যান্ডার্ড">Content standard</h2><p data-en="Lessons distinguish description from inference, association from causation, and model output from real-world decisions. Labs state their convention, validate input, and avoid presenting statistical significance as practical importance." data-bn="Lesson-এ description ও inference, association ও causation এবং model output ও real-world decision আলাদা করা হয়েছে। Lab-এ convention বলা হয়, input validate করা হয় এবং statistical significance-কে practical importance হিসেবে দেখানো হয় না।">Lessons distinguish description from inference, association from causation, and model output from real-world decisions. Labs state their convention, validate input, and avoid presenting statistical significance as practical importance.</p><h2 data-en="Privacy" data-bn="প্রাইভেসি">Privacy</h2><p data-en="Calculator data never leaves the page. Bookmarks, language, theme and lesson completion are optional browser-local preferences stored with localStorage." data-bn="Calculator data page-এর বাইরে যায় না। bookmark, language, theme ও lesson completion optional browser-local preference হিসেবে localStorage-এ থাকে।">Calculator data never leaves the page. Bookmarks, language, theme and lesson completion are optional browser-local preferences stored with localStorage.</p></article><aside class="credit-card"><span class="eyebrow">Credits</span><h2>Saiful Islam</h2><p data-en="Idea and developed by Saiful Islam." data-bn="Idea and developed by Saiful Islam.">Idea and developed by Saiful Islam.</p><div class="credit-links"><a href="https://saifulshuvo.com" target="_blank" rel="noopener noreferrer">Website ↗</a><a href="https://github.com/SaifulIslamDS/" target="_blank" rel="noopener noreferrer">GitHub ↗</a><a href="https://www.linkedin.com/in/saifulislampro/" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a></div><hr><p class="small" data-en="Conceptually inspired by a public statistics learning repository. This rebuild uses original architecture, interface and educational copy." data-bn="একটি public statistics learning repository থেকে conceptually inspired। এই rebuild-এর architecture, interface ও educational copy original।">Conceptually inspired by a public statistics learning repository. This rebuild uses original architecture, interface and educational copy.</p><a href="https://github.com/tafshir027/stats" target="_blank" rel="noopener noreferrer">Original inspiration ↗</a></aside></div></section>
"""
    (ROOT / "about" / "index.html").write_text(html_shell(title="About | Statistics Learning Hub", description="About the Statistics Learning Hub, its learning model, privacy approach and credits.", page="about", base="about/", main_html=about_main), encoding="utf-8")

    topic_by_id = {t["id"]: t for t in data["topics"]}
    module_by_id = {m["id"]: m for m in data["modules"]}
    for topic in data["topics"]:
        module = module_by_id[topic["module"]]
        topic_dir = ROOT / "topics" / topic["id"]
        topic_dir.mkdir(parents=True, exist_ok=True)
        static_main = f"""
<section class="topic-shell" id="topic-app">
  <div class="container">
    <nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><a href="/catalog/">Catalog</a><span>/</span><span>{escape(topic['title_en'])}</span></nav>
    <header class="topic-hero">
      <div><span class="eyebrow">{escape(module['title_en'])}</span><h1>{escape(topic['title_en'])}</h1><p>{escape(topic['summary_en'])}</p></div>
      <div class="topic-actions"><button class="icon-action" id="bookmark-topic" type="button" aria-label="Bookmark lesson" title="Bookmark">☆</button><button class="button primary" id="complete-topic" type="button">Mark complete</button></div>
    </header>
    <div id="topic-content"></div>
  </div>
</section>"""
        extra = '<script src="/assets/js/topic.js" defer></script>'
        (topic_dir / "index.html").write_text(html_shell(title=f"{topic['title_en']} | Statistics Learning Hub", description=topic["summary_en"], page="topic", base=f"topics/{topic['id']}/", body_attrs=f'data-topic="{topic["id"]}"', main_html=static_main, extra_scripts=extra), encoding="utf-8")

    tool_by_id = {t["id"]: t for t in data["tools"]}
    for tool in data["tools"]:
        tool_dir = ROOT / "tools" / tool["id"]
        tool_dir.mkdir(parents=True, exist_ok=True)
        static_main = f"""
<section class="tool-shell"><div class="container"><nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><a href="/tools/">Labs</a><span>/</span><span>{escape(tool['title_en'])}</span></nav><header class="tool-hero"><div><span class="eyebrow">Interactive lab</span><h1>{escape(tool['title_en'])}</h1><p>{escape(tool['description_en'])}</p></div><span class="privacy-pill">Runs locally</span></header><div id="tool-app" data-tool="{tool['id']}"></div></div></section>"""
        extra = '<script src="https://cdn.jsdelivr.net/npm/chart.js@4.5.1/dist/chart.umd.min.js" defer></script><script type="module" src="/assets/js/tools.js"></script>'
        (tool_dir / "index.html").write_text(html_shell(title=f"{tool['title_en']} | Statistics Learning Hub", description=tool["description_en"], page="tool", base=f"tools/{tool['id']}/", body_attrs=f'data-tool="{tool["id"]}"', main_html=static_main, extra_scripts=extra), encoding="utf-8")

    not_found = """
<section class="page-hero error-page"><div class="container"><span class="error-code">404</span><h1 data-en="This page is not in the curriculum." data-bn="এই পেজটি কারিকুলামে নেই।">This page is not in the curriculum.</h1><p data-en="Use the catalog or global search to find the lesson or lab you need." data-bn="প্রয়োজনীয় lesson বা lab খুঁজতে catalog অথবা global search ব্যবহার করুন।">Use the catalog or global search to find the lesson or lab you need.</p><div class="hero-actions"><a class="button primary" href="/catalog/" data-en="Open catalog" data-bn="ক্যাটালগ খুলুন">Open catalog</a><a class="button ghost" href="/" data-en="Return home" data-bn="হোমে ফিরুন">Return home</a></div></div></section>"""
    (ROOT / "404.html").write_text(html_shell(title="Page not found | Statistics Learning Hub", description="The requested page was not found.", page="404", base="404.html", main_html=not_found), encoding="utf-8")

    # Sitemap
    urls = ["/", "/catalog/", "/paths/", "/tools/", "/glossary/", "/about/"]
    urls += [f"/{t['url']}" for t in data["topics"]]
    urls += [f"/{t['url']}" for t in data["tools"]]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(f"  <url><loc>{SITE_URL}{u}</loc></url>" for u in urls) + "\n</urlset>\n"
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")


def main() -> None:
    data = build_content()
    content_js = "window.SLH_CONTENT = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n"
    (ROOT / "assets" / "js" / "content.js").write_text(content_js, encoding="utf-8")
    write_pages(data)
    print(f"Generated {len(data['topics'])} lessons, {len(data['tools'])} labs, and {len(data['paths'])} paths.")


if __name__ == "__main__":
    main()
