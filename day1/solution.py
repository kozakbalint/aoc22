lines = []

def parseInput():
    with open("./input.txt") as f:
        for line in f:
            lines.append(line.replace("\n", "").rstrip())               

def partOne():
    elf_inv = []
    max_cal = 0
    for line in lines:
        if(line != ''):
           elf_inv.append(int(line))
        else:
            if max_cal < sum(elf_inv) : max_cal = sum(elf_inv)
            elf_inv = []
    print(max_cal)

def partTwo():
    elf_inv = []
    totalCalories = []
    for line in lines:
        if(line != ''):
            elf_inv.append(int(line))
        else:
            totalCalories.append(sum(elf_inv))
            elf_inv = []

    top = sorted(totalCalories)
    top = top[::-1]
    print(top[0]+top[1]+top[2])
 


if __name__ == "__main__":
    parseInput()
    partSel = input("Choose a part: (1) for Part One or (2) for Part Two\n")
    if partSel == "1":
        partOne()
    else:
        partTwo()
        
