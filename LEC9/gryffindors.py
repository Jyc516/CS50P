students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]


for i, student in enumerate(sorted(students, key=lambda s: s["house"])):
    print(i + 1, student["name"])


def comprehension():
    gryffindors = [
        student["name"] for student in students if student["house"] == "Gryffindor"
    ]

    gryffindict = {
        student["name"]: "Gryffindor" for student in students if student["house"] == "Gryffindor"
    }


def is_gryffindor(s):
    if s["house"] == "Gryffindor":
        return True
    else: return False


gryffindors = filter(is_gryffindor, students)
"""
gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

the lambda-expr version
"""


for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])