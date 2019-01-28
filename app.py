from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import hashlib
import os

app = Flask(__name__)
client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
app.debug = True
db = client.app

@app.route('/')
def hello():
    return '이용 방법 입니다 :' \
        '1. /user/ - 모든 user들을 hash로 표현 해줍니다' \
        '2. /user/new/ - 새로운 user를 등록합니다' \
        '3. /user/<hash>/ - hash에 해당하는 user 정보를 보여줍니다' \

@app.route("/user/new/", methods = ['POST','GET'])
def insert_data():
    if request.method == 'GET' :
        return render_template ('new.html')

    elif request.method == 'POST' :
        user_name = request.form['user_name']
        user_tel = request.form['user_tel']
        hash_string = user_name + user_tel
        user_hash = hashlib.sha256(hash_string.encode()).hexdigest()
        
db.user.insert({'user_name':user_name,'user_tel':user_tel,'user_hash':user_hash})

        return "your data inserted successfully" +"    "+ user_hash
    else:
        return "please try again"
    

@app.route("/user/<hash>/", methods = ['GET'])
def find_data(hash):
    if request.method == 'GET':
        find = db.user.find_one({'user_hash' : hash}, {'_id':0, 
'user_hash':0})
        return str(find)
    else :
        return "There is no Data"

if __name__ =='__main__':
    app.run(host ='0.0.0.0',debug=True)

