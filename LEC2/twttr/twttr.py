string = input("Input: ")
for c in string:
    flag = True
    for _ in ['a', 'e', 'i', 'o', 'u']:
        if c.lower() == _:
            flag = False
            break
    if flag:
        print(c, end = "")
