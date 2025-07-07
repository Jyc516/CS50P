import sys
import csv
from tabulate import tabulate

def main():
    name = get_name()
    try:
        print_file(name)
    except FileNotFoundError:
        sys.exit("File does not exist")


def get_name():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-lines arguments")

    name = sys.argv[1].lstrip()
    if not name.endswith(".csv"):
        sys.exit("Not a CSV file")
    return name


def print_file(name):
    with open(name) as file:
        reader = csv.DictReader(file)
        table = []
        for row in reader:
            table.append(row)
        print(tabulate(table, headers="keys", tablefmt="grid"))


main()