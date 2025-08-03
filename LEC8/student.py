class Student:
    def __init__(self, name, house, patronus):
        
        self.name = name
        self.house = house
        self.patronus = patronus


    def __str__(self):
        return f"{self.name} from {self.house}"
    

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return cls(name, house, patronus)


    #getter
    @property
    def name(self):
        return self._name

    @property
    def house(self):
        return self._house
    

    #setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

        
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]:
            raise ValueError("Invalid house")
        self._house = house


    def charm(self):
        if self.patronus == "Stag":
            return "🐎"
        elif self.patronus == "Otter":
            return "🦦"
        elif self.patronus == "Jack Russell Terrier":
            return "🐕"
        else:
            return "🪄"


def main():
    # student = get_student()
    student = Student.get()
    student.house = "Number Four, Privet Drive"
    print(student)
    print("Expecto Patronum!")
    print(student.charm())


# def get_student():  
#     # student = Student()
#     # student.name = input("Name: ")
#     # student.house = input("House: ")
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus: ")
#     return Student(name, house, patronus)



# def main():
#     student = get_student()
#     if student[0] == "Padma":
#         student = (student[0], "Ravenclaw")
#     '''
#     a tuple is immutable
#     '''
#     print(f"{student[0]} from {student[1]}")
#
#
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return (name, house)


# def main():
#     student = get_student()
#     if student["name"] == "Padma":
#         student["house"] = "Ravenclaw"
#     '''
#     dict and list are mutable
#     '''
#     print(f"{student['name']} from {student['house']}")
#     '''
#     pay attention to quote
#     '''
#
#
# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student


if __name__ == "__main__":
    main()