import re

email = input("What's your email? ").strip()

if re.search(r"^[a-zA-z0-9_]+@(\w+\.)?\w+\.(edu|gov|com|org|net)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

'''
. for any character
* for 0 or more repetitions
+ for 1 or more repetitions
? for 0 or 1 repetition
{m} for m repetitions
{m,} for m or more repetitions
{m,n} for m-n repetitions
\ for escape
\d for decimal digit
\D for not decimal digit
\s for whitespace
\S for not whitespace
\w for letter character as well as decimal digit and underscore
\W for not word charater
^ matches the start of the string
$ matches the end of the string
[] for set of characters, no seperation required
[^] for complementing the set
[-] for a specific range
A|B for A or B
() for a group
(?:…) for non-capturing version
flags = re.IGNORECASE, re.MULTILINE, re.DOTALL

re.match(): search from the start of the string
re.fullmatch(): match till the end of the string
'''

# try:
#     username, domain = email.split("@")
# except ValueError:
#     print("Invalid")
# else:
#     if username and domain.endswith(".edu"):
#         print("Valid")
#     else:
#         print("Invalid")