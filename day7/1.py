lines = []

def parseInput():
    with open("./test.txt") as f:
        for line in f:
            l = ''
            for c in line:
                if c != '\n':
                    l += c
            lines.append(l)

def partOne():





if __name__ == "__main__":
    parseInput()
