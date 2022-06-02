from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok , _run_ngrok
import pymongo as PyMongo
from flask_cors import CORS
import socket
import json
import base64
from PIL import Image
from io import BytesIO
from flask_qrcode import QRcode
from datetime import datetime
from datetime import date

app = Flask(__name__)
# client = PyMongo.MongoClient("mongodb://127.0.0.1:27017")
# socket.getaddrinfo("localhost", 8080)
client = PyMongo.MongoClient("mongodb+srv://root:root@cluster0.tu2pq.mongodb.net/?retryWrites=true&w=majority")
socket.getaddrinfo("localhost", 8080)

run_with_ngrok(app)
CORS(app)
QRcode(app)


def first():
    a = _run_ngrok()
    print(type(a))
    b = a+'/save_data'
    print(b)
    r = QRcode.qrcode(b)
    e = r.replace('data:image/png;base64,','')
    print(e)
    im = Image.open(BytesIO(base64.b64decode(e)))
    im.save('rrrr.png', 'PNG')
first()

@app.route('/',methods=['GET'])
def base():
    return 'Akshay'

@app.route('/save_data',methods=['GET','POST'])
def save_data():
    if request.method == 'POST':
        name = request.form.get('file')
        # d = datetime.now()
        d = datetime.today().strftime('%Y-%m-%d')
        now = datetime.now()
        t = now.strftime("%H:%M:%S")
        data = {
                    "name":name,    
                    "datew":d,
                    "time":t,
                }
        # client.Messi.attendence.insert_one(data)
        
        db_data = client.Messi.attendence.find({'datew':d})
        for i in db_data:
            # print(i)
            if i.get('name') == name :
                dat = ''
                print("Already Punched in")
                break
            else:
                dat = "Not exist"
                pass
        if dat == "Not exist":
            client.Messi.attendence.insert_one(data)
        return 'Data Saved'
    return '''
    <!doctype html>
    <title>Attendence</title>
    <h1>Attendence</h1>
    <form method=post enctype=multipart/form-data>
      <input type=text name=file>
      <input type=submit value=Punch in>
    </form>
        '''


if __name__ == "__main__":
    app.run() 