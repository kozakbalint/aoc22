lines = []
def parseInput():
    with open("./input.txt") as f:
        for line in f:
            lines.append(line.replace("\n", "").rstrip())

def partOne():
    pairs = 0
    for line in lines:
        first = line.split(',')[0].split('-')
        second = line.split(',')[1].split('-')
        first = list(map(int, first))
        second = list(map(int, second))

        if ((int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1])) 
        or (int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]))):
            pairs += 1
    print(pairs)

def partTwo():
    pairs = 0
    for line in lines:
        first = line.split(',')[0].split('-')
        second = line.split(',')[1].split('-')
        first = list(map(int, first))
        second = list(map(int, second))

        if max(first[0],second[0]) <= min(first[1],second[1]):
            pairs += 1
    print(pairs)


if __name__ == "__main__":
    parseInput()
    partSel = input("Choose a part: (1) for Part One or (2) for Part Two\n")
    if partSel == "1":
        partOne()
    else:
        partTwo()
