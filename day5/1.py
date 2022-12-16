matrix =    [["Z", "P", "M", "H", "R"],
            ["P", "C", "J", "B"],
            ["S", "N", "H", "G", "L", "C", "D"],
            ["F", "T", "M", "D", "Q", "S", "R", "L"],
            ["F", "S", "P", "Q", "B", "T", "Z", "M"],
            ["T", "F", "S", "Z", "B", "G"],
            ["N", "R", "V"],
            ["P", "G", "L", "T", "D", "V", "C", "M"],
            ["W", "Q", "N", "J", "F", "M", "L"]]

nums = []

lasts = ''

def readInput():
    with open("aoc22/day5/input.txt", "r") as f:
        for lines in f:
            l = ''
            for c in lines:
                if c != '\n':
                    l += c
            l = l.split()
            for i in range(len(l)):
                if l[i].isnumeric():
                    nums.append(int(l[i]))

def move(x, origin, dest):
    tmp = ''
    origin = origin-1
    dest = dest - 1 
    for i in range(x):
        tmp = matrix[origin].pop()
        matrix[dest].append(tmp)

if __name__ == "__main__":
    readInput()
    for i in range(0,len(nums),3):
        move(nums[i],nums[i+1],nums[i+2])
    
    for j in range(len(matrix)):
        lasts += matrix[j][-1]

    print(lasts)

    
