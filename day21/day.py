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

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    #a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

def problem_a(input_string :str, expected_result):
    """Problem A solved function
    """

    cont = True

    while False:
        cont = False
        rows :str = input_string.splitlines()
        for row in rows:
            monkeyName, monkeyAction = row.split(':')
            numbers = re.findall('[0-9]+', monkeyAction)
            if len(numbers) > 0: 
                if numbers[0] == monkeyAction.strip():
                    #we have a monkey with a number
                    numb = numbers[0]
                    if monkeyName == 'root':
                        solution = int(numb)
                        break
                    input_string = input_string.replace(row, '&&&:&&&') #later on remove full line
                    input_string = input_string.replace(monkeyName, numb)
                    cont = True
                elif len(numbers) == 2:
                    #we have an expression
                    expression = monkeyAction.strip().split(' ')
                    part1 = int(expression[0])
                    operator = expression[1]
                    part2 = int(expression[2])
                    match operator:
                        case '+':
                            sum = part1 + part2
                        case '-':
                            sum = part1 - part2
                            if sum < 0:
                                print('Hello!')
                        case '/':
                            sum = part1 // part2
                            #if part1 % part2 != 0:
                            continue
                            #    rest = part1 % part2
                            #    print(rest)
                        case '*':
                            sum = part1 * part2
                    input_string = input_string.replace(monkeyAction, ' '+str(sum))
                    cont = True

    newString = ''
    storageD = {}
    for row in input_string.splitlines():
        if row != '&&&:&&&':
            monkeyName, monkeyAction = row.split(':')
            storageD[monkeyName] = monkeyAction
    cont = True
    while cont:
        cont = False
        rows :str = input_string.splitlines()
        for monkeyName in storageD:
            if monkeyName == 'root':
                continue
            monkeyAction = storageD[monkeyName]
            numbers = re.findall('[0-9]+', monkeyAction)
            if len(numbers) > 0: 
                if numbers[0] == monkeyAction.strip():
                    #we have a monkey with a number
                    numb = numbers[0]
                    if monkeyName == 'root':
                        solution = int(numb)
                        break
                    for monkey2Name in storageD:
                        monkey2Action = storageD[monkey2Name]
                        if monkeyName in monkey2Action:
                            monkey2Action = monkey2Action.replace(monkeyName, numb)
                            storageD[monkey2Name] = monkey2Action
                            break
                    storageD.pop(monkeyName, None)
                    cont = True
                    break
                elif len(numbers) == 2 and '.' not in monkeyAction and '(' not in monkeyAction:
                    #we have an expression
                    expression = monkeyAction.strip().split(' ')
                    part1 = int(expression[0])
                    operator = expression[1]
                    part2 = int(expression[2])
                    match operator:
                        case '+':
                            sum = part1 + part2
                        case '-':
                            sum = part1 - part2
                            if sum < 0:
                                print('Hello!')
                        case '/':
                            sum = '(' + monkeyAction + ')'
                        case '*':
                            sum = part1 * part2
                    for monkey2Name in storageD:
                        monkey2Action = storageD[monkey2Name]
                        if monkeyName in monkey2Action:
                            monkey2Action = monkey2Action.replace(monkeyName, str(sum))
                            if monkey2Action == ' 130.5 * 2':
                                monkey2Action = ' (130.5 * 2)'
                            storageD[monkey2Name] = monkey2Action
                            storageD.pop(monkeyName, None)
                            break
                    cont = True
                    break
                elif len(numbers) > 2:
                    found = False
                    # if monkeyAction == ' 2173 + 70282.4':
                    #     monkeyAction = ' 72455.4'
                    #     found = True
                    # elif monkeyAction == '  72455.4 / 2':
                    #     monkeyAction = ' 36227.7'
                    #     found = True
                    # elif monkeyAction == '   36227.7 - 489 * 5':
                    #     monkeyAction = ' 178693.5'
                    #     found = True
                    # elif monkeyAction == '  178693.5 - 320':
                    #     monkeyAction = ' 178373.5'
                    #     found = True
                    # elif monkeyAction == '  178373.5 / 5':
                    #     monkeyAction = ' 35674.7'
                    #     found = True
                    # elif monkeyAction == '  35674.7 + 1144':
                    #     monkeyAction = '36818.7'
                    #     found = True

                    for monkey2Name in storageD:
                        monkey2Action = storageD[monkey2Name]
                        if monkeyName in monkey2Action:
                            monkey2Action = monkey2Action.replace(monkeyName, monkeyAction)
                            if not found:
                                monkey2Action = '(' + monkey2Action + ')'
                            storageD[monkey2Name] = monkey2Action
                            storageD.pop(monkeyName, None)
                            break

                    cont = True
                    break



    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

#problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 0) #484326268424810
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