"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day3/input.txt").read_text()

EXAMPLE_INPUT1 = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
EXAMPLE_RESULT1 = 157

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    #a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    sum = 0
    rows = string_worker(input_string)
    for row in rows:
        length = len(row)
        half = int((length/2))
        new_fh = row[:half]
        new_sh = row[half:]
        common_list = set(new_fh).intersection(new_sh)

        for commmonChar in common_list:
            temp =  ord(commmonChar)
            if temp > 96:
                sum += temp - 96
            else:
                sum += temp - 65 + 27



    solution = sum

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")


##################################################################################################


def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    sum = 0
    rows = string_worker(input_string)
    length = len(rows)

    divBy3 = length // 3

    for rowN in range(divBy3):

        line1 = rows[rowN*3]
        common_list = set(line1).intersection(rows[rowN*3+1]).intersection(rows[rowN*3+2])

        for commmonChar in common_list:
            temp =  ord(commmonChar)
            if temp > 96:
                sum += temp - 96
            else:
                sum += temp - 65 + 27



    solution = sum

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b(EXAMPLE_INPUT1, 70)
problem_b(PROGBLEM_INPUT_TXT, 0)
print("\n")