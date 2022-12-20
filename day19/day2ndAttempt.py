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
    +"day19/input.txt").read_text()

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
        self.maxGeodes = 0
        self.allMetals = ['ore', 'clay', 'obsidian', 'geode']
        #self.allMetals.reverse()
        self.cacheD = {}
        self.MaxOreNeeded = bluePrintClass.getMaximumOreNeeded(bluePrintID)

    

    def worker(self, numberOfOreRobots, numberOfClayRobots, numberOfObsidianRobots, numberOfGeodeRobots, \
         numberOfOre, numberOfClay, numberOfObsidian, numberOfGeode, time, targetMetall, cacheInput):
        #first build with what we got
        TurnsLeft = 24 - time
        if time < 24:
            if targetMetall != 'noTargetMetal':
                allMetals = [targetMetall]
            else:
                allMetals = self.allMetals
            for metal in allMetals:
                OreConsumed = ClayConsumed = ObsidianConsumed = 0
                newOreRobot = newClayRobots = newObsidianRobots = newGeodeRoboots = 0
                match metal:
                    case 'ore':
                        if numberOfOreRobots < self.MaxOreNeeded:
                            if numberOfOre >= self.bluePrintC.getOreCost(self.bluePrintId):
                                OreConsumed +=  self.bluePrintC.getOreCost(self.bluePrintId)
                                newOreRobot = 1
                                targetMetall = 'noTargetMetal'
                            else:
                                targetMetall = metal
                        else:
                            continue
                    case 'clay':
                        if numberOfOre >= self.bluePrintC.getClayCost(self.bluePrintId):
                            OreConsumed += self.bluePrintC.getClayCost(self.bluePrintId)
                            newClayRobots = 1
                            targetMetall = 'noTargetMetal'
                        else:
                            if numberOfOreRobots > 0 and (numberOfOreRobots * TurnsLeft + numberOfOre) >= self.bluePrintC.getClayCost(self.bluePrintId):
                                targetMetall = metal
                            else:
                                continue
                    case 'obsidian':
                        if numberOfOre >= self.bluePrintC.getObsidianCost(self.bluePrintId)[0] and numberOfClay >= self.bluePrintC.getObsidianCost(self.bluePrintId)[1]:
                            OreConsumed +=self.bluePrintC.getObsidianCost(self.bluePrintId)[0]
                            ClayConsumed +=self.bluePrintC.getObsidianCost(self.bluePrintId)[1]
                            newObsidianRobots = 1
                            targetMetall = 'noTargetMetal'
                        else:
                            if numberOfClayRobots > 0 and (numberOfClayRobots * TurnsLeft + numberOfClay) >= self.bluePrintC.getObsidianCost(self.bluePrintId)[1]:
                                targetMetall = metal
                            else:
                                continue
                    case 'geode':
                        if numberOfOre >= self.bluePrintC.getGeodeCost(self.bluePrintId)[0] and numberOfObsidian >= self.bluePrintC.getGeodeCost(self.bluePrintId)[1]:
                            OreConsumed +=self.bluePrintC.getGeodeCost(self.bluePrintId)[0]
                            ObsidianConsumed +=self.bluePrintC.getGeodeCost(self.bluePrintId)[1]
                            newGeodeRoboots = 1
                            targetMetall = 'noTargetMetal'
                        else:
                            if numberOfObsidianRobots > 0 and (numberOfObsidianRobots * TurnsLeft + numberOfObsidian) >= self.bluePrintC.getGeodeCost(self.bluePrintId)[1]:
                                targetMetall = metal
                            else:
                                continue
                #produce and consume metals robot temporarly
                OreForNS = numberOfOre + numberOfOreRobots -  OreConsumed
                ClayForNS = numberOfClay + numberOfClayRobots - ClayConsumed
                ObsidianForNS = numberOfObsidian + numberOfObsidianRobots - ObsidianConsumed
                GeodeForNS = numberOfGeode + numberOfGeodeRobots
                #update number of robots temporarly
                OreRobotsForNS = numberOfOreRobots + newOreRobot
                ClayRobotsForNS = numberOfClayRobots + newClayRobots
                ObsidianRobotsForNS = numberOfObsidianRobots + newObsidianRobots
                GeodeRobotsForNS = numberOfGeodeRobots + newGeodeRoboots

                cachString = str(OreRobotsForNS) + ',' + str(ClayRobotsForNS) + ',' + \
                    str(ObsidianRobotsForNS) + ',' + str(GeodeRobotsForNS) + ',' + str(OreForNS) + \
                        ',' + str(ClayForNS) + ',' + str(ObsidianForNS) + ',' + str(GeodeForNS) + ',' + str(time) + targetMetall
                if cachString not in self.cacheD:
                    self.worker(OreRobotsForNS, ClayRobotsForNS, ObsidianRobotsForNS, GeodeRobotsForNS,\
                         OreForNS, ClayForNS, ObsidianForNS, GeodeForNS, time + 1, targetMetall, cachString)
                    #Add to cache
                    self.cacheD[cachString] = self.maxGeodes
        else:
            #print('we have reached the whole way', pathIn)
            if numberOfGeode > self.maxGeodes:
                self.maxGeodes = numberOfGeode
                print('whoho! produced:', numberOfGeode, 'CahcheStr=', cacheInput, 'with BluePrint:', self.bluePrintId)

def problem_a(input_string :str, expected_result):
    """Problem A solved function
    """
    solution = 0
    bluePrints = robotFactoryBluePrint(input_string)
    rows = input_string.splitlines()

    for i in range(len(rows)):
        optimizer = optimizeProduction(i + 1, bluePrints)
        optimizer.worker(1, 0, 0, 0, 0, 0, 0, 0, 0, 'noTargetMetal', '')   
        bPrintG = optimizer.maxGeodes
        solution += bPrintG * (i + 1)
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 0)  # 1097 too low
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
