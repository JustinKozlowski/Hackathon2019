def sortFunc(itemDict):
    return itemDict['sort']


def main(productList, workout):
    myList = productList
    myList.sort(key = sortFunc)
    if(workout):
        listHold = myList
        listLen = len(myList)
        for x in range(listLen):
            if(x % 2):
                myList[x] = listHold[listLen - (x/2 + 1)]
            else:
                myList[x] = listHold[(x+1)/2 - 1]
    return myList
    
