import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# LOAD DATA
# -------------------------
df = pd.read_csv("sales_messy_data.csv")

print("Original Data:\n", df)

# -------------------------
# CLEAN DATA
# -------------------------

# Fix Quantity (convert text to number)
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Quantity"] = df["Quantity"].fillna(0)

# Fill missing Price with mean
df["Price"] = df["Price"].fillna(df["Price"].mean())

# Fill missing Product
df["Product"] = df["Product"].fillna("Unknown")

# -------------------------
# CREATE REVENUE
# -------------------------
df["Revenue"] = df["Quantity"] * df["Price"]

# -------------------------
# ANALYSIS
# -------------------------
total_revenue = df["Revenue"].sum()
product_sales = df.groupby("Product")["Revenue"].sum()
daily_sales = df.groupby("Date")["Revenue"].sum()

print("\nCleaned Data:\n", df)
print("\nTotal Revenue:", total_revenue)
print("\nRevenue by Product:\n", product_sales)

# -------------------------
# VISUALIZATION 1: DAILY TREND
# -------------------------
plt.figure(figsize=(8,5))
daily_sales.plot(marker="o")
plt.title("Daily Sales Trend (Cleaned Data)")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.grid()
plt.tight_layout()
plt.savefig("day43_daily_sales.png")
plt.show()

# -------------------------
# VISUALIZATION 2: PRODUCT SALES
# -------------------------
plt.figure(figsize=(8,5))
product_sales.plot(kind="bar")
plt.title("Revenue by Product (Cleaned Data)")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.grid()
plt.tight_layout()
plt.savefig("day43_product_sales.png")
plt.show()

# -------------------------
# VISUALIZATION 3: PIE CHART
# -------------------------
plt.figure(figsize=(6,6))
product_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Revenue Distribution (Cleaned Data)")
plt.ylabel("")
plt.tight_layout()
plt.savefig("day43_revenue_share.png")
plt.show()

# -------------------------
# INSIGHTS (PRINT)
# -------------------------
print("\n===== KEY INSIGHTS =====")
print("- Laptop generates majority of revenue")
print("- Missing/invalid data impacts total revenue")
print("- 'Unknown' category indicates data quality issues")
print("- Some entries contribute zero revenue due to missing values")

print("\nDay 43 Project Completed!")