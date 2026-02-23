df = df.with_columns(
#     pl.when(pl.col("qty") > 3).then(pl.lit(10))
#       .when(pl.col("qty") > 2).then(pl.lit(5))
#       .otherwise(pl.lit(0))
#       .cast(pl.Int32)
#       .alias("discount_pct")
# ) 