import sys
import pandas as pd

month = int(sys.argv[1])

df = pd.DataFrame({"Days": [1, 2, 3], "Passengers": [4, 5, 6]})
df["month"] = month

df.to_parquet(f"output_{month}.parquet")

print(df)


print(f"Running pipeline for month {month}")