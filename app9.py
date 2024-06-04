class Animal:
    def sound(self):
        print("This animal makes a sound")

## Polymorphism.
class Dog(Animal):
    def sound(self):
        super().sound()
        print("The dog barks")

class Dinnosar(Animal):
        def __init__(self):
                pass
        
d1=Dog()
d1.sound()

dino=Dinnosar()
dino.sound()