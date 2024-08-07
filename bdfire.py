import os
from dotenv import load_dotenv
import pyrebase
from tkinter import messagebox

def load_database():

    load_dotenv()

    apiKey = os.getenv('apiKey')
    authDomain = os.getenv('authDomain')
    databaseURL = os.getenv('databaseURL')
    projectId = os.getenv('projectId')
    storageBucket = os.getenv('storageBucket')
    messagingSenderId = os.getenv('messagingSenderId')
    appId = os.getenv('appId')
    
    firebase_config = {
        "apiKey": apiKey,
        "authDomain": authDomain, 
        "databaseURL": databaseURL,
        "projectId": projectId,
        "storageBucket": storageBucket,
        "messagingSenderId": messagingSenderId,
        "appId": appId
    }

    try:
        firebase = pyrebase.initialize_app(firebase_config)
        db = firebase.database()
        return db
    except Exception as e:
        messagebox.showerror("Error", f"Erro ao inicializar o Firebase: {e}")
        return None