import pyrebase

config = {
    "apiKey": "AIzaSyAT4CknPPpJmPb8kT_DOgLcLG1a1eeUshY",
    "authDomain": "attendance-app-3dbd3.firebaseapp.com",
    "databaseURL": "https://attendance-app-3dbd3.firebaseio.com/",
    "storageBucket": "attendance-app-3dbd3.appspot.com",
    }
firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.create_user_with_email_and_password("agrawalmohit741@gmail.com", "password")

# Get a reference to the database service
db = firebase.database()
    
data = {
        "name": "Mortimer 'Morty' Smith",
        "email" : "ag@abc.com"
    }

    # Pass the user's idToken to the push method
results = db.child("users").push(data, user['idToken'])