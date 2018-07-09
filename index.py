# imports from flask module:
from flask import Flask, redirect, render_template, request, jsonify, url_for, session, abort, flash
import datetime
from datetime import datetime, time
from dbhandling import add_to_table, check_for_user, check_email, add_user
import os
# json:
import json
#----------------
# imports from sqlite3:
import sqlite3 as sql

#from signUpForm import SignupForm

app = Flask(__name__)
#nav:
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')    
    else:
        return redirect(url_for('result'))

@app.route('/result', methods = ['POST', 'GET'])
def result():
    #TODO:
    if not session.get('logged_in'):
        return render_template('login.html')
    conn = sql.connect('SmartServiceDevelopmentProjectdb.db') #connect to db
    conn.row_factory = sql.Row 
    cur = conn.cursor() #make a cursor
    cur.execute("SELECT * FROM temp_readings") #select everything with cursor
    rows = cur.fetchall() #save selected
    return render_template('list.html', rows = rows)
#Logging:
@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    if check_for_user(POST_USERNAME, POST_PASSWORD) == True:
        session['logged_in'] = True
    elif request.method == 'GET':
        return sign_in()
    else:
        flash('wrong password!')
    return home()
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
@app.route('/signin', methods = ['GET'])
def sign_in():
    return render_template('signin.html')
@app.route('/signin/result', methods = ['GET', 'POST'])
def sign_in_result():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    POST_EMAIL = str(request.form['email'])
    if check_email(POST_EMAIL) == True:
        flash('Already Registered')
    else:
        add_user(POST_USERNAME, POST_PASSWORD, POST_EMAIL)
    return sign_in()

#Collector to Server Route:
@app.route('/api/add_message/', methods=['GET', 'POST'])
def add_message():
    if request.method == 'POST':
        content = request.json
        add_to_table(content)
        return jsonify({"Status":"ok"})
    else:
        return redirect(url_for('home'))

#Debug Route
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)