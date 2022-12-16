a = []
depth = 0
separator = ' '
sums = []
with open("aoc22/day7/test.txt", "r") as f:
    for lines in f:
        l = ''
        for c in lines:
            if c != '\n':
                l += c
        a.append(l)

for i in range(len(a)):
    parts = a[i].split()
    if parts[0] == '$':
        if parts[1] == 'cd':
            if parts[2] == '..':
                depth -= 1
            else:
                depth += 1
                print(f"{depth*separator} {parts[2]}")
    else:
        print(f"{depth*separator}- {parts[1]} {parts[0]}")

    