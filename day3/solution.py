lines = []

def parseInput():
    with open("./input.txt") as f:
        for line in f:
            lines.append(line.replace("\n", "").rstrip())

def partOne():
    priorities = 0
    for line in lines:
        halfpoint = int(len(line) / 2)
        l1 = line[:halfpoint]
        l2 = line[halfpoint:]

        both = ""
        for i in range(len(l1)):
            if l1[i] in l2:
                both = l1[i]
        if both.islower():
            priorities += ord(both) - 96
        else:
            priorities += ord(both) - 38
            
    print(priorities)

def partTwo():
    priorities = 0
    chunk = []
    lineI = 0

    for line in lines:
        chunk.append(line)
        lineI += 1
        char = ''

        if lineI % 3 == 0:
            for i in range(len(chunk[0])):
                if chunk[0][i] in chunk[1] and chunk[0][i] in chunk[2]:
                    char = chunk[0][i]

            chunk = []

            if char.islower():
                priorities += (ord(char)-96)
            else:
                priorities += (ord(char)-38)

    print(priorities)


if __name__ == "__main__":
    parseInput()
    partSel = input("Choose a part: (1) for Part One or (2) for Part Two\n")
    if partSel == "1":
        partOne()
    else:
        partTwo()

