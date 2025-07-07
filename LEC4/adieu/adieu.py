import sys
from inflect import engine

p = engine()
names = []

while True:
    try:
        name = input("Name: ")
    except EOFError:
        break
    else:
        names.append(name)


print("Adieu, adieu, to " + p.join(names))