from db import DB

class Student():

    def __init__(self):
        db=DB()
        self.cur=db.cur
        self.conn=db.conn
        pass

    def list(self):
        try:
            self.cur.execute("""
             SELECT * FROM student   
            """)
            students=self.cur.fetchall()
            student_arr=[]
            for student in students:
                student_arr.append(
                {"id":student[0],"name":student[1],"email":student[2]}
                )
            return student_arr
        except Exception as e:
            print(f"an error occured:{e}")
    
    def add(self,name,email):
        try:
            self.cur.execute("""
             INSERT INTO student (name,email)
            VALUES(%s,%s)
            """,(name,email))
            
            self.conn.commit()
            print("Student added successfully")
            return {"message":"Student added successfully"}
        except Exception as e:
            print(f"an error occured:{e}")
            return None