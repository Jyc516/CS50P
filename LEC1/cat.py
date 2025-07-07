def zoo():
    i = 3
    while i != 0:
        print("Meow")
        i -= 1

    for j in [6, 2, 7]:
        print("Wulf")

    for _ in range(3):      #start from 0 and up to, not through 3
        print("Oink")

    print("Crack\n" * 3, end = "")


def main():
    number = get_number()
    cat(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


def cat(n):
    for _ in range(n):
        for _ in range(_):
            print("Meow")


main()