"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path
import re
import functools

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day13/input.txt").read_text()

EXAMPLE_INPUT1 = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

EXAMPLE_RESULT1 = 13

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n\n")
    #a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

def findArray(inputS):
    firstChar  = inputS[0]
    if firstChar == '[':
        #find matching ]
        matchCount = 0
        newArray = ''
        for idx, x in enumerate(inputS[1:]):
            newArray += x
            if x == '[':
                matchCount += 1
            elif x == ']':
                if matchCount == 0:
                    #we are done
                    return newArray[0:-1] #drop the last ]
                else:
                    matchCount -= 1
    else:
        return inputS

def splitWhereNoParams(inputS):
    outputArray = []
    matchCount = 0
    newArrayElement = ''
    for idx, x in enumerate(inputS):
        if x == '[':
            matchCount += 1
        elif x == ']':
            matchCount -= 1
        if matchCount == 0 and x == ',':
            outputArray.append(newArrayElement)
            newArrayElement = ''
        else:
            newArrayElement += x #inner level just add
        
    outputArray.append(newArrayElement)    
    return outputArray

def recursiveWorker(leftSideInput, rightSideInput):
    leftSide = findArray(leftSideInput)
    leftArray = splitWhereNoParams(leftSide)
    rightSide = findArray(rightSideInput)
    rightArray = splitWhereNoParams(rightSide)
    whoWon = 0
    length = min(len(leftArray), len(rightArray))
    for l in range(length):
        if leftArray[l].isnumeric() and rightArray[l].isnumeric():
            leftCompare = int(leftArray[l])
            rightCompare = int(rightArray[l])
            #print(leftCompare, rightCompare)
            if leftCompare > rightCompare:
                return 1
            elif leftCompare < rightCompare:
                return -1
            else:
                pass #draw continue
        else:
            if leftArray[l].isnumeric():
                leftArray[l] = '[' + leftArray[l] + ']'
            if rightArray[l].isnumeric():
                rightArray[l] = '[' + rightArray[l] + ']'
            if min(len(leftArray[l]), len(rightArray[l])) > 0:
                whoWon = recursiveWorker(leftArray[l], rightArray[l])
        if whoWon != 0:
            return whoWon
    if rightArray[0] == '' and leftArray[0] == '':
        return 0
    if len(leftArray) > len(rightArray) or rightArray[0] == '':
        return 1
    elif len(leftArray) < len(rightArray) or leftArray[0] == '':
        return -1
    
    return 0

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0
    pairs = string_worker(input_string)
    for id, pair in enumerate(pairs):
        leftSide = pair.split('\n')[0]
        rightSide = pair.split('\n')[1]
        result2 = recursiveWorker(leftSide, rightSide)
        
        if result2 == -1:
            solution += id + 1                        

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 5292)
print("\n")

def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0
    input_string = input_string.replace('\n\n', '\n')
    
    rows = input_string.split('\n')
    rows.append('[[2]]')
    rows.append('[[6]]')

    rows = sorted(rows, key=functools.cmp_to_key(recursiveWorker))

    solution = (rows.index('[[2]]')+1)*(rows.index('[[6]]')+1)

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b(EXAMPLE_INPUT1, 140)
problem_b(PROGBLEM_INPUT_TXT, 0)
print("\n")