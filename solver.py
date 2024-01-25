
from copy import deepcopy
class Solver:
    def __init__(self, matrix):
        self.original = matrix
        self.solutions = []
    def findZero(self, matrix):
        for x in range(3):
            for y in range(3):
                if matrix[x][y] == 0:
                    return [x, y]
    def solve(self, matrix):
        if self.checkSolve(matrix):
            print("already solved")
        else:
            zeroIsAt = self.findZero(matrix)
            if zeroIsAt[0] != 0:
                self.moveUp(deepcopy(matrix), [])
            if zeroIsAt[1] != 0:
                self.moveLeft(deepcopy(matrix), [])
            if zeroIsAt[0] != 2:
                self.moveDown(deepcopy(matrix), [])
            if zeroIsAt[1] != 2:
                self.moveRight(deepcopy(matrix), [])
    def moveUp(self, matrix, steps):
        steps.append("up")
        matrixLoc = self.findZero(matrix)
        helper = matrix[matrixLoc[0] - 1][matrixLoc[1]]
        matrix[matrixLoc[0] - 1][matrixLoc[1]] = matrix[matrixLoc[0]][matrixLoc[1]]
        matrix[matrixLoc[0]][matrixLoc[1]] = helper
        self.solveRecursion(matrix, steps)
    def moveDown(self, matrix, steps):
        steps.append("down")
        matrixLoc = self.findZero(matrix)
        helper = matrix[matrixLoc[0] + 1][matrixLoc[1]]
        matrix[matrixLoc[0] + 1][matrixLoc[1]] = matrix[matrixLoc[0]][matrixLoc[1]]
        matrix[matrixLoc[0]][matrixLoc[1]] = helper
        self.solveRecursion(matrix, steps)
    def moveLeft(self, matrix, steps):
        steps.append("left")
        matrixLoc = self.findZero(matrix)
        helper = matrix[matrixLoc[0]][matrixLoc[1] - 1]
        matrix[matrixLoc[0]][matrixLoc[1] - 1] = matrix[matrixLoc[0]][matrixLoc[1]]
        matrix[matrixLoc[0]][matrixLoc[1]] = helper
        self.solveRecursion(matrix, steps)
    def moveRight(self, matrix, steps):
        steps.append("right")
        matrixLoc = self.findZero(matrix)
        helper = matrix[matrixLoc[0]][matrixLoc[1] + 1]
        matrix[matrixLoc[0]][matrixLoc[1] + 1] = matrix[matrixLoc[0]][matrixLoc[1]]
        matrix[matrixLoc[0]][matrixLoc[1]] = helper
        self.solveRecursion(matrix, steps)
    def checkSolve(self, matrix):
        soughtInt = 1
        for x in range(3):
            for y in range(3):
                if matrix[x][y] == soughtInt:
                    soughtInt += 1
                elif matrix[x][y] == 0:
                    soughtInt += 1
                else:
                    return False
        return True
    def solveRecursion(self, matrix, steps):
        if self.checkSolve(matrix):
            self.solutions.append(steps)
        elif len(steps) > 30:
            pass
        elif self.original == matrix:
            pass
        else:
            zeroIsAt = self.findZero(matrix)
            if zeroIsAt[0] != 0:
                self.moveUp(deepcopy(matrix), steps)
            if zeroIsAt[1] != 0:
                self.moveLeft(deepcopy(matrix), steps)
            if zeroIsAt[0] != 2:
                self.moveDown(deepcopy(matrix), steps)
            if zeroIsAt[1] != 2:
                self.moveRight(deepcopy(matrix), steps)