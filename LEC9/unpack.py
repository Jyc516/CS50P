def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

print(total(knuts=25, galleons=100, sickles=50), "Knuts")

coins: dict = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**coins), "Knuts")

coins1: list = [100, 50, 25]
print(total(*coins1), "Knuts")

coins2: tuple = (100, 50, 25)
print(total(*coins2), "Knuts")

coins3: set = {100, 50, 25}
print(total(*coins3), "Knuts")

"""
numeration stucture that preserves order support unpacking
"""


def f1(*args, **kwargs):
    print("Positional:", args)

f1(100, 50, 25)
f1(100, 50, 25, 5)

def f2(*args, **kwargs):
    print("Name:", kwargs)

f2(galleons=100, sickles=50, knuts=25)