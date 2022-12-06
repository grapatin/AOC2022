"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day6/input.txt").read_text()

EXAMPLE_INPUT1 = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""
EXAMPLE_RESULT1 = 29

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    #a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0

    for l in range(len(input_string)):
        storageD = {}
        found = True
        for k in range(14):
            if input_string[l + k] in storageD:
                found = False
                break
            else:
                storageD[input_string[l + k]] = True

        if found:
            solution = l + 14
            break


    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_b(PROGBLEM_INPUT_TXT, 2635)
print("\n")

