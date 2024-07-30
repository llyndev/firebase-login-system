import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime, timedelta

cred = credentials.Certificate("YOUR_CREDENTIALS.JSON")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'YOUR_DATABASE_URL'
})

def register_user(username, password, days_valid):
    ref = db.reference('users')
    expiration_date = (datetime.now() + timedelta(days=days_valid)).strftime('%Y-%m-%d %H:%M:%S')
    ref.child(username).set({
        'password': password,
        'expiration': expiration_date
    })