
class Student():
    def __init__(self,name,mark):
        self.name=name
        self.cat_dogs=mark
        self.n=0
    
    @property
    def mark(self):
        #print("Somene is trying to get the mark")
        self.n=self.n+1
        return self.cat_dogs
    
    @mark.setter
    def mark(self,value):
        if value>0 and value <100:
            self.cat_dogs=value
            return
        raise ValueError("Value must be between 0 and 100")

st=Student("Sam",90)


## Getter (how a person gets data) and setters 
## Security

# print(vars(st))
# print(st.mark)
# # print(vars(st))
# print(vars(st))
# print(st.mark)
# # print(vars(st))

st.mark=39
print(vars(st))