
# Getter And Setters
# Decorator 
class Student:

    def __init__(self,name = "Uknown", age = 0,mark=0):
       self.name=name
       self.age=age
       self._mark=mark # This is private 
       self.mark_access_counter=0
       self.updateGrade(mark)

    @property# function decorator.
    def mark(self):
        self.mark_access_counter=self.mark_access_counter + 1
        return self._mark
    
    @mark.setter
    def mark(self,mark):
        self._mark=mark
        self.updateGrade(mark)
        return f"${self.mark} ${self.grade}"
    
    def updateMark(self,mark):
        self._mark=mark
        self.updateGrade(mark)
        return f"${self.mark} ${self.grade}"
    
    def updateGrade(self,mark):
        if mark>=90 and mark<100:
            self.grade="A"
            return
        if mark >=75 and mark<90:
            self.grade="B"
            return
        if mark>=65 and mark<75:
            self.grade="C"
            return
        if mark >=50 and mark<65:
            self.grade="D"
            return
        if mark>=0 and mark <50:
            self.grade="E"
            return
        self.grade="Uknown"


# st1=Student("Samson",23,34)
# print(vars(st1))
# print(st1._mark)
# print(vars(st1))
# print(st1.name)

# st1=Student("Samson",23,34)
# print(vars(st1))
# st1.updateMark(87)
# print(vars(st1))


""""
Decorators in python are a way to modify or
enhance behavior of function and methofs. in 
Order to  extend its behavior without modifying
It.
"""

# Simple Example

def my_decorator(func):
    print("My decorator function called")
    def wrapper():
        print("""
            Something is happending here
              Before we call the function
        """)   
        func()
        print("""
            Something is happending here
              After  we call the function
        """)   
    return wrapper

# def sayHello():
#     print("Hello World")
# # my_decorator(sayHello)
# hello=my_decorator(sayHello)

# hello()

@my_decorator
def sayHello():
    print("Hello World")


sayHello()