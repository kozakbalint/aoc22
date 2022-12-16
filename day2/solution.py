lines = []

def parseInput():
    with open("./input.txt") as f:
        for line in f:
            lines.append(line.replace("\n", "").rstrip())

def partOne():
    s = 0
    for line in lines:
        match line[2]:
            case 'X': s += 1
            case 'Y': s += 2
            case 'Z': s += 3
        match line[0]:
            case 'A': 
                if line[2] == 'X': s+=3
                elif line[2] == 'Y': s+=6
            case 'B': 
                if line[2] == 'Y': s+=3
                elif line[2] == 'Z': s+=6
            case 'C': 
                if line[2] == 'Z': s+=3
                elif line[2] == 'X': s+=6
    print(s)

def partTwo():
    s = 0
    for line in lines:
        match line[2]:
            case 'Y': s += 3
            case 'Z': s += 6

        match line[0]:
            case 'A': 
                if line[2] == 'X': s+=3
                elif line[2] == 'Y': s+=1
                else: s+= 2
            case 'B': 
                if line[2] == 'X': s+=1
                elif line[2] == 'Y': s+=2
                else: s+=3
            case 'C': 
                if line[2] == 'X': s+=2
                elif line[2] == 'Y': s+=3
                else: s+=1
    print(s)

if __name__ == "__main__":
    parseInput()
    partSel = input("Choose a part: (1) for Part One or (2) for Part Two\n")
    if partSel == "1":
        partOne()
    else:
        partTwo()
     

