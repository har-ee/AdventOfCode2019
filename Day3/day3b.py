from enum import Enum
class Mode(Enum):
    CHECK = 1
    LOG = 2

f = open("./input", "r")
input = [[(a[0], int(a[1:])) for a in line.split(sep=',')]
         for line in f.read().split(sep='\n')]
f.close()

intersections = set([])

memory = {} # maps x to y to dist

def check(x, y, distance):
    if(x in memory and y in memory[x]):
        intersections.add(((x, y), memory[x][y], distance))

def log(x, y, distance):
    if(x not in memory):
        memory[x] = {y : distance}
    else:
        memory[x][y] = distance

def movex(coords, number, mode, distance):
    xold, y = coords
    for x in range(xold, xold + number):
        dist = distance + abs(abs(x) - abs(xold))
        check(x,y, dist) if mode == Mode.CHECK else log(x,y, dist)
    return (xold + number, y)

def movey(coords, number, mode, distance):
    x, yold = coords
    for y in range(yold, yold + number):
        dist = distance + abs(abs(y) - abs(yold))
        check(x,y, dist) if mode == Mode.CHECK else log(x,y, dist)
    return (x, yold + number)

def move(coords, direction, number, mode, distance):
    switch = {
        'R': lambda: movex(coords, number, mode, distance),
        'L': lambda: movex(coords, -number, mode, distance),
        'U': lambda: movey(coords, number, mode, distance),
        'D': lambda: movey(coords, -number, mode, distance),
    }
    return (switch[direction](), distance + abs(number))
    
distance = 0
coords = (0,0)
for instr in input[0]:
    coords, distance = move(coords, instr[0], instr[1], Mode.LOG, distance)

distance = 0
coords = (0,0)

for instr in input[1]:
    coords, distance = move(coords, instr[0], instr[1], Mode.CHECK, distance)

print(min(map(lambda x: abs(x[1]) + abs(x[2]), intersections)))