import numpy as np
def reader(filename):
    col1, col2, updates = [],[],[]#np.array([]), np.array([]), np.empty((0,2))
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if '|' in line:
                first, second = line.strip().split('|')
                col1.append(int(first))
                col2.append(int(second))
            elif ',' in line:
                numbers = line.strip().split(',')
                updates.append(list(map(int, numbers)))
    return(col1, col2, updates)

def isordered(col1, col2, updates):
    col1 = np.array(col1)
    col2 = np.array(col2)
    #updates = np.array(updates)
    for update in updates[0:1]:
        #print(update)
        ordered = True
        for i in range(len(update)):
            # finds all half-relevant rule indexes
            if update[i] in col1:
                rules1 = np.where(col1==update[i])[0]
            if update[i] in col2:
                rules1 = np.append(rules1, np.where(col2==update[i])[0])
            if (update not in col1) and (update not in col2):
                x=1
            if i!=(len(update)-1): # if not at last number
                first = update[i]
                second = update[i+1]
                for j in range(len(update[i+1:])):
                    if (update[j] in col1) or (update[j] in col2):
                        x=3
            print(rules1)
        for r in rules1:
            if r not in update:
                #rules.pop(r)
                x=1
    return rules


col1,col2,updates = reader('/Users/piiamt/Documents/codes/Python/day5test.txt')
print(isordered(col1,col2,updates))
#print(np.where(col1==75)[0])
#print(updates[0])
