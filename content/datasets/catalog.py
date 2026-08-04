"""Synthetic practice-dataset catalog shared across future tool tracks."""
from __future__ import annotations

DATASETS = [
    {
        "id": "retail-sales",
        "title_en": "Retail Sales",
        "title_bn": "রিটেইল সেলস",
        "description_en": "Synthetic transaction-level sales data for cleaning, KPI, trend, product and regional analysis.",
        "description_bn": "Cleaning, KPI, trend, product ও regional analysis-এর জন্য synthetic transaction-level sales data।",
        "file": "/assets/datasets/retail_sales.csv",
        "dictionary": "/assets/datasets/retail_sales_dictionary.csv",
        "rows": 240,
        "status": "available",
    },
    {
        "id": "customer-orders",
        "title_en": "Customer Orders",
        "title_bn": "কাস্টমার অর্ডার",
        "description_en": "Synthetic order and customer data for joins, segmentation, cohort and retention practice.",
        "description_bn": "Join, segmentation, cohort ও retention practice-এর জন্য synthetic order ও customer data।",
        "file": "/assets/datasets/customer_orders.csv",
        "dictionary": "/assets/datasets/customer_orders_dictionary.csv",
        "rows": 180,
        "status": "available",
    },
    {
        "id": "ngo-expenses",
        "title_en": "NGO Project Expenses",
        "title_bn": "NGO Project Expense",
        "description_en": "Synthetic budget and expense records for variance, utilization, control and reporting practice.",
        "description_bn": "Variance, utilization, control ও reporting practice-এর জন্য synthetic budget ও expense record।",
        "file": "/assets/datasets/ngo_project_expenses.csv",
        "dictionary": "/assets/datasets/ngo_project_expenses_dictionary.csv",
        "rows": 144,
        "status": "available",
    },
]

PROJECTS = [
    {
        "id": "retail-sales-foundations",
        "title_en": "Retail Sales Foundations Project",
        "title_bn": "রিটেইল সেলস ফাউন্ডেশন প্রজেক্ট",
        "description_en": "Use the shared retail dataset to define analytical questions, audit data quality, summarize performance and write defensible findings.",
        "description_bn": "Shared retail dataset দিয়ে analytical question define, data quality audit, performance summarize ও defensible finding লিখুন।",
        "status": "available",
        "level": "Beginner",
        "dataset": "retail-sales",
        "url": "/projects/retail-sales-foundations/",
    },
    {
        "id": "cross-tool-sales-analysis",
        "title_en": "Cross-tool Sales Analysis",
        "title_bn": "Cross-tool Sales Analysis",
        "description_en": "The future capstone will repeat one analytical problem in Excel, SQL, Power BI and Python.",
        "description_bn": "Future capstone-এ একই analytical problem Excel, SQL, Power BI ও Python-এ করা হবে।",
        "status": "roadmap",
        "level": "Intermediate",
        "dataset": "retail-sales",
        "url": None,
    },
]
