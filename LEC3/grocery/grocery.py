items = {}

while True:
    try:
        item = input().capitalize()
    except EOFError:
        break
    else:
        if item in items:
            items[item] += 1
        else:
            items.setdefault(item, 1)

d = sorted(items)

for i in range(len(d)):
    print(f"{items[d[i]]} {d[i]}")
