"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path
import re
import time

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day15/input.txt").read_text()

EXAMPLE_INPUT1 = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
EXAMPLE_RESULT1 = 26

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    #a_steps = [int(number) for number in input_string.split(',')]
    return a_steps


def problem_a(input_string, expected_result, target):
    """Problem A solved function
    """
    solution = 0
    rows = string_worker(input_string)
    storageD = {}
    StoreBeaconsOnTarget = {}

    for row in rows:
        numbersInRow = re.findall('[-0-9]+', row)
        xS = int(numbersInRow[0])
        yS = int(numbersInRow[1])
        xB = int(numbersInRow[2])
        yB = int(numbersInRow[3])
        if yB == target:
            StoreBeaconsOnTarget[str('xB')+','+str('xY')] = True

        manhattanDistanceX = abs(xS - xB)
        manhattanDistanceY = abs(yS - yB)
        manhattanDistanceTotal = manhattanDistanceX + manhattanDistanceY

        distanceY = target - yS

        if abs(distanceY) <= manhattanDistanceTotal:
            #This will affect the scoore
            howMuch = manhattanDistanceTotal - abs(distanceY)
            for i in range(howMuch+1):
                storageD[xS + i] = '#'
                storageD[xS - i] = '#'
    solution = len(storageD) - len(StoreBeaconsOnTarget)
    
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1, 10)
problem_a(PROGBLEM_INPUT_TXT, 0, 2000000)
print("\n")

def find_over_lapp_cords(new_low, new_high, current_low, current_high):
        #find X overlapp
        if new_low > current_high or new_high < current_low:
            #no overlapp
            return False, 0, 0
        else:
            #we have a overlapp
            if new_low >= current_low:
                overlapp_low = new_low
            else:
                overlapp_low = current_low
            if new_high <= current_high:
                overlapp_high = new_high
            else:
                overlapp_high = current_high
            return True, overlapp_low, overlapp_high

def problem_b(input_string, expected_result, target):
    """Problem A solved function
    """
    solution = 0
    storageD = {}
    rows = string_worker(input_string)

    maxV = target*2
    for i in range(maxV + 1):
        storageD[i] = [0, maxV]

    for row in rows:
        numbersInRow = re.findall('[-0-9]+', row)
        xS = int(numbersInRow[0])
        yS = int(numbersInRow[1])
        xB = int(numbersInRow[2])
        yB = int(numbersInRow[3])

        manhattanDistanceX = abs(xS - xB)
        manhattanDistanceY = abs(yS - yB)
        manhattanDistanceTotal = manhattanDistanceX + manhattanDistanceY

        yMin = yS - manhattanDistanceTotal
        yMax = yS + manhattanDistanceTotal

        if yMin < 0:
            yMin = 0
        if yMax > maxV:
            yMax = maxV

        for rowID in range(yMin, yMax + 1):
            distanceY = rowID - yS

            #review and update valid spaces
            howMuch = manhattanDistanceTotal - abs(distanceY)
            lowPoint = xS - howMuch
            highPoint = xS + howMuch
            noSensorArray = storageD[rowID]
            length = len(noSensorArray)
            newSensorArray = []
            for idx in range(length // 2):
                currentLowPoint = noSensorArray[2 * idx]
                currentHighPoint = noSensorArray[(2 * idx) + 1]
                # 0 till 20, -4 till 5  blir 5 - 20
                if lowPoint <= currentLowPoint:
                    if highPoint <= currentLowPoint:
                        if lowPoint == currentLowPoint:
                            newSensorArray.append(currentLowPoint + 1)
                            newSensorArray.append(currentHighPoint)
                        else:
                            newSensorArray.append(currentLowPoint)
                            newSensorArray.append(currentHighPoint)
                    elif highPoint <= currentHighPoint:
                        #we have a partial overlap lower part
                        currentLowPoint = highPoint + 1
                        newSensorArray.append(currentLowPoint)
                        newSensorArray.append(currentHighPoint)
                    else:
                        pass
                        # full overlapp 
                elif lowPoint <= currentHighPoint:
                        #we have an overlap 
                        if highPoint < currentHighPoint:
                            #Internal overlap, need split into 2 arrays
                            newSensorArray.append(currentLowPoint)
                            newSensorArray.append(lowPoint-1)
                            newSensorArray.append(highPoint+1)
                            newSensorArray.append(currentHighPoint)       
                        else:
                            #we have a partial overlap higher part
                            currentHighPoint = lowPoint - 1
                            newSensorArray.append(currentLowPoint)
                            newSensorArray.append(currentHighPoint)
                            #keep currenntHighPoint
                elif lowPoint > currentHighPoint:
                    #outside no change
                    newSensorArray.append(currentLowPoint)
                    newSensorArray.append(currentHighPoint)
            storageD[rowID] = newSensorArray

    for key in storageD:
        if len(storageD[key]) > 0:
            solution = storageD[key][0]*4000000 + key
    solution = 0
    if solution == expected_result:
        print("Correct solution found b:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b(EXAMPLE_INPUT1, 56000011, 10)
start = time.process_time()
problem_b(PROGBLEM_INPUT_TXT, 0, 2000000)
print('Processing took:', time.process_time() - start, 'seconds')
print("\n")