import pandas as pd
import numpy as np

df = pd.read_excel("C:/Users/hp/Documents/COVID19- Africa-Analysis.xlsx")
print(df.head())



duplicated_rows = df[df.duplicated()]
print(duplicated_rows)

print(df.describe())


mask = df.isnull()
print(mask)

missing_values = mask.sum()
print(missing_values)

Column = (df.columns.tolist())
print(Column)

print(df['Country'])
