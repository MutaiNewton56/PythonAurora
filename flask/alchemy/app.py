from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

db_config={
    'dbname':'postgres',
    'user':'postgres.erojatpkqtqexubknucv',
    'password':'4zY63KNsPFznj2oX',
    'host':'aws-0-ap-south-1.pooler.supabase.com',
    'port':'5432'
}

app.config["SQLALCHEMY_DATABASE_URI"]=f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:5432/postgres"
db=SQLAlchemy(app)

class Student(db.Model):
    __tablename__="student"
    id=db.Column(db.BigInteger,primary_key=True)
    name=db.Column(db.String(255),nullable=False)
    email=db.Column(db.String,unique=True,nullable=False)

    def __repr__(self):
        return f"Name: {self.name}, {self.email}"


#crud operations.
# CREATE , READ , UPDATE , DELETE

@app.route("/student",methods=["POST"])
def create_student():
    new_student=Student(name="Harry potter",email="harr@gmail.com")
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message':"New student created successfully"})

@app.route("/student",methods=["GET"])
def student_list():
    students=Student.query.all()
    output=[]
    for student in students:
        student_data={'id':student.id,'name':student.name,'email':student.email}
        output.append(student_data)
    return jsonify(output),200

if __name__=='__main__':
    app.run(debug=True)