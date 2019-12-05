f = open("./input", "r")
memory = [int(a) for a in f.read().split(sep=',')]
f.close()

input = 5
output = None

pc = 0
while(True):
    opcode = memory[pc] % 100
    modes = [int(c) for c in str(100000 + memory[pc])[1:4]]

    def get(i):
        return memory[pc + i] if modes[3 - i] else memory[memory[pc + i]]
    
    if(opcode == 99):
        break
    if(opcode == 1):
        memory[memory[pc + 3]] = get(1) + get(2)
        pc += 4
    elif(opcode == 2):
        memory[memory[pc + 3]] = get(1) * get(2)
        pc += 4
    elif(opcode == 3): 
        memory[memory[pc + 1]] = input
        pc += 2
    elif(opcode == 4): 
        output = get(1)
        pc += 2
    elif(opcode == 5):
        pc = get(2) if get(1) else pc + 3
    elif(opcode == 6):
        pc = get(2) if not get(1) else pc + 3
    elif(opcode == 7):
        memory[memory[pc + 3]] = 1 if get(1) < get(2) else 0
        pc += 4
    elif(opcode == 8):
        memory[memory[pc + 3]] = 1 if get(1) == get(2) else 0
        pc += 4

print("Output",output)