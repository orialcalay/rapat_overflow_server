from pymongo import MongoClient
import json
from bson.json_util import dumps
import datetime

client = MongoClient("localhost:27017")
db=client.rapat_overflow


def dbGetQuestions():
    return dumps(db.questions.find())


def dbGetQuestionsByTag(tag):
    return dumps(db.questions.find({'tags': { "$in" : [tag]}}))


def dbAddQuestion(title, body, tags):
    currentTime = datetime.datetime.now().timestamp()
    question = {
        'title' : title,
        'description' : body,
        'tags' : tags,
        'view_count' : 0,
        'answers_count' : 0,
        'score' : 0,
        'creation_date' : currentTime,
        'last_activity_date' : currentTime,
        'owner_name' : 'Ori Alcalay'
    }
    result=db.questions.insert_one(question)
    print("add new question")