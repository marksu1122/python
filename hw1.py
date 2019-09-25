import pandas as pd
from pandas import DataFrame

pd_data = pd.read_csv('/Users/marksu/Downloads/Reviews.csv', index_col=0)[:10000]

df = pd.DataFrame(pd_data)
df = df.drop(df.columns[[0,3,4,6,7,8]],axis=1) 
part_one =df.groupby('UserId')['Score'].agg({'count','mean'})

df = pd.merge(df, part_one, on=['UserId'])
df.sort_values(by = ['count','UserId'],inplace = True,ascending=False)

df=df.drop_duplicates(['UserId']).drop(['Score'],1).head(10)
df = df.reset_index(drop=True)
print(df)

#df.insert(4,column='times',value=df.groupby(['UserId']).count())
#print(df.duplicated(['UserId']))
#print(df[df.duplicated(['UserId'])].count())

