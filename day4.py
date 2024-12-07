# day 4
import sys

def wordInDirection(L: list[str], word: str, y: int, x: int, dy: int, dx: int) -> bool:
    for i in range(len(word)):
        # calc position based on i and dydx/xy
        y0 = y + dy * i
        x0 = x + dx * i
        # if out of bounds, that's a nope
        if not(0 <= y0 < len(L) and 0 <= x0 < len(L[y0])):
            return False
        
        if (L[y0][x0].lower() != word[i].lower()):
            return False
        
    return True


def partOne(L: list[str]):
    total = 0

    word = "XMAS"

    # headass behavior to gen list and  prevent dupes or 0,0 because I'm feeling goofy
    directionsDyDx = {(x,y) if not(x == 0 and y == 0) else (1,1) for x in [-1,0,1] for y in [-1,0,1]} 

    for y in range(len(L)):
        for x in range(len(L[y])):
            if L[y][x].lower() == word[0].lower():
                # Maybe a potential match! Check all directions
                for (dy,dx) in directionsDyDx:
                   if wordInDirection(L, word, y, x, dy, dx) :
                       total += 1
    return total

def isXMas(L : list[str], x: int, y: int) -> bool:
    if L[y][x].lower() != "A".lower(): 
        return False

    if (x == 0 or y == 0 or y >= len(L) - 1 or x == len(L[y]) - 1):
        return False # on the edge, could not be X Mas
    
    directionsDyDx = [(1,1), (1,-1)]
    MasCount = 0
    for dy,dx in directionsDyDx:
        y0 = y + dy
        x0 = x + dx
        y1 = y - dy
        x1 = x - dx
        L0 = L[y0][x0].lower()
        L1 = L[y1][x1].lower()
        if ((L0 == "M".lower() and L1 == "S".lower())
            or (L0 == "S".lower() and L1 == "M".lower())):
            MasCount += 1
    
    if MasCount == 2:
        return True
    
    return False


def partTwo(L: list[str]):
    total = 0

    for y in range(len(L)):
        for x in range(len(L[y])):
            if L[y][x].lower() == "A".lower() and isXMas(L, x, y):
                total += 1
                
    return total


def main(args: list[str]):
    path = args[1]
    debug = True if len(args) == 3 and args[2] == "debug" else False
    print("source path" + path)
    with open(path) as f:
        contents = f.readlines();

    result1 = partOne(contents)
    print("Result 1: {0}".format(result1))
    result2 = partTwo(contents)
    print("Result 2: {0}".format(result2))
    

if __name__ == "__main__":
    main(sys.argv)