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
EXAMPLE_RESULT1 = 6032

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

        #SampleSolution
        self.cubeSize = 4


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

    def outOfBounds(self, previousPos, nextPos):
        #Find out which side of cube we are on
        #Find out what is the hext side?
        #rotate acordingly and set new x and y
        size = 4 #example part 2
        checkMe = []
        moveFrom = moveTo = 0
        oneX = [2*size, 3*size]
        oneY = [0, size]
        checkMe.append(oneX + oneY)
        twoX = [0, size]
        twoY = [size, 2*size]
        checkMe.append(twoX + twoY)
        threeX = [size, 2*size]
        threeY = [size, 2*size]
        checkMe.append(threeX + threeY)
        fourX = [2*size, 3*size]        
        fourY = [size, 2*size]
        checkMe.append(fourX + fourY)
        fiveX = [2*size, 3*size]
        fiveY = [2*size, 3*size]
        checkMe.append(fiveX + fiveY)
        sixX  = [3*size, 4*size]
        sixY  = [2*size, 3*size]
        checkMe.append(sixX + sixY)

        _7X = [0, size]
        _7Y = [0, size]
        checkMe.append(_7X + _7Y)

        _8X = [size, 2*size]
        _8Y = [0, size]
        checkMe.append(_8X + _8Y)

        _9X = [3*size, 4*size]
        _9Y = [0, size]
        checkMe.append(_9X + _9Y)

        _10X = [3*size, 4*size]
        _10Y = [size, 2*size]
        checkMe.append(_10X + _10Y)

        _11X = [0, size]
        _11Y = [2*size, 3*size]
        checkMe.append(_11X + _11Y)

        _12X = [size, 2*size]
        _12Y = [2*size, 3*size]
        checkMe.append(_12X + _12Y)

        for i in range(6):
            if checkMe[i][0] <= previousPos[0] < checkMe[i][1] and checkMe[i][2] <= previousPos[1] < checkMe[i][3]:
                moveFrom = i + 1
                break
        
        for i in range(6, 12):
            if checkMe[i][0] <= nextPos[0] < checkMe[i][1] and checkMe[i][2] <= nextPos[1] < checkMe[i][3]:
                moveTo = i + 1
                break
        print('We are moving from:', moveFrom, '->', moveTo)
        deltaXFrom = checkMe[moveFrom - 1][]
        match moveFrom:
            case 2:
                match moveTo:
                    case 10:
                        #move to 6 top moving down 
                        #y becomes x
                        nextPos = []


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
                    self.outOfBounds(previousPos, nextPos)
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
problem_a(PROGBLEM_INPUT_TXT, 1484)
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