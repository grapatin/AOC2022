"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path
import numpy as np
import sys

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day24/input.txt").read_text()

EXAMPLE_INPUT1 = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""
EXAMPLE_RESULT1 = 18

class mapClass():
    def __init__(self, inputString):
        self.mapD = {}
        self.emptyMapD = {}
        self.mapCache = {}
        self.cacheD = {}
        x = y = 0
        for row in inputString.splitlines():
            for char in row:
                self.mapD[self.fixIt(x,y)] = char
                if char not in "#SF":
                    char = '.'
                self.emptyMapD[self.fixIt(x,y)] = char
                x += 1
            y += 1
            self.maxX = x
            x = 0
        self.maxY = y
        self.BestResult = 850

    def timeTickOnMap(self, inputMap):
        mapCopy = self.emptyMapD.copy()
        
        for key in inputMap:
            currentPos = inputMap[key]
            if currentPos in '.#':
                continue
            x,y = int(key.split(',')[0]), int(key.split(',')[1])
            for char in currentPos:
                match char:
                    case '.':
                        continue
                    case '<':
                        deltaPos = np.array([-1, 0])
                    case '>':
                        deltaPos = np.array([1, 0])
                    case 'v':
                        deltaPos = np.array([0, 1])
                    case '^':
                        deltaPos = np.array([0, -1])
                newPos = [x, y] + deltaPos
                newChar = mapCopy[self.fixIt(newPos[0], newPos[1])]
                if newChar == '#':
                    newPos = newPos + deltaPos
                    newPos = (newPos + deltaPos) 
                    newPos = newPos % np.array([self.maxX, self.maxY]) #trick to get back on other side..
                existingString = mapCopy[self.fixIt(newPos[0], newPos[1])]

                mapCopy[self.fixIt(newPos[0], newPos[1])] = existingString + char
        return mapCopy

    def fixIt(self, x, y):
        return str(x) + ',' + str(y)

    def mazeMover(self, currentPos, ticks, currentMapState, targetDestination, stayTime):
        if ticks not in self.mapCache:
            currentMapState = self.timeTickOnMap(currentMapState) #returns a copy!
            self.mapCache[ticks] = currentMapState
            print('Created cache for:', ticks)
        else:
            currentMapState = self.mapCache[ticks]
        ticks += 1
        if str(currentPos) + ',' + str(ticks) in self.cacheD:
            return #Already in cache

        if ticks >= self.BestResult:
            return #Abort, we know a better route

        #find alternatives, abort if no alternatives
        alternatives = ['S', 'W', 'N', 'E', 'STAY']
        possibleWays = []

        for alternative in alternatives:
            match alternative:
                case 'S':
                    deltaPos = np.array([0,1])
                case 'W':
                    deltaPos = np.array([-1,0])
                case 'N':
                    deltaPos = np.array([0,-1])
                case 'E':
                    deltaPos = np.array([1,0])
                case 'STAY':
                    if stayTime > 600:
                        continue #skip we stayed to long    
                    deltaPos = np.array([0,0])
                    
            newPos = currentPos + deltaPos
            newPos = newPos % np.array([self.maxX, self.maxY]) #trick to get back on other side..
            if newPos[0] == targetDestination[0] and newPos[1] == targetDestination[1]:
                #we are done
                if ticks < self.BestResult:
                    self.BestResult = ticks
                    print('New best found', ticks)
                return
            if currentMapState[self.fixIt(newPos[0], newPos[1])] == '.':
                possibleWays.append(alternative)
        #move accordingly, check if destination

        for alternative in possibleWays:
            match alternative:
                case 'S':
                    deltaPos = np.array([0,1])
                    stayTime = 0
                case 'W':
                    deltaPos = np.array([-1,0])
                    stayTime = 0
                case 'N':
                    deltaPos = np.array([0,-1])
                    stayTime = 0
                case 'E':
                    deltaPos = np.array([1,0])
                    stayTime = 0
                case 'STAY':
                    deltaPos = np.array([0,0])
                    stayTime += 1
            self.mazeMover(currentPos+deltaPos, ticks, currentMapState, targetDestination, stayTime)
        self.cacheD[str(currentPos) + ',' + str(ticks)] = 'visited'

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0
    map = mapClass(input_string)
    map.mazeMover([1,0], 0, map.mapD, [120,26], 0)

    solution = map.BestResult

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

sys.setrecursionlimit(15000)
#problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")

def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_b(PROGBLEM_INPUT_TXT, 253)
print("\n")