import re


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    if s == "um":
        return 1
    matches = re.findall(r"((?:^um[^a-zA-z])|(?:[^a-zA-z])um(?:[^a-zA-z])|(?:[^a-zA-z]um$))", s)
    return len(matches)


if __name__ == "__main__":
    main()