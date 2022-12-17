"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path
import re

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day11/input.txt").read_text()

EXAMPLE_INPUT1 = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
EXAMPLE_RESULT1 = 10605

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n\n")
    #a_steps = [int(number) for number in input_string.split(',')]
    return a_steps


class dividor:
    def __init__(self, number):
        self.primes = [2,3,5,7,11,13,17,19, 23]
        self.factorsD = {}
        for prime in self.primes:
            self.factorsD[prime] = number % prime

    def multiply(self, number):
        for prime in self.primes:
            newResult = (self.factorsD[prime] * number) % prime
            self.factorsD[prime] = newResult

    def square(self):
        for prime in self.primes:
            newResult = (self.factorsD[prime] * self.factorsD[prime]) % prime
            self.factorsD[prime] = newResult

    def add(self, number):
        for prime in self.primes:
            newResult = (self.factorsD[prime] + number) % prime
            self.factorsD[prime] = newResult
    

class monkey:
    def __init__(self, _input, l):
        self.monkeyName = 'Name' + str(l)
        rows = _input.split('\n')
        numbers = re.findall("[0-9]+", rows[1])
        self.items = list(map(int, numbers))
        operationS = rows[2].split('=')[1]
        operationS = operationS.lstrip()
        parts = operationS.split(' ')
        self.operationPart1 = parts[0]
        self.operationPart2 = parts[2]
        self.operand = parts[1]
        self.testNumber = int(re.findall("[0-9]+", rows[3])[0])
        self.ifTrueNewMonkey = int(re.findall("[0-9]+", rows[4])[0])
        self.ifFalseNewMonkey = int(re.findall("[0-9]+", rows[5])[0])
        self.numberOfInspections = 0
        self.itemsF = []
        for item in self.items:
            self.itemsF.append(dividor(item))

    def add(self, newItemRisk):
        self.items.append(newItemRisk)
    
    def addPart2(self, newItemRisk):
        self.itemsF.append(newItemRisk)

    def doMonkey(self, monkeyD):
        newRisk = 0
        for item in self.items:
            if self.operand == '*':
                if self.operationPart2 == 'old':
                    newRisk = item*item
                else:
                    newRisk = item*int(self.operationPart2)
            else: # '+' 
                    newRisk = item+int(self.operationPart2)
            newRisk = newRisk // 3
            divD = newRisk % self.testNumber
            if divD == 0:
                monkeyD[self.ifTrueNewMonkey].add(newRisk)
            else:
                monkeyD[self.ifFalseNewMonkey].add(newRisk)
            self.numberOfInspections += 1
        self.items = []

    def doMonkey3(self, monkeyD):
        newRisk = 0
        for item in self.items:
            if self.operand == '*':
                if self.operationPart2 == 'old':
                    newRisk = item*item
                else:
                    newRisk = item*int(self.operationPart2)
            else: # '+' 
                    newRisk = item+int(self.operationPart2)
            newRisk = newRisk % (2*3*5*7*11*13*17*19*23)
            divD = newRisk % self.testNumber
            if divD == 0:
                monkeyD[self.ifTrueNewMonkey].add(newRisk)
            else:
                monkeyD[self.ifFalseNewMonkey].add(newRisk)
            self.numberOfInspections += 1
        self.items = []

    def doMonkeyPart2(self, monkeyD):
        newRisk = 0
        for item in self.itemsF:
            if self.operand == '*':
                if self.operationPart2 == 'old':
                    item.square()
                else:
                    item.multiply(int(self.operationPart2))
            else: # '+' 
                    item.add(int(self.operationPart2))

            if item.factorsD[self.testNumber] == 0:
                monkeyD[self.ifTrueNewMonkey].addPart2(item)
            else:
                monkeyD[self.ifFalseNewMonkey].addPart2(item)
            self.numberOfInspections += 1
        self.itemsF = []    


def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0
    parts = string_worker(input_string)

    monkeyD = {}

    for l in range(len(parts)):
        monkeyD[l] = monkey(parts[l], l)

    for turns in range(20):
            for l in range(len(parts)):
                monkeyD[l].doMonkey(monkeyD)


    inspections = []
    for l in range(len(parts)):
        inspections.append(monkeyD[l].numberOfInspections)

    inspections.sort()
    solution = inspections[-1]*inspections[-2]

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 111210)
print("\n")

def problem_b(input_string, expected_result):
    solution = 0
    parts = string_worker(input_string)

    monkeyD = {}

    for l in range(len(parts)):
        monkeyD[l] = monkey(parts[l], l)

    length = len(parts)
    for turns in range(10000):
            for l in range(length):
                monkeyD[l].doMonkey3(monkeyD)
            #print('l = ', turns)

    inspections = []
    for l in range(len(parts)):
        inspections.append(monkeyD[l].numberOfInspections)

    inspections.sort()
    solution = inspections[-1]*inspections[-2]

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b(EXAMPLE_INPUT1, 2713310158)
problem_b(PROGBLEM_INPUT_TXT, 15447387620)
print("\n")