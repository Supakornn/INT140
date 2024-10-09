# GroupName in LEB2: c09_wed05
# FileName: c09_wed05_students2.py
# member list in the file
# 041 Supakorn Ieamgomol
# 043 Somchai Wantaeng
# 050 Sirinda Charoenwai
# 051 Siriyakon Sangkaew

def read_one_student():
    count = 0
    while True:
        try:
            id = int(input("Enter id: "))
            if not str(id).startswith("67130500"):
                raise ValueError("id must start with 67130500")
            break
        except ValueError as ve:
            count += 1
            if count == 3:
                print("You have entered wrong id 3 times.")
                if input("Do you want to continue (y/n): ").lower() == 'n':
                    print("Please try again later.")
                    exit()
            print("Id must be Integer")
            print("Please try again.")

    while True:
        try:
            name = input("Enter name: ")
            if not name.isalpha():
                raise ValueError("Name must be string")
            break
        except ValueError as ve:
            count += 1
            if count == 3:
                print("You have entered wrong id 3 times.")
                if input("Do you want to continue (y/n): ").lower() == 'n':
                    print("Please try again later.")
                    exit()
            print(f"Invalid name: {ve}")
            print("Please try again.")

    while True:
        try:
            lastname = input("Enter lastname: ")
            if not lastname.isalpha():
                raise ValueError("Lastname must be string")
            break
        except ValueError as ve:
            count += 1
            if count == 3:
                print("You have entered wrong id 3 times.")
                if input("Do you want to continue (y/n): ").lower() == 'n':
                    print("Please try again later.")
                    exit()
            print(f"Invalid lastname: {ve}")
            print("Please try again.")

    return id, name, lastname


def add_student_to_dict(students_dict, id, name, lastname):
    student = {
        "id": id,
        "name": name,
        "lastname": lastname
    }
    students_dict.append(student)


def add_student_to_lists(student_lists, id, name, lastname):
    student_lists["ids"].append(id)
    student_lists["names"].append(name)
    student_lists["lastnames"].append(lastname)


def print_student_from_dict(student_dict):
    for student in student_dict:
        print(student)


def print_student_from_lists(student_lists):
    for id, name, lastname in zip(student_lists["ids"], student_lists["names"], student_lists["lastnames"]):
        print({"id": id, "name": name, "lastname": lastname})


def main():
    students_dict = []
    students_lists = {"ids": [], "names": [], "lastnames": []}

    while True:
        if input("Do you want to add student (y/n): ").lower() == 'y':
            id, name, lastname = read_one_student()
            add_student_to_dict(students_dict, id, name, lastname)
            add_student_to_lists(students_lists, id, name, lastname)
        else:
            print_student_from_dict(students_dict)
            print_student_from_lists(students_lists)
            break


main()
