import calculater as calc

def test_positive():
    assert calc.square(2) == 4
    assert calc.square(3) == 9


def test_negative():
    assert calc.square(-2) == 4
    assert calc.square(-3) == 9


def test_zero():
    assert calc.square(0) == 0
'''
"assert" is required to jump out of the test function when meeting an error
must start with "test_" so as to be detected by pytest
'''




# def main():
#     test_square()

# def test_square():
#     try:
#         assert calc.square(2) == 4
#     except AssertionError:
#         print("2 squared is not 4")
#     try:
#         assert calc.square(3) == 9
#     except AssertionError:
#         print("3 squared is not 9")
#     try:
#         assert calc.square(-2) == 4
#     except AssertionError:
#         print("-2 squared is not 4")
#     try:
#         assert calc.square(-3) == 9
#     except AssertionError:
#         print("-3 squared is not 9")
#     try:
#         assert calc.square(0) == 0
#     except AssertionError:
#         print("0 squared is not 0")


# if __name__ == "__main__":
#     main()
