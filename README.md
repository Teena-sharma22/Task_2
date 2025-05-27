# 📊 Sales Data Analysis Dashboard

This project involves cleaning, analyzing, and visualizing a company's sales dataset using **Python** and creating a business insights **dashboard** (in Power BI).

---

## 📁 Project Overview

- 🧹 **Cleaned raw sales data** using Python (Pandas)
- 📈 Created **8 meaningful sales charts** for business insights
- 🗃️ Prepared dataset for building a dashboard to monitor sales, customers, and product trends

---

## 🧹 Data Cleaning Summary (Python)

Raw dataset: `sales_data.csv`  
Cleaned dataset: `cleaned_sales_data.csv`

### 🔧 Cleaning Steps:

- Converted all column names to lowercase and removed spaces
- Parsed `orderdate` into datetime format and dropped invalid rows
- Removed leading/trailing spaces from all text columns
- Filled missing values:
  - `addressline2`: filled with empty string
  - `phone`: filled with `'Unknown'`
- Converted columns like `quantityordered`, `sales`, `priceeach`, and `msrp` to numeric
- Removed rows with missing or invalid numeric values
- Reset the index and saved cleaned data

See code: `data_clean.py`

---

## 📊 Dashboard Visuals

These charts were created to explore and present business insights:

| No. | Chart | Type | What it Shows |
|-----|-------|------|----------------|
| 1️⃣ | **Monthly Sales Trend** | Line Chart | How total sales change over time |
| 2️⃣ | **Sales by Product Line** | Bar / Pie Chart | Which product categories perform best |
| 3️⃣ | **Top 10 Customers by Sales** | Horizontal Bar | Highest-spending customers |
| 4️⃣ | **Sales by Country** | Map / Bar Chart | Which regions bring in the most revenue |
| 5️⃣ | **Orders by Deal Size** | Donut / Bar Chart | Order distribution by size (Small, Medium, Large) |
| 6️⃣ | **Quantity Ordered by Product** | Bar Chart | Best-selling products by units sold |
| 7️⃣ | **Average Price per Product Line** | Bar Chart | Price comparison across product categories |
| 8️⃣ | **Order Status Overview** | Pie / Stacked Bar | Status distribution (Shipped, On Hold, Cancelled) |

---

## 📊 Example Fields from Dataset

| Column | Description |
|--------|-------------|
| `ordernumber` | Unique ID for each order |
| `orderdate` | Date of order |
| `sales` | Total sales value for an order line |
| `productline` | Category of product |
| `customername` | Name of customer |
| `country` | Customer's country |
| `dealSize` | Size category of deal (Small, Medium, Large) |
| `status` | Order status |
| `productcode`, `quantityordered`, `priceeach` | Product details |

---

## 🛠️ Tools Used

- **Python (Pandas)** – Data cleaning & preprocessing
- **Power BI** – Dashboard design and visualization
---

## 📸 Dashboard Preview
 
> ![Dashboard Screenshot](DATA%20ANALYSIS%20DASHBOARD.pdf)
..

## FILES

[RAW DATA](sales_data.csv)

[CLEANING PYTHON FILE](data_clean.py)

[CLEAN DATA](cleaned_sales_data.csv)

[VISUAL REPORT/DASHBOARD](DATA%20ANALYSIS%20DASHBOARD.pdf)

