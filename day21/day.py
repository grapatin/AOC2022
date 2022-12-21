"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path
import re

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day21/input.txt").read_text()

EXAMPLE_INPUT1 = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""
EXAMPLE_RESULT1 = 152

def problem_a(input_string :str, expected_result):
    """Problem A solved function
    """
    storageD = {}
    for row in input_string.splitlines():
        monkeyName, monkeyAction = row.split(':')
        storageD[monkeyName] = monkeyAction
    cont = True
    while cont:
        cont = False
        for monkeyName in storageD:
            if monkeyName == 'root':
                continue
            monkeyAction = storageD[monkeyName]
            charsG = re.findall('[a-z]+', monkeyAction)
            if len(charsG) == 0: #This is a math only string
                for monkey2Name in storageD:
                    monkey2Action = storageD[monkey2Name]
                    if monkeyName in monkey2Action:
                        monkey2Action = monkey2Action.replace(monkeyName, '(' + monkeyAction + ')')
                        storageD[monkey2Name] = monkey2Action
                        storageD.pop(monkeyName, None)
                        cont = True
                        break
                break
                        

    print(storageD['root'].strip())
    solution = int(eval(storageD['root']))
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 324122188240430)
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