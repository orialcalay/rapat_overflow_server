from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
from flask_cors import CORS, cross_origin
from dbUserFunctions import dbAddUser, dbGetUsers, dbUserLogin
from dbQuestionFunctions import dbGetQuestions, dbGetQuestionsByTag
from dbTagFunctions import dbGetTags

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def hello():
    response = jsonify({'some': 'data'})
    return response


@app.route('/addUser', methods = ['POST'])
@cross_origin()
def addUser():
    content = request.get_json()
    dbAddUser(content["firstName"], content["lastName"], content["email"], content["password"])
    resp = Response("True")
    return resp


@app.route('/users', methods = ['GET'])
@cross_origin()
def getUsers():
    users = dbGetUsers()
    resp = Response(users)
    return resp


@app.route('/login', methods = ['POST'])
@cross_origin()
def login():
    content = request.get_json()
    login = dbUserLogin(content["name"], content["password"])
    if login:
        return 'True'
    return 'False'


@app.route('/questions', methods = ['GET'])
@cross_origin()
def getQuestions():
    questions = dbGetQuestions()
    resp = Response(questions)
    return resp


@app.route('/questions/<tag>', methods = ['GET'])
@cross_origin()
def getQuestionsByTag(tag):
    questions = dbGetQuestionsByTag(tag)
    resp = Response(questions)
    return resp


@app.route('/tags', methods = ['GET'])
@cross_origin()
def getTags():
    tags = dbGetTags()
    resp = Response(tags)
    return resp


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)