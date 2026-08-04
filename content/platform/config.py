"""Product identity and static-site configuration for Data Learning Hub v2."""
from __future__ import annotations

SITE = {
    "name": "Data Learning Hub",
    "short_name": "DLH",
    "tagline_en": "From data foundations to portfolio-ready analytics.",
    "tagline_bn": "ডেটার ভিত্তি থেকে পোর্টফোলিও-রেডি অ্যানালিটিক্স পর্যন্ত।",
    "description_en": (
        "A tutorial-first English-first bilingual static learning platform for Data Analytics, beginning with "
        "data foundations and statistics, then expanding through Excel, SQL, Power BI, Python and projects."
    ),
    "description_bn": (
        "Data Analytics শেখার English-first bilingual static platform—Data Foundations ও Statistics থেকে শুরু করে "
        "Excel, SQL, Power BI, Python এবং project পর্যন্ত।"
    ),
    "site_url": "https://data-learning-hub.netlify.app",
    "repository": "https://github.com/SaifulIslamDS/statistics_learning_hub",
    "creator": "Saiful Islam",
    "website": "https://saifulshuvo.com",
    "github": "https://github.com/SaifulIslamDS/",
    "linkedin": "https://www.linkedin.com/in/saifulislampro/",
    "inspiration": "https://github.com/tafshir027/stats",
    "version": "2.1.0",
}

STORAGE = {
    "prefix": "dlh-",
    "legacy_prefix": "slh-",
    "schema_version": 3,
}

TOOL_BASELINES = [
    {
        "id": "excel",
        "name": "Excel",
        "baseline_en": "Excel for Microsoft 365; Power Query and the Data Model are introduced where relevant.",
        "baseline_bn": "Excel for Microsoft 365; প্রয়োজন অনুযায়ী Power Query ও Data Model অন্তর্ভুক্ত।",
        "official_url": "https://support.microsoft.com/en-us/excel/",
    },
    {
        "id": "sql",
        "name": "SQL",
        "baseline_en": "Portable SQL concepts with PostgreSQL as the primary teaching dialect.",
        "baseline_bn": "Portable SQL concept; primary teaching dialect হিসেবে PostgreSQL।",
        "official_url": "https://www.postgresql.org/docs/current/",
    },
    {
        "id": "power-bi",
        "name": "Power BI",
        "baseline_en": "Power BI Desktop, Power Query, semantic modeling and DAX for the Data Analyst role.",
        "baseline_bn": "Data Analyst role-এর জন্য Power BI Desktop, Power Query, semantic modeling ও DAX।",
        "official_url": "https://learn.microsoft.com/en-us/training/powerplatform/power-bi",
    },
    {
        "id": "python",
        "name": "Python",
        "baseline_en": "Python 3 with Jupyter, NumPy, pandas and Matplotlib for analytical workflows.",
        "baseline_bn": "Analytical workflow-এর জন্য Python 3, Jupyter, NumPy, pandas ও Matplotlib।",
        "official_url": "https://docs.python.org/3/tutorial/",
    },
]
