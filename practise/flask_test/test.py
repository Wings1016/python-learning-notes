#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask,render_template,redirect,url_for
import os

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/')
def index():
    return redirect(url_for('login'))

print(os.urandom(16).decode('utf-8'))