import pandas as pd
'''
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

df.sort_values(by=['Team'])
df.groupby(['cluster']).mean()
print (df)
'''
df = pd.DataFrame({'A': ['a', 'b', 'a', 'c', 'a', 'c', 'b', 'c'], 
                       'B': [2, 8, 1, 4, 3, 2, 5, 9], 
                       'C': [102, 98, 107, 104, 115, 87, 92, 123]})
print (df)
print ("==================================")
count = df.groupby('A').count()


#count = count.drop(count.columns[[1]], axis=1) 
print (count)
#df.insert(4,column='times',value=count['B'])


print (pd.merge(df, count, on=['A']))


#print (df.join(count, on='B'))