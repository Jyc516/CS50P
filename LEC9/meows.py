import argparse


def meow(n: int) -> str:
    """
    Meow n times

    :param n: number of times to meow
    :type n: int
    :raise TypeError: if n is not an int
    :return: a string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n


parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="numbers of time to meow", type=int)
args = parser.parse_args()


number: int = int(args.n)
meows: str = meow(number)
print(meows, end="")
"""
use "mypy meows.py" to test type conpatibility
"""



# class Cat:
#     MEOWS = 3


#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("meow")


# cat = Cat()
# cat.meow()