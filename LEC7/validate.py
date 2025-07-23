email = input("What's your email? ").strip()

try:
    username, domain = email.split("@")
except ValueError:
    print("Invalid")
else:
    if username and domain.endswith(".edu"):
        print("Valid")
    else:
        print("Invalid")