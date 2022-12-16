#Rock       A   X
#Paper      B   Y
#Scissors   C   Z

s = 0
with open("aoc22/day2/input.txt", "r") as f:
    for lines in f:
        l = ''
        
        for c in lines:
            if c != '\n':
                l += c
        match l[2]:
            case 'X': s += 1
            case 'Y': s += 2
            case 'Z': s += 3

        match l[0]:
            case 'A': 
                if l[2] == 'X': s+=3
                elif l[2] == 'Y': s+=6
            case 'B': 
                if l[2] == 'Y': s+=3
                elif l[2] == 'Z': s+=6
            case 'C': 
                if l[2] == 'Z': s+=3
                elif l[2] == 'X': s+=6
print(s)
        
