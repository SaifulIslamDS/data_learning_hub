"""Career routes. Data Analyst is the active v2 route; other roles remain transparent roadmaps."""
from __future__ import annotations

CAREER_PATHS = [
    {
        "id": "data-analyst",
        "title_en": "Data Analyst",
        "title_bn": "ডেটা অ্যানালিস্ট",
        "status": "active",
        "description_en": "The primary path: ask good questions, prepare data, analyze evidence, build reports and communicate decisions.",
        "description_bn": "Primary path: ভালো প্রশ্ন, data preparation, evidence analysis, report build ও decision communication।",
        "available_topics": [
            "statistics-and-data", "population-and-sample", "variables-and-observations",
            "measurement-scales", "categorical-and-numerical-data", "data-quality-dimensions",
            "frequency-tables", "mean-median-and-mode", "variance-and-standard-deviation",
            "histograms", "box-plots", "exploratory-data-analysis", "confidence-intervals",
            "hypothesis-testing-framework", "pearson-and-spearman-correlation", "simple-linear-regression",
            "kpi-design", "cohort-analysis", "funnel-analysis", "a-b-testing",
            "moving-averages-and-smoothing", "forecast-evaluation", "data-storytelling"
        ],
        "phases": [
            {"id": "foundations", "title_en": "Data Foundations", "title_bn": "ডেটা ফাউন্ডেশন", "status": "available", "release": "v2.0.0"},
            {"id": "statistics", "title_en": "Statistics for Analytics", "title_bn": "অ্যানালিটিক্সের জন্য স্ট্যাটিস্টিকস", "status": "available", "release": "v2.0.0"},
            {"id": "excel", "title_en": "Excel", "title_bn": "Excel", "status": "curriculum-ready", "release": "v2.1.0"},
            {"id": "sql", "title_en": "SQL", "title_bn": "SQL", "status": "curriculum-ready", "release": "v2.2.0"},
            {"id": "power-bi", "title_en": "Power BI", "title_bn": "Power BI", "status": "curriculum-ready", "release": "v2.3.0"},
            {"id": "python", "title_en": "Python", "title_bn": "Python", "status": "curriculum-ready", "release": "v2.4.0"},
            {"id": "projects", "title_en": "Portfolio Projects", "title_bn": "পোর্টফোলিও প্রজেক্ট", "status": "foundation-ready", "release": "v2.5.0"},
        ],
    },
    {
        "id": "bi-analyst",
        "title_en": "Business Intelligence Analyst",
        "title_bn": "বিজনেস ইন্টেলিজেন্স অ্যানালিস্ট",
        "status": "roadmap",
        "description_en": "A reporting and semantic-model specialization after the core Data Analyst path.",
        "description_bn": "Core Data Analyst path-এর পর reporting ও semantic-model specialization।",
        "available_topics": [],
        "phases": [],
    },
    {
        "id": "data-scientist",
        "title_en": "Data Scientist",
        "title_bn": "ডেটা সায়েন্টিস্ট",
        "status": "roadmap",
        "description_en": "An advanced future route that begins after analytics, statistics and Python foundations.",
        "description_bn": "Analytics, statistics ও Python foundation-এর পর future advanced route।",
        "available_topics": [],
        "phases": [],
    },
    {
        "id": "data-engineer",
        "title_en": "Data Engineer",
        "title_bn": "ডেটা ইঞ্জিনিয়ার",
        "status": "roadmap",
        "description_en": "An advanced future route through SQL, Python, data modeling, pipelines, quality and governance.",
        "description_bn": "SQL, Python, data modeling, pipeline, quality ও governance-এর future advanced route।",
        "available_topics": [],
        "phases": [],
    },
    {
        "id": "research-analyst",
        "title_en": "Research & Decision Analyst",
        "title_bn": "রিসার্চ ও ডিসিশন অ্যানালিস্ট",
        "status": "supporting",
        "description_en": "A statistics-heavy supporting route using the retained research and experimentation library.",
        "description_bn": "Retained research ও experimentation library-ভিত্তিক statistics-heavy supporting route।",
        "available_topics": [
            "population-and-sample", "measurement-scales", "data-collection-methods",
            "probability-and-non-probability-sampling", "sampling-bias-and-confounding",
            "confidence-intervals", "hypothesis-testing-framework", "tests-for-proportions",
            "chi-square-tests", "analysis-of-variance", "experimental-design", "causal-inference",
            "data-storytelling"
        ],
        "phases": [],
    },
]
