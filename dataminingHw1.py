import itertools

#itemsets = [['A','C','D'],['B','C','E'],['A','B','C','E'],['B','E']]
itemsets = [['Bread','Milk'],['Bread','Diaper','Beer','Eggs'],['Milk','Diaper','Beer','Coke'],['Bread','Milk','Diaper','Beer'],['Bread','Milk','Diaper','Coke']]

def C1(itemsets):
    C1 = {}
    for itemset in itemsets:
        for item in itemset:
            item =tuple([item])
            count = C1.get(item)            
            if(count != None):
                count += 1
                C1.update({item:count})
            else: 
                C1.update({item: 1})
    return C1

# C1 to sortlist
def C2(l1,itemsets):
    listC1 =[]
    listC2 =[]
    C2 ={}
    for key in l1:
        #convert single tuple to string [print(str(key)) == ('Bread',) ]      
        listC1.append("".join(key))
        listC1.sort()
    for s in itertools.combinations(listC1, 2):
        listC2.append(list(s))
    C2 = Search(listC2,itemsets)
    return C2

# search Ck support
def Search(listCk,itemsets):
    #TODO 前一步就產生CK??
    ck={}
    for itemset in itemsets:
        for data in listCk:
            count = ck.get(tuple(data))
            # TODO count值處理
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
            ck.update({tuple(data):count})
    return ck  


# JoinStep TODO 怪怪的
def JoinStep(lk):
    listk = []
    newlist = []
    for key in lk:
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

# PruneStep
def PruneStep(listk,lk):
    for data in listk:
        check = 0
        #subsetcheck
        for s in itertools.combinations(data, len(data)-1):
            notfound = True
            for item in lk:
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

# produce LK check minmumSupport  //return dictionary
def Lk(ck,minimumSup):
    for key in ck.copy():
        if(ck[key] < minimumSup):
            del ck[key]
    return ck



def Apriori(itemsets):
    #TODO itemset minmunsup conf
    minimumSup = 2
    conf = 0.5
    c1 = C1(itemsets)
    l1 = Lk(c1,minimumSup)
    c2 = C2(l1,itemsets)
    #TODO range
    for k in range(2,1000):
        #LK
        locals()['l%s'%k] = Lk(locals()['c%s'%k],minimumSup)
        #produce listL(k+1) JoinStep 
        locals()['listL%s'%(k+1)] = JoinStep(locals()['l%s'%k])
        #PruneStep listL(k+1) 
        locals()['listL%s'%(k+1)] = PruneStep(locals()['listL%s'%(k+1)],locals()['l%s'%k])
        #ck
        locals()['c%s'%(k+1)] = Search(locals()['listL%s'%(k+1)],itemsets)

        #TODO
        if(not locals()['c%s'%(k+1)]):
            for i in range(k,0,-1):
                for key,value in locals()['l%s'%i].items():
                    for s in itertools.combinations(key, len(key)):
                        print("S=====>",s)

                print('===L',i,'========>',locals()['l%s'%i])
            break

Apriori(itemsets)