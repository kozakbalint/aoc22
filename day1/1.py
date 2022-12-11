caloriesEach = []
max = 0
with open("/Users/balintkozak/dev/python/aoc22/day1/input.txt","r") as f:
    for line in f:
        l  = ''
        for c in line:
            if c != '\n':
                l += c
        if(l != ''):
            caloriesEach.append(int(l))
        else:
            if max < sum(caloriesEach) : max = caloriesEach
            caloriesEach = []

print(max)
        


        
