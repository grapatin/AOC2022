"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path
import re
import itertools as it

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day20/input.txt").read_text()

EXAMPLE_INPUT1 = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""
EXAMPLE_RESULT1 = 33

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    #a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

class robotFactoryBluePrint:
    def __init__(self, string :str):
        self.bluePrintD = {}
        for row in string.splitlines():
            numbersInString = re.findall('[0-9]+', row)
            self.bluePrintD[int(numbersInString[0])] = numbersInString[1:]

    def getMaximumOreNeeded(self, bluePrintId):
        return int(max(self.bluePrintD[bluePrintId][0], self.bluePrintD[bluePrintId][1], self.bluePrintD[bluePrintId][2], self.bluePrintD[bluePrintId][4]))

    def getOreCost(self, bluePrintId :int) -> int:
        return int(self.bluePrintD[bluePrintId][0])

    def getClayCost(self, bluePrintId :int) -> int:
        return int(self.bluePrintD[bluePrintId][1])

    def getObsidianCost(self, bluePrintId :int):
        return int(self.bluePrintD[bluePrintId][2]), int(self.bluePrintD[bluePrintId][3])

    def getGeodeCost(self, bluePrintId :int):
        return int(self.bluePrintD[bluePrintId][4]), int(self.bluePrintD[bluePrintId][5])
    

class optimizeProduction:
    def __init__(self, bluePrintID :int, bluePrintClass :robotFactoryBluePrint):
        self.bluePrintC = bluePrintClass
        self.bluePrintId = bluePrintID
        self.numberOfOreRobots = 1
        self.numberOfClayRobots = 0
        self.numberOfObsidianRobots = 0
        self.numberOfGeodeRobots = 0
        self.numberOfOre = 0
        self.numberOfClay = 0
        self.numberOfObsidian = 0
        self.numberOfGeode = 0
        self.time = 0
        self.maxGeodes = 0
        self.decisionA = [True, False]
        self.robotT = ['ore', 'clay', 'obsidian', 'geode']
        #self.robotT.reverse()
        self.permutations = list(it.permutations(self.robotT))
        self.cacheD = {}
        self.target = 23
        self.MaxOreNeeded = bluePrintClass.getMaximumOreNeeded(bluePrintID)

    def build(self, numberOfOreRobots, numberOfClayRobots, numberOfObsidianRobots, numberOfGeodeRobots):
        return numberOfOreRobots, numberOfClayRobots, numberOfObsidianRobots, numberOfGeodeRobots

    def worker(self, numberOfOreRobots, numberOfClayRobots, numberOfObsidianRobots, numberOfGeodeRobots, numberOfOre, numberOfClay, numberOfObsidian, numberOfGeode, time, targetMetall, pathIn, cacheInput):
        #first build with what we got
        pathS :str =  'nAction'
        if time < 24:
            permutations = self.permutations
            if targetMetall != '':
                permutations = [targetMetall]
            for alternative in permutations:
                if targetMetall != '':
                    alternative = [targetMetall]
                newNoOreConsumed = newNoClayConsumed = newNoObsidianConsumed = 0
                newOreRobot = 0
                newClayRobots = 0
                newObsidianRobots = 0
                newGeodeRoboots = 0
                for metal in alternative:
                    match metal:
                        case 'ore':
                            if numberOfOreRobots < self.MaxOreNeeded:
                                pathS = 'ore '
                                if numberOfOre - newNoOreConsumed >= self.bluePrintC.getOreCost(self.bluePrintId):
                                    newNoOreConsumed +=  self.bluePrintC.getOreCost(self.bluePrintId)
                                    newOreRobot = 1
                                    targetMetall = ''
                                else:
                                    targetMetall = metal
                            else:
                                targetMetall = ''
                        case 'clay':
                            pathS = 'c '
                            if numberOfOre - newNoOreConsumed >= self.bluePrintC.getClayCost(self.bluePrintId):
                                newNoOreConsumed += self.bluePrintC.getClayCost(self.bluePrintId)
                                newClayRobots = 1
                                targetMetall = ''
                            else:
                                targetMetall = metal
                        case 'obsidian':
                            pathS = 'ob '
                            if numberOfOre - newNoOreConsumed >= self.bluePrintC.getObsidianCost(self.bluePrintId)[0] and numberOfClay - newNoClayConsumed > self.bluePrintC.getObsidianCost(self.bluePrintId)[1]:
                                newNoOreConsumed +=self.bluePrintC.getObsidianCost(self.bluePrintId)[0]
                                newNoClayConsumed +=self.bluePrintC.getObsidianCost(self.bluePrintId)[1]
                                newObsidianRobots = 1
                                targetMetall = ''
                            else:
                                if newClayRobots + numberOfClayRobots > 0:
                                    targetMetall = metal
                        case 'geode':
                            pathS = 'ge '
                            if numberOfOre - newNoOreConsumed >= self.bluePrintC.getGeodeCost(self.bluePrintId)[0] and numberOfObsidian - newNoObsidianConsumed >= self.bluePrintC.getGeodeCost(self.bluePrintId)[1]:
                                newNoOreConsumed +=self.bluePrintC.getGeodeCost(self.bluePrintId)[0]
                                newNoObsidianConsumed +=self.bluePrintC.getGeodeCost(self.bluePrintId)[1]
                                newGeodeRoboots = 1
                                targetMetall = ''
                            else:
                                if newObsidianRobots + numberOfObsidianRobots > 0:
                                    targetMetall = metal
                                    if time < self.target:
                                        print('Time', time)
                                        print(pathIn)
                                        self.target -= 1

                    NewNoOreProduced, NewNoClayProduced, NewNoObsidianProduced, NewNofGeodeProduced = self.build(numberOfOreRobots, numberOfClayRobots, numberOfObsidianRobots, numberOfGeodeRobots)
                    newPath = pathIn + pathS + str(time) + ' '
                    OreRobotsForNextStage = numberOfOreRobots + newOreRobot
                    ClayRobotsForNextStage = numberOfClayRobots + newClayRobots
                    ObsidianRobotsForNextStage = numberOfObsidianRobots + newObsidianRobots
                    GeodeRobotsForNextStage = numberOfGeodeRobots + newGeodeRoboots
                    OreForNS = numberOfOre + NewNoOreProduced -  newNoOreConsumed
                    ClayForNS = numberOfClay + NewNoClayProduced - newNoClayConsumed
                    ObsidianForNS = numberOfObsidian + NewNoObsidianProduced - newNoObsidianConsumed
                    GeodeForNS = numberOfGeode + NewNofGeodeProduced
                    cachStringAlt = str(OreRobotsForNextStage) + ',' + str(ClayRobotsForNextStage) + ',' + str(ObsidianRobotsForNextStage) + ',' + str(GeodeRobotsForNextStage) + ',' + str(OreForNS) + ',' + str(ClayForNS) + ',' + str(ObsidianForNS) + ',' + str(GeodeForNS) + ',' + str(time) + targetMetall
                    if cachStringAlt not in self.cacheD:
                        #print(newPath)
                        self.worker(OreRobotsForNextStage, ClayRobotsForNextStage, ObsidianRobotsForNextStage, GeodeRobotsForNextStage, OreForNS, ClayForNS, ObsidianForNS, GeodeForNS, time + 1, targetMetall, newPath, cachStringAlt)
                        #Add to cache
                        self.cacheD[cachStringAlt] = self.maxGeodes
        else:
            #print('we have reached the whole way', pathIn)
            if numberOfGeode > self.maxGeodes:
                self.maxGeodes = numberOfGeode
                print('whoho! produced:', numberOfGeode, 'For path:', pathIn, 'CahcheStr=', cacheInput)




def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    bluePrints = robotFactoryBluePrint(input_string)
    optimizer = optimizeProduction(2, bluePrints)

    optimizer.worker(1, 0, 0, 0, 0, 0, 0, 0, 0, '', 'Start:', '')   
    solution = optimizer.maxGeodes
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
#problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")

def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

#problem_b(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
#problem_b(PROGBLEM_INPUT_TXT, 0)
print("\n")
