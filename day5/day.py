"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day5/input.txt").read_text()

EXAMPLE_INPUT1 = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
EXAMPLE_RESULT1 = 'CMZ'

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n\n")
    #a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    solution = ''

    parts = string_worker(input_string)
    storageD = {}
    for id in range(1,11):
        storageD[id] = []

    rows = parts[0].split('\n')
    for row in rows:
        for i in range(len(row)):
            l = row[i]
            if l == '[':
                stack = i // 4 + 1
                storageD[stack].insert(0, row[i+1])
        pass

    rows = parts[1].split('\n')
    for row in rows:
        commands = row.split(' ')
        noBoxes = int(commands[1])
        fromS = commands[3]
        toS = commands[5]

        for _ in range(noBoxes):
            storageD[int(toS)].append(storageD[int(fromS)].pop())

    for i in range(1, 10):
        solution += storageD[i][-1]
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

#problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")


######################################################################################

def problem_b(input_string, expected_result):
    """Problem B solved function
    """
    solution = ''

    parts = string_worker(input_string)
    storageD = {}
    for id in range(1,11):
        storageD[id] = []

    rows = parts[0].split('\n')
    for row in rows:
        for i in range(len(row)):
            l = row[i]
            if l == '[':
                stack = i // 4 + 1
                storageD[stack].insert(0, row[i+1])
        pass

    rows = parts[1].split('\n')
    for row in rows:
        commands = row.split(' ')
        noBoxes = int(commands[1])
        fromS = commands[3]
        toS = commands[5]

        tempL = []

        for _ in range(noBoxes):
            tempL.append(storageD[int(fromS)].pop())

        tempL.reverse() 

        for temp in tempL:
            storageD[int(toS)].append(temp)

    for i in range(1, 10):
        solution += storageD[i][-1]

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

#problem_b(EXAMPLE_INPUT1, 'MCD')
problem_b(PROGBLEM_INPUT_TXT, 0)
print("\n")