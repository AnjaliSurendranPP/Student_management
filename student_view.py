from mysql import connector
from datetime import datetime

class DbConnect:
    def get_connection(self):
        try:
            self.connection = connector.connect(
                host="localhost",
                user="root",
                password="Anjali94!",
                database="student_management"
            )
            return self.connection
        except Exception as e:
            return None

class StudentManagement(DbConnect):
    def get(self):
        try:
            self.connection = super().get_connection()
            self.cursor = self.connection.cursor()
            query = "select * from students"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            for data in records:
                print(data)
        except Exception as e:
            print(e)

    def post(self, **kwargs):
        try:
            self.connection = super().get_connection()
            self.cursor = self.connection.cursor()
            query = "insert into students(name,email,phone,course_id) values(%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Student added successfully")
        except Exception as e:
            print(e)

    def get_object(self, id=None):
        try:
            self.connection = super().get_connection()
            self.cursor = self.connection.cursor()
            query = "select * from students where id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)

    def retrieve(self, id=None):
        try:
            record = self.get_object(id=id)
            print("retrieve:", record)
        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            record = self.get_object(id=id)
            values = (id,)
            if record != None:
                query = "delete from students where id=%s"
                self.cursor.execute(query, values)
                self.connection.commit()
                print("student",id," deleted successfully")
            else:
                print("delete:student not found")
        except Exception as e:
            print(e)

    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)
            if record != None:
                self.connection = super().get_connection()
                self.cursor = self.connection.cursor()
                placeholder = ""
                for k in kwargs.keys():
                    placeholder += k + "=%s, "
                placeholder = placeholder.rstrip(", ")
                query = f"update students set {placeholder} where id=%s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query, values)
                self.connection.commit()
                print("students updated successfully")
            else:
                print("put:student not found")
        except Exception as e:
            print(e)

connection_instance=DbConnect()
print(connection_instance.get_connection())

student_instance=StudentManagement()
# donor_instance.post(name="Anjali",email="anjali@gmail.com",phone="8547403112",course_id="101")
# donor_instance.post(name="Anju",email="anju@gmail.com",phone="8547403221",course_id="102")
# student_instance.post(name="Akhil",email="akhil@gmail.com",phone="9495900638",course_id="101")
print("------------student details-----------------------")
student_instance.get()
print("-----------------------------------")
print("get_object:",student_instance.get_object(2))
print("-----------------------------------")
student_instance.retrieve(1)
print("-----------------------------------")
student_instance.delete(3)
print("------------after deletion-----------------------")
student_instance.get()
print("----------after updation------------------------")
student_instance.put(2,course_id=102)
student_instance.retrieve(2)