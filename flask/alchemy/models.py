
# class inherits from db Model

class Student(db.Model):
    id=db.Column(db.Integer,primary_key=True)