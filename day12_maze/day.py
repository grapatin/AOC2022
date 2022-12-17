"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path
import sys

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day12_maze/input.txt").read_text()

EXAMPLE_INPUT1 = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
EXAMPLE_RESULT1 = 31

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    #a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

class posC():
    def __init__(self, char):
        self.shortestPath = 9999999999999
        if char == 'E':
            self.target = True
            self.hight = ord('z')
        elif char == 'S':
            self.target = False
            self.hight = ord('a')
        else:
            self.target = False
            self.hight = ord(char)

class mazeMove():
    def __init__(self, mazeString):
        self.directions = ['down','right', 'up', 'left']
        self.mazeD = {}
        rows = mazeString.split('\n')
        self.lengthR = len(rows)
        self.lengthC = len(rows[0])
        self.maxSteps = 422
        self.newBest = self.maxSteps
        self.bestArray = []
        for rowN in range(self.lengthR):
            for cN in range(self.lengthC):
                self.mazeD[self.fixIt(cN, rowN)] = posC(rows[rowN][cN])
                if rows[rowN][cN] == 'S':
                    self.startX = cN
                    self.startY = rowN
    
    def mover(self, currentX, currentY, direction, currentHight):
        match direction:
            case 'up':
                if currentY > 0:
                    currentY -= 1
            case 'down':
                if currentY < self.lengthR - 1:
                    currentY += 1
            case 'left':
                if currentX > 0:
                    currentX -= 1                    
            case 'right':
                if currentX < self.lengthC - 1:
                    currentX += 1
   
        newHight = self.mazeD[self.fixIt(currentX,currentY)].hight
        if newHight - currentHight < 2:
            return True, currentX, currentY
        else:
            return False, currentX, currentY
    
    def workerS(self, posX, posY, steps):
        currentHight = self.mazeD[self.fixIt(posX,posY)].hight
        #if currentHight == ord('r'):
        #    print('r found found after steps:', steps,'at pos', posX, posY)
        steps += 1
        if steps < self.newBest:
            for direction in self.directions:
                possible, newX, newY = self.mover(posX, posY, direction, currentHight)
                if possible == True:
                    object = self.mazeD[self.fixIt(newX, newY)]
                    if steps < object.shortestPath:
                        object.shortestPath = steps
                        if object.target == True:
                            self.newBest = steps
                            # print('Target found after this many steps:', steps)
                        else:
                            self.workerS(newX, newY, steps)
                    else:
                        pass #no need to continue

    def fixIt(self, x, y):
        return str(x)+ ',' + str(y)

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0
    maze = mazeMove(input_string)
    maze.workerS(maze.startX,maze.startY,0)
    solution = maze.newBest
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 420)
print("\n")

def getPossibleStartingPos(maze):
    possibleStart = []
    for key, value in maze.mazeD.items():
        if value.hight == ord('a'):
            possibleStart.append(key)
    return possibleStart


def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    solution = 999999
    maze = mazeMove(input_string)
    possibleStart = getPossibleStartingPos(maze)
    for start in possibleStart:
        values = start.split(',')
        maze.workerS(int(values[0]),int(values[1]),0)
        if maze.newBest < solution:
            solution = maze.newBest

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)


problem_b(EXAMPLE_INPUT1, 29)
problem_b(PROGBLEM_INPUT_TXT, 414)
print("\n")