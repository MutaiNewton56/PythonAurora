# ABSTRACTION
# Reason for OBJECT ORITENTED PROGRAMMING

### cat
# def sound():
#     print("meaow")

# age=23
# name=49

# class Cat:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def sound(self):
#         print("meaow")

# c1=Cat("Ali",3)
# print(vars(c1))
# c1.sound()

## Go Abstraction 

####---> Inheritance


#inheritance is concept
# that allows a class to inherit
# Attributes and methods from another class

# class Animal:
#     def __init__(self,name,sound):
#         self.name=name
#         self.sound=sound
#     def make_sound(self):
#         print(self.sound)

# class Dog(Animal):
#     def __init__(self,name):
#         super().__init__(name,"Bark")

# class Cat(Animal):
#       def __init__(self,name):
#             super().__init__(name,"Meawoos")
# Dry<do not repeat yourself.>

class Shapes():
    def __init__(self,type,l,w,r):
        self.l=l
        self.w=w
        self.r=r
        self.type=type
    def area(self):
        if self.type=="Rectangle":
            return self.l*self.w
        if self.type=="Square":
            return self.l*self.l
        if self.type=="Circle":
            return 3.142*self.r
        return "Shape not found"
    def parentSayHello(self):
        print("Shapes Hello")

 
class Recatange(Shapes):
    def __init__(self,l,w):
        super().__init__("Rectangle",l,w,None)
    def sayHello(self):
        super().parentSayHello()

class Square(Shapes):
    def __init__(self,l):
         super().__init__("Square",l,l,None)
    
class Circle(Shapes):
    def __init__(self,r):
       super().__init__("Circle",None,None,r)
    def area(self):
        print("Calculatint are of a circle")
        return super().area()

# r1=Recatange(10,20)
# print(vars(r1))
# print(r1.area())
# c1=Circle(1)
# print(vars(c1))
# print(c1.area())
# print(c1.parentSayHello())
# print(r1.sayHello())

# c1=Circle(1)
# print(c1.area())