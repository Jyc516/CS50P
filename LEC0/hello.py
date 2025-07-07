def main():
    # Get user's name and capitalize it
    name = input("What's your name? ").title().strip()
    ## title() turn first letters of every word into capitalization
    ## strip() delete all the whitespace in the beginning and at the end of a string
    ## upper() lower()

    # Print user's name
    hello(name)
    hello()


def hello(to = "world"):
    print(f"Hello, {to}")

main()