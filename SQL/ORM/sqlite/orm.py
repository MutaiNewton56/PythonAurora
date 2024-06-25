import sqlite3


db_path="/home/arthur-codex/Documents/DEV/MORINGA/Python/SQL/sqlite.db"

class Student():
    def __init__(self):
        try:
              conn=sqlite3.connect(db_path)
              self.conn=conn
              cur=conn.cursor()
              self.cur=cur
              cur.execute("""
               CREATE TABLE IF NOT EXISTS student(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name VARCHAR(255) NOT NULL,
                 email VARCHAR(255) NOT NULL UNIQUE           
               )
              """)
              conn.commit()
              print("Created student table.")
        except Exception as e:
         print(f"an error occured:{e}")

    def add(self,name,email):
         try:
              self.cur.execute("""
                INSERT INTO student (name,email)
                VALUES (?,?)
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

st=Student()

st.add("Samson","sam@sam.com")
st.add("John","john@john.com")
st.list()

### SQLALCHEMY