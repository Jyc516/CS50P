import sys
import requests

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=ca74f3d07b81388c99e00fd512c4a1126144ff9d696f603025aa6c840a0ae85a")
except requests.RequestException:
    sys.exit()
o = response.json()

price = n * float(o["data"]["priceUsd"])

print(f"${price:,.4f}")