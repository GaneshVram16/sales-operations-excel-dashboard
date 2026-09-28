from pathlib import Path
import numpy as np
import pandas as pd

np.random.seed(42)
ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)

n = 12000
categories = ["Electronics","Home","Fashion","Beauty","Sports","Books"]
dates = pd.to_datetime("2025-01-01") + pd.to_timedelta(np.random.randint(0,365,n), unit="D")

df = pd.DataFrame({
    "Order_ID":[f"SO-{i:06d}" for i in range(1,n+1)],
    "Order_Date":dates,
    "Region":np.random.choice(["South","West","North","East"],n,p=[.34,.25,.24,.17]),
    "Salesperson":np.random.choice(["Aarav","Diya","Ishaan","Meera","Kabir","Ananya","Rohan","Nisha"],n),
    "Channel":np.random.choice(["Direct","Partner","Online"],n,p=[.42,.28,.30]),
    "Product_Category":np.random.choice(categories,n),
    "Units":np.random.choice([1,2,3,4,5],n,p=[.38,.28,.18,.10,.06]),
})

gross = np.random.gamma(2.8,1800,n)+400
discount = np.random.choice([0,.05,.10,.15],n,p=[.45,.25,.20,.10])
df["Gross_Sales"] = np.round(gross,2)
df["Discount_Rate"] = discount
df["Net_Sales"] = np.round(df["Gross_Sales"]*(1-discount),2)
df["Cost"] = np.round(df["Net_Sales"]*np.random.uniform(.58,.78,n),2)
df["Profit"] = np.round(df["Net_Sales"]-df["Cost"],2)
df["Margin_Pct"] = np.round(df["Profit"]/df["Net_Sales"],4)

df.to_csv(DATA/"sales_transactions.csv",index=False)
print(f"Created {len(df):,} synthetic sales rows.")