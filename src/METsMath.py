def nodeLoc(aisle, sort, side):
    x = 0
    y = 0
    nodeDict = {
            "Dairy": [53,5],
            "Service Meat":[105,9],
            "Cheese Shop": [79,9],
            "Floral":[77,15],
            "Mediterranean Bar":[81,24],
            "Deli":[96,16],
            "Seafood":[105,19],
            "Packaged Bakery":[103,26],
            "Bakery":[97,41],
            "Kosher Deli":[104,36],
            "Prepared Foods":[105,45],
            "Sushi":[106,52],
            "Asian Bar": [97,61],
            "Salad Bar":[101,51],
            "Sub Shop":[116,58],
            "Pizza":[99,64],
            "European Breads":[89,63],
            "Coffee Shop":[89,66],
            "Newspapers":[72,67],
            "Catering":[48,68],
            "Beer Shop":[6,6],
            "Pharmacy":[51,43],
            "Produce":[77,47],
            "22":[9,10],
            "21":[6,7],
            "20":[2,4],
            "19":[2,4],
            "18":[6,7],
            "17":[9,11],
            "16":[13,14],
            "15":[16,18],
            "14":[20,21],
            "13":[23,25],
            "12":[27,28],
            "11":[30,32],
            "10":[34,35],
            "9":[37,39],
            "8":[41,43],
            "7":[44,46],
            "6":[48,49],
            "5":[51,53],
            "4":[55,57],
            "3":[59,60],
            "2":[62,63],
            "1":[65,66],
            "A":43,
            "B":20
            }

    if len(aisle) > 3:
        x = nodeDict[aisle][0]
        y = nodeDict[aisle][1]
    elif len(aisle) == 3:
        x = nodeDict[aisle[:2]][side]
        y = nodeDict[aisle[2:]]
    else:
        x = nodeDict[aisle][0]
        y = nodeDict[aisle][1]
    return (x, y)


def bfs(grid, start, goal):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < 120 and 0 <= y2 < 76 and grid[y2][x2] != 0 and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

def nodeDist(path):
    dist = len(path)
    return dist


def GetMets(carttype, weight):
    if carttype == "basket":
        return (weight*0.0566 + 2.3)
    if carttype == "cart":
        if weight > 30:
            return (weight*0.066 + 3)
        else:
            return (weight*0.133 + 1)

def MetsMath(carttype, weight, path):
        dist = nodeDist(path)
        METs = GetMets(carttype, weight)
        MetsValue = weight *0.453592
        time = dist/1609.34
        caloriesburned = Mets*MetsValue*time
        return caloriesburned
