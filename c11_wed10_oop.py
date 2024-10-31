# GroupName in LEB2: c11_wed10
# FileName: c11_wed10_oop.py
# member list in the file
# 041 Supakorn Ieamgomol
# 043 Somchai Wantaeng
# 050 Sirinda Charoenwai
# 051 Siriyakon Sangkaew


class Employee:
        def __init__(self, eid, name, salary):
            self.__eid = eid
            self.__name = name
            self.__salary = salary
        
        def __repr__(self):
            return f"Employee({self.__eid}, {self.__name}, {self.__salary})"
        
        def get_eid(self):
            return self.__eid
        
        def get_name(self):
            return self.__name
        
        def get_salary(self):
            return self.__salary
        
        def set_name(self, name):
            self.__name = name
            
        def set_salary(self, salary):
            self.__salary = salary
            
        def compare_employee(self, other):
            if self.__eid < other.__eid :
                return -1
            elif self.__eid == other.__eid:
                return 0
            else:
                return 1
        
em1 = Employee(1, "Gap", 1000)
print(em1)
print(em1.get_eid())
print(em1.get_name())
print(em1.get_salary())

print("Change name and salary")
em1.set_name("Gop")
em1.set_salary(1500)
print(em1)

em2 = Employee(2, "Rew", 2000)
print(em2)
print(em1.compare_employee(em2))
