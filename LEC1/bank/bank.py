def main():
    greeting = input("Greeting: ").strip().lower()
    money = check(greeting)
    print(money)


def check(string):
    model = "hello"
    if len(string) == 0:
        return 100
    elif string[0] != 'h':
        return 100
    else:
        for i in range(5):
            if i == len(string) or string[i] != model[i]:
                return 20
        return 0
    

main()