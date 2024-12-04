import numpy as np
import re
def reader(filename):
    with open(filename, 'r') as file:
        text = [line.rstrip() for line in file]
    return(text)

def transposer(lines):
    '''Transposes a matrix of strings'''
    transposed = []
    for i in range(len(lines[0])):
        newline = ''
        for j in range(len(lines)):
            newline += lines[j][i]
        transposed.append(newline)
    return(transposed)

def counttimes(lines):
    '''Counts occurrences of 'XMAS' forwards and backwards in input array'''
    counter = 0
    for line in lines:
        counter += line.count('XMAS') + line.count('SAMX')
    return counter

def findMASindex(lines):
    '''Finds the midpoint indexes of all MAS occurrences in a pre-shifted array'''
    indexes = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            try:
                if (lines[i][j-1:j+2]=='MAS') or (lines[i][j-1:j+2]=='SAM'):
                    indexes.append([i,j])
                else:
                    next
            except: next
    return(indexes)

def XMASfinder(lines):
    '''
    Finds all occurrences of 'XMAS' in lines going forward, backward,
    up, down and diagonally in all ways
    '''
    counter = 0
    rightshift = []
    leftshift = []
    for i in range(len(lines)): 
        # first reading forward and backward occurrences of XMAS
        counter = counter + (lines[i].count('XMAS') + lines[i].count('SAMX'))
        # Making a matrix of shifting diagonals into verticals
        addedr = lines[i].ljust(len(lines[i])+len(lines[i])-1-i, '.')
        addedr = addedr[::-1].ljust(len(addedr)+i, '.')[::-1]
        rightshift.append(addedr)
        addedl = lines[i][::-1].ljust(len(lines[i])+len(lines[i])-1-i, '.')[::-1]
        addedl = addedl.ljust(len(addedl)+i, '.')
        leftshift.append(addedl)
    # Creating transposed str matrix for reading words up and down
    T = transposer(lines)
    rightshiftT = transposer(rightshift)
    leftshiftT = transposer(leftshift)
    counter += counttimes(T) + counttimes(rightshiftT) + counttimes(leftshiftT)
    # Now finding indexes of the midpoints of all MAS-es
    rightAs = findMASindex(rightshift)
    rightAsT = findMASindex(rightshiftT)
    leftAs = findMASindex(leftshift)
    leftAsT = findMASindex(leftshiftT)
    Xcounter = 0
    OGir = []
    OGil = []
    dimensions = len(lines)
    for i in rightAsT:
        OGir.append([i[1], i[0]-i[1]])
    for i in leftAsT:
        OGil.append([i[1], i[0]-dimensions+i[1]+1])
    for index in OGir:
        if index in OGil:
            Xcounter += 1
    return counter, Xcounter


lines = reader('/Users/piiamt/Documents/codes/Python/day4.txt')
print(XMASfinder(lines))