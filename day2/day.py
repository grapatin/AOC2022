"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day2/input.txt").read_text()

EXAMPLE_INPUT1 = """A Y
B X
C Z"""
EXAMPLE_RESULT1 = 15


WIN = 6
DRAW = 3
LOSS = 0

X = 1 #ROCK A
Y = 2 #PAPER B 
Z = 3 #SCISSOR C

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    #sa_steps = [int(number) for number in input_string.split(',')]
    return a_steps

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    rows = string_worker(input_string)

    sum = 0
    for row in rows:
        commands = row.split(' ')
        if commands[1] == 'X':
            sum += 1
        elif commands[1] == 'Y':
            sum += 2
        else:
            sum += 3

        if commands[0] == 'A':
            if commands[1] == 'X':
                sum += 3
            elif commands[1] == 'Y':
                sum += 6
            else:
                sum+= 0

        elif commands[0] == 'B':
            if commands[1] == 'X':
                sum += 0
            elif commands[1] == 'Y':
                sum += 3
            else:
                sum+= 6
        else:
            if commands[1] == 'X':
                sum += 6
            elif commands[1] == 'Y':
                sum += 0
            else:
                sum+= 3

    solution = sum

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 14163)
print("\n")

def problem_b(input_string, expected_result):
    """Problem A solved function
    """

    # x = loose
    # y = draw
    # z = win

    rows = string_worker(input_string)

    sum = 0
    for row in rows:
        commands = row.split(' ')
        if commands[1] == 'X':
            sum += 0
        elif commands[1] == 'Y':
            sum += 3
        else:
            sum += 6

        if commands[0] == 'A':
            if commands[1] == 'X':
                sum += 3
            elif commands[1] == 'Y':
                sum += 1
            else:
                sum+= 2

        elif commands[0] == 'B':
            if commands[1] == 'X':
                sum += 1
            elif commands[1] == 'Y':
                sum += 2
            else:
                sum+= 3
        else:
            if commands[1] == 'X':
                sum += 2
            elif commands[1] == 'Y':
                sum += 3
            else:
                sum+= 1

    solution = sum

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b(EXAMPLE_INPUT1, 12)
problem_b(PROGBLEM_INPUT_TXT, 12091)
print("\n")