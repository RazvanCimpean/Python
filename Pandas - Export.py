import pandas as pd

data = {'Product': ['Desktop Computer','Tablet','Printer','Laptop'],
        'Price': [850,200,150,1300]
        }

df = pd.DataFrame(data, columns= ['Product', 'Price'])

df = df.astype({"Price": int})

# df.to_csv (r'C:\Users\Razvan Cimpean\Desktop\Export.csv', sep ='\t')

print(df.Price.dtype)

print (df)
