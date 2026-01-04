Customer Churn Dashboard 

IT300 Complete BI Project - Tunis Business School

 What it does
Analyzes 7.2% monthly churn for fintech SaaS (1000+ accounts). 
Full pipeline: raw data → Power BI dashboard.

Tech Stack
CSV → Python ETL → Star Schema → Dashboard
fact_subscriptions → dim_accounts, churn, support_tickets

Features
• 3 DAX measures: Churn Rate, Active Subs, Support/Account
• 3 pages: Executive + Deep Dive + Q1 2026 Forecast  
• 8+ visuals + slicers (country, priority)

 Key Findings
1. High-priority accounts churn 2x faster
2. Support tickets predict cancellations
3. Q1 response time crisis coming

Files
Churn_Analysis.pbix     [Dashboard]
AIflow_week2.ipynb      [ETL]
Data_Dictionary.pdf     [Week 1]
Measures.pdf           [DAX]
