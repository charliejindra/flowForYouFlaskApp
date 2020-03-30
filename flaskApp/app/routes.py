from flask import Flask, session, request, redirect, render_template, url_for
from app import app

import os
import requests
from pyrebase import pyrebase
import firebase_admin
from firebase_admin import credentials


@app.route('/')
@app.route('/index') #Retreiving data from the database
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

