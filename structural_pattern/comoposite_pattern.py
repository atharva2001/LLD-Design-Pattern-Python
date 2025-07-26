from abc import ABC,  abstractmethod

class EmployeeHierarchy(ABC):

    @abstractmethod
    def show_details(self, indent=0):
        pass 


# Leaf Node
class SWE(EmployeeHierarchy):

    def __init__(self, name):
        self.name = name

    def show_details(self, indent=0):
        print("-" * indent + f"SWE Employee: {self.name}")


#Composite
class Lead(EmployeeHierarchy):

    def __init__(self, name):
        self.name = name 
        self.swe = []

    def add(self, swe: SWE):
        self.swe.append(swe)

    def show_details(self, indent=0):
        print(" - " * indent + f"Lead Name: {self.name}")
        for emp in self.swe:
            emp.show_details(indent+1)


class Manager(EmployeeHierarchy):
    def __init__(self, name):
        self.name = name 
        self.lead = []

    def add(self, lead: Lead):
        self.lead.append(lead)

    def show_details(self, indent=0):
        print(" - " * indent + f"Manager Name: {self.name}")
        for emp in self.lead:
            emp.show_details(indent+1)



emp1 = SWE("Ron")
emp2 = SWE("Shawn")
emp3 = SWE("Jacob")

lead1 = Lead("Josh")
lead2 = Lead("John")
lead3 = Lead("Liam")

lead1.add(emp1)
lead1.add(emp3)
lead2.add(emp2)

manager = Manager("Don")
manager.add(lead1)
manager.add(lead2)
manager.add(lead3)

manager.show_details()