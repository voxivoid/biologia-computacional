# coding=utf-8

print("Hello World")


class Item:
   value = 0
   traceback = []

   def addItemToTraceback(self, item):
      self.traceback.append(item)

   def setValue(self, value):
      self.value = value

def initMatrix(s1, s2, gapValue):
   #size of the strings + gap + string representation
   matrix = [[0 for i in range(len(s1) + 2)] for j in range(len(s2) + 2)]

   #initializing gap line and column
   for i in range(0, len(matrix) - 1):
      matrix[i + 1][1] = gapValue * i

   for j in range(0, len(matrix[0]) - 1):
      matrix[1][j + 1] = gapValue * j

   #inserting strings in the matrix
   for i in range(0, len(s1)):
      matrix[i + 2][0] = s1[i]

   for j in range(0, len(s2)):
      matrix[0][j + 2] = s2[j]

   return matrix


initMatrix("teste", "teste", -3)