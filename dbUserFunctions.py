from pymongo import MongoClient
import json
from bson.json_util import dumps

client = MongoClient("localhost:27017")
db=client.rapat_overflow

def dbAddUser(firstName, lastName, email, password):
    user = {
        'first_name' : firstName,
        'last_name' : lastName,
        'email' : email,
        'password' : password
    }
    result=db.users.insert_one(user)
    print("add new user")


def dbGetUsers():
    return dumps(db.users.find())


def dbUserLogin(name, password):
    users = db.users.find()
    for user in users:
        if user["first_name"] == name and user["password"] == password:
            return True
    return False 