"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day4/input.txt").read_text()

EXAMPLE_INPUT1 = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
EXAMPLE_RESULT1 = 2

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    #a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0


    rows = string_worker(input_string)
    for row in rows:
        found = False
        pairs = row.split(',')
        numbers1 = [int(number) for number in pairs[0].split('-')]
        numbers2 = [int(number) for number in pairs[1].split('-')]

        if numbers2[0] >= numbers1[0]:
            if numbers2[1] <= numbers1[1]:
                solution += 1
                found = True
        if (numbers1[0] >= numbers2[0]) and found == False:
            if numbers1[1] <= numbers2[1]:
                solution += 1

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 507)
print("\n")

def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0


    rows = string_worker(input_string)
    for row in rows:
        found = False
        pairs = row.split(',')
        numbers1 = [int(number) for number in pairs[0].split('-')]
        numbers2 = [int(number) for number in pairs[1].split('-')]
        
        rangeD = {}
        start = numbers1[0]

        for l in range(start, numbers1[1]+1):
            rangeD[l] = True

        for k in range(numbers2[0], numbers2[1]+1):
            if k in rangeD:
                solution += 1
                break

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)



problem_b(EXAMPLE_INPUT1, 4)
problem_b(PROGBLEM_INPUT_TXT, 897)
#print("\n")