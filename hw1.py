import pandas as pd
import numpy as np
from pandas import DataFrame

import pandas as pd
import numpy as np
from pandas import DataFrame

pd_data = pd.read_csv('/Users/marksu/Downloads/Reviews.csv', index_col=0)[:10000]

df = pd.DataFrame(pd_data)
df = df.drop(df.columns[[0,3,4,6,7,8]],1) 

count = df.groupby('UserId').count()
count = count.drop(['Score'],1) 
count.rename(columns={'ProfileName':'Count'},inplace = True)
df = pd.merge(df, count, on=['UserId'])

df.sort_values(by = ['Count','UserId','ProfileName'],inplace = True,ascending=False)
mean = df.groupby('UserId')['Score'].agg(['mean', 'sum'])
df = pd.merge(df, mean, on=['UserId'])

df=df.drop_duplicates(['UserId']).drop(['Score','Count'],1).head(10)
df.rename(columns={'mean':'Score mean','sum':'Score count'},inplace = True)

print (df)
#df.insert(4,column='times',value=df.groupby(['UserId']).count())
#print(df.duplicated(['UserId']))
#print(df[df.duplicated(['UserId'])].count())

    


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