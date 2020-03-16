import requests
import json
from pymongo import MongoClient
from googletrans import Translator


client = MongoClient("localhost:27017")
db=client.rapat_overflow


translator = Translator()


def getStackOverflowQuestions():
    response = requests.get("https://api.stackexchange.com/questions?site=stackoverflow")
    if(response.status_code==200):
        data = response.json()
        for item in data['items']:
            owner = item['owner']
            try:
                heTitle = translateString(item['title'])
                insertToDB(heTitle, heTitle, item['tags'], item['view_count'], item['answer_count'], item['score'], item['creation_date'], item['last_activity_date'], owner['display_name'])
            except:
                insertToDB(item['title'], item['title'], item['tags'], item['view_count'], item['answer_count'], item['score'], item['creation_date'], item['last_activity_date'], owner['display_name'])
    else:
       print("Error receiving data")


def insertToDB(title, description, tags, view_count, answers_count, score, creation_date, last_activity_date, owner_name):
    question = {
        'title' : title,
        'description' : description,
        'tags' : tags,
        'view_count': view_count,
        'answers_count': answers_count,
        'score': score,
        'creation_date': creation_date,
        'last_activity_date': last_activity_date,
        'owner_name': owner_name
    }
    result=db.questions.insert_one(question)
    print("insert 1 question")

def translateString(str):
    translated = translator.translate(str, src='en', dest='he')
    return translated.text


getStackOverflowQuestions()