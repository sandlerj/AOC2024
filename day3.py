# day 3 NO PART TWO

# I didn't actually want to do this with for loops but just to make sure I understand....
import sys

def canParseInt(s:str):
    try:
        int(s)
        return True
    except:
        return False

def partOne(contents: list[str]):
    tokenStart = "mul("
    maxIntChars = 3
    minimumAddtlChars = len("x,y)")
    maxAddtlChars = len("xxx,yyy)")
    total = 0

    dont = "don't()"
    do = "do()"
    enabled = True

    for line in contents:
        while 0 < len(line):
            tokenI = line.find(tokenStart)
            if -1 != tokenI and tokenI + len(tokenStart) + minimumAddtlChars <= len(line):
                # found the mul( token
                # not at the very end yet, we have at least enough chars for the nums, could be!
                line = line[tokenI:]
                tokenI = 0
                closeParenI = line.find(')')
                diff = closeParenI - tokenI
                if closeParenI != -1:
                    # paren closes somewhere in line!
                    if len(tokenStart) + minimumAddtlChars - 1 <= diff < len(tokenStart)+ maxAddtlChars:
                        # space between parans isn't too long or short
                        parts = line[tokenI + len(tokenStart) : closeParenI].split(',')
                        if len(parts) == 2 and all(1 <= len(part) <= 3 and canParseInt(part) and part.isdigit() for part in parts):
                            # two parts in between, both are between 1 and 3 chars long, and can parse to int so we're good!
                            total += int(parts[0]) * int(parts[1])
                    line = line[1:]
                else:
                    
                    line = line[:len(line)]
            else:
                break

    return total



def main(args: list[str]):
    path = args[1]
    debug = True if len(args) == 3 and args[2] == "debug" else False
    print("source path" + path)
    with open(path) as f:
        contents = f.readlines();

    result1 = partOne(contents)
    print("Result 1: {0}".format(result1))
    

if __name__ == "__main__":
    main(sys.argv)
