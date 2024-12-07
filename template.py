# day 3
import sys

def partOne(contents: list[str]):
    pass

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