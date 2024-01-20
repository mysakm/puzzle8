import tkinter


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def solveWorker():
    notace = entry.get()
    if len(notace) != 9:
        warning.config(text="Nesprávné množství elementů.")
    else:
        matrix = [[], [], []]
        for x in range(len(notace)):
            matrix[x // 3].append(int(notace[x]))
        print(matrix)
        if checkSolve(matrix):
            warning.config(text="Already solved!")
        else:
            zeroPos = findZero(matrix)
            print(zeroPos)
            attemptSolve(matrix)


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


def attemptSolve(matrix):
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
parent = tkinter.Tk()
tkinter.Label(parent, text="Vlož číselnou notaci puzzle:").grid()
entry = tkinter.Entry(parent)
entry.grid()
warning = tkinter.Label(parent, text="")
warning.grid()
tkinter.Button(parent, text="Vyřešit", command=solveWorker).grid()
tkinter.mainloop()
