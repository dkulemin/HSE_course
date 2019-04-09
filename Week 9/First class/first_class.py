from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, myList):
        self.myList = copy.deepcopy(myList)

    def __str__(self):
        result = ''
        for i in self.myList:
            result += '\t'.join(map(str, i))
            result += '\n'
        return result[:-1]

    def size(self):
        return len(self.myList), len(self.myList[0])

    def __add__(self, other):
        if self.size() == other.size():
            newMatrix = []
            for i in range(len(self.myList)):
                tempList = []
                for j in range(len(self.myList[i])):
                    tempList.append(self.myList[i][j] + other.myList[i][j])
                newMatrix.append(tempList)
        else:
            raise MatrixError(self, other)
        return Matrix(newMatrix)

    def __mul__(self, n):
        newMatrix = []
        for i in range(len(self.myList)):
            tempList = []
            for j in range(len(self.myList[i])):
                tempList.append(self.myList[i][j] * n)
            newMatrix.append(tempList)
        return Matrix(newMatrix)

    __rmul__ = __mul__

    def transpose(self):
        tempMatrix = []
        for i in range(len(self.myList[0])):
            tempList = []
            for now in self.myList:
                tempList.append(now[i])
            tempMatrix.append(tempList)
        self.myList = tempMatrix
        return self

    @staticmethod
    def transposed(matrix):
        newMatrix = []
        for i in range(len(matrix.myList[0])):
            tempList = []
            for now in matrix.myList:
                tempList.append(now[i])
            newMatrix.append(tempList)
        return Matrix(newMatrix)


exec(stdin.read())
