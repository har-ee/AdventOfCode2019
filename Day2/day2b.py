foundAnswer = 0
for noun in range(100):
    if(foundAnswer):
        break
    for verb in range(100):
        f = open("./input", "r")
        input = [int(a) for a in f.read().split(sep=',')]
        f.close()
        input[1] = noun
        input [2] = verb

        for pc in range(0, len(input), 4):
            if(input[pc] == 99):
                break
            input[input[pc+3]] = (input[input[pc+1]] + input[input[pc+2]]) if (input[pc] == 1) else (input[input[pc+1]] * input[input[pc+2]])

        print(input[0])
        if(input[0] == 19690720):
            foundAnswer = 1
            print(noun, verb)
            break
