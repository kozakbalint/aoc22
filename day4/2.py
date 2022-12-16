pairs = 0

with open("aoc22/day4/input.txt", "r") as f:
    for lines in f:
        l = ''
        for c in lines:
            if c != '\n':
                l += c

        first = l.split(',')[0].split('-')
        second = l.split(',')[1].split('-')
        first = list(map(int, first))
        second = list(map(int, second))

        #find single sections
        if max(first[0],second[0]) <= min(first[1],second[1]):
            pairs += 1


print(pairs)