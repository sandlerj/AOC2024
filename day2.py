import sys

def main(args: list[str]):
    path = args[1]
    debug = True if len(args) == 3 and args[2] == "debug" else False
    print("source path" + path)
    with open(path) as f:
        contents = f.readlines();
    reports = [list(map(int,x.split())) for x in contents]


    dampener = True # tolerance for one bad value
    safeCount = 0
    for report in reports:
        if debug:
            print(report)
        if isSingleDirectionAndSafe(report, debug):
            if debug: print("is safe ^^")
            safeCount += 1
        else:
            if debug: print("is not safe")
            # could iterate through possible removals here, though that's not super performant lmao
            if not dampener:
                continue
            if debug: print("oops not safe, trying some options")
            for i in range(len(report)):
                if debug: print("Trying {}".format(report[0:i] + report[i:]))
                if isSingleDirectionAndSafe(report[0:i] + report[i + 1:]):
                    if debug: print("found a safe option")
                    safeCount += 1
                    break

    return safeCount
    

def isSafeDiff(a:int, b:int):
    minInc = 1
    maxInc = 3
    return minInc <= abs(a-b) <= maxInc

def isSingleDirectionAndSafe(l: list[int], debug=False):
    if len(l) < 2: return True
    if len(l) == 2: return isSafeDiff(l[0], l[1])

    asc = False
    if l[1] > l[0]:
        asc = True

    for i in range(1, len(l)):
        cur = l[i]
        prev = l[i-1]
        if isSafeDiff(cur, prev):
            if not ((asc and cur > prev) or (not asc and prev > cur)):
                if debug:
                    print("not single dir")
                return False
        else:
            return False

    return True


if __name__ == "__main__":
    print(main(sys.argv))