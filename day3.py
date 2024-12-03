import re
def reader(filename):
    alllines = ''
    with open(filename, 'r') as file:
        lines = file.readlines()
        alllines = ''.join(lines)
    return(alllines)

def sum_multiplications(data):
    multiplications = []
    found = re.findall(r'mul\(\d+,\d+\)', data)
    for n in found:
        iend = n.find(')')
        numbers = n[4:iend].split(',')     
        try:
            number1,number2 = int(numbers[0]),int(numbers[1])
            multiplications.append(number1*number2)
        except: next
    return sum(multiplications)