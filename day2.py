from day1 import reader

def similarityscore(list1, list2):
    list1.sort()
    list2.sort()
    similarity = 0
    for i in list1:
        amount = list2.count(i)
        similarity = similarity + i*amount
    return(similarity)