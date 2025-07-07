def main():
    x = get_fraction()
    check_fraction(x)


def get_fraction():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)
            return float(x / y)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def check_fraction(x):
    if x > 1:
        main()
    elif x >= 0.99:
        print("F")
    elif x > 0.01:
        print(f"{int(round(x, 2) * 100)}%")
    else:
        print("E")


main()