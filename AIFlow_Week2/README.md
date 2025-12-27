
---

## 🔧 ETL Process

### 1. Extract
- Loaded 5 raw CSV files from RavenStack SaaS platform

### 2. Transform
- Converted date columns to proper datetime format
- Handled missing values:
  - Categorical: filled with "Unknown"
  - Numeric: filled with 0
- Created derived columns:
  - `customer_type`: paid vs. trial/free segmentation
- Data quality checks performed

### 3. Load
- Exported 5 cleaned CSV files ready for analysis

---

##  Data Dictionary

### Table 1: fact_subscriptions (Main Fact Table)

| Column Name | Data Type | Description | Example Value |
|-------------|-----------|-------------|---------------|
| subscription_id | string | Unique identifier for each subscription | S-51c0d1 |
| account_id | string | Foreign key linking to dim_accounts table | A-659280 |
| start_date | date | Date when subscription began | 2024-11-25 |
| end_date | date | Date when subscription ended (null if active) | 2024-12-15 |
| plan_tier | string | Subscription level (Basic/Pro/Enterprise) | Enterprise |
| mrr_amount | int | Monthly recurring revenue in USD | 62 |
| churn_flag | int | 1 = churned, 0 = active subscription | 0 |
| seats | int | Number of user licenses purchased | 5 |
| is_trial | boolean | True if subscription is in trial period | False |
| auto_renew | boolean | True if subscription auto-renews | True |
| subscription_type | string | Billing frequency (monthly/quarterly/annual) | annual |
| tenure_days | int | Days between start_date and end_date or reference date | 371 |
| customer_type | string | 'paid' if MRR > 0, 'trial/free' if MRR = 0 (derived) | paid |

---

### Table 2: dim_accounts (Customer Dimension)

| Column Name | Data Type | Description | Example Value |
|-------------|-----------|-------------|---------------|
| account_id | string | Unique customer/company identifier | A-659280 |
| account_name | string | Company or customer name | Acme Corp |
| signup_date | date | Date when account was created | 2023-11-15 |
| region | string | Geographic region (US/EU/APAC/etc.) | US |
| country | string | Country code | USA |
| industry | string | Business sector (Technology/Healthcare/Finance/etc.) | Technology |
| company_size | string | Employee count category (SMB/Mid-Market/Enterprise) | Mid-Market |
| referral_source | string | How customer found the product | Paid |
| contract_value | int | Total contract value in USD | 7440 |

---

### Table 3: dim_support_tickets

| Column Name | Data Type | Description | Example Value |
|-------------|-----------|-------------|---------------|
| ticket_id | string | Unique support ticket identifier | TKT-00123 |
| account_id | string | Foreign key to dim_accounts | A-659280 |
| subscription_id | string | Foreign key to fact_subscriptions | S-51c0d1 |
| created_date | datetime | Timestamp when ticket was created | 2024-12-01 14:30:00 |
| resolved_date | datetime | Timestamp when ticket was resolved | 2024-12-01 16:45:00 |
| priority | string | Urgency level (Critical/High/Medium/Low) | High |
| category | string | Issue type (Technical/Billing/Feature Request/Bug) | Technical |
| status | string | Current state (Open/In Progress/Resolved/Closed) | Resolved |
| first_response_time_minutes | int | Minutes from creation to first agent response | 45 |
| resolution_time_hours | float | Hours from creation to resolution | 2.25 |
| escalation_flag | int | 1 = escalated, 0 = resolved at first level | 1 |
| satisfaction_score | int | Customer rating (1-5 scale) | 4 |

---

### Table 4: dim_churn_events

| Column Name | Data Type | Description | Example Value |
|-------------|-----------|-------------|---------------|
| churn_event_id | string | Unique churn event identifier | CHR-00456 |
| subscription_id | string | Foreign key to fact_subscriptions | S-51c0d1 |
| account_id | string | Foreign key to dim_accounts | A-659280 |
| churn_date | date | Date when customer churned | 2024-12-15 |
| churn_reason | string | Primary reason (Price/Features/Support/Competitor) | Price |
| churn_reason_detail | string | Additional context or explanation | Too expensive |
| voluntary_churn | boolean | True if customer canceled, False if forced | True |
| final_mrr | int | MRR at time of churn | 62 |
| customer_lifetime_value | int | Total revenue before
