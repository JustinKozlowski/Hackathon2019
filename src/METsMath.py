def nodeDist(Node1, Node2):
    #get path between nodes
    unit = #figure out unit


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
        time = dist/#speed make in hours
        caloriesburned = Mets*MetsValue*time
        return caloriesburned
