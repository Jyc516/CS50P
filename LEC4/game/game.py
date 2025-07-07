def main():
    import random as rd

    number = get_number("Level: ")
    answer = rd.randint(1, number)
    guess_number(answer)


def get_number(string):
    while True:
        try:
            number = int(input(string))
        except ValueError:
            pass
        else:
            if number > 0:
                return number


def guess_number(answer):
    import sys
    
    while True:
        number = get_number("Guess: ")
        if number > answer:
            print("Too large!")
        elif number < answer:
            print("Too small!")
        else:
            print("Just right!")
            sys.exit()


main()
