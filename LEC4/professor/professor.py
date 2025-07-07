import random as rd

def main():
    level = get_level()
    score = get_score(10, level)
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            number = int(input("Level: "))
        except ValueError:
            pass
        else:
            if 0 < number < 4:
                return number


def generate_integer(level):
    if level == 1:
        return rd.randint(0, 9)
    elif level == 2:
        return rd.randint(10, 99)
    else:
        return rd.randint(100, 999)


def get_score(round, level):
    score = 0
    for _ in range(round):
        score += start_game(level)
    return score


def start_game(level):
    a = generate_integer(level)
    b = generate_integer(level)
    for _ in range(3):
        print(f"{a} + {b} = ", end = "")
        try:
            answer = int(input())
        except ValueError:
            print("EEE")
            pass
        else:
            if answer == a + b:
                return 1
            else:
                print("EEE")
    print(f"{a} + {b} = {a + b}")
    return 0



if __name__=="__main__":
    main()