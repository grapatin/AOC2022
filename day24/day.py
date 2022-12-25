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
EXAMPLE_RESULT1 = 54

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
        self.BestResult = 300
        self.roadWalked = ''

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

    def createMapCache(self):
        currentMapState = self.mapD
        for ticks in range(0, 850):
            currentMapState = self.timeTickOnMap(currentMapState)
            self.mapCache[ticks] = currentMapState
            print('Created cache for:', ticks)

    def mazeMover(self, currentPos, ticks:int, targetDestination, stayTime :int, endPos, startPos, state :str, roadWalked):

        currentMapState = self.mapCache[ticks]
        ticks += 1
        if str(currentPos) + ',' + str(ticks)+state in self.cacheD:
            return #Already in cache

        if ticks >= self.BestResult:
            return #Abort, we know a better route

        #find alternatives, abort if no alternatives
        alternatives = ['S', 'W', 'N', 'E', 'STAY']

        for alternative in alternatives:
            match alternative:
                case 'S':
                    deltaPos = np.array([0,1])
                    roadWalkedNew = 'S'
                case 'W':
                    deltaPos = np.array([-1,0])
                    roadWalkedNew = 'W'
                case 'N':
                    deltaPos = np.array([0,-1])
                    roadWalkedNew = 'N'
                case 'E':
                    deltaPos = np.array([1,0])
                    roadWalkedNew = 'E'
                case 'STAY':
                    roadWalked += 'P'
                    if stayTime > 200:
                        continue #skip we stayed to long    
                    deltaPos = np.array([0,0])
                    
            newPos = currentPos + deltaPos
            newPos = newPos % np.array([self.maxX, self.maxY]) #trick to get back on other side..to hit a wall
            newTargetDestination = targetDestination
            newState = state
            if newPos[0] == targetDestination[0] and newPos[1] == targetDestination[1]:
                if state == 'first':
                    #lets turn back
                    newTargetDestination = startPos
                    newState = 'second'
                    #print('Turning back after', ticks)
                elif state == 'second':
                    newTargetDestination = endPos
                    newState = 'third'
                    #print('Turning back after again', ticks)
                else:
                    #we are done
                    if ticks < self.BestResult:
                        self.BestResult = ticks
                        self.roadWalked = roadWalked
                        print('New best found', ticks)
                        print('Road:', self.roadWalked)
                    return
            if currentMapState[self.fixIt(newPos[0], newPos[1])] == '.':
                self.mazeMover(newPos, ticks, newTargetDestination, stayTime, endPos, startPos, newState, roadWalked + roadWalkedNew)
        self.cacheD[str(currentPos) + ',' + str(ticks) + state] = 'visited'
        

def problem_a(input_string, expected_result, finish_pos):
    """Problem A solved function
    """
    solution = 0
    map = mapClass(input_string)
    map.createMapCache()
    map.BestResult = 850
    map.mazeMover([1,0], 0, finish_pos, 0, finish_pos, [1,0], "first", '')

    solution = map.BestResult

    f = open("output.log", "w")
    mazeStr :str = ''
    for i in range(solution):
        for y in range(map.maxY):
            for x in range(map.maxX):
               mazeStr += map.mapCache[i][map.fixIt(x,y)]
            mazeStr += '\n'
        mazeStr += '\n'
        
    f.write(mazeStr)
    f.close

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

sys.setrecursionlimit(15000)
#problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1, [6,5])
problem_a(PROGBLEM_INPUT_TXT, 0, [120,26])
print("\n")