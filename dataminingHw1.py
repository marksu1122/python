import itertools
import operator

"""
itemsets = [
    ["A", "C", "D"],
    ["B", "C", "E"],
    ["A", "B", "C", "E"],
    ["B", "E"],
    #   ["B", "E", "D"],
    #   ["B", "E", "D", "A"],
    #   ["A", "C", "E"]
]
"""
itemsets = [
    ["a", "c", "d","f","g","i","m","p"],
    ["a", "b", "c","f","i","m","o"],
    ["b","f","h","j","o"],
    ["b", "c", "k","s","p"],
    ["a", "c", "e","f","l","m","n","p"]
]
"""
itemsets = [
    ["Bread", "Milk", "Beer"],
    ["Bread", "Coffee"],
    ["Bread", "Egg"],
    ["Bread", "Milk", "Coffee"],
    ["Milk", "Egg"],
    ["Bread", "Egg"],
    ["Milk", "Egg"],
    ["Bread", "Milk", "Egg", "Beer"],
    ["Bread", "Milk", "Egg"]
]
"""

def C1(itemsets):
    C1 = {}
    for itemset in itemsets:
        for item in itemset:
            item = tuple([item])
            count = C1.get(item)
            if count != None:
                count += 1
                C1.update({item: count})
            else:
                C1.update({item: 1})
    return C1


# C1 to sortlist
def ListC2(l1):
    listC1 = []
    listC2 = []
    for key in l1:
        # convert single tuple to string [print(str(key)) == ("Bread",) ]
        listC1.append("".join(key))
        listC1.sort()
    for s in itertools.combinations(listC1, 2):
        listC2.append(list(s))
    return listC2


# search Ck support
def Search(listCk, itemsets):
    ck = {}
    for itemset in itemsets:
        for data in listCk:
            count = ck.get(tuple(data))
            # TODO count值處理 三元？？
            if not count:
                count = 0
            match = 0
            for thing in data:
                for item in itemset:
                    if thing == item:
                        match += 1
                        break
                if match == len(data):
                    count += 1
            ck.update({tuple(data): count})
    return ck


# JoinStep TODO 怪怪的
def JoinStep(lk):

    listk = []
    newlist = []
    for key in lk:
        listk.append(list(key))
    listk.sort()

    k = len(listk[0]) - 1
    for i in range(len(listk)):
        l1 = listk[i]
        for j in range(i + 1, len(listk)):
            l2 = listk[j]
            compare = True
            for a in range(k):
                if l1[a] != l2[a]:
                    compare = False
                    break
            if compare:
                temp = l1.copy()
                temp.append(str(l2[k]))
                newlist.append(temp)
    return newlist


# PruneStep
def PruneStep(listk, lk):
    for data in listk:
        check = 0
        # subsetcheck
        for s in itertools.combinations(data, len(data) - 1):
            notfound = True
            for item in lk:
                # TODO 比較(list compare?)tuple
                if s == item:
                    check += 1
                    notfound = False
                    break
            if notfound:
                break

        if check != len(data):
            listk.remove(data)
    return listk


# produce LK check minmumSupport  //return dictionary
def Lk(ck, minimumSup):
    for key in ck.copy():
        if ck[key] < minimumSup:
            del ck[key]
    return ck


# TODO while????
def RuleGeneration(candidate, i, support, conf, ruleList, lkDic):
    for rule in itertools.combinations(candidate, i):
        # 查
        times = lkDic.get("l" + str(i)).get(rule)
        # check confidence
        if (support / times) < conf:
            continue
        ruleList.append({rule: set(candidate).difference(set(rule))})
        if i > 1:
            RuleGeneration(candidate, i - 1, support, conf, ruleList, lkDic)
    return ruleList


def Apriori(itemsets, minimumSup, conf):
    lkDic = {}
    ruleList = []
    c1 = C1(itemsets)
    l1 = Lk(c1, minimumSup)
    lkDic.update({"l1": l1})
    listC2 = ListC2(l1)
    c2 = Search(listC2, itemsets)
    for k in range(2, len(itemsets)):
        # LK
        locals()["l%s" % k] = Lk(locals()["c%s" % k], minimumSup)

        if not locals()["l%s" % (k)]:
            break
        lkDic.update({"l" + str(k): locals()["l%s" % k]})
        # produce listL(k+1) JoinStep
        locals()["listL%s" % (k + 1)] = JoinStep(locals()["l%s" % k])
        # PruneStep listL(k+1)
        locals()["listL%s" % (k + 1)] = PruneStep(
            locals()["listL%s" % (k + 1)], locals()["l%s" % k]
        )
        # ck
        locals()["c%s" % (k + 1)] = Search(locals()["listL%s" % (k + 1)], itemsets)

        if not locals()["c%s" % (k + 1)]:
            break

    for i in range(len(lkDic), 1, -1):
        candidateLi = lkDic.get("l" + str(i))
        for key, value in candidateLi.items():
            # 母項個數
            candidate = list(key)
            ruleList = RuleGeneration(candidate, i - 1, value, conf, ruleList, lkDic)

    return ruleList

"""
print("================================")
print(Apriori(itemsets, 2, 0.8))
print("================================")
"""

def link(node, linkDic):
    point = linkDic.get(node.name)
    if point:
        node.next = point

    linkDic.update({node.name: node})


class Node:
    def __init__(self, name):
        self.name = name
        self.value = 1
        self.children = []
        self.parent = None
        self.next = None

    def insert(self, node, linkDic):
        for child in self.children:
            if node.name == child.name:
                child.value += 1
                return child

        self.children.append(node)
        node.parent = self
        link(node, linkDic)
        return node
    def disp(self, ind=1):
        print(' ' * ind, self.name, ' ', self.value)
        for child in self.children:
            child.disp(ind + 1)


def Path(node):
    path = []
    while node:
        if node.name != "root":
            path.append(node.name)
        node = node.parent
    path.reverse()
    return path


def FPtree(itemsets, orderList):
    root = Node("root")
    root.value = None
    linkDic = {}
    for itemset in itemsets:
        for item in itemset.copy():
            if item not in orderList:
                itemset.remove(item)
        itemset = sorted(itemset, key=orderList.index)
        parent = root
        for item in itemset:
            node = Node(item)
            parent = parent.insert(node, linkDic)
    print("===========================================")       
    print(root.disp())
    print("===========================================")   
    return linkDic


def FreqTree(value, minimumSup):
    dic = {}
    for item in value:
        num = item[1]
        for node in item[0]:
            count = dic.get(node)
            num = num if not count else count + num
            dic.update({node: num})
    dic = Lk(dic, minimumSup)
    return dic


def FP_Growth(itemsets, minimumSup):
    c1 = C1(itemsets)
    l1 = Lk(c1, minimumSup)

    sorted_x = sorted(l1.items(), key=operator.itemgetter(1))
    sorted_x.reverse()
    orderList = []
    for itemset in sorted_x:
        orderList.append("".join(itemset[0]))
    orderList = ['f','c','a','b','m','p']
    linkDic = FPtree(itemsets, orderList)
    
    orderList.reverse()
    pathDic = {}
    for item in orderList:

        dot = linkDic.get(item)
        pathList = []
        while dot:
            path = Path(dot.parent)
            if path:
                pathList.append([path, dot.value])
            dot = dot.next
        pathDic.update({linkDic.get(item).name: pathList})
        #print("==========PATH====================\n",linkDic.get(item).name,"\n",pathList)

    orderList.reverse()

    for key, value in pathDic.items():
        print("key==========>\n" , key)
        print("value==========>\n", value)
        print(FreqTree(value, minimumSup))
        # TODO recursive rule generation


FP_Growth(itemsets, 3)

