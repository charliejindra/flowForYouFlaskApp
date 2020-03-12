from flask import Flask, session, request, redirect, render_template, url_for
from app import app

import os
import requests
from pyrebase import pyrebase
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("app/flowforyou-fbc4e.json")
default_app = firebase_admin.initialize_app(cred)

dispensers = {"Bev Warren Student Rec and Wellness Center"}

@app.route('/')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

config = {
  "apiKey": os.environ['FIREBASE_API_KEY'],
  "authDomain": "flowforyou-fbc4e.firebaseapp.com",
  "databaseURL": "https://flowforyou-fbc4e.firebaseio.com",
  "projectId": "flowforyou-fbc4e",
  "storageBucket": "flowforyou-fbc4e.appspot.com",
  "serviceAccount": "app/flowforyou-fbc4e.json",
  "messagingSenderId": "1052538486567"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def new_dispenser(): #sending data to the Firebase database
    if request.method == "GET":
        return render_template('index.html')
    else:
        new_dispenser = dict(request.form)
        db.child("dispensers").push(new_dispenser) #replaces appending to dispensers variable with firebase db call.
        return redirect('/')

@app.route('/index') #Retreiving data from the database
def index():
    db_dispensers = db.child("dispensers").get().val().values()
    return render_template('index.html', dispensers = db_dispensers)