# coding=utf-8
from Bio.SubsMat import MatrixInfo


class Item:
    value = 0
    # items on traceback are represented by tuples eg. item matrix[1][1] is represented by the tuple (1,1)
    traceback = [0,0,0]
    visited = False

    def __init__(self, value):
        self.value = value
        self.traceback = [0,0,0]

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


def initMatrix(s1, s2, gapValue):
    # size of the strings + gap + string representation
    matrix = [[0 for line in range(len(s1) + 2)] for column in range(len(s2) + 2)]

    # initializing gap line and column
    for line in range(0, len(matrix) - 1):
        item = Item(gapValue * line)
        if (line > 0):
            item.setTraceback([0,1,0])
        matrix[line + 1][1] = item

    for column in range(0, len(matrix[0]) - 1):
        item = Item(gapValue * column)
        if (column > 0):
            item.setTraceback([0,0,1])
        matrix[1][column + 1] = item

    # inserting strings in the matrix
    for column in range(0, len(s1)):
        matrix[0][column + 2] = s1[column].upper()

    for line in range(0, len(s2)):
        matrix[line + 2][0] = s2[line].upper()

    """for line in range(len(matrix)):
        print matrix[line]"""

    return matrix


def needlemanWunsch(matrix, scoringMatrix, gapValue):
    for line in range(2, len(matrix)):
        for column in range(2, len(matrix[0])):

            """for l in range(len(matrix)):
                print matrix[l]

            print "Line: " + str(line) + " Column: " + str(column)
            print "Score : " + str(scoringMatrix.get((matrix[0][column], matrix[line][0]))) + str(
                matrix[0][column]) + "," + str(matrix[line][0])"""
            gapUp = matrix[line - 1][column].getValue() + gapValue
            gapLeft = matrix[line][column - 1].getValue() + gapValue

            # this is made because the matrix doesn't have all the combinations eg. there's no (C,I) but there's (I,C)
            s = scoringMatrix.get((matrix[0][column], matrix[line][0]))
            if (s is None):
                s = scoringMatrix.get((matrix[line][0], matrix[0][column]))
            match = matrix[line - 1][column - 1].getValue() + s

            traceback = [0, 0, 0]
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
        s1 = matrix[0][y] + s1
        s2 = matrix[x][0] + s2
        traceback(matrix, x - 1, y - 1, s1, s2)
    if(tb[1] == 1):
        #print "Cima"
        s1 = "-" + s1
        s2 = matrix[x][0] + s2
        traceback(matrix, x - 1, y, s1, s2)
    if(tb[2] == 1):
        #print "Esquerda"
        s1 = matrix[0][y] + s1
        s2 = "-" + s2
        traceback(matrix, x, y - 1, s1, s2)

matrix = initMatrix("WPCIWWPC", "IIWPC", -5)
matrix = needlemanWunsch(matrix, MatrixInfo.blosum50, -5)
traceback(matrix, len(matrix) - 1, len(matrix[0]) - 1, "", "")

for line in range(len(matrix)):
    print matrix[line]