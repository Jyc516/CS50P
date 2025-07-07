due = 50
while due > 0:
    print(f"Amount Due: {due}")
    coin = int(input("Insert Coin: "))
    for _ in [25, 10, 5]:
        if coin == _:
            due -= coin
print(f"Change Owed: {0 - due}")