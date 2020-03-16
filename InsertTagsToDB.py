import requests
import json
from pymongo import MongoClient


client = MongoClient("localhost:27017")
db=client.rapat_overflow


def addQuestionsTagsToDB():
    questions = db.questions.find()
    tagsDict = {}
    tag_description = 'דוגמה לתיאור של תג: שפת java הינה שפה עילית, שאינה תלוית פלטפורמה, בעלת טיפוסיות סטטית ומוכוונת עצמים'
    
    for question in questions:
        for tag in question['tags']:
            if tag not in tagsDict.keys():
                tagsDict[tag] = {'tag_description' : tag_description, 'tag_questions_number' : 1}
            else:
                tagsDict[tag] = {'tag_description' : tagsDict[tag]['tag_description'], 'tag_questions_number' : tagsDict[tag]['tag_questions_number'] + 1}
    
    for key in tagsDict:
        addTagToDB(key, tagsDict[key]['tag_description'], tagsDict[key]['tag_questions_number'])


def addTagToDB(tag_name, tag_description, tag_questions_number):
    tag = {
        'tag_name' : tag_name,
        'tag_description' : tag_description,
        'tag_questions_number' : tag_questions_number
    }
    result=db.tags.insert_one(tag)
    print("insert 1 tag")


addQuestionsTagsToDB()