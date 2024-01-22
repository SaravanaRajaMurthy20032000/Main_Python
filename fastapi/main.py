from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

class bkcreate(BaseModel):
    title = str
    author = str

class book(bkcreate):
   id = int

def create_conn():
   conn = sqlite3.connect('fastapi/new_book.db')
   return conn

app = FastAPI()

@app.get("/")
def root():
 return {"message": "Welcome to the FastAPI"}

# def create_table():
#     connection = create_conn()
#     conn = connection.cursor()
#     conn.execute("""
#     create table book if not exist,
#     id int primary key auto increment,
#     title varchar(50) not null,
#     author varchar(25) not null
#     """)
#     connection.commit()
#     connection.close()

# print(create_table())

# if __name__ == '__main__':
#    app.run(debug = True)