import re
def reader(filename):
    alllines = ''
    with open(filename, 'r') as file:
        lines = file.readlines()
        alllines = ''.join(lines)
    return(alllines)

def multiplicationslist(data):
    multiplications = []
    # Finding all valid multiplications
    found = re.findall(r'mul\(\d+,\d+\)', data)
    for n in found:
        iend = n.find(')')
        numbers = n[4:iend].split(',')     
        try:
            number1,number2 = int(numbers[0]),int(numbers[1])
            multiplications.append(number1*number2)
        except: next
    return(multiplications)

def sum_multiplications(data):
    multiplications = multiplicationslist(data)
    # Added do() and don't()
    dont = data.split("don't()")
    domult = []
    for i in range(len(dont)):
        if i==0:
            domult.append(sum(multiplicationslist(dont[i])))
        else:
            dostr = dont[i].split("do()")
            for j in range(len(dostr)):
                if j!=0:
                    domult.append(sum(multiplicationslist(dostr[j])))
    return(sum(multiplications), sum(domult))

data = reader('/Users/piiamt/Documents/codes/Python/day3.txt')
print((sum_multiplications(data)))