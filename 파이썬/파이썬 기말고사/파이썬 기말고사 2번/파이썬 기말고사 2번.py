import pandas as pd
csv_test=pd.read_csv("D:\파이썬기말고사 파일\diamonds.csv")

row_5=csv_test.loc[0:5, :]
print(row_5)

new=csv_test.drop(['cut'], axis=1)
new_id=new.iloc[0:5, :]
print(new_id)

re=csv_test.sort_values(by='price', ascending=False)
col=re['price']
print(col)

special = csv_test.iloc[2:5, 0:2]
print(special)
