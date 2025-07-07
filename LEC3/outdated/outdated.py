months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    outdate = input("Date: ").strip()
    try:
        mm, dd, yyyy = outdate.split("/")
    except ValueError:
        try:
            mm, dd, yyyy = outdate.split(" ")
        except ValueError:
            pass
        else:
            try:
                mm = months[mm]
            except KeyError:
                pass
            else:
                try:
                    if dd == dd.removesuffix(','):
                        continue
                    dd = int(dd.removesuffix(','))
                except ValueError:
                    pass
                else:
                    if 0 < mm < 13 and 0 < dd < 31:
                        break
    else:
        try:
            mm = int(mm)
            dd = int(dd)
        except:
            pass
        else:
            if 0 < mm < 13 and 0 < dd < 31:
                break

print(f"{yyyy}-{mm:02}-{dd:02}") 