import pandas as pd
import numpy as np
from pandas import DataFrame
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',15)

pd_data = pd.read_csv('/Users/marksu/Downloads/Reviews.csv')[:10000]

df = pd.DataFrame(pd_data)

#print(df.duplicated(['UserId']))
#print(df[df.duplicated(['UserId'])].count())

#pd_data.sort_values(by=['UserId'])

#df = df.drop('HelpfulnessNumerator', 1)
df = df.drop(df.columns[[4,5,7,8,9]],1) 
count = df.groupby('UserId').count()
count = count.drop(count.columns[[1,2,3]], axis=1) 
count.rename(columns={'Id':'Count'},inplace = True)
df = pd.merge(df, count, on=['UserId'])
df.sort_values(by = ['Count','UserId'],inplace = True,ascending=False)
mean = df.groupby('UserId')['Score'].agg(['mean', 'sum'])
df = pd.merge(df, mean, on=['UserId'])
df=df.drop_duplicates(['UserId']).head(10)

# print(df)
print (df)
#df.insert(4,column='times',value=df.groupby(['UserId']).count())

#print(pd_data.sort_values(by=['UserId']))
#print(pd_data)

    


"""
import csv
with open('/Users/marksu/Downloads/Reviews.csv') as csvfile:
    rows = csv.reader(csvfile)
    date=[]    
    i = 0
    for item in rows:
        date.append(item)    
  
    while i < 10:
        print (date[i])    
        i = i+1

"""