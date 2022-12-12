"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day7/input.txt").read_text()

EXAMPLE_INPUT1 = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
EXAMPLE_RESULT1 = 95437

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
    MAX_SIZE = 100001
    rows = string_worker(input_string)
    storageD = {}
    currentDirectory = ''

    for row in rows:
        match row:
            case '$ ls':
                pass
            case '$ cd ..':
                lastF = currentDirectory[:-1].rfind('/') #Get the second last /
                currentDirectory = currentDirectory[:lastF+1]
            case s if s.startswith('$ cd '):
                directory = row.split(' ')[2]
                currentDirectory += directory + '/'
            case s if s.startswith('dir'):
                pass
            case _: #file
                parts = row.split(' ')
                filesize = int(parts[0])
                cD = ''
                dirParts = currentDirectory[0:-1].split('/') #Dont include last /
                for dirPart in dirParts[1:]:
                    cD += dirPart + '/'
                    if cD in storageD:
                        storageD[cD] += filesize
                    else:
                        storageD[cD] = filesize
    for d in storageD:
        if storageD[d] < MAX_SIZE:
            solution += storageD[d]
        #print(d, storageD[d])

    print('Solution part1', solution)
    DISK_SIZE = 70000000
    NEED_FREE_SPACE = 30000000

    currentSize = storageD['/']
    currentFreeSize = DISK_SIZE - currentSize
    sizeToFreeUp = NEED_FREE_SPACE - currentFreeSize

    smallest = 1000000000000
    for d in storageD:
        if storageD[d] > sizeToFreeUp:
            if storageD[d] < smallest:
                smallest = storageD[d]
    solution = smallest

    if solution == expected_result:
        print("Solution part2", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

print('Example:')
problem_a(EXAMPLE_INPUT1, 24933642)
print('Problem:')
problem_a(PROGBLEM_INPUT_TXT, 1623571)
print("\n")
