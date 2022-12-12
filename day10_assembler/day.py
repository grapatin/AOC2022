"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day10/input.txt").read_text()

EXAMPLE_INPUT1 = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""
EXAMPLE_RESULT1 = 13140

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    #a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

class AssemblyProcessor:
    """Class for Advent Of Code assembly language processing
    """
    def __init__(self, code_array):
        self.registry_dict = {
        }
        self.cycles_dict = {}
        self._program_counter = 0
        self._cpu_cycles = 1
        self._code_array = code_array
        self._length = len(code_array)
        self.registry_dict['X'] = 1
        self._output = 1
        self._sound = 0

    def _addx(self, code_string):
        """addx V
        Takes 2 cycles to complete
        Increases X by the value V
        """
        parts = code_string.split()
        self.cycles_dict[self._cpu_cycles] = self.registry_dict['X']
        self._cpu_cycles += 1
        self.cycles_dict[self._cpu_cycles] = self.registry_dict['X']
        self._cpu_cycles += 1
        self.registry_dict['X'] += int(parts[1])
        self.cycles_dict[self._cpu_cycles] = self.registry_dict['X']
        self._program_counter += 1
    
    def _noop(self, code_string):
        """noop
        Takes 1 cycles to complete
        """
        parts = code_string.split()
        self._cpu_cycles += 1
        self.cycles_dict[self._cpu_cycles] = self.registry_dict['X']
        self._program_counter += 1
    
    def execute(self):
        """Executor of next command in code_string
        """
        if self._program_counter < len(self._code_array):
            code_string = self._code_array[self._program_counter]
            if 'addx' in code_string:
                self._addx(code_string)
            elif 'noop' in code_string:
                self._noop(code_string)
            else:
                assert False
            return True
        else:
            return False

def problem(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0
    code_strings = string_worker(input_string)
    runner_instance = AssemblyProcessor(code_strings)
    while runner_instance.execute():
        pass

    cycleA = [20, 60, 100, 140, 180, 220]
    for cycle in cycleA:
        solution += runner_instance.cycles_dict[cycle]*cycle 

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)


    outputString = ''
    displayPos = 0
    for i in range(240):
        currentSpritePos = runner_instance.cycles_dict[i+1]
        if abs(currentSpritePos - displayPos) < 2:
            outputString += '#'
        else:
            outputString += '.' 
        if displayPos == 39:
            displayPos = 0
            outputString += '\n'
        else:
            displayPos += 1

    print(outputString)

problem(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem(PROGBLEM_INPUT_TXT, 16020)
print("\n")