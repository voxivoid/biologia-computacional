# coding=utf-8
from Bio.SubsMat import MatrixInfo
import time



class Item:
    value = 0

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "V: " + str(self.value)

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value


#transition matrix
transitionMatrix = [["", 1, 2, 3], [1, 0.6, 0.4, 0], [2, 0.25, 0.5, 0.25], [3, 0.25, 0.25, 0.5]]

#emission matrix
emissionMatrix = [["", "A", "T", "G", "C"], [1, 0.4, 0.3, 0.3, 0], [2, 0.1, 0.1, 0.4, 0.4], [3, 0.4, 0.3, 0, 0.3]]
#emissionMatrix = [["", "A", "T", "G", "C"], [1, 0.4, 0.3, 0.3, 0], [2, 0.2, 0.2, 0.3, 0.3], [3, 0.5, 0, 0, 0.5]]

states = len(transitionMatrix[0]) - 1

def initMatrix(seq):
    # size of the strings + string representation || state number
    matrix = [[0 for column in range(len(seq) + 1)] for line in range(states + 1)]

    # inserting strings in the matrix
    for column in range(len(seq)):
        matrix[0][column + 1] = seq[column].upper()

    for line in range(0, states):
        matrix[line + 1][0] = transitionMatrix[line + 1][0]

    # initializing gap line and column
    for line in range(0, len(matrix) - 1):
        item = Item(getEmissionValue(seq[0], line + 1) * (1/float(states)))
        matrix[line + 1][1] = item

    return matrix

def getEmissionValue(char, state):
    if(char == "A"):
        return emissionMatrix[state][1]
    elif(char == "T"):
        return emissionMatrix[state][2]
    elif(char == "G"):
        return emissionMatrix[state][3]
    elif(char == "C"):
        return emissionMatrix[state][4]

def getTransitionValue(state1, state2):
    return transitionMatrix[state1][state2]


def forward(matrix):
    for column in range(2, len(matrix[0])):
        for line in range(1, len(matrix)):
            currentValue = 0
            for state in range(1, len(matrix)):
                currentValue += float(matrix[state][column-1].getValue()) * float(getEmissionValue(matrix[0][column], line)) * float(getTransitionValue(state, line))
            matrix[line][column] = Item(currentValue)
    return matrix

start = time.time()

#matrix = initMatrix("CATG")
matrix = initMatrix("CATGCGGGTTATAAC")
forward(matrix)

forward = 0
for i in range(1, len(matrix)):
    forward += matrix[i][len(matrix[0]) - 1].getValue()
forward *= (1/float(states))

for line in range(len(matrix)):
    print matrix[line]
print forward

end = time.time()
print end - start
