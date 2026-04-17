from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import hashlib

app=FastAPI()

conn = sqlite3.connect("user_data",check_same_thread=False)
cursor=conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
               username TEXT,
               password TEXT
               )
        """)
conn.commit()

@app.get("/")
def home():
    return{"message":"Hello!!"}
@app.get("/about")
def about():
    return{"message":"Iam learning Python Backend Development"}
class User(BaseModel):
    username:str
    password:str
def hash_password(password:str):
    return hashlib.sha256(password.encode()).hexdigest()

@app.post("/register")
def register(user:User):
    hashed_password=hash_password(user.password)
    cursor.execute(
        "INSERT INTO users(username,password) VALUES(?,?)",
        (user.username,hashed_password)

    )
    conn.commit()
    return{"message":"registered success"}
@app.post("/login")
def login(user:User):
    hashed_password=hash_password(user.password)
    
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                   (user.username,hashed_password)
    )
    result=cursor.fetchone()
    if result:
        return{"message":"login success"}
    else:
        return{"message":"invalid credentials"}
@app.get("/users")
def users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()
       

        

               

 
        
              
