# coding=utf-8
from Bio.SubsMat import MatrixInfo

class Item:
    value = 0
    #items on traceback are represented by tuples eg. item matrix[1][1] is represented by the tuple (1,1)
    traceback = []

    def __init__(self, value):
        self.value = value
        self.traceback = []

    def __repr__(self):
        #return "V: " + str(self.value) + " Tb: " +str(self.traceback)
        return str(self.value)

    def addItemToTraceback(self, item):
        self.traceback.append(item)

    def setTraceback(self, traceback):
        self.traceback = traceback

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value


def initMatrix(s1, s2, gapValue):
    # size of the strings + gap + string representation
    matrix = [[0 for line in range(len(s1) + 2)] for column in range(len(s2) + 2)]

    # initializing gap line and column
    for line in range(0, len(matrix) - 1):
        item = Item(gapValue * line)
        if(line > 0):
            item.addItemToTraceback((line,1))
        matrix[line + 1][1] = item

    for column in range(0, len(matrix[0]) - 1):
        item = Item(gapValue * column)
        if(column > 0):
            item.addItemToTraceback((1,column))
        matrix[1][column + 1] = item

    # inserting strings in the matrix
    for column in range(0, len(s1)):
        matrix[0][column + 2] = s1[column].upper()

    for line in range(0, len(s2)):
        matrix[line + 2][0] = s2[line].upper()

    for line in range(len(matrix)):
        print matrix[line]

    return matrix


def needlemanWunsch(matrix, scoringMatrix, gapValue):
    for line in range(2, len(matrix)):
        for column in range(2, len(matrix[0])):

            for l in range(len(matrix)):
                print matrix[l]

            print "Line: " + str(line) + " Column: " + str(column)
            print "Score : " + str(scoringMatrix.get((matrix[0][column], matrix[line][0]))) + str(matrix[0][column]) + "," + str(matrix[line][0])
            gapUp = matrix[line - 1][column].getValue() + gapValue
            gapLeft = matrix[line][column - 1].getValue() + gapValue

            #this is made because the matrix doesn't have all the combinations eg. there's no (C,I) but there's (I,C)
            s = scoringMatrix.get((matrix[0][column], matrix[line][0]))
            if(s is None):
                s = scoringMatrix.get((matrix[line][0], matrix[0][column]))
            match = matrix[line - 1][column - 1].getValue() + s

            #traceback is initialized with match item
            """
            traceback = [(line - 1, column - 1)]
            value = match

            if(match < gapUp):
                traceback = [(line - 1, column)]
                value = gapUp
            elif(match == gapUp):
                traceback.append((line - 1, column))

            if(gapUp < gapLeft):
                traceback = [(line, column - 1)]
                value = gapLeft
            elif(gapUp == gapLeft):
                traceback.append((line, column - 1))
            """
            traceback = []
            value = max([gapUp, gapLeft, match])

            if(gapUp == value):
                traceback = [(line - 1, column)]

            if(gapLeft == value):
                traceback = [(line, column - 1)]

            if(match == value):
                traceback = [(line - 1, column - 1)]

            matrix[line][column] = Item(value)
            matrix[line][column].setTraceback = traceback

            #TODO adicionar o traceback
    return matrix

matrix = initMatrix("WPCIWWPC", "IIWPC", -5)
matrix = needlemanWunsch(matrix, MatrixInfo.blosum50, -5)

for line in range(len(matrix)):
    print matrix[line]