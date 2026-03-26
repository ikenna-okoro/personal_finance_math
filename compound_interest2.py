# Using Pandas (For viewing tables and charts)

import pandas as pd

rates = [0.25, 0.50, 0.75, 1.0, 1.25, 1.5, 2.0, 3.0]
periods = [4, 6, 7, 8, 20, 30, 40]

data = {
    f"{r}%": [(1 + r / 100) ** n for n in periods] 
    for r in rates
}

df = pd.DataFrame(data, index=periods)
df.index.name = "Periods"

# Optional rounding
df = df.round(6)

print(df)

