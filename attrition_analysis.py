"""
Attrition Analysis - HR Employee Dataset

This script analyzes employee attrition factors using Python, Pandas, and Seaborn.

Key Insights:
✅ Understanding attrition distribution
✅ Finding key factors influencing attrition
✅ Visualizing data for better insights
✅ Providing HR recommendations
"""

# 📌 Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create a folder to store plots
plot_dir = "plots"
os.makedirs(plot_dir, exist_ok=True)

# Load dataset
df = pd.read_csv(r"C:\Users\Lenovo\Downloads\WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Display basic dataset information
print(df.info())
print(df.head())
print(df.isnull().sum())  # Check for missing values

# 📌 Step 2: Understanding Employee Attrition
print(df["Attrition"].value_counts())  # Count of Attrition (Yes/No)

# Visualize Attrition distribution
plt.figure(figsize=(5, 4))
sns.countplot(x="Attrition", data=df, palette=["red", "green"])
plt.title("Employee Attrition Distribution")
plt.savefig(f"{plot_dir}/attrition_distribution.png")
plt.show()

# 📌 Step 3: Key Factors Affecting Attrition
## 👉 3.1 Age vs Attrition
print(df.groupby("Attrition")["Age"].mean())
plt.figure(figsize=(10, 5))
sns.histplot(data=df, x="Age", hue="Attrition", kde=True, palette=["red", "green"])
plt.title("Age vs Attrition")
plt.savefig(f"{plot_dir}/age_vs_attrition.png")
plt.show()

## 👉 3.2 Job Role vs Attrition
print(df.groupby("JobRole")["Attrition"].value_counts(normalize=True))
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="JobRole", hue="Attrition", palette=["red", "green"])
plt.xticks(rotation=45)
plt.title("Job Role vs Attrition")
plt.savefig(f"{plot_dir}/jobrole_vs_attrition.png")
plt.show()

## 👉 3.3 Salary vs Attrition
print(df.groupby("Attrition")["MonthlyIncome"].median())
plt.figure(figsize=(10, 5))
sns.boxplot(x="Attrition", y="MonthlyIncome", data=df, palette=["red", "green"])
plt.title("Salary vs Attrition")
plt.savefig(f"{plot_dir}/salary_vs_attrition.png")
plt.show()

## 👉 3.4 Distance from Home vs Attrition
print(df.groupby("Attrition")["DistanceFromHome"].median())
plt.figure(figsize=(10, 5))
sns.boxplot(x="Attrition", y="DistanceFromHome", data=df, palette=["red", "green"])
plt.title("Distance from Home vs Attrition")
plt.savefig(f"{plot_dir}/distance_vs_attrition.png")
plt.show()

# 📌 Step 4: Advanced Insights
## 👉 4.1 Work-Life Balance vs Attrition
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="WorkLifeBalance", hue="Attrition", palette=["red", "green"])
plt.title("Attrition by Work-Life Balance")
plt.xlabel("Work-Life Balance (1 = Low, 4 = High)")
plt.ylabel("Count")
plt.savefig(f"{plot_dir}/worklife_vs_attrition.png")
plt.show()

## 👉 4.2 Overtime vs Attrition
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="OverTime", hue="Attrition", palette=["red", "green"])
plt.title("Attrition by Overtime")
plt.xlabel("Overtime")
plt.ylabel("Count")
plt.savefig(f"{plot_dir}/overtime_vs_attrition.png")
plt.show()

## 👉 4.3 Years at Company vs Attrition
plt.figure(figsize=(8, 5))
sns.boxplot(x="Attrition", y="YearsAtCompany", data=df, palette=["red", "green"])
plt.title("Years at Company vs Attrition")
plt.xlabel("Attrition")
plt.ylabel("Years at Company")
plt.savefig(f"{plot_dir}/years_at_company_vs_attrition.png")
plt.show()

## 👉 4.4 Promotion & Career Growth
plt.figure(figsize=(8, 5))
sns.boxplot(x="Attrition", y="YearsSinceLastPromotion", data=df, palette=["red", "green"])
plt.title("Years Since Last Promotion vs Attrition")
plt.xlabel("Attrition")
plt.ylabel("Years Since Last Promotion")
plt.savefig(f"{plot_dir}/promotion_vs_attrition.png")
plt.show()

# 📌 Step 5: Summary & Next Steps
print("\n✅ Key Insights:")
print("1.️Employees with poor work-life balance leave more.")
print("2.️Overtime workers have a higher attrition rate.")
print("3. New employees (0-3 years) leave more.")
print("4. Lack of promotion leads to higher attrition.")

print("\n🎯 Recommendations for HR:")
print("✔ Improve work-life balance policies.")
print("✔ Reduce excessive overtime.")
print("✔ Strengthen employee onboarding programs.")
print("✔ Focus on career growth opportunities.")