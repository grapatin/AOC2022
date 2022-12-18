"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path
import re

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day18/input.txt").read_text()

EXAMPLE_INPUT1 = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""
EXAMPLE_RESULT1 = 64

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    #a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

class dropletsClass:
    def __init__(self, string_input):
        rows :str = string_worker(string_input)
        self.storageD = {}
        self.dropletD = {}
        self.gapsD = {}
        self.maxX = 0
        self.minX = 99999999
        self.maxY = 0
        self.minY = 99999999
        self.maxZ = 0
        self.minZ = 99999999
        for row in rows:
            cords = re.findall('[-0-9]+', row)
            int_cords = [int(cords[0]), int(cords[1]), int(cords[2]), "droplet"]
            self.maxX = max(int(cords[0]), self.maxX)
            self.maxY = max(int(cords[1]), self.maxY)
            self.maxZ = max(int(cords[2]), self.maxZ)
            self.minX = min(int(cords[0]), self.minX)
            self.minY = min(int(cords[1]), self.minY)
            self.minZ = min(int(cords[2]), self.minZ)

            self.storageD[row] = int_cords
    
    def countManhattanDistanceBetweenAll(self):
        counter = 0
        for point1 in self.storageD.values():
            for point2 in self.storageD.values():
                if point1 != point2:
                    distance = abs(point1[0]-point2[0]) + abs(point1[1]-point2[1]) + abs(point1[2]-point2[2])
                    if distance == 1:
                        counter += 1
        return counter

    def countManhattanDistanceBetweenAllUnknownAir(self):
        counter = 0
        for point1 in self.storageD.values():
            if point1[3] == 'unknownair':
                for point2 in self.storageD.values():
                    if point2[3] == 'unknownair':
                        if point1 != point2:
                            distance = abs(point1[0]-point2[0]) + abs(point1[1]-point2[1]) + abs(point1[2]-point2[2])
                            if distance == 1:
                                counter += 1
        return counter

    def countManhattanDistanceBetweenDropletandouterAir(self):
        counter = 0
        for point1 in self.storageD.values():
            if point1[3] == 'droplet':
                for point2 in self.storageD.values():
                    if point1 != point2:
                        if point2[3] == 'outerair':
                            distance = abs(point1[0]-point2[0]) + abs(point1[1]-point2[1]) + abs(point1[2]-point2[2])
                            if distance == 1:
                                counter += 1
        return counter

    def checkForOuterAir(self, point):
        x = point[0]
        y = point[1]
        z = point[2]
        adjentPoint = []
        adjentPoint.append( [x - 1, y, z])
        adjentPoint.append( [x + 1, y, z])
        adjentPoint.append( [x, y + 1, z])
        adjentPoint.append( [x, y - 1, z])
        adjentPoint.append( [x, y, z + 1])
        adjentPoint.append( [x, y, z - 1])

        for aPoint in adjentPoint:
            cordS = str(aPoint[0]) + ',' + str(aPoint[1]) + ',' + str(aPoint[2])
            pointN = self.storageD.get(cordS, [x, y, z, "unknownair"])
            if pointN[3] == "outerair":
                return "outerair"
        
        return "unknownair"


    def fillOuterWithAir(self):
        for x in [self.minX -1, self.maxX + 1]:
            for y in range(self.minY - 1, self.maxY + 1):
                for z in range(self.minZ - 1, self.maxZ + 1):
                    cordS = str(x) + ',' + str(y) + ',' + str(z)
                    self.storageD[cordS] = [x, y, z, "outerair"] #air
        for y in [self.minY - 1, self.maxY + 1]:
            for x in range(self.minX - 1, self.maxX + 1):
                for z in range(self.minZ - 1, self.maxZ + 1):
                    cordS = str(x) + ',' + str(y) + ',' + str(z)
                    self.storageD[cordS] = [x, y, z, "outerair"] #air

        for z in [self.minZ - 1, self.maxZ + 1]:
            for x in range(self.minX - 1, self.maxX + 1):
                for y in range(self.minY - 1, self.maxY + 1):
                    cordS = str(x) + ',' + str(y) + ',' + str(z)
                    self.storageD[cordS] = [x, y, z, "outerair"] #air        
        

    def scanTheWhole(self):
        for x in range(self.minX - 1, self.maxX + 1):
            for y in range(self.minY - 1, self.maxY + 1):
                for z in range(self.minZ - 1, self.maxZ + 1):
                    cordS = str(x) + ',' + str(y) + ',' + str(z)
                    point = self.storageD.get(cordS, [x, y, z, "unknownair"])
                    if point[3] == "unknownair":
                        point[3] = self.checkForOuterAir(point)
                    self.storageD[cordS] = point
    
    def getUknownAirCount(self):
        count = 0
        for x in range(self.minX, self.maxX + 1):
            for y in range(self.minY, self.maxY + 1):
                for z in range(self.minZ, self.maxZ + 1):
                    cordS = str(x) + ',' + str(y) + ',' + str(z)
                    if cordS not in self.storageD:
                        pass
                    else:
                        point = self.storageD.get(cordS, [x, y, z, "unknownair"])
                        if point[3] == "unknownair":
                            count += 1    
        return count

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    rows = string_worker(input_string)
    solution = len(rows)*6
    droplets = dropletsClass(input_string)

    overlaps = droplets.countManhattanDistanceBetweenAll()

    solution -= overlaps

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 3470
)
print("\n")

def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    rows = string_worker(input_string)
    solution = len(rows)*6
    droplets = dropletsClass(input_string)
    overlaps = droplets.countManhattanDistanceBetweenAll()

    droplets.fillOuterWithAir()
    droplets.scanTheWhole()
    internalAirCount = droplets.getUknownAirCount()
    internalAirCount2 = 0
    while (internalAirCount != internalAirCount2):
        internalAirCount2 = internalAirCount
        droplets.scanTheWhole()
        internalAirCount = droplets.getUknownAirCount()

    droplets.scanTheWhole()
    internalAirCount = droplets.getUknownAirCount()
    externalSurfaceForInteralAir = internalAirCount*6 - droplets.countManhattanDistanceBetweenAllUnknownAir()

    solution -= externalSurfaceForInteralAir
    solution -= overlaps

    print('Solution alternative 1:', solution)
    solution = droplets.countManhattanDistanceBetweenDropletandouterAir()
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b(EXAMPLE_INPUT1, 58)
problem_b(PROGBLEM_INPUT_TXT, 0)
print("\n")