# Static Methods And 
# Static Atrbutes.

# Static 

# Static Attributes Class Atributes
# Static Methods 

class House:
    names=[]
    def __init__(self,color,length,width,name):
        self.color = color
        self.length = length
        self.width = width
        self.name = name
        House.names.append(name)
    
    @classmethod
    def idealHouse(cls):
        print(cls.names)
        print("Length 230 Width 340")

    def sayHello(self):
        print("Say Hello")

        

h1=House("blue",200,120,"Jonathan") #Instance of a  class.
h2=House("green",200,120,"Faith")
print(House.names)
# h1.idealHouse()
# print(vars(h1))
# h2=House("green",200,120,"Pal")
# print(vars(h2))
# print(House.names)

# House.idealHouse()
#House.idealHouse()