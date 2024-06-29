class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def set_name(self, name):
        self.__name = name
    
    def set_age(self, age):
        self.__age = age
    
    def set_salary(self, salary):
        self.__salary = salary
    
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

employe1 = Employee('Raze', 20, 1500)

print("Name:", employe1.get_name())
print("Age:", employe1.get_age())
print("Salary:", employe1.get_salary())

employe1.set_name("Jett")
employe1.set_age(24)
employe1.set_salary(20000)

print("\nSetelah dimodifikasi:")
print("Name:", employe1.get_name())
print("Age:", employe1.get_age())
print("Salary:", employe1.get_salary())
