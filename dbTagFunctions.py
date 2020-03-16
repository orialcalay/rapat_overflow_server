from pymongo import MongoClient
import json
from bson.json_util import dumps

client = MongoClient("localhost:27017")
db=client.rapat_overflow


def dbGetTags():
    return dumps(db.tags.find())


def dbAddTag():
    pass