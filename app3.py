
#Attributes are variables associated
# with a specific object. They store data
# methods a

# Properties. 
# Allow us to access (Get and Set)
# Private attributes. 

class House:
    def __init__(self,width,length,height):
        self._width = width ## private attributes
        self._length=length
        self.height = height ## attributes
#GEETER 
    @property
    def width(self):
        print("Thanks for getting the width")
        return self._width
    
    @width.setter
    def width(self,w):
        if not isinstance(w,(int)):
            print("Error width must be a number")
            return "error"
        
        if w>1000 or w<10:
            print("Error width must in range [10, 1000]")
            return "error"  
        self._width = w
        return self._width


h1=House(23,34,56)
print(f"intial width {h1.width}")
print(f"intial width {h1._width}")
a=h1.width="232423"
print(f"set to string {a}")
b=h1.width=234456
print(f"set to 234456 {b}")
c=h1.width=800
print(f"set to 800 {c}")