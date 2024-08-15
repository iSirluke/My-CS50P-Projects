import sys

def main():
    check_arg()
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()

    except FileNotFoundError:
        sys.exit("File does not exist")

    numberOfLines = 0
    for line in lines:
        if check_lines(line) == False:
            numberOfLines += 1
    print(numberOfLines)

def check_arg():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a python file")

def check_lines(line):
    if line.lstrip() == "":
        return True
    if line.lstrip().startswith("#"):
        return True
    return False

if __name__ == "__main__":
    main()


