import itertools


#itemsets = [['A','C','D'],['B','C','E'],['A','B','C','E'],['B','E']]
itemsets = [['Bread','Milk'],['Bread','Diaper','Beer','Eggs'],['Milk','Diaper','Beer','Coke'],['Bread','Milk','Diaper','Beer'],['Bread','Milk','Diaper','Coke']]
dic_test={}
minimumSup = 3
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
    if(dic_test[key] < minimumSup):
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

# search CK support
def search(ck,dk):
    for itemset in itemsets:
        for data in ck:
            count = dk.get(tuple(data))
            # TODO
            if(count == None):
                count = 0
            match = 0
            for thing in data:
                for item in itemset:
                    if(thing == item):
                        match +=1
                        break
                if(match == len(data)):
                    count +=1
            dk.update({tuple(data):count})
    return dk        

# produce LK
def LK(dk):
    for key in dk.copy():
        if(dk[key] < minimumSup):
            del dk[key]
    return dk





# join parameters:list
def join(dk):
    listk = []
    newlist = []
    for key in dk:
        listk.append(list(key))
    listk.sort()

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
                newlist.append(temp)
    return newlist

# TODO prune step
def prune(listk,dk):
    for data in listk:
        check = 0
        #subsetcheck
        for s in itertools.combinations(data, len(data)-1):
            notfound = True
            for item in dk:
                # TODO 比較(list compare?)tuple
                if(s == item):
                    check +=1
                    notfound = False
                    break     
            if(notfound):
                break
 
        if(check != len(data)):
            listk.remove(data)
    return listk

# TODO forloop generate CK LK
dic_1={}
dic_2={}
print(list2)
dic_1 = search(list2,dic_1)
print("==============>",dic_1)
dic_1 = LK(dic_1)
print("==============>",dic_1)
listtest = join(dic_1)
print("==============>",listtest)
listtest = prune(listtest,dic_1)
print("==============>",listtest)
dic_2 = search(listtest,dic_2)
print("==============>",dic_2)

