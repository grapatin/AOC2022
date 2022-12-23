"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path
import numpy as np
import re

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day22/input.txt").read_text()

EXAMPLE_INPUT1 = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
"""
EXAMPLE_RESULT1 = 1514

class boardClass:
    def __init__(self, inputString :str):
        self.mapD = {}
        startPos = -1
        inputString, self.movingCommand = inputString.split('\n\n')

        maxRowLength = 0
        for row in inputString.splitlines():
            if len(row) > maxRowLength:
                maxRowLength = len(row)

        rowId = 0
        for row in inputString.splitlines():
            for charPos in range(len(row)):
                self.mapD[self.fixIt(charPos, rowId)] = row[charPos]
                if rowId == 0 and row[charPos] == '.' and startPos == -1:
                    startPos = charPos
            charPos += 1
            for i in range(charPos, maxRowLength):
                self.mapD[self.fixIt(i, rowId)] = ' '
            rowId += 1
        self.maxY = rowId
        self.maxX = maxRowLength
        self.maxA = np.array([self.maxX, self.maxY])
        self.possibleDirections = {}
        self.possibleDirections[0] = np.array([1,0]) # 'R'
        self.possibleDirections[1] = np.array([0,1]) # 'D'
        self.possibleDirections[2] = np.array([-1,0]) # 'L'
        self.possibleDirections[3] = np.array([0,-1]) # 'U'
        self.facingDirection = 0
        self.commandPos = 0

        self.steps = re.findall('[0-9]+',self.movingCommand)
        self.turns = re.findall('[RL]',self.movingCommand)

        self.currentPosition = np.array([startPos, 0])


    def processCommands(self):
        cont = True
        steps :int = 0
        while cont:          
            noSteps = self.steps[self.commandPos]
            steps = int(noSteps)
            for _ in range(steps):
                previousPos = self.currentPosition
                nextPos = self.currentPosition + self.possibleDirections[self.facingDirection]
                nextPos = nextPos % self.maxA #keep us within bound
                nextSym = self.mapD[self.fixNP(nextPos)] #means warp
                if nextSym == '#':
                    break
                elif nextSym == '.':
                    self.currentPosition = nextPos
                elif nextSym == ' ':
                    #are we out of bounds
                    #lets move inbound
                    while (nextSym == ' '):
                        nextPos = nextPos+ self.possibleDirections[self.facingDirection]
                        nextPos = nextPos % self.maxA
                        nextSym = self.mapD[self.fixNP(nextPos)] #means wrap
                    if nextSym == '#':
                        nextPos = previousPos # we hit a wall revert back to last real position
                    self.currentPosition = nextPos
            if self.commandPos < len(self.turns):
                match self.turns[self.commandPos]:
                    case 'R':
                        self.facingDirection += 1
                    case 'L':
                        self.facingDirection += 3
                self.facingDirection = self.facingDirection % 4
                self.commandPos += 1
            else:
                cont = False

    
    def fixIt(self, x :int,y :int) -> str:
        return str(x) + ',' + str(y)

    def fixNP(self, pos :np.array):
        return str(pos[0])+','+str(pos[1])

class boardClassPart2:
    def __init__(self, inputString :str):
        self.mapD = {}
        startPos = -1
        inputString, self.movingCommand = inputString.split('\n\n')

        maxRowLength = 0
        for row in inputString.splitlines():
            if len(row) > maxRowLength:
                maxRowLength = len(row)

        rowId = 0
        for row in inputString.splitlines():
            for charPos in range(len(row)):
                self.mapD[self.fixIt(charPos, rowId)] = row[charPos]
                if rowId == 0 and row[charPos] == '.' and startPos == -1:
                    startPos = charPos
            charPos += 1
            for i in range(charPos, maxRowLength):
                self.mapD[self.fixIt(i, rowId)] = ' '
            rowId += 1
        self.maxY = rowId
        self.maxX = maxRowLength
        self.maxA = np.array([self.maxX, self.maxY])
        self.possibleDirections = {}
        self.possibleDirections[0] = np.array([1,0]) # 'R'
        self.possibleDirections[1] = np.array([0,1]) # 'D'
        self.possibleDirections[2] = np.array([-1,0]) # 'L'
        self.possibleDirections[3] = np.array([0,-1]) # 'U'
        self.facingDirection = 0
        self.commandPos = 0

        self.steps = re.findall('[0-9]+',self.movingCommand)
        self.turns = re.findall('[RL]',self.movingCommand)

        self.currentPosition = np.array([startPos, 0])

        #Sample solution 
        size = 4

        startX = 2 * size
        startY = 0
        array1 = self.createCubeSide(size, startX, startY)

        startX = 0
        startY = size
        array2 = self.createCubeSide(size, startX, startY)

        startX = size
        startY = size
        array3 = self.createCubeSide(size, startX, startY)

        startX = 2 * size
        startY = size
        array4 = self.createCubeSide(size, startX, startY)

        startX = 2 * size
        startY = 2 * size
        array5 = self.createCubeSide(size, startX, startY)

        startX = 3 * size
        startY = 2 * size
        array6 = self.createCubeSide(size, startX, startY)

        # '' array
        startX = 0
        startY = 0
        arrayEmpty = self.createCubeSide(size, startX, startY)

        arrayA = np.array(array1)
        arrayB = np.array(array4)
        arrayC = np.array(array5)
        arrayD = np.rot90(np.array(array2), 2) #180 degrees
        arrayE = np.rot90(np.array(array6), 2) #180 degrees
        arrayF = np.rot90(np.array(array3), 1) # rotate 90

        #Create a new matrix based on above
        arrayRow1 = np.concatenate((arrayEmpty, arrayD, arrayEmpty), axis=1)
        arrayRow2 = np.concatenate((arrayF, arrayA, arrayE), axis=1)
        arrayRow3 = np.concatenate((arrayEmpty, arrayB, arrayEmpty), axis=1)
        arrayCompleteA = np.concatenate((arrayRow1, arrayRow2, arrayRow3), axis = 0)

        arrayRow1 = np.concatenate((arrayEmpty, arrayA, arrayEmpty), axis=1)
        arrayRow2 = np.concatenate((np.rot90(arrayF, -1), arrayB, np.rot90(arrayE, 1)), axis=1)
        arrayRow3 = np.concatenate((arrayEmpty, arrayC, arrayEmpty), axis=1)
        arrayCompleteB = np.concatenate((arrayRow1, arrayRow2, arrayRow3), axis = 0)

        arrayRow1 = np.concatenate((arrayEmpty, arrayB, arrayEmpty), axis=1)
        arrayRow2 = np.concatenate((np.rot90(arrayF, -2), arrayC, np.rot90(arrayE, 2)), axis=1)
        arrayRow3 = np.concatenate((arrayEmpty, arrayD, arrayEmpty), axis=1)
        arrayCompleteC = np.concatenate((arrayRow1, arrayRow2, arrayRow3), axis = 0)

        arrayRow1 = np.concatenate((arrayEmpty, arrayC, arrayEmpty), axis=1)
        arrayRow2 = np.concatenate((np.rot90(arrayF, -3), arrayD, np.rot90(arrayE, 3)), axis=1)
        arrayRow3 = np.concatenate((arrayEmpty, arrayA, arrayEmpty), axis=1)
        arrayCompleteD = np.concatenate((arrayRow1, arrayRow2, arrayRow3), axis = 0)
    
        arrayRow1 = np.concatenate((arrayEmpty, np.rot90(arrayD, 1), arrayEmpty), axis=1)
        arrayRow3 = np.concatenate((arrayA, arrayE, np.rot90(arrayC, 2)), axis=1)
        arrayRow4 = np.concatenate((arrayEmpty, np.rot90(arrayB, -1), arrayEmpty), axis=1)
        arrayCompleteE = np.concatenate((arrayRow1, arrayRow2, arrayRow3, arrayRow4), axis = 0)
    
        arrayRow1 = np.concatenate((arrayEmpty, np.rot90(arrayD, -1), arrayEmpty), axis=1)
        arrayRow3 = np.concatenate((np.rot90(arrayC, 2), arrayF, arrayA), axis=1)
        arrayRow4 = np.concatenate((arrayEmpty, np.rot90(arrayB, 1), arrayEmpty), axis=1)
        arrayCompleteF = np.concatenate((arrayRow1, arrayRow2, arrayRow3, arrayRow4), axis = 0)


    def createCubeSide(self, size :int, startX :int, startY :int) -> list[list]:
        array = []
        temp = []
        for y in range(size):
            for x in range(size):
                temp.append(self.mapD[self.fixIt(startX + x, startY + y)])
            array.append(temp)
            temp = []

        return array
    


    def fallingOff(self, nextPos, previousPos):
        #are we out of bounds
        #lets move inbound
        x = nextPos[0]
        y = nextPos[1]
        boxXforNext = x // (self.maxX // 3)
        boxYforNext = y // (self.maxY // 4)

        x = previousPos[0]
        y = previousPos[1]
        boxXforPrevious = x // (self.maxX // 3)
        boxYforPrevious = y // (self.maxY // 4)

    def processCommands(self):
        cont = True
        steps :int = 0
        while cont:          
            noSteps = self.steps[self.commandPos]
            steps = int(noSteps)
            for _ in range(steps):
                previousPos = self.currentPosition
                nextPos = self.currentPosition + self.possibleDirections[self.facingDirection]
                nextPos = nextPos % self.maxA #keep us within bound
                nextSym = self.mapD[self.fixNP(nextPos)] #means warp
                if nextSym == '#':
                    break
                elif nextSym == '.':
                    self.currentPosition = nextPos
                elif nextSym == ' ':
                    self.fallingOff(nextPos, previousPos)
            if self.commandPos < len(self.turns):
                match self.turns[self.commandPos]:
                    case 'R':
                        self.facingDirection += 1
                    case 'L':
                        self.facingDirection += 3
                self.facingDirection = self.facingDirection % 4
                self.commandPos += 1
            else:
                cont = False

    
    def fixIt(self, x :int,y :int) -> str:
        return str(x) + ',' + str(y)

    def fixNP(self, pos :np.array):
        return str(pos[0])+','+str(pos[1])

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    board = boardClass(input_string)
    board.processCommands()

    solution = (board.currentPosition[1]+1)*1000 + (board.currentPosition[0]+1)*4+board.facingDirection
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")

def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    board = boardClassPart2(input_string)
    board.processCommands()

    solution = (board.currentPosition[1]+1)*1000 + (board.currentPosition[0]+1)*4+board.facingDirection

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b(EXAMPLE_INPUT1, 5031)
problem_b(PROGBLEM_INPUT_TXT, 0)
print("\n")