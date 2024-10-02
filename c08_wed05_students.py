# GroupName in LEB2: c08_wed05
# FileName: c08_wed05_students.py
# member list in the file
# 041 Supakorn Ieamgomol
# 043 Somchai Wantaeng
# 050 Sirinda Charoenwai
# 051 Siriyakon Sangkaew

def student_data(all: list, id: int, name: str, lastname: str):
    # build a list of (id, name, lastname)
    # append this list to all
    if not isinstance(id, int):
        raise TypeError("id must be an integer")
    if not isinstance(name, str) or any(char.isdigit() for char in name):
        raise TypeError("name must be a string")
    if not isinstance(lastname, str) or any(char.isdigit() for char in name):
        raise TypeError("lastname must be a string")
    
    id_str = str(id)
    if not id_str.startswith("67130500"):
        raise ValueError("Invalid ID")
    
    student_info = [id, name, lastname]
    all.append(student_info)

def read_one_member(all: list):
    while True:
        try:
            # read id, name, lastname from user input
            id = int(input("Enter id: "))
            name = input("Enter name: ")
            lastname = input("Enter lastname: ")
            student_data(all, id, name, lastname)
            break 
        except (TypeError, ValueError) as e:
            print(f"Error: {e}. Please try again.")

def main():
    students = []
    # loop until all members are read
    while True:
        read_one_member(students)
        if input("Do you want to add more student (y/n): ").lower() == 'n':
            break
    print(students)

main()