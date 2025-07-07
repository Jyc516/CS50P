def main():
    indoor = input("What's your input? ")
    indoor = lowercase(indoor)
    print(f"{indoor}")


def lowercase(string):
    return string.lower()


main()