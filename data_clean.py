import pandas as pd

# Load data
df = pd.read_csv("sales_data.csv", encoding='latin1')

# Show basic info
print("Original Data Info:")
print(df.info())

# Standardize column names: remove spaces and make lowercase
df.columns = df.columns.str.strip().str.lower()

# Convert 'orderdate' to datetime
df['orderdate'] = pd.to_datetime(df['orderdate'], errors='coerce')

# Drop rows where orderdate is NaT (invalid)
df = df.dropna(subset=['orderdate'])

# Strip leading/trailing spaces from string columns
str_cols = df.select_dtypes(include='object').columns
df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())

# Fill missing values in 'addressline2' with empty string
if 'addressline2' in df.columns:
    df['addressline2'] = df['addressline2'].fillna('')

# Fill missing phone numbers or mark them as 'Unknown'
if 'phone' in df.columns:
    df['phone'] = df['phone'].fillna('Unknown')

# Convert relevant numeric columns
numeric_cols = ['quantityordered', 'priceeach', 'sales', 'msrp']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with any NaN in essential numeric columns
df = df.dropna(subset=numeric_cols)

# Reset index
df = df.reset_index(drop=True)

# Check cleaned data
print("\nCleaned Data Info:")
print(df.info())

# Export cleaned data
df.to_csv("cleaned_sales_data.csv", index=False)
