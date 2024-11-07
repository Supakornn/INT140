# group id: c12_wed10
# filename: c12_wed10_student_class.py
# 041 Supakorn Ieamgomol
# 043 Somchai Wantaeng
# 050 Sirinda Charoenwai
# 051 Siriyakon Sangkaew

class Ui:
    def __init__(self):
        self.__bl = _Bl()
        
    def main_menu(self):
        while True:
            print("\nStudent Information System")
            print("  [1] Add a student into the database.")
            print("  [2] Search for a student by id.")
            print("  [3] List all students.")
            result = input("  Choose one [1|2|3] or anything else to exit: ")
            try:
                match int(result):
                    case 1: self.add_student()
                    case 2: self.search_student()
                    case 3: self.list_students()
                    case _: break
            except:
                break
        print("\nExit program normally.")
        
    def add_student(self):
        print("Adding a student into the database:")
        try:
            sid = self.__input_new_student_id()
            firstname = self.__input_student_name("firstname")
            lastname = self.__input_student_name("lastname")
            self.__bl.add_student(sid, firstname, lastname)
            print(f"Student[{sid}: {firstname} {lastname}] is added into the database successfully.")
        except ValueError:
            print("  -- No student is added --")
    
    def __input_student_id(self):
        while True:
            value = input("  Please type a valid student id and press Enter\n"
                        "  (or just press Enter to abort): ")
            if value == "":
                raise ValueError
            sid = self.__bl.transform_to_sid(value)
            if sid is not None:
                return sid
            print("  invalid student id format")
        
    def __input_new_student_id(self):
        while True:
            sid = self.__input_student_id()
            if self.__bl.get_student(sid) is None:
                return sid
            print("  this student id has already existed")
    
    def __input_student_name(self, name: str):
        while True:
            value = input(f"  Please type the student {name} and press Enter\n"
                        "  (or just press Enter to abort): ")
            if value == "":
                raise ValueError
            if self.__bl.validate_name(value):
                return value
            print("  invalid student name format (whitespace is not allowed)")

    
    def search_student(self):
        print("Searching for a student by student id:")
        try:
            sid = self.__input_student_id()
            name = self.__bl.get_student(sid)
            if name is None:
                print("  student not found")
            else:
                print(f"  student id: {sid}, firstname: {name[0]}, lastname: {name[1]}")
        except ValueError:
            print("  -- No student to be searched --")
    
    def list_students(self):
        sids = self.__bl.get_all_student_ids()
        if len(sids) == 0:
            print("  -- No students in the database. --")
        for sid in sids:
            firstname, lastname = self.__bl.get_student(sid)
            print(f"  student id: {sid}, firstname: {firstname}, lastname: {lastname}")
        

class _Bl:
    def __init__(self):
        self.__db = self.__create_student_db()
        
    def __create_student_db(self):
        return {}
    
    def transform_to_sid(self, sid: int | str) -> int | None:
        try:
            value = int(sid)
            if 6713050000 <= value <= 67130509999:
                return value
        except:
            return None
    
    def validate_name(self, name: str) -> bool:
        if type(name) is not str or ' ' in name or '\t' in name or '\n' in name:
            return False
        return True
    
    def add_student(self, sid: int, firstname: str, lastname: str) -> None:
        self.__db[sid] = firstname, lastname
    
    def get_student(self, sid: int) -> tuple[str,str] | None:
        return self.__db.get(sid)
    
    def get_all_student_ids(self) -> list[int]:
        return list(self.__db.keys())
        

def main():
    ui = Ui()
    ui.main_menu()

if __name__ == "__main__":
    main()
