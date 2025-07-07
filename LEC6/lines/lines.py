import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

name = sys.argv[1].lstrip()

if not name.endswith('.py'):
    sys.exit("Not a Python file")

try:
    with open(name) as file:
        count = 0
        for line in file:
            line = line.lstrip()
            if line == "" or line.startswith("#"):
                continue
            else:
                count += 1
        print(count)
except FileNotFoundError:
    sys.exit("File does not exist")