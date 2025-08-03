import datetime
import re
import sys
import inflect

p = inflect.engine()


def main():
    birth = get(input("Date of birth: "))
    print(output(datetime.date.today() - birth))


def get(s):
    if matches := re.search(r"(\d{4})-(\d{2})-(\d{2})", s):
        yyyy, mm, dd = matches.groups()
        return datetime.date(int(yyyy), int(mm), int(dd))
    else:
        sys.exit("Invalid date")


def output(delta):
    number = p.number_to_words(delta.days * 24 * 60, wantlist=True)
    if len(number) == 1:
        return number[0].capitalize().replace(" and", "") + " minutes"
    else:
        string = number[0].capitalize().replace(" and", "") + ","
        for _ in range(1, len(number)):
            string = string +  " " + number[_].replace(" and", "")
        return string + " minutes"

if __name__ == "__main__":
    main()