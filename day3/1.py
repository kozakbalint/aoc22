piorities = 0
with open("/Users/balintkozak/dev/python/aoc22/day3/input.txt", 'r') as f:
    for lines in f:
        l = ''
        for c in lines:
            if c != '\n':
                l += c
        halfpoint = int(len(l) / 2)
        l1 = l[:halfpoint]
        l2 = l[halfpoint:]
        
        both = ''
        for i in range(len(l1)):
            if l1[i] in l2:
                both = l1[i]
        if both.islower():
            piorities += (ord(both)-96)
        else:
            piorities += (ord(both)-38)

print(piorities)