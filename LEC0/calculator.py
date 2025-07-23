def main():
    x = float(input("What's x? "))
    y = float(input("what's y? "))
    z = round(square(x + y), 2)
    '''
    round()四舍五入
    '''

    print(f"({x} + {y}) ** 2 = {z:,.2f}")



def square(n):
    return n ** 2


main()