"""Practice functions for the Data Learning Hub Python Analytics course."""
from pathlib import Path
import pandas as pd

def load_sales(path="python_retail_sales.csv"):
    df = pd.read_csv(path, parse_dates=["order_date"])
    df["margin"] = df["profit"].div(df["revenue"]).where(df["revenue"].ne(0))
    return df

def quality_report(df):
    return pd.DataFrame({"dtype": df.dtypes.astype(str), "missing": df.isna().sum(), "unique": df.nunique(dropna=False)})

def regional_summary(df):
    return df.groupby("region", as_index=False).agg(orders=("order_id","nunique"), revenue=("revenue","sum"), profit=("profit","sum"))

if __name__ == "__main__":
    sales = load_sales()
    print(quality_report(sales))
    print(regional_summary(sales))
