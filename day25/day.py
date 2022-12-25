"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day25/input.txt").read_text()

EXAMPLE_INPUT1 = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""
EXAMPLE_RESULT1 = 36251175625102

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    #a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    nextNumber :int= 0
    sum = 0
    for row in input_string.splitlines():
        size = len(row)
        count = 0
        for i in row:
            position = size - count - 1
            match i:
                case '2':
                    nextNumber = 2
                case '1':
                    nextNumber = 1
                case '0':
                    nextNumber = 0
                case '-':
                    nextNumber = -1
                case '=':
                    nextNumber = -2

            nextNumber = nextNumber * (5**position)
            sum += nextNumber
            count += 1
        
    print('Sum result:', sum)

    resultA = []
    
    for i in range(30, -1, -1):
        temp = sum // (5**i)
     
        resultA.append(temp)
        sum = sum % (5**i)
    
    memory = 0
    result = ''
    #print(resultA)
    resultA.reverse()

    for value in resultA:
        newValue = value + memory
        memory = 0
        match newValue:
            case 0:
                result += '0'
            case 1:
                result += '1'
            case 2:
                result += '2'
            case 3:
                result += '='
                memory = 1
            case 4:
                result += '-'
                memory = 1
            case 5:
                result += '0'
                memory = 1
    
    result = result[::-1]
    solution = result.lstrip('0')

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)


problem_a(EXAMPLE_INPUT1, '2=-1=0')
problem_a(PROGBLEM_INPUT_TXT, '20===-20-020=0001-02')