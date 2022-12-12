"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day8/input.txt").read_text()

EXAMPLE_INPUT1 = """30373
25512
65332
33549
35390"""
EXAMPLE_RESULT1 = 21

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
    trees = string_worker(input_string)

    depth = len(trees)
    width = len(trees[0])
    storageD = {}

    for l in range(width):
        maxHTopp = -1
        maxHBottom = -1
        for k in range(depth):
            if int(trees[k][l]) > maxHTopp:
                storageD[l+(k*1000)] = 'Counted'
                maxHTopp = int(trees[k][l])
        for k in range(0, depth):
            k_back = depth - k - 1
            if int(trees[k_back][l]) > maxHBottom:
                storageD[l+((k_back)*1000)] = 'Counted'
                maxHBottom = int(trees[k_back][l])

    for k in range(depth):
        maxHTopp = -1
        maxHBottom = -1
        for l in range(width):
            if int(trees[k][l]) > maxHTopp:
                storageD[l+(k*1000)] = 'Counted'
                maxHTopp = int(trees[k][l])
        for l in range(0, depth):
            l_b = depth - l - 1
            if int(trees[k][l_b]) > maxHBottom:
                storageD[l_b+((k)*1000)] = 'Counted'
                maxHBottom = int(trees[k][l_b])

    solution = len(storageD)
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 1698)
print("\n")


def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    trees = string_worker(input_string)

    depth = len(trees)
    width = len(trees[0])
  
    maxScenic = 0


    for r in range(depth):
        for t in range(depth):
            seenT = 0
            currentH = trees[r][t]
            for l in range(1,depth):
                newRU = r - l
                if newRU > -1:
                    if trees[newRU][t] < currentH:
                        seenT += 1
                    elif trees[newRU][t] >= currentH:
                        seenT += 1
                        break
            scenicS = seenT
            seenT = 0
            
            for l in range(1,depth):
                newRD = r + l
                if newRD < depth:
                    if trees[newRD][t] < currentH:
                        seenT += 1
                    elif trees[newRD][t] >= currentH:
                        seenT += 1
                        break

            scenicS = seenT * scenicS
            seenT = 0
            for l in range(1,depth):
                newTL = t - l
                if newTL > - 1:
                    if trees[r][newTL] < currentH:
                        seenT += 1
                    elif trees[r][newTL] >= currentH:
                        seenT += 1
                        break

            scenicS = seenT * scenicS
            seenT = 0
            for l in range(1,depth):
                newTR = t + l
                if newTR < depth:
                    if trees[r][newTR] < currentH:
                        seenT += 1
                    elif trees[r][newTR] >= currentH:
                        seenT += 1
                        break
            scenicS = seenT * scenicS
            seenT = 0

            if scenicS > maxScenic:
                maxScenic = scenicS
            scenicS = 0

    solution = maxScenic

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b(EXAMPLE_INPUT1, 8)
problem_b(PROGBLEM_INPUT_TXT, 672280)
print("\n")