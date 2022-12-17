"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day17/input.txt").read_text()

EXAMPLE_INPUT1 = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""
EXAMPLE_RESULT1 = 3068

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    #a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

class shapes:
    def __init__(self, typeId):
        # 0 -
        # 1 +
        # 2 reversed L
        # 3 I
        # 4 square
        self.stringRepresentation :str = []
        match typeId:
            case 0:
                self.stringRepresentation.append('|..@@@@.|')
                self.addH = 1
            case 1:
                self.stringRepresentation.append('|...@...|')
                self.stringRepresentation.append('|..@@@..|')
                self.stringRepresentation.append('|...@...|')
                self.addH = 3
            case 2:
                self.stringRepresentation.append('|....@..|')
                self.stringRepresentation.append('|....@..|')
                self.stringRepresentation.append('|..@@@..|')
                self.addH = 3
            case 3:
                self.stringRepresentation.append('|..@....|')
                self.stringRepresentation.append('|..@....|')
                self.stringRepresentation.append('|..@....|')
                self.stringRepresentation.append('|..@....|')
                self.addH = 4
            case 4:
                self.stringRepresentation.append('|..@@...|')
                self.stringRepresentation.append('|..@@...|')
                self.addH = 2



class game:
    def __init__(self, keyboardscommands :str):
        self.gameD = {}
        self.gameD[0] = '+-------+'
        self.gameDHight = 1
        self.commands :str = keyboardscommands
        self.currentCommandPos :int = 0
        self.sprites :shapes = []
        for i in range(5):
            self.sprites.append(shapes(i))
        self.currentShape :int = 0

    def getNextCommand(self):
        length = len(self.commands)
        nextCommand = self.commands[self.currentCommandPos % length]
        self.currentCommandPos += 1
        return nextCommand

    def addNextSprite(self):
        nextSprite :shapes = self.sprites[self.currentShape % 5]
        self.currentShape += 1
        numberOfRows = nextSprite.addH
        for i in range(3):
            self.gameD[self.gameDHight] = '|.......|'
            self.gameDHight += 1

        for i in range(numberOfRows):
            self.gameD[self.gameDHight] = nextSprite.stringRepresentation[numberOfRows - i - 1]
            self.gameDHight += 1

    def moveAccordingToCommand(self):
        thisCommand = self.getNextCommand()
        currentHigth = self.gameDHight
        boardD = self.gameD.copy()
            #scan gameBoard and see if a move is possible
        possible = True
        for i in range(1, 5): 
            if currentHigth - i > 0:
                currentRow = self.gameD[currentHigth - i]
                if '@' in currentRow:
                    newRow = currentRow.replace('@','.')
                    if thisCommand == '>':
                        direction = 1
                    else:
                        direction = -1
                    for l in range(1,8):
                        if currentRow[l] == '@':
                            if currentRow[l + direction] in '@.':
                                pass
                            else:
                                possible = False
                                break
                    for l in range(len(currentRow)):
                        if currentRow[l] == '@':
                            newRow = self.swapString(newRow, l + direction, '@')
                    if possible:
                        boardD[currentHigth - i] = newRow 
                    else:
                        break          
        if possible:
            self.gameD = boardD
            

    def swapString(self, s :str, index :int, newstring :str) -> str: 
        s = s[:index] + newstring + s[index + 1:]
        return s

    def fallDownOneStep(self):
        currentHight = self.gameDHight
        boardD = self.gameD.copy()
            #scan gameBoard and see if a move is possible
        cont = True
        #fall until no longer possible
        currentFall = boardD.copy()
        start = self.gameDHight - 5
        if start < 0:
            start = 0
        for row in range(start, currentHight):
            if '@' in boardD[row]:
                # if row == 0:
                #     cont = False #we are done
                #     break              
                currentRow = boardD[row]
                rowBelow = boardD[row - 1]
                for indexC in range(8):
                    char = currentRow[indexC + 1]
                    charBelow = rowBelow[indexC + 1]
                    if char in '.@':
                        if charBelow in '.@':
                            rowBelow = self.swapString(rowBelow, indexC + 1, char)
                            currentRow = self.swapString(currentRow, indexC + 1, '.')
                        elif char == '.':
                            pass
                        else:
                            #we are done
                            cont = False
                            break
                currentFall[row] = currentRow
                currentFall[row -1] = rowBelow
        if cont == True:
            boardD = currentFall
            self.gameDHight -= 1
        else: # Falling complete swap out
            for row in range(currentHight):
                boardD[row] = boardD[row].replace('@', '#')
        self.gameD = boardD
        return cont

    def checkHight(self):
        length = len(self.gameD)
        for l in range(length - 1, 0, -1):
            row = self.gameD[l]
            if '#' in row:
                self.gameDHight = l + 1
                break

def problem_a(input_string :str, expected_result :int):
    """Problem A solved function
    """
    solution :int = 0
    gameObject = game(input_string)

    for l in range(2022):
        gameObject.addNextSprite()
        cont = True

        while (cont):
            gameObject.moveAccordingToCommand()
            cont = gameObject.fallDownOneStep()

        gameObject.checkHight()

    solution = gameObject.gameDHight - 1
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 3153)
print("\n")

def problem_b(input_string :str, expected_result):
    """Problem A solved function
    """
    solution :int = 0
    totalTime = 1000000000000
    gameObject = game(input_string)
    initial = 45
    repetition = 35
    times = (totalTime - initial) // repetition
    leftOvers = (totalTime - initial)% repetition

    print('Length of input:', len(input_string))
    for l in range(initial):
        gameObject.addNextSprite()
        cont = True
        while (cont):
            gameObject.moveAccordingToCommand()
            cont = gameObject.fallDownOneStep()
        gameObject.checkHight()
    hight = gameObject.gameDHight

    if (gameObject.currentShape % 5 == 0):
        print('command pos', gameObject.currentCommandPos % 40, 'H:', hight, 'No. sprites', gameObject.currentShape)
    for l in range(repetition):
            gameObject.addNextSprite()
            cont = True
            while (cont):
                gameObject.moveAccordingToCommand()
                cont = gameObject.fallDownOneStep()
            gameObject.checkHight()

    diffBetweenRepetition = gameObject.gameDHight - hight
    print('command pos', gameObject.currentCommandPos % 40, "H:", gameObject.gameDHight, 'Diff:', diffBetweenRepetition, 'No. sprites', gameObject.currentShape, 'Times: ')
    hight = gameObject.gameDHight

    for k in range(times):
        for l in range(repetition):
            gameObject.addNextSprite()
            cont = True
            while (cont):
                gameObject.moveAccordingToCommand()
                cont = gameObject.fallDownOneStep()
            gameObject.checkHight()

        diff = gameObject.gameDHight - hight
        print('command pos', gameObject.currentCommandPos % 40, "H:", gameObject.gameDHight, 'Diff:', diff, 'No. sprites', gameObject.currentShape, 'Times: ', k)
        hight = gameObject.gameDHight

    for l in range(leftOvers):
        gameObject.addNextSprite()
        cont = True
        while (cont):
            gameObject.moveAccordingToCommand()
            cont = gameObject.fallDownOneStep()
        gameObject.checkHight()

    #diff = gameObject.gameDHight - hight
    #print('command pos', gameObject.currentCommandPos % 40, "H:", gameObject.gameDHight, 'Diff:', diff, 'No. sprites', gameObject.currentShape, 'Times: ', k)
    hight = gameObject.gameDHight

    totalTime = initial + leftOvers + (times)*repetition 
    solution = hight - 1 + (times-1) * diffBetweenRepetition
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)


problem_b(EXAMPLE_INPUT1, 1514285714288)
problem_b(PROGBLEM_INPUT_TXT, 0)
print("\n")