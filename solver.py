import threading
import time
import tkinter
from copy import deepcopy


class Solver:
    def __init__(self, matrix, listbox, resultNumber):
        self.original = matrix
        self.maxSolutions = int(resultNumber)
        self.solutions = []
        self.final = []
        self.solve(matrix)
        while len(self.solutions) < self.maxSolutions:
            time.sleep(5)
        self.final = self.solutions[0]
        for i in range(len(self.solutions)):
            if len(self.solutions[i]) < len(self.final):
                self.final = self.solutions[i]
        print(self.final)
        currMat = matrix
        for x in self.final:
            listbox.insert("end", self.unwrap(currMat))
            if x == "right":
                matrixLoc = self.findZero(currMat)
                helper = currMat[matrixLoc[0]][matrixLoc[1] + 1]
                currMat[matrixLoc[0]][matrixLoc[1] + 1] = currMat[matrixLoc[0]][matrixLoc[1]]
                currMat[matrixLoc[0]][matrixLoc[1]] = helper
            elif x == "left":
                matrixLoc = self.findZero(currMat)
                helper = currMat[matrixLoc[0]][matrixLoc[1] - 1]
                currMat[matrixLoc[0]][matrixLoc[1] - 1] = currMat[matrixLoc[0]][matrixLoc[1]]
                currMat[matrixLoc[0]][matrixLoc[1]] = helper
            elif x == "up":
                matrixLoc = self.findZero(currMat)
                helper = currMat[matrixLoc[0] - 1][matrixLoc[1]]
                currMat[matrixLoc[0] - 1][matrixLoc[1]] = currMat[matrixLoc[0]][matrixLoc[1]]
                currMat[matrixLoc[0]][matrixLoc[1]] = helper
            elif x == "down":
                matrixLoc = self.findZero(currMat)
                helper = currMat[matrixLoc[0] + 1][matrixLoc[1]]
                currMat[matrixLoc[0] + 1][matrixLoc[1]] = currMat[matrixLoc[0]][matrixLoc[1]]
                currMat[matrixLoc[0]][matrixLoc[1]] = helper
        listbox.insert("end", self.unwrap(currMat))

    def findZero(self, matrix):
        for x in range(3):
            for y in range(3):
                if matrix[x][y] == 0:
                    return [x, y]

    def unwrap(self, matrix):
        result = ""
        for a in matrix:
            for b in a:
                result += str(b)
        return result

    def solve(self, matrix):
        if self.checkSolve(matrix):
            print("already solved")
        else:
            try:
                zeroIsAt = self.findZero(matrix)
                if zeroIsAt[0] != 0:
                    threadUp = threading.Thread(target=self.moveUp, args=(deepcopy(matrix), []))
                    threadUp.start()
                    #self.moveUp(deepcopy(matrix), [])
                if zeroIsAt[1] != 0:
                    threadLeft = threading.Thread(target=self.moveLeft, args=(deepcopy(matrix), []))
                    threadLeft.start()
                    #self.moveLeft(deepcopy(matrix), [])
                if zeroIsAt[0] != 2:
                    threadDown = threading.Thread(target=self.moveDown, args=(deepcopy(matrix), []))
                    threadDown.start()
                    #self.moveDown(deepcopy(matrix), [])
                if zeroIsAt[1] != 2:
                    threadRight = threading.Thread(target=self.moveRight, args=(deepcopy(matrix), []))
                    threadRight.start()
                    #self.moveRight(deepcopy(matrix), [])
            except:
                pass

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
            print(matrix, len(steps), self.solutions)
            self.solutions.append(steps)
        elif len(steps) > 30:
            pass
        elif self.original == matrix:
            pass
        else:
            #print(matrix, len(steps), self.solutions)
            zeroIsAt = self.findZero(matrix)
            if zeroIsAt[0] != 0 and steps[-1] != "down" and len(self.solutions) < self.maxSolutions:
                threadUp = threading.Thread(target=self.moveUp, args=(deepcopy(matrix), deepcopy(steps)))
                threadUp.start()
                #self.moveUp(deepcopy(matrix), deepcopy(steps))
            if zeroIsAt[1] != 0 and steps[-1] != "right" and len(self.solutions) < self.maxSolutions:
                threadLeft = threading.Thread(target=self.moveLeft, args=(deepcopy(matrix), deepcopy(steps)))
                threadLeft.start()
                #self.moveLeft(deepcopy(matrix), deepcopy(steps))
            if zeroIsAt[0] != 2 and steps[-1] != "up" and len(self.solutions) < self.maxSolutions:
                threadDown = threading.Thread(target=self.moveDown, args=(deepcopy(matrix), deepcopy(steps)))
                threadDown.start()
                #self.moveDown(deepcopy(matrix), deepcopy(steps))
            if zeroIsAt[1] != 2 and steps[-1] != "left" and len(self.solutions) < self.maxSolutions:
                threadRight = threading.Thread(target=self.moveRight, args=(deepcopy(matrix), deepcopy(steps)))
                threadRight.start()
                #self.moveRight(deepcopy(matrix), deepcopy(steps))
