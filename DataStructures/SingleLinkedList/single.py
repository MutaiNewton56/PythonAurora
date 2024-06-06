class Person:
   def __init__(self,name,next=None):
      self.name=name
      self.next=next

class LinkedList:
   
   def __init__(self,name):
      self.head=Person(name)


linked=LinkedList("Isaak")
print(vars(linked))