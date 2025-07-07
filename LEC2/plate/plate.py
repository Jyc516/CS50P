def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False
    for i in range(2):
        if not "A" <= s[i] <= "Z":
            return False
    flag = False
    while(i < len(s)):
        if flag:
            if not "0" <= s[i] <= "9":
                return False
        elif "1" <= s[i] <= "9":
            flag = True
        elif not "A" <= s[i] <= "Z":
            return False
        i += 1
    return True


main()