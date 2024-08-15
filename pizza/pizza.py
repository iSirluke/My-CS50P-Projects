# Expects one command-line argument
# Has a name ending with .csv
# File in Pinocchio format must output in ASCII art
# Table to be formatted using grid format
# Check c-largv

from tabulate import tabulate
import sys
import csv

def main():
    check_argv()
    tableArt = []
    try:
        with open(sys.argv[1], "r") as csvf:
            reader = csv.reader(csvf)
            for row in reader:
                tableArt.append(row)

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(tableArt[1:], headers=tableArt[0], tablefmt="grid"))

def check_argv():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
