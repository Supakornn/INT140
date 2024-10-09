# GroupName in LEB2: c08_wed05
# FileName: c08_wed05_students.py
# member list in the file
# 041 Supakorn Ieamgomol
# 043 Somchai Wantaeng
# 050 Sirinda Charoenwai
# 051 Siriyakon Sangkaew

def student_data(all: list, id: int, name: str, lastname: str):    
    student_info = [id, name, lastname]
    all.append(student_info)

def read_one_member(all: list):
    while True:
        try:
            while True:
                try:
                    id = int(input("Enter id: "))
                    if not str(id).startswith("67130500"):
                        raise ValueError("id must start with 67130500")
                    break
                except ValueError as ve:
                    print(f"Invalid id: {ve}")
                    print("Please try again.")
            
            while True:
                try:
                    name = input("Enter name: ")
                    if not name.isalpha():
                        raise ValueError("Name must be string")
                    break
                except ValueError as ve:
                    print(f"Invalid name: {ve}")
                    print("Please try again.")
            
            while True:
                try:
                    lastname = input("Enter lastname: ")
                    if not lastname.isalpha():
                        raise ValueError("Lastname must be string")
                    break
                except ValueError as ve:
                    print(f"Invalid lastname: {ve}")
                    print("Please try again.")
            
            student_data(all, id, name, lastname)
            break
        except (ValueError, TypeError) as e:
            print(f"Invalid input: {e}")
            print("Please try again.")

def main():
    students = []
    while True:
        read_one_member(students)
        if input("Do you want to add more student (y/n): ").lower() == 'n':
            break
    print(students)

main()