import csv
## csv can help fix corner cases

def write_data():
    name = input("What's your name? ")
    home = input("What's your home? ")
    house = input("What's your house? ")

    with open("students.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["house", "name", "home"])
        # writer.writerow({"house": "house", "name": "name", "home": "home"})
        '''
        commentized simply for not appending headers over and again
        '''
        writer.writerow({"house": house, "name": name, "home": home})


def read_data():
    students = []

    with open("students.csv") as file:
        # reader = csv.reader(file)
        # for name, house in reader:
        #     # student = {}
        #     # student["name"] = row[0]
        #     # student["house"] = row[1]
        #     student = {"name": name, "house": house}
        #     students.append(student)

        reader = csv.DictReader(file)
        for row in reader:
            # students.append({"name": row["name"], "house": row["house"], "home": row["home"]})
            students.append(row)
        '''
        DictReader return dictionary once at a time, with the first row of .csv being the key
        '''

    # def get_name(student):
    #     return student["name"]


    # for student in sorted(students, key = get_name):
    #     print(f"{student['name']} is in {student['house']}")

    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} in {student['house']} is from {student['home']}")

    '''
    a lambda expression is an anonymous function
    '''

write_data()