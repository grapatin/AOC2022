"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day20C/input.txt").read_text()

EXAMPLE_INPUT1 = """1
2
-3
3
-2
0
4"""
EXAMPLE_RESULT1 = 3

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    #a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

class numberClass:
    def __init__(self, number):
        self.number = number
        self.before :numberClass
        self.next :numberClass

    def removeMe(self):
        beforeO = self.before
        nextO = self.next
        beforeO.next = nextO
        nextO.before = beforeO

    def moveAccordingly(self, steps):
        current :numberClass = self
        next = self.next
        before = self.before

        if steps != 0:
            self.removeMe()
                    
        if steps > 0:
            for i in range(steps):
                current = next
                next = current.next
        if steps < 0:
            for i in range(abs(steps) + 1):
                current = before
                before = current.before

        if steps != 0:
            oneAfter = current.next
            current.next = self
            oneAfter.before = self
            self.next = oneAfter
            self.before = current

def printList(firstO :numberClass):
    for i in range(7):
        print(firstO.number, end=' ')
        firstO = firstO.next
    print('')

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0
    originalOrderD = {}
    StorageD = {}
    rows = string_worker(input_string)
    orginalOrder = 0
    firstN = int(rows[0])
    firstO = numberClass(firstN)
    originalOrderD[orginalOrder] = firstO
    orginalOrder += 1
    previous = firstO
    length = len(rows)
    for rowId in range(1, len(rows)):
        number = int(rows[rowId])
        numberO = numberClass(number)
        if number == 0:
            StorageD[0] = numberO
        numberO.before = previous
        previous.next = numberO
        originalOrderD[orginalOrder] = numberO
        orginalOrder += 1
        previous = numberO
    previous.next = firstO
    firstO.before = previous

    #printList(originalOrderD[0])
    for i in range(orginalOrder):
        numberO :numberClass = originalOrderD[i]
        steps  = numberO.number
        if steps > 0:
            steps = numberO.number % (length - 1)
            pass
        elif steps < 0:
            pass
            steps = (abs(numberO.number) % (length - 1)) * -1
            #steps = steps + length - 1

        numberO.moveAccordingly(steps)
        #print('Steps:', steps)
        #printList(numberO)

    length = len(rows)
    steps = 1000

    ZeroO = StorageD[0]

    nextO = ZeroO
    for l in range(steps):
        nextO = nextO.next
    print(nextO.number)
    solution = nextO.number

    steps = 2000
    nextO = ZeroO
    for l in range(steps):
        nextO = nextO.next
    print(nextO.number)
    solution += nextO.number

    steps = 3000
    nextO = ZeroO
    for l in range(steps):
        nextO = nextO.next
    print(nextO.number)
    solution += nextO.number

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 19559)
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