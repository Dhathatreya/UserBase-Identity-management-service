import mysql.connector
import json
from flask import make_response
class user_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="Dhathu@26",database="flask_tutorial")
            self.cur=self.con.cursor(dictionary=True)
            print("connection successful")
        except:
            print("Some error")

    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result=self.cur.fetchall()
        if len(result)>0:
           return {"payload":result}
        else:
            return "No Data"
    
    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO users(name, email, phone, roleid, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['roleid']}', '{data['password']}')")
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)