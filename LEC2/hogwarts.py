# students  = ["Hermione", "Harry", "Ron"]

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])


def lists():
    Gryffindor = ["Hermione", "Harry", "Ron"]
    Slytherin = ["Malfoy"]
    Ravenclaw = []
    Hufflepuff = []
    students = [Gryffindor, Slytherin, Ravenclaw, Hufflepuff]
    for i in range(len(students)):
        for j in range(len(students[i])):
            print(students[i][j])


def dictionary():
    students = {
        "Hermione": "Gryffindor",
        "Harry": "Gryffindor",
        "Ron": "Gryffindor",
        "Draco": "Slytherin"
    }

    for student in students:
        print(student, students[student], sep = ", ")


def mix():
    students = [
        {"Name": "Hermione", "House": "Gryffindor", "Patronus": "Otter"},
        {"Name": "Harry", "House": "Gryffindor", "Patronus": "Stag"},
        {"Name": "Ron", "House": "Gryffindor", "Patronus": "Jack Russel Terrier"},
        {"Name": "Draco", "House": "Slytherin", "Patronus": None}
    ]

    for student in students:
        print(student["Name"], student["House"], student["Patronus"], sep = ", ")