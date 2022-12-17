"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path
import copy
import re


PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day16/input.txt").read_text()

EXAMPLE_INPUT1 = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""
EXAMPLE_RESULT1 = 1651

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    #a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

class valve:
    def __init__(self, stringI):
        parts = stringI.split(' ')
        self.name = parts[1]
        self.pressure = int(re.findall('[-0-9]+', parts[4])[0])
        self.connectingValves = []
        valvesSplit = stringI[1:].split('valves') #destroyng first valve
        if len(valvesSplit) == 1:
            valvesSplit = stringI[1:].split('valve') #destroyng first valve
        self.connectingValves = valvesSplit[1].lstrip().split(', ')
        self.open = False
        self.openTime = -1


class mazeMove():
    def __init__(self, mazeString):
        self.mazeD = {}
        rows = mazeString.split('\n')
        self.numberOfValvesWithP = 0
        for row in rows:
            valveInstance = valve(row)
            self.mazeD[valveInstance.name] = valveInstance
            if valveInstance.pressure > 0:
                self.numberOfValvesWithP += 1
        self.bestResult = 0
        self.time = 0
    
    def scoreCalc(self, finalMaze):
        score = 0
        timeW = 30
        for valve in finalMaze.values():
            if valve.open == True:
                timeValveWasOpen = timeW - valve.openTime
                score += timeValveWasOpen * valve.pressure

        if score > self.bestResult:
            self.bestResult = score
            print('Score', score)

    def makeCopyOfD(self, mazeD):
        newmazeD = {}

        for key, value in mazeD.items():
            newmazeD[key] = copy.deepcopy(value)

        return newmazeD

    def mover(self, currentValve, currentTime, mazeD, numberOfOpenValves):

        #print('CurrentValve', currentValve.name, currentTime)
        finalMaze = mazeD
        if numberOfOpenValves < self.numberOfValvesWithP:
            if currentTime < 31:
                if currentValve.open == False and currentValve.pressure > 0: #maybe not always open but assume that for now
                    # print('Opening Value', currentValve.name)
                    currentTime += 1
                    numberOfOpenValves += 1
                    currentValve.open = True
                    currentValve.openTime = self.time        
                directions = currentValve.connectingValves
                if currentTime < 31:
                    for nextValve in directions:
                        finalMaze, timeR = self.mover(mazeD[nextValve], currentTime + 1, self.makeCopyOfD(mazeD), numberOfOpenValves)
        else:
            #all valvues open no need to run around
            currentTime = 31

        self.scoreCalc(finalMaze)
        return finalMaze, currentTime
        
        
def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0
    mazeI = mazeMove(input_string)

    mazeI.mover(mazeI.mazeD['AA'], 0, mazeI.mazeD, 0)

    solution = mazeI.bestResult


    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
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
problem_b(PROGBLEM_INPUT_TXT, 0)
print("\n")