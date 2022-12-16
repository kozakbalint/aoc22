pairs = 0

with open("aoc22/day4/input.txt", "r") as f:
    for lines in f:
        l = ''
        for c in lines:
            if c != '\n':
                l += c

        first = l.split(',')[0].split('-')
        second = l.split(',')[1].split('-')
        if ((int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1])) or (int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]))):
            pairs += 1


print(pairs)