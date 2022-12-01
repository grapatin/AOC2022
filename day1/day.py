"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day1/input.txt").read_text()

EXAMPLE_INPUT1 = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
EXAMPLE_RESULT1 = 24000

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n\n")
    #a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    groups = string_worker(input_string)
    candyList = []
    for group in groups:
        lines = group.split('\n')
        sum = 0
        for line in lines:
            sum += int(line)
        candyList.append(sum)

    solution = max(candyList)
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 70509)
print("\n")


def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    groups = string_worker(input_string)
    candyList = []

    for group in groups:
        lines = group.split('\n')
        sum = 0
        for line in lines:
            sum += int(line)
        candyList.append(sum)

    candyList.sort(reverse=True)
    solution = candyList[0]+candyList[1]+candyList[2]
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b(EXAMPLE_INPUT1, 45000)
problem_b(PROGBLEM_INPUT_TXT, 208567)
print("\n")