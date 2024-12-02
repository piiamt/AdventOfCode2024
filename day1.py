import numpy as np
def reader(filename):
    col1, col2 = [], []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            first, second = line.strip().split()
            col1.append(int(first))
            col2.append(int(second))
    return(col1, col2)

def totaldistance(list1, list2):
    list1.sort()
    list2.sort()
    distance = 0
    for i in np.arange(len(list1)):
        diff = abs(list1[i] - list2[i])
        distance = distance + diff
    return(distance)