x, y ,z = input("Expression: ").split(" ")
x = float(x)
z = float(z)
if y == "+":
    res = x + z
elif y == "-":
    res = x - z
elif y == "*":
    res = x * z
else:
    res = x / z
res = round(res, 1)
print(res)