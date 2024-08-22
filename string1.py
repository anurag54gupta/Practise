import pandas as pd

df=pd.read_csv("pokemon_data.csv")
#print(df.tail(3))
#print(df.columns)
print(df['Name',"Type 1","HP"].head(5))
#print(df.Name[0:8])


