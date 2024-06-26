# students.
# CREATE student table.
# add student.
# list student.

import psycopg2

db_config={
    'dbname':'postgres',
    'user':'postgres.erojatpkqtqexubknucv',
    'password':'4zY63KNsPFznj2oX',
    'host':'aws-0-ap-south-1.pooler.supabase.com',
    'port':'5432'
}

### SQL ALCHEMY

class Student():

    def __init__(self):
         try:
              conn=psycopg2.connect(**db_config)
              self.conn=conn
              cur=conn.cursor()
              self.cur=cur
              cur.execute("""
               CREATE TABLE IF NOT EXISTS student(
                 id BIGSERIAL PRIMARY KEY,
                 name VARCHAR(255) NOT NULL,
                 email VARCHAR(255) NOT NULL UNIQUE           
               )
              """)
              conn.commit()
              print("Created student table.")

         except Exception as e:
              print(f"an error occured:{e}")
        #UPDATE WHE
    def add(self,name,email):
         try:
              self.cur.execute("""db_config={
    'dbname':'postgres',
    'user':'postgres.erojatpkqtqexubknucv',
    'password':'4zY63KNsPFznj2oX',
    'host':'aws-0-ap-south-1.pooler.supabase.com',
    'port':'5432'
      }
                """,(name,email))
              ## SQL INJECTION
              ## PHP<>
              self.conn.commit()
              print("Student added successfully")
         except Exception as e:
              print(f"an error occured:{e}")    
    
    def list(self):
         try:
              self.cur.execute("""
                 SELECT * FROM student
            """)
              
              students=self.cur.fetchall()
              for student in students:
                   print(student)
         except Exception as e:
            print(f"an error occured:{e}")   

st1=Student()   
# st1.add("JOJO","jojo@gmail.com")
st1.list()