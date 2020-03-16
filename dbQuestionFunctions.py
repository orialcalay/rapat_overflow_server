from pymongo import MongoClient
import json
from bson.json_util import dumps

client = MongoClient("localhost:27017")
db=client.rapat_overflow


def dbGetQuestions():
    return dumps(db.questions.find())


def dbGetQuestionsByTag(tag):
    return dumps(db.questions.find({'tags': { "$in" : [tag]}}))


def dbAddQuestion():
    pass