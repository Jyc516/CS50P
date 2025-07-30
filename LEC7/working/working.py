import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")


def convert(s):
    if matches := re.search(r"^(\d{1,2}):?(\d\d)? (AM|PM) to (\d{1,2}):?(\d\d)? (AM|PM)$", s):
        time1 = checktime(matches.group(1), matches.group(2), matches.group(3))
        time2 = checktime(matches.group(4), matches.group(5), matches.group(6))
        return time1 + " to " + time2
    else:
        raise ValueError


def checktime(hh, mm, dd):
    hh = int(hh)
    if hh == 0 or hh > 12:
        raise ValueError
    elif hh == 12:
        hh = 0
    if not mm == None:
        min = int(mm)
        if min > 59:
            raise ValueError
    else:
        mm = "00"
    time = ""
    if dd == "PM":
        hh += 12
    elif hh < 10:
        time += "0"
    time = time + str(hh) + ":" + mm
    return time


if __name__ == "__main__":
    main()
