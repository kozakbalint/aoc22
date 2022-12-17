moves = []
stacks = []

def parseInput():
    lines = []
    with open("./input.txt", "r") as f:
        for line in f:
            lines.append(line.replace('\n', ''))
    
    for i in range(len(lines)):
        if lines[i] == '':
            moves = lines[i+1:-1]
            lines = lines[:i]
            break
    
    cols = len(lines[-1].replace(" ", ''))
    lines = lines[::-1]
    
    stack = []
    for i in range(1, 4*cols-1,4):
        for j in range(1,len(lines)):
            stack.append(lines[j][i])
        stack = [x for x in stack if x != ' ']
        stacks.append(stack)
        stack = []

    for i in range(len(moves)):
        moves[i] = ''.join(c for c in moves[i] if c.isnumeric() or c.isspace()) 
        moves[i] = moves[i].split()

    return stacks, moves

def partOne(stacks, moves):
    for move in moves:
        for i in range(int(move[0])):
            tmp = stacks[int(move[1])-1].pop()
            stacks[int(move[2])-1].append(tmp)
            tmp = []

    result = ""
    for i in range(len(stacks)):
        result += stacks[i][-1]
    print(result)

def partTwo(stacks, moves):
    tmp = []
    for move in moves:
        for i in range(int(move[0])):
            tmp.append(stacks[int(move[1])-1].pop())
        tmp.reverse()
        stacks[int(move[2])-1] += tmp
        tmp = []

    result = ""
    for i in range(len(stacks)):
        result += stacks[i][-1]
    print(result)

if __name__ == "__main__":
    stacks, moves = parseInput()
    partSel = input("Select [1] for Part One or [2] for Part Two\n")
    if partSel == "1":
        partOne(stacks, moves)
    else:
        partTwo(stacks, moves)

