import pandas as pd
import matplotlib.pyplot as plt
import os

# Use non-interactive backend (important on Windows)
plt.switch_backend("Agg")

# -------------------------------
# Create visuals folder
# -------------------------------
os.makedirs("visuals", exist_ok=True)

# -------------------------------
# 1. Load Dataset
# -------------------------------
df = pd.read_csv("data/superstore.csv", encoding="ISO-8859-1")

# -------------------------------
# 2. Data Cleaning
# -------------------------------
df["Order Date"] = pd.to_datetime(df["Order Date"])
df.drop_duplicates(inplace=True)

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Year-Month"] = df["Order Date"].dt.to_period("M")

# -------------------------------
# 3. KPI Calculations
# -------------------------------
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
profit_margin = (total_profit / total_sales) * 100

print("===== BUSINESS KPIs =====")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Profit Margin: {profit_margin:.2f}%")

# -------------------------------
# 4. Monthly Sales Trend
# -------------------------------
monthly_sales = df.groupby("Year-Month")["Sales"].sum()

plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Time")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visuals/monthly_sales_trend.png")
plt.close()

# -------------------------------
# 5. Sales by Category
# -------------------------------
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure()
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("visuals/sales_by_category.png")
plt.close()

# -------------------------------
# 6. Profit by Category
# -------------------------------
category_profit = df.groupby("Category")["Profit"].sum()

plt.figure()
category_profit.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("visuals/profit_by_category.png")
plt.close()

# -------------------------------
# 7. Sales by Region
# -------------------------------
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure()
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("visuals/sales_by_region.png")
plt.close()

# -------------------------------
# 8. Top 10 Products
# -------------------------------
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure()
top_products.plot(kind="barh")
plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("visuals/top_10_products.png")
plt.close()

print("\n✅ All charts successfully saved to the 'visuals/' folder.")
