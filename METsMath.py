def bfs(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

def nodeDist(Node1, Node2):
    path = bfs(grid, Node1, Node2)
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

def MetsMath(Node1, Node2, carttype, weight):
        dist = node1 - node2
        METs = GetMets(carttype, weight)
        MetsValue = weight *0.453592
        dist = nodeDist(Node1, Node2)
        time = dist/1609.34
        caloriesburned = Mets*MetsValue*time
        return caloriesburned
