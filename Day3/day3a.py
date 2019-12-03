f = open("./input", "r")
input = [[(a[0], int(a[1:])) for a in line.split(sep=',')]
         for line in f.read().split(sep='\n')]
f.close()

intersections = set([])

memory = {} # maps x to y

def check(x, y):
    if(x in memory and y in memory[x]):
        intersections.add((x, y))

def log(x, y):
    if(x not in memory):
        memory[x] = set([y])
    else:
        memory[x].add(y)

def movex(coords, number, mode):
    xold, y = coords
    for x in range(xold, xold + number):
        check(x,y) if mode == 'check' else log(x,y)
    return (xold + number, y)

def movey(coords, number, mode):
    x, yold = coords
    for y in range(yold, yold + number):
        check(x,y) if mode == 'check' else log(x,y)
    return (x, yold + number)

def move(coords, direction, number, mode):
    switch = {
        'R': lambda : movex(coords, number, mode),
        'L': lambda : movex(coords, -number, mode),
        'U': lambda : movey(coords, number, mode),
        'D': lambda : movey(coords, -number, mode),
    }
    return switch[direction]()
    
coords = (0,0)
for instr in input[0]:
    coords = move(coords, instr[0], instr[1], 'log')

coords = (0,0)

for instr in input[1]:
    coords = move(coords, instr[0], instr[1], 'check')

print(min(map(lambda x: abs(x[0]) + abs(x[1]), intersections)))