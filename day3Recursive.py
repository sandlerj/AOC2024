# day 3
"""
Self imposed constraints:
- No Regex:
    re can be pretty costly performance-wise if not done right.
    I haven't run this in comparison to an RE solution bc I didn't write one and don't wanna snipe someone elses.
    I don't know how to write performant re and at this point I'm afraid to ask, and I haven't found a scenario
    IRL at work or in leetcode BS where regex was actually a better option for me personally than using whatever
    optimized string searching a framework already provided.
        Plus we aren't back tracking here so this is basically O(n) (I think, don't quote me)
- No for loops:
    Sometimes, it's okay to be a tryhard who doesen't get to use python or recursion at her day job. (read: I don't
    go out of my way to do recursion and it doesn't really come up except for like, one file abstraction lib I 
    may or may not have worked on).
"""
import sys

def canParseInt(s:str):
    try:
        int(s)
        return True
    except:
        return False


def partsGood(line:str, startToken: str, end: int):
    start = line.find(startToken) 
    if start == -1: return 0
    parts = line[start + len(startToken) : end].split(',')
    if len(parts) == 2 and all(1 <= len(part) <= 3 and canParseInt(part) \
                                   and part.isdigit() for part in parts):
        return int(parts[0]) * int(parts[1])
    else:
        return 0



def calculateMult(line: str) -> int:
    tokenStart = "mul("
    end = ')'
    longAdditional = len("xxx,yyy" + end)
    shortAdditional = len("x,y" + end)

    if len(line) < len(tokenStart) + shortAdditional:
        return 0
    
    if line.startswith(tokenStart) \
    and len(tokenStart) + shortAdditional - 1 <= line.find(end) < len(tokenStart) + longAdditional:
        return partsGood(line, tokenStart, line.find(end)) + calculateMult(line[line.find(end) + 1:])
    
    # Jump ahead? If we go char by char we'll get stack overflow
    nextStart = line.find(tokenStart, 1)
    return calculateMult(line[nextStart:])
    

def redactDont(s: str, enabled = True):
    dont = "don't()"
    do = "do()"
    
    if len(s) <= 1:
         return s if enabled else ""
    if not enabled:
        doI = s.find(do)
        if doI == -1: 
            # never enabled again
            return ""
        else:
            # activated again starting at doI
            return redactDont(s[doI + len(do):], True)
    else: #enabled
        dontI = s.find(dont)
        if dontI == -1:
            # not disabled again
            return s
        else:
            return s[:dontI] + redactDont(s[dontI + len(dont):], False)

def partOne(contents: list[str]):
    # No regex you nerd

    lines = " ".join(contents)
    contents = redactDont(lines).split(" ")

    def getVal(L : list[str]):
        if len(L) == 0:
            return 0
        return calculateMult(L[0]) + getVal(L[1:])
    
    return getVal(contents)



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
