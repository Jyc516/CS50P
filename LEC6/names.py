# names = []

# for _ in range(3):
#     name = input("What's your name? ")
#     names.append(name)

# for name in sorted(names):
#     print(f"Hello, {name}")


name = input("what's your name? ")

# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

## by using with, file can be automatically closed after being written
## "w" for write (and rewrite everytime the program runs)
## "a" for append
## "r" for read can be omitted as an implicit default

names = []

with open("names.txt") as file:
#     lines = file.readlines()

# for line in lines:
#     print("Hello,", line.rstrip())

    for line in file:
        names.append(line.rstrip())

    for name in sorted(names, reverse = False):
        print("Hello,", name)