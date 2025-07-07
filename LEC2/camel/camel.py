string = input("camelCase: ")
for c in string:
    if "A" <= c <= "Z":
        print("_", c.lower(), sep = "", end = "")
    else:
        print(c, end = "")
print()