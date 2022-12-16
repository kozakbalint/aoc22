piorities = 0
chunk = []
lineI = 0
with open("aoc22/day3/input.txt", 'r') as f:
    for lines in f:
        l = ''
        for c in lines:
            if c != '\n':
                l += c

        chunk.append(l)
        lineI += 1
        char = ''
        if lineI % 3 == 0:
            for i in range(len(chunk[0])):
                if chunk[0][i] in chunk[1] and chunk[0][i] in chunk[2]:
                    char = chunk[0][i]

            chunk = []
            print(char)
            if char.islower():
                piorities += (ord(char)-96)
            else:
                piorities += (ord(char)-38)

print(piorities)
