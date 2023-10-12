class Parent:
    id: int = 0  # static variable
    name: str = 'shankar'

    def __init__(self, number: int, name: str, salary: float):
        self.number: int = number  # instance variable
        self.name: str = name  # instance variable
        self.__salary: float = salary  # private variable
        self.id = 0
        print('instance variable', self.id)
        print('static variable', Parent.id)
        self.id += 1  # instance variable
        Parent.id += 1
        self.print_all()

    def __private_method(self) -> None:
        __private_variable: int = 100
        print('Private Method::' + __private_variable)

    def set_salary(self, salary: float) -> None:
        # setter method
        self.__salary = salary

    def get_salary(self) -> float:
        # getter method
        return self.__salary

    @classmethod
    def class_function(cls) -> None:
        print('class_function', cls.id)

    @staticmethod
    def static_function() -> None:
        print('static_function', Parent.id)

    def print_all(self):
        print(self.id)  # accessing instance variable inside function
        print(self.number)  # accessing instance variable inside function
        print(self.name)  # accessing instance variable inside function
        print(self.__salary)  # accessing instance variable inside function
        print(Parent.id)  # accessing static variable inside function


x = Parent(10, 'Shankar', 20000.00)
x = Parent(20, 'Priya', 30000.00)
x = Parent(30, 'Pooja', 40000.00)

print(x.id)  # accessing instance variable outside of class
print(x.number)  # accessing instance variable outside of class
print(x.name)  # accessing instance variable outside of class
# x.__private_method() # cannot access AttributeError
# print(x.__salary)  # accessing instance private variable outside of class #AttributeError

print(x.name)  # accessing instance variable outside of class

# getter setter example
x.set_salary(40000)
print(x.get_salary())

print(Parent.id)  # accessing static variable outside of class
Parent.static_function()  # calling static function outside of class
Parent.class_function()  # calling class function outside of class
