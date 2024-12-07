#! /usr/bin/python
import sys
from collections import Counter

def main(args: list[str]):
    path = args[1]
    print("source path" + path)
    with open(path) as f:
        content = f.readlines();
    leftL = list()
    rightL = list()
    for line in content:
        split = line.split()

        leftL.append(int(split[0]))
        rightL.append(int(split[1]))
    sortedLeft = sorted(leftL)
    sortedRight = sorted(rightL)
    total = 0
    for i in range(len(content)):
        total += abs(sortedLeft[i] - sortedRight[i])
    
    print("Total diff: {}".format(total))

    # not using counter i guess
    rightCounter = dict()
    for number in rightL:
        if number in rightCounter:
            rightCounter[number] += 1
        else:
            rightCounter[number] = 1
    
    similarityScore = 0
    for n in leftL:
        val = rightCounter.get(n)
        similarityScore += n * (0 if val == None else val)
    
    print("Sim score: {}".format(similarityScore))



if __name__ == "__main__":
    main(sys.argv)