import pandas as pd
from sqlalchemy import create_engine
import re
from urllib.parse import quote_plus  # Import quote_plus

# --- 1. EXTRACT AND TRANSFORM ---
print("Reading and cleaning the dataset...")

# Load the dataset
df = pd.read_csv("data/superstore.csv", encoding="latin1")


# Clean column names
# Converts 'Order Date' to 'order_date', 'Sub-Category' to 'sub_category', etc.
def clean_col_names(df):
    cols = df.columns
    new_cols = []
    for col in cols:
        new_col = re.sub(
            r"[^a-zA-Z0-9]", "_", col
        )  # Replace non-alphanumeric with underscore
        new_col = new_col.lower()
        new_cols.append(new_col)
    df.columns = new_cols
    return df


df = clean_col_names(df)

# Convert date columns to datetime objects
df["order_date"] = pd.to_datetime(df["order_date"], format="%m/%d/%Y")
df["ship_date"] = pd.to_datetime(df["ship_date"], format="%m/%d/%Y")

# Verify cleaning
print("Data cleaned successfully. Columns are now:")
print(df.columns)
print("\nData types:")
print(df.info())


# --- 2. LOAD ---
print("\nConnecting to the database...")

# Database connection details
# IMPORTANT: Replace with your actual database password and details
db_user = "postgres"
db_password_raw = "Abhin@vFaldu9"  # Store raw password
db_host = "localhost"
db_port = "5432"
db_name = "ecommerce_db"
table_name = "superstore"

# URL-encode the password
db_password_encoded = quote_plus(db_password_raw)

# Create a connection engine to the database
try:
    engine = create_engine(
        f"postgresql://{db_user}:{db_password_encoded}@{db_host}:{db_port}/{db_name}"
    )

    # Load the DataFrame into the 'superstore' table in PostgreSQL
    # 'if_exists='replace'' will drop the table if it already exists and create a new one.
    # This is useful for re-running the script.
    print(f"Loading data into '{table_name}' table...")
    df.to_sql(table_name, engine, if_exists="replace", index=False)

    print("Data loaded successfully into PostgreSQL!")

except Exception as e:
    print(f"An error occurred: {e}")
