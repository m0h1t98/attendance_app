from flask import Flask, redirect,url_for,request,render_template
import pyrebase


config = {
        "apiKey": "AIzaSyAT4CknPPpJmPb8kT_DOgLcLG1a1eeUshY",
        "authDomain": "attendance-app-3dbd3.firebaseapp.com",
        "databaseURL": "https://attendance-app-3dbd3.firebaseio.com/",
        "storageBucket": "attendance-app-3dbd3.appspot.com",
    }
firebase = pyrebase.initialize_app(config)
db = firebase.database()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/attendance', methods=['POST'])
def attendance():
    from datetime import datetime
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        empid = request.form['empID']
        now =  datetime.now()
        time = now.strftime("%H:%M:%S")
        
        data = { "name": name, "email" : email, "empID" : empid, "time"  : time}

        db.child("users").push(data)
    return render_template('result.html', name=name, email=email, empid=empid, time=time)

 
if __name__ == '__main__':
    app.run(debug=True)