import tkinter
from solver import Solver


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# 182043765

def solveWorker():
    notace = entry.get()
    if len(notace) != 9:
        warning.config(text="Nesprávné množství elementů.")
    else:
        matrix = [[], [], []]
        for x in range(len(notace)):
            matrix[x // 3].append(int(notace[x]))
        if checkSolve(matrix):
            warning.config(text="Already solved!")
        else:
            solveeer = Solver(matrix)



def findZero(matrix):
    for x in range(3):
        for y in range(3):
            if matrix[x][y] == 0:
                return [x, y]


def checkSolve(matrix):
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
"""


def attemptSolve(matrix):
    currentInfo = {
        "matrix" : matrix,
        "original" : matrix,
        "zeroAt" : findZero(matrix),
        "steps" : []
    }
    allMoves = []
    if currentInfo["zeroAt"][0] != 0:
        allMoves.append(moveUp(deepcopy(currentInfo)))
    if currentInfo["zeroAt"][1] != 0:
        allMoves.append(moveLeft(deepcopy(currentInfo)))
    if currentInfo["zeroAt"][0] != 2:
        allMoves.append(moveDown(deepcopy(currentInfo)))
    if currentInfo["zeroAt"][1] != 2:
        allMoves.append(moveRight(deepcopy(currentInfo)))
    # 182043765
    print("Done")
    for i in allMoves:
        print(i)
    print("Done")
def moveUp(currentInfo):
    currentInfo["steps"].append("up")
    rebuiltArr = deepcopy(currentInfo["matrix"])
    helper = rebuiltArr[currentInfo["zeroAt"][0] - 1][currentInfo["zeroAt"][1]]
    rebuiltArr[currentInfo["zeroAt"][0] - 1][currentInfo["zeroAt"][1]] = rebuiltArr[currentInfo["zeroAt"][0]][currentInfo["zeroAt"][1]]
    rebuiltArr[currentInfo["zeroAt"][0]][currentInfo["zeroAt"][1]] = helper
    currentInfo["matrix"] = rebuiltArr
    return attemptSolveRecursion(currentInfo)
def moveDown(currentInfo):
    currentInfo["steps"].append("down")
    rebuiltArr = deepcopy(currentInfo["matrix"])
    helper = rebuiltArr[currentInfo["zeroAt"][0] + 1][currentInfo["zeroAt"][1]]
    rebuiltArr[currentInfo["zeroAt"][0] + 1][currentInfo["zeroAt"][1]] = rebuiltArr[currentInfo["zeroAt"][0]][currentInfo["zeroAt"][1]]
    rebuiltArr[currentInfo["zeroAt"][0]][currentInfo["zeroAt"][1]] = helper
    currentInfo["matrix"] = rebuiltArr
    return attemptSolveRecursion(currentInfo)
def moveRight(currentInfo):
    currentInfo["steps"].append("right")
    rebuiltArr = deepcopy(currentInfo["matrix"])
    helper = rebuiltArr[currentInfo["zeroAt"][0]][currentInfo["zeroAt"][1] + 1]
    rebuiltArr[currentInfo["zeroAt"][0]][currentInfo["zeroAt"][1] + 1] = rebuiltArr[currentInfo["zeroAt"][0]][currentInfo["zeroAt"][1]]
    rebuiltArr[currentInfo["zeroAt"][0]][currentInfo["zeroAt"][1]] = helper
    currentInfo["matrix"] = rebuiltArr
    return attemptSolveRecursion(currentInfo)
def moveLeft(currentInfo):
    currentInfo["steps"].append("left")
    rebuiltArr = deepcopy(currentInfo["matrix"])
    helper = rebuiltArr[currentInfo["zeroAt"][0]][currentInfo["zeroAt"][1] - 1]
    rebuiltArr[currentInfo["zeroAt"][0]][currentInfo["zeroAt"][1] - 1] = rebuiltArr[currentInfo["zeroAt"][0]][currentInfo["zeroAt"][1]]
    rebuiltArr[currentInfo["zeroAt"][0]][currentInfo["zeroAt"][1]] = helper
    currentInfo["matrix"] = rebuiltArr
    return attemptSolveRecursion(currentInfo)
def attemptSolveRecursion(currentInfo):
    gotLooped = True
    for originalItem in currentInfo["original"]:
        for currentItem in currentInfo["matrix"]:
            if originalItem != currentItem:
                gotLooped = False
    if gotLooped:
        pass
    elif len(currentInfo["steps"]) > 30:
        pass
    elif checkSolve(currentInfo["matrix"]):
        return currentInfo
    else:
        allMovesPrep = []
        allMoves = []
        currentInfo["zeroAt"] = findZero(currentInfo["matrix"])
        if currentInfo["zeroAt"][0] != 0 and currentInfo["steps"][-1] != "down":
            allMovesPrep.append(moveUp(deepcopy(currentInfo)))
        if currentInfo["zeroAt"][1] != 0 and currentInfo["steps"][-1] != "right":
            allMovesPrep.append(moveLeft(deepcopy(currentInfo)))
        if currentInfo["zeroAt"][0] != 2 and currentInfo["steps"][-1] != "up":
            allMovesPrep.append(moveDown(deepcopy(currentInfo)))
        if currentInfo["zeroAt"][1] != 2 and currentInfo["steps"][-1] != "left":
            allMovesPrep.append(moveRight(deepcopy(currentInfo)))
        if type(allMovesPrep) == list:
            for item in allMovesPrep:
                if item != None:
                    if type(item) == list:
                        for item2 in item:
                            allMoves.append(item2)
                    else:
                        allMoves.append(item)
        else:
            allMoves = allMovesPrep
        for i in range(1, len(allMoves)):
            try:
                if allMoves[i] is not None:
                    if len(allMoves[i]["steps"]) > len(allMoves[i - 1]["steps"]):
                        allMoves.pop(i)
                        i-=1
                print(allMoves)
            except:
                break
        return allMoves
 """

parent = tkinter.Tk()
tkinter.Label(parent, text="Vlož číselnou notaci puzzle:").grid()
entry = tkinter.Entry(parent)
entry.grid()
warning = tkinter.Label(parent, text="")
warning.grid()
tkinter.Button(parent, text="Vyřešit", command=solveWorker).grid()
entry.focus()
tkinter.mainloop()
