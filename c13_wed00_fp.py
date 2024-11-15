
"""
group id: c13_wed00
file: c13_wed00_fp.py
deadline: sun 17 nov before midnight (23:59)
# 041 Supakorn Ieamgomol
# 043 Somchai Wantaeng
# 050 Sirinda Charoenwai
# 051 Siriyakon Sangkaew 
"""

class Employees:
    def __init__(self, eid, name, salary):
        self.eid = eid
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.salary
    
    def getEid(self):
        return self.eid
    
    def getName(self):
        return self.name
    
    def setEid(self, eid):
        self.eid = eid
    
    def setName(self, name):
        self.name = name
    
    def setSalary(self, salary):
        self.salary = salary

    def __repr__(self):
        return f"Employees(eid={self.eid}, name={self.name}, salary={self.salary})"

def filterItems(items, filterFunc):
    return list(filter(filterFunc, items))

def mapItems(items, mapFunc):
    return list(map(mapFunc, items))

def averageItems(items, valueFunc):
    return sum(map(valueFunc, items)) / len(items)

def main():
    empList = [Employees(1, 'A', 1000), Employees(2, 'B', 2000), Employees(3, 'C', 3000), Employees(4, 'D', 4000), Employees(5, 'E', 5000), Employees(6, 'F', 6000)]
    print(filterItems(empList, lambda x: x.getSalary() > 3000))
    print(mapItems(empList, lambda x: x.getName()))
    print(averageItems(empList, lambda x: x.getSalary()))
main()