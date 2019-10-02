import numpy as np

itemsets = [['A','C','D'],['B','C','E'],['A','B','C','E'],['B','E']]
dic_test={}
#C1
for itemset in itemsets:
    for item in itemset:
        count = dic_test.get(item)
        if(count != None):
            count += 1
            dic_test.update({item:count})
        else: 
            dict2 = {item: 1}
            dic_test.update(dict2)                

#minimal support
for key in dic_test.copy():
    if(dic_test[key] < 2):
        del dic_test[key]

#dic_test.update({('A','B'):0})
#dic_test['John', 'Smith'] = 10000.0
print(dic_test)

#C2
list1 = [] 
list2 = [] 
for key1 in dic_test:
    list1.append(str(key1))
list1.sort()
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        list2.append([str(list1[i]),str(list1[j])])

# TODO search C2 in DB to produce L2



#join parameters:list
def join(listk):
    newlist = []
    k = len(listk[0])-1 
    for i in range(len(listk)):
        l1 = listk[i]
        for j in range(i+1,len(listk)):
            l2 = listk[j]
            compare = True
            for a in range(k):
                if(l1[a] != l2[a]):
                    compare = False
                    break
            if(compare):
                temp = l1.copy()
                temp.append(str(l2[k]))
                print(temp)
                newlist.append(temp)
    return newlist

                   


print("==============>",join(list2))