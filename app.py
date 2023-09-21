# importing required libraries
from flask import Flask, render_template
import mysql.connector
from cloudUserApp import userAction


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html',hello="Hello World")


dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="",
database = "finalproject"
)

#print(dataBase)

#preparing a cursor object
cursorObject = dataBase.cursor()

def get_user_input():
   user_input = input("Enter ID of task you want to delete: ") 
   user_input = user_input.strip()
   return user_input

def insertIntoDB(userInput):
    sql = f"insert into tasks values('2','{userInput}', '1')"
    cursorObject.execute(sql)
    dataBase.commit()

def showTask():
    query = "SELECT * FROM tasks"
    cursorObject.execute(query)
    
    myresult = cursorObject.fetchall()
    
    for x in myresult:
        print(x)

def delete_task():
    task_ID = get_user_input()
    print(task_ID)
    


#get_menu_function
user_action = userAction()
print(user_action)

if user_action.startswith('show'):
    showTask()
elif user_action.startswith('add'):
    task = user_action[4:] + "\n"
    insertIntoDB(task) 
elif user_action.startswith('delete'):
    delete_task()

#disconnecting from server
def disconnectDB():
    dataBase.close()

disconnectDB()

