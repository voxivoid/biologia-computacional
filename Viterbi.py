# coding=utf-8
from Bio.SubsMat import MatrixInfo
import time



class Item:
    value = 0
    #traceback[0] = diagonal, traceback[1] = up, traceback[2] = left
    traceback = []

    def __init__(self, value):
        self.value = value
        self.traceback = []

    def __repr__(self):
        return "V: " + str(self.value) + " Tb: " +str(self.traceback)
        #return str(self.value)

    def addItemToTraceback(self, item):
        self.traceback.append(item)

    def setTraceback(self, traceback):
        self.traceback = traceback

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def getTraceback(self):
        return self.traceback


#transition matrix
transitionMatrix = [["", 1, 2, 3], [1, 0.6, 0.4, 0], [2, 0.25, 0.5, 0.25], [3, 0.25, 0.25, 0.5]]

#emission matrix
emissionMatrix = [["", "A", "T", "G", "C"], [1, 0.4, 0.3, 0.3, 0], [2, 0.1, 0.1, 0.4, 0.4], [3, 0.4, 0.3, 0, 0.3]]

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

    for line in range(len(matrix)):
        print matrix[line]

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


def needlemanWunsch(matrix, scoringMatrix, gapValue):
    for line in range(2, len(matrix)):
        for column in range(2, len(matrix[0])):
            gapUp = matrix[line - 1][column].getValue() + gapValue
            gapLeft = matrix[line][column - 1].getValue() + gapValue

            # this is made because the matrix doesn't have all the combinations eg. there's no (C,I) but there's (I,C)
            s = scoringMatrix.get((matrix[0][column], matrix[line][0]))
            if (s is None):
                s = scoringMatrix.get((matrix[line][0], matrix[0][column]))
            match = matrix[line - 1][column - 1].getValue() + s

            traceback = [0,0,0]
            value = max([gapUp, gapLeft, match])

            if (match == value):
                traceback[0] = 1

            if (gapUp == value):
                traceback[1] = 1

            if (gapLeft == value):
                traceback[2] = 1

            matrix[line][column] = Item(value)
            matrix[line][column].setTraceback(traceback)
    return matrix

def traceback(matrix, x, y, seq1, seq2):
    currentItem = matrix[x][y]
    s1 = seq1
    s2 = seq2

    if(x == 1 and y == 1 ):
        dashes = ""
        for i in range(len(s1)):
            dashes += "|"
        print "Score: " + str(matrix[len(matrix) - 1][len(matrix[0]) - 1].getValue())
        print s1
        print dashes
        print s2

    tb = currentItem.getTraceback()
    if(tb[0] == 1):
        #print "Diagonal"
        s1temp = matrix[0][y] + s1
        s2temp = matrix[x][0] + s2
        traceback(matrix, x - 1, y - 1, s1temp, s2temp)
    if(tb[1] == 1):
        #print "Cima"
        s1temp = "-" + s1
        s2temp = matrix[x][0] + s2
        traceback(matrix, x - 1, y, s1temp, s2temp)
    if(tb[2] == 1):
        #print "Esquerda"
        s1temp = matrix[0][y] + s1
        s2temp = "-" + s2
        traceback(matrix, x, y - 1, s1temp, s2temp)


start = time.time()

matrix = initMatrix("CATGCGGGTTATAAC")
#traceback(matrix, len(matrix) - 1, len(matrix[0]) - 1, "", "")

#for line in range(len(matrix)):
 #   print matrix[line]

end = time.time()
print end - start
