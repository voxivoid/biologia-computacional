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
        return "V: " + str(self.value) + " Tb: " +str(self.traceback)

    def addItemToTraceback(self, item):
        self.traceback.append(item)

    def setValue(self, value):
        self.value = value


def initMatrix(s1, s2, gapValue):
    # size of the strings + gap + string representation
    matrix = [[0 for i in range(len(s1) + 2)] for j in range(len(s2) + 2)]

    # initializing gap line and column
    for i in range(0, len(matrix) - 1):
        item = Item(gapValue * i)
        if(i > 0):
            item.addItemToTraceback((i,1))
        matrix[i + 1][1] = item

    for j in range(0, len(matrix[0]) - 1):
        item = Item(gapValue * j)
        if(j > 0):
            item.addItemToTraceback((1,j))
        matrix[1][j + 1] = item

    # inserting strings in the matrix
    for i in range(0, len(s1)):
        matrix[i + 2][0] = s1[i].upper()

    for j in range(0, len(s2)):
        matrix[0][j + 2] = s2[j].upper()

    for i in range(len(matrix)):
        print matrix[i]

    return matrix


def needlemanWunsch(matrix, scoringMatrix, gapValue):
    return


matrix = initMatrix("teste", "teste", -3)