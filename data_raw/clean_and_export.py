import pandas as pd
import os
import pandas as pd
import numpy as np
import os

# Create output folder
os.makedirs("data_cleaned", exist_ok=True)


print("="*60)
print("CLEANING CHURN EVENTS")
print("="*60)  

churn_raw = pd.read_csv("data_raw/churn_events.csv")
print(f"Raw shape: {churn_raw.shape}")
print("\nFirst 5 rows:")

print(churn_raw.head())
print("\nColumn info:")
print(churn_raw.info())
print("\nMissing values:")
print(churn_raw.isna().sum())

# Clean
churn_clean = churn_raw.copy()

# Convert date columns to datetime
for col in churn_clean.columns:
    if "date" in col.lower() or "time" in col.lower():
        churn_clean[col] = pd.to_datetime(churn_clean[col], errors="coerce")

# Fill missing categorical with "Unknown"
for col in churn_clean.select_dtypes(include="object").columns:
    churn_clean[col] = churn_clean[col].fillna("Unknown")

# Fill missing numeric with 0
for col in churn_clean.select_dtypes(include=[np.number]).columns:
    churn_clean[col] = churn_clean[col].fillna(0)

# Export
churn_clean.to_csv("data_cleaned/dim_churn_events_clean.csv", index=False)
print(f"\n✅ Saved dim_churn_events_clean.csv ({churn_clean.shape[0]} rows, {churn_clean.shape[1]} cols)\n")


# Clean
print("="*60)
print("CLEANING FEATURE USAGE")
print("="*60)

usage_raw = pd.read_csv("data_raw/feature_usage.csv")
print(f"Raw shape: {usage_raw.shape}")
print("\nFirst 5 rows:")
print(usage_raw.head())
print("\nColumn info:")
print(usage_raw.info())
print("\nMissing values:")
print(usage_raw.isna().sum())

# Clean
usage_clean = usage_raw.copy()

# Convert date columns to datetime
for col in usage_clean.columns:
    if "date" in col.lower() or "time" in col.lower():
        usage_clean[col] = pd.to_datetime(usage_clean[col], errors="coerce")

# Fill missing categorical with "Unknown"
for col in usage_clean.select_dtypes(include="object").columns:
    usage_clean[col] = usage_clean[col].fillna("Unknown")

# Fill missing numeric with 0
for col in usage_clean.select_dtypes(include=[np.number]).columns:
    usage_clean[col] = usage_clean[col].fillna(0)

# Export
usage_clean.to_csv("data_cleaned/dim_feature_usage_clean.csv", index=False)
print(f"\n✅ Saved dim_feature_usage_clean.csv ({usage_clean.shape[0]} rows, {usage_clean.shape[1]} cols)\n")
