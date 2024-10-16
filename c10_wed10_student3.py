# GroupName in LEB2: c10_wed10
# FileName: c10_wed10_students3.py
# member list in the file
# 041 Supakorn Ieamgomol
# 043 Somchai Wantaeng
# 050 Sirinda Charoenwai
# 051 Siriyakon Sangkaew

def ui_read_student(students_dict):
    count = 0
    while True:
        try:
            id = input("Enter id: ")
            id = int(id)
            if not isinstance(id, int):
                raise ValueError("id must be integer")
            if not str(id).startswith("67130500"):
                raise ValueError("id must start with 67130500")
            bl_check_duplicate_id(students_dict, id)
            break
        except ValueError as ve:
            count += 1
            if count == 3:
                print("You have entered wrong id 3 times.")
                if input("Do you want to continue (y/n): ").lower() == 'n':
                    print("Please try again later.")
                    exit()
            print(f"Error : {ve}")
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

def bl_check_duplicate_id(students_dict, id):
    for student in students_dict:
        if student["id"] == id:
            raise ValueError("id is duplicate")


def bl_search_stuent(students_dict, id):
    for student in students_dict:
        if student["id"] == id:
            return student
    return {}

def bl_add_student(students_dict, id, name, lastname):
    student = {
        "id": id,
        "name": name,
        "lastname": lastname
    }
    students_dict.append(student)

def main() :
    students = []
    while True:
        print(" 1. Add student \n 2. Search student \n 3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            id, name, lastname = ui_read_student(students)
            bl_add_student(students, id, name, lastname)
        elif choice == "2":
            id = int(input("Enter id: "))
            student = bl_search_stuent(students, id)
            if student:
                print(student)
            else:
                print("Student not found")
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid choice \n Please try again")
    
main()