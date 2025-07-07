def flip_coin():
    from random import choice

    coin = choice(["head", "tail"])
    ## random.choice() get a random result from the list

    print(coin)


def guess_number():
    import random

    number = random.randint(1, 10)
    ## random.randint(a, b) get a number from a to b inclusively

    print(number)


def shuffle_card():
    import random

    cards = ["jack", "queen", "king"]
    random.shuffle(cards)
    for card in cards:
        print(card)


shuffle_card()
