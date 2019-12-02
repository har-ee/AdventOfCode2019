f = open("./input", "r")
input = [int(a) for a in f.read().split(sep=',')]
f.close()

for pc in range(0, len(input), 4):
    if(input[pc] == 99):
        break
    input[input[pc+3]] = (input[input[pc+1]] + input[input[pc+2]]) if (input[pc] == 1) else (input[input[pc+1]] * input[input[pc+2]])

print(input)