import sys
import cowsay as cs

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    '''
    get a slice from the second element to the end
    [1:-1] get a slice from the second element to the second to last
    '''
    print(f"Hello, my name is {arg}")
    cs.cow(f"Hello, {arg}")