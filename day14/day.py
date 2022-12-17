"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2022/"\
    +"day14/input.txt").read_text()

EXAMPLE_INPUT1 = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
EXAMPLE_RESULT1 = 24


class sand():
    def __init__(self,input):
        self.storageD = {}

        rows = input.split('\n')
        # lengthX = len(rows[0])
        # lengthY = len(rows)

        # for idY, row in enumerate(rows):
        #     for idX, char in enumerate(row):
        #         self.storageD
        self.maxY = 0
        for row in rows:
            cords = row.split(' -> ')
            arrayX = []
            arrayY = []

            for cord in cords:
                arrayX.append(int(cord.split(',')[0]))
                arrayY.append(int(cord.split(',')[1]))
            
            for l in range(len(arrayX) - 1):
                self.storageD[self.fixIt(arrayX[l],arrayY[l])] = '#'
                if arrayX[l] > arrayX[l+1]:
                    direction = -1
                else:
                    direction = 1
                for x in range(arrayX[l], arrayX[l+1] + direction, direction):
                    self.storageD[self.fixIt(x,arrayY[l])] = '#'

                if arrayY[l] > arrayY[l+1]:
                    direction = -1
                else:
                    direction = 1
                for y in range(arrayY[l],arrayY[l+1]+direction, direction):
                    self.storageD[self.fixIt(arrayX[l],y)] = '#'
                    if y > self.maxY:
                        self.maxY = y
        self.maxY += 2
        for x in range(0, 1000):
                    self.storageD[self.fixIt(x,self.maxY)] = '#'


    def falling(self,x, y):
        falling = True

        while(falling):
            xCurrent = x
            yCurrent = y
            y += 1
            if self.fixIt(x,y) in self.storageD:
                x -= 1
                if self.fixIt(x,y) in self.storageD:
                    x += 2  
                    if self.fixIt(x,y) in self.storageD:
                        #We cannot fall deeper
                        falling = False
            if falling == False and y < self.maxY + 1:
                self.storageD[self.fixIt(xCurrent, yCurrent)] = 'O'
                if xCurrent == 500 and yCurrent == 0:
                    return False
                else:
                    return True #continue
            if falling == True and y > self.maxY:
                return False # stop we have reached maximum

            
            
    def work(self):
        startX = 500
        startY = 0

        cont = True
        while (cont):
            cont = self.falling(startX, startY)

        
                    

    def fixIt(self, x, y):
        return str(x)+','+str(y)

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0
    cave = sand(input_string)
    cave.work()

    for element in cave.storageD.values():
        if element == 'O':
            solution += 1

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")

def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0
    cave = sand(input_string)
    cave.work()

    for element in cave.storageD.values():
        if element == 'O':
            solution += 1

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b(EXAMPLE_INPUT1, 93)
problem_b(PROGBLEM_INPUT_TXT, 0)
print("\n")