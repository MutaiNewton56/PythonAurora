class Parent():
    def __init__(self,name,email):
        self.name=name
        self.email=email


class Student():

    def __init__(self,name,parent):
        self.name=name
        self.parent=parent


p1=Parent("Dan","dan@gmail.com")
print(vars(p1))

st=Student("Samson",p1)

print(vars(st))