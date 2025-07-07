def main():
    while True:
        try:
            percentage = convert(input("Fraction: "))
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break

    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x < 0:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise  ValueError
    else:
        return int(round(x / y * 100, 0))
    

def gauge(percentage):
    if percentage > 98:
        return "F"
    elif percentage < 2:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()