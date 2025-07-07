import sys
import csv

def main():
    input, output = get_name()
    try:
        print_file(input, output)
    except FileNotFoundError:
        sys.exit("Could not read", input)


def get_name():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-lines arguments")

    input = sys.argv[1].lstrip()
    if not input.endswith(".csv"):
        sys.exit("Not a CSV file")
    output = sys.argv[2].lstrip()
    if not output.endswith(".csv"):
        sys.exit("Not a CSV file")
    return input, output


def print_file(input, output):
    with open(input) as file_i, open(output, "w", newline="") as file_o:
        reader = csv.DictReader(file_i)
        writer = csv.DictWriter(file_o, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader:
            last, first = row["name"].split(',')
            writer.writerow({"first": first.strip(), "last": last.strip(), "house": row["house"]})


main()