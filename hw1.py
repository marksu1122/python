import pandas as pd
from pandas import DataFrame
#讀取csv檔
pd_data = pd.read_csv('/Users/marksu/Downloads/Reviews.csv', index_col=0)[:10000]

df = pd.DataFrame(pd_data)
#刪除不用的欄位,根據'UserId'進行分群後對'Score'進行mean &count
df = df.drop(df.columns[[0,3,4,6,7,8]],axis=1) 
part_one =df.groupby('UserId')['Score'].agg({'count','mean'})
#merge two dataframe
df = pd.merge(df, part_one, on=['UserId'])
#排序後選出前十名
df.sort_values(by = ['count','UserId'],inplace = True,ascending=False)
df=df.drop_duplicates(['UserId']).drop(['Score'],1).head(10)

df = df.reset_index(drop=True)
print(df)

#df.insert(4,column='times',value=df.groupby(['UserId']).count())
#print(df.duplicated(['UserId']))
#print(df[df.duplicated(['UserId'])].count())

