def main():
    string = input("Input: ")
    print(shorten(string))


def shorten(word):
    new_word  =""
    for c in word:
        if c.lower() != "a" and c.lower() != "e" and c.lower() != "i" and c.lower() != "o" and c.lower() != "u":
            new_word += c
    return new_word

if __name__ == "__main__":
    main()