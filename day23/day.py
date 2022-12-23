"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path
import numpy as np

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day23/input.txt").read_text()

EXAMPLE_INPUT1 = """..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
.............."""
EXAMPLE_RESULT1 = 110

class planting:
    def __init__(self, inputString :str):
        self.storageD = {}
        rowId = 0
        charId = 0
        for row in inputString.splitlines():
            for char in row:
                if char == '#':
                    self.storageD[self.fixIt(charId, rowId)] = char
                charId += 1
            charId = 0
            rowId += 1
        self.turn = 0
    
    def checkNort(self, pos):
        NW = np.array([-1, -1])
        N = np.array([0, -1])
        NE = np.array([1, -1])
        if self.getPos(pos + NW) == '.':
            if self.getPos(pos + N) == '.':
                if self.getPos(pos + NE) == '.':
                    return True
        return False

    def checkSouth(self, pos):
        NW = np.array([-1, 1])
        N = np.array([0, 1])
        NE = np.array([1, 1])
        if self.getPos(pos + NW) == '.':
            if self.getPos(pos + N) == '.':
                if self.getPos(pos + NE) == '.':
                    return True
        return False

    def checkWest(self, pos):
        NW = np.array([-1, -1])
        N = np.array([-1, 0])
        NE = np.array([-1, 1])
        if self.getPos(pos + NW) == '.':
            if self.getPos(pos + N) == '.':
                if self.getPos(pos + NE) == '.':
                    return True
        return False

    def checkEast(self, pos):
        NW = np.array([1, -1])
        N = np.array([1, 0])
        NE = np.array([1, 1])
        if self.getPos(pos + NW) == '.':
            if self.getPos(pos + N) == '.':
                if self.getPos(pos + NE) == '.':
                    return True
        return False

    def convertStrToArray(self, cord :str):
        x, y = cord.split(',')
        return [int(x),int(y)]

    def doRound(self):
        cont = True
        rounds = 0
        while cont:
            # print('Start of Round', rounds)
            # for y in range(12):
            #     for x in range(14):
            #         print(self.getPos([x,y]), end='')
            #     print('')
            suggestMove = {}
            for cord in self.storageD:
                if self.storageD[cord] == '#':
                    moveCount = 0
                    moveHereA = []
                    cordA = self.convertStrToArray(cord)
                    if rounds % 4 == 0:
                        if self.checkNort(cordA):
                            moveCount += 1
                            moveHereA = cordA + np.array([0,-1])
                        if self.checkSouth(cordA):
                            if moveCount == 0:
                                moveHereA = cordA + np.array([0,1])
                            moveCount += 1
                        if self.checkWest(cordA):
                            if moveCount == 0:
                                moveHereA = cordA + np.array([-1,0])
                            moveCount += 1
                        if self.checkEast(cordA):
                            if moveCount == 0:
                                moveHereA = cordA + np.array([1,0])
                            moveCount += 1
                    elif rounds % 4 == 1:
                        if self.checkSouth(cordA):
                            if moveCount == 0:
                                moveHereA = cordA + np.array([0,1])
                            moveCount += 1
                        if self.checkWest(cordA):
                            if moveCount == 0:
                                moveHereA = cordA + np.array([-1,0])
                            moveCount += 1
                        if self.checkEast(cordA):
                            if moveCount == 0:
                                moveHereA = cordA + np.array([1,0])
                            moveCount += 1
                        if self.checkNort(cordA):
                            if moveCount == 0:
                                moveHereA = cordA + np.array([0,-1])
                            moveCount += 1
                    elif rounds % 4 == 2:
                        if self.checkWest(cordA):
                            if moveCount == 0:
                                moveHereA = cordA + np.array([-1,0])
                            moveCount += 1
                        if self.checkEast(cordA):
                            if moveCount == 0:
                                moveHereA = cordA + np.array([1,0])
                            moveCount += 1
                        if self.checkNort(cordA):
                            if moveCount == 0:
                                moveHereA = cordA + np.array([0,-1])
                            moveCount += 1
                        if self.checkSouth(cordA):
                            if moveCount == 0:
                                moveHereA = cordA + np.array([0,1])
                            moveCount += 1
                    else:
                        if self.checkEast(cordA):
                            if moveCount == 0:
                                moveHereA = cordA + np.array([1,0])
                            moveCount += 1
                        if self.checkNort(cordA):
                            if moveCount == 0:
                                moveHereA = cordA + np.array([0,-1])
                            moveCount += 1
                        if self.checkSouth(cordA):
                            if moveCount == 0:
                                moveHereA = cordA + np.array([0,1])
                            moveCount += 1
                        if self.checkWest(cordA):
                            if moveCount == 0:
                                moveHereA = cordA + np.array([-1,0])
                            moveCount += 1
                    if moveCount == 4 or moveCount == 0: #Do not move
                        continue
                    moveHereS = str(moveHereA[0]) + ',' + str(moveHereA[1])
                    if moveHereS not in suggestMove:
                        suggestMove[moveHereS] = cord
                    else:
                        #we got a conflict
                        suggestMove[moveHereS] = 'crowded'
            #do the actual move
            for moveHereS in suggestMove:
                if suggestMove[moveHereS] != 'crowded': #this is something we should move
                    oldPos = suggestMove[moveHereS]
                    self.storageD.pop(oldPos, None)
                    self.storageD[moveHereS] = '#'
            if len(suggestMove) == 0:
                print('Solution Part 2:', rounds+1)
                break
            rounds += 1
            if rounds % 10 == 0:
                print('Round:', rounds, '# moves:',len(suggestMove))

    def getPos(self, pos):
        return self.storageD.get(str(pos[0])+ ',' + str(pos[1]), '.')

    def fixIt(self, x, y):
        return str(x) + ',' + str(y)

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0
    plant = planting(input_string)
    plant.doRound()

    minX = minY = 100000
    maxX = maxY = 0
    count = 0
    for pos in plant.storageD:
        if plant.storageD[pos] == '#':
            count += 1
            xP, yP = int(pos.split(',')[0]), int(pos.split(',')[1])
            if xP > maxX:
                maxX = xP
            if yP > maxY:
                maxY = yP
            if xP < minX:
                minX = xP
            if yP < minY:
                minY = yP

    square = (maxX - minX + 1)*(maxY - minY + 1)
    solution = square - count

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")

