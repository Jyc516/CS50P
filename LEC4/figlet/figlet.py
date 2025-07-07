import sys
import random as rd
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font=rd.choice(fonts))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    if sys.argv[2] in fonts:
        figlet.setFont(font = sys.argv[2])
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

string = input("Input: ")
print(figlet.renderText(string))
