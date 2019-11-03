def sortFunc(itemDict):
    return itemDict['sort']


def mySort(productList, workout):
    myList = productList
    myList.sort(key = sortFunc)
    if(workout):
        listHold = myList
        listLen = len(myList)
        for x in range(listLen):
            if (x % 2 == 0):
                myList[x] = listHold[round(listLen - (x/2 + 1))]
            else:
                myList[x] = listHold[round((x+1)/2 - 1)]
    return myList
    
