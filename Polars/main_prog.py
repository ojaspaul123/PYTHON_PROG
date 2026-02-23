from turtle import heading

import polars as pl
sal = pl.read_csv(r"C:\Users\KIIT\Desktop\VS Code\Mini Project\Mini-Project-\Polars\turtle_showroom_sales_report.csv")
# print(sal.head())
# print(sal.describe())

print(f"  Shape  : {sal.shape[0]} rows x {sal.shape[1]} columns")
print(f"\n  Schema :\n  {sal.schema}")
print(f"\n  First 5 rows:\n{sal.head(5)}")

df = sal.clone()

# # DATA CLEANING
# Rename columns 
df = sal.rename({
    "Sale ID":           "sale_id",
    "Date":              "date",
    "Customer Name":     "customer",
    "Turtle Species":    "species",
    "Quantity":          "qty",
    "Unit Price (INR)":  "unit_price",
    "Total Price (INR)": "total_price",
    "Payment Method":    "payment",
    "Salesperson":       "salesperson",
    "Region":            "region",
    "Status":            "status",
})
print(f"  Columns: {df.columns}")

#  Duplicate Sale ID check
dupes = df.shape[0] - df["sale_id"].n_unique()
print(f"    Total rows: {df.shape[0]}  |  Unique IDs: {df['sale_id'].n_unique()}  |  Duplicates: {dupes}")
if dupes > 0:
    df = df.unique(subset=["sale_id"], keep="first", maintain_order=True)
    print(f"    Removed {dupes} duplicate(s). Remaining: {df.shape[0]}")
else:
    print("    No duplicates found.  OK")
    

print(f"    Distinct values: {df['status'].unique().to_list()}  OK")
print(f"\n  CLEANED DATASET: {df.shape[0]} rows x {df.shape[1]} columns")   

##  DATA MANIPULATION
# Discount %: 10% for qty>3, 5% for qty>2, else 0

df = df.with_columns(
    pl.when(pl.col("qty") > 3).then(pl.lit(10))
      .when(pl.col("qty") > 2).then(pl.lit(5))
      .otherwise(pl.lit(0))
      .cast(pl.Int32)
      .alias("discount_pct")
)

#  Discount amount & net total
df = df.with_columns([
    (pl.col("total_price") * pl.col("discount_pct") / 100).round(2).alias("discount_amt"),
    (pl.col("total_price") * (1 - pl.col("discount_pct") / 100)).round(2).alias("net_total"),
])

#  Price category
df = df.with_columns(
    pl.when(pl.col("unit_price") >= 10000).then(pl.lit("High-End"))
      .when(pl.col("unit_price") >=  5000).then(pl.lit("Mid-Range"))
      .otherwise(pl.lit("Affordable"))
      .alias("price_category")
)

# Revenue contribution % per row
grand_total = df["net_total"].sum()
df = df.with_columns(
    (pl.col("net_total") / grand_total * 100).round(2).alias("revenue_pct")
)

print(df.select([
    "sale_id","customer","qty","total_price",
    "discount_pct","discount_amt","net_total",
    "month","week_no","weekday",
    "sale_tier","price_category","revenue_pct"
]))

# # DATA FILTERING
completed = df.filter(pl.col("status") == "Completed")
print(completed.select(["sale_id","customer","species","net_total","status"]))

pending = df.filter(pl.col("status") == "Pending")
print(pending.select(["sale_id","customer","net_total","status"]))

premium = df.filter(pl.col("sale_tier") == "Premium")
print(premium.select(["sale_id","customer","species","net_total","sale_tier"]))

jan = df.filter(pl.col("month").str.starts_with("January"))
print(jan.select(["sale_id","date","customer","net_total"]))

delhi = df.filter(pl.col("region") == "Delhi")
print(delhi.select(["sale_id","customer","net_total","salesperson"]))

upi = df.filter(pl.col("payment") == "UPI")
print(upi.select(["sale_id","customer","net_total","payment"]))

bulk = df.filter(pl.col("qty") > 2)
print(bulk.select(["sale_id","customer","species","qty","discount_pct","net_total"]))

high_end = df.filter(pl.col("price_category") == "High-End")
print(high_end.select(["sale_id","customer","species","unit_price","net_total"]))

big_comp = df.filter((pl.col("status") == "Completed") & (pl.col("net_total") > 10000))
print(big_comp.select(["sale_id","customer","species","net_total","status"]))

hvc = df.filter(pl.col("net_total") > 10000)


## LOGIC FILTERS
total_rev = completed["net_total"].sum()
avg_order = completed["net_total"].mean()
# Revenue by salesperson
top_sp = completed.group_by("salesperson").agg(pl.col("net_total").sum().alias("Revenue")).sort("Revenue", descending=True).row(0, as_dict=True)
best_sp = df.group_by("species").agg(pl.col("qty").sum().alias("units")).sort("units", descending=True).row(0, as_dict=True)
exports = []
#Revenue by Region
heading("Revenue by Region")
region_agg = (
    completed.group_by("region")
        .agg([
            pl.col("net_total").sum().round(2).alias("Revenue"),
            pl.len().alias("Transactions"),
            pl.col("net_total").mean().round(2).alias("Avg_Sale"),
        ])
        .sort("Revenue", descending=True)
)
print(region_agg)

#  Payment Distribution
pay_agg = (
    comp.group_by("payment")
        .agg([
            pl.len().alias("Count"),
            pl.col("net_total").sum().round(2).alias("Revenue"),
        ])
        .with_columns(
            (pl.col("Count") / comp.shape[0] * 100).round(1).alias("Share_pct")
        )
        .sort("Count", descending=True)
)
print(pay_agg)

##FINAL SUMMARY
print(f"""
  Source File                        : {sal}
  Raw Records                        : {sal.shape[0]}
  After Cleaning                     : {df.shape[0]}
  Completed Sales                    : {completed.shape[0]}
  Pending Sales                      : {pending.shape[0]}
  {'─'*52}
  Total Revenue (Completed)          : INR {total_rev:,.2f}
  Avg Order Value                    : INR {avg_order:,.2f}
  Total Discount Given               : INR {completed['discount_amt'].sum():,.2f}
  {'─'*52}
  Top Salesperson                    : {top_sp['salesperson']} (INR {top_sp['Revenue']:,.2f})
  Best-Selling Species               : {best_sp['species']} ({best_sp['units']} units)
  High-Value Customers (>INR 10K)    : {hvc.shape[0]}
  CSVs Exported                      : {len(exports)} files
  {'─'*52}
""")

