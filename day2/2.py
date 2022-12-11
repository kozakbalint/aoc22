#Rock       A   X   L
#Paper      B   Y   D
#Scissors   C   Z   W

s = 0
with open("/Users/balintkozak/dev/python/aoc22/day2/input.txt","r") as f:
    for lines in f:
        l = ''
        
        for c in lines:
            if c != '\n':
                l += c
        match l[2]:
            case 'Y': s += 3
            case 'Z': s += 6

        match l[0]:
            case 'A': 
                if l[2] == 'X': s+=3
                elif l[2] == 'Y': s+=1
                else: s+= 2
            case 'B': 
                if l[2] == 'X': s+=1
                elif l[2] == 'Y': s+=2
                else: s+=3
            case 'C': 
                if l[2] == 'X': s+=2
                elif l[2] == 'Y': s+=3
                else: s+=1
print(s)
        
