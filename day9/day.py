"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path
import numpy as np

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day9/input.txt").read_text()

EXAMPLE_INPUT1 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
EXAMPLE_RESULT1 = 13

def mover(headPos, tailPos):
        diffX, diffY = np.array(headPos) - np.array(tailPos)

        if abs(diffX) < 2 and abs(diffY) < 2:
            return tailPos

        diffX = np.clip(diffX, -1, 1)
        diffY = np.clip(diffY, -1, 1)

        tailPos = np.array(tailPos) + np.array([diffX, diffY])

        return tailPos

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    #a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

def fixIt(l):
    return str(l[0]) + ',' + str(l[1])

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0
    storageD = {}
    headPos = [0,0]
    tailPos = [0,0]
    rows = string_worker(input_string)
    storageD[fixIt(tailPos)] = 'Visited'

    for row in rows:
        parts = row.split(' ')
        match parts[0]:
            case 'U':
                direction = (0,1)
            case 'D':
                direction = (0,-1)
            case 'R':
                direction = (1, 0)
            case 'L':
                direction = (-1, 0)
        distance = int(parts[1])

        for _ in range(distance):
            headPos[0] += direction[0]
            headPos[1] += direction[1]
            diffX = headPos[0] - tailPos[0]
            diffY = headPos[1] - tailPos[1]
            if diffX > 1:
                tailPos[0] += 1
                tailPos[1] = headPos[1]
            elif diffX < -1:
                tailPos[0] -= 1
                tailPos[1] = headPos[1]
            elif diffY > 1:
                tailPos[1] += 1
                tailPos[0] = headPos[0]
            elif diffY < -1:
                tailPos[1] -= 1
                tailPos[0] = headPos[0]
            storageD[fixIt(tailPos)] = 'Visited'
            #print(fixIt(tailPos))
    solution = len(storageD)

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 5619)
print("\n")
    

moveDiffMatrix = {}
moveDiffMatrix['U'] = [0,1]
moveDiffMatrix['D'] = [0,-1]
moveDiffMatrix['R'] = [1,0]
moveDiffMatrix['L'] = [-1,0]

def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0
    storageD = {}
    knotPos = []
    for _ in range(10):
        knotPos.append([0,0])
    rows = string_worker(input_string)
    storageD[fixIt(knotPos[9])] = 'Visited'

    for row in rows:
        directionStr, distanceStr = row.split(' ')
        direction = moveDiffMatrix[directionStr]       
        distance = int(distanceStr)
        for _ in range(distance):
            knotPos[0] = np.array(knotPos[0]) + np.array(direction)
            for i in range(9):
                knotPos[i+1] = mover(knotPos[i].copy(), knotPos[i+1].copy())
                
            storageD[fixIt(knotPos[9])] = 'Visited'
    solution = len(storageD)

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b("""R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""", 36)
problem_b(PROGBLEM_INPUT_TXT, 2376)
print("\n")