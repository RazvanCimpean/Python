import pandas as pd

df = pd.read_csv('F:\Workspace\data.csv')

df.to_csv (r'C:\Users\Razvan Cimpean\Desktop\Export2.csv')

print(df.to_string())

