# imports from flask module:
from flask import Flask, redirect, render_template, request, jsonify, url_for, session, abort, flash
import datetime
from datetime import datetime, time
import time
from time import sleep
from dbhandling import add_to_table, check_for_user, check_email, add_user, get_content, get_user_id
import os
# json:
import json
#----------------
# imports from sqlite3:
import sqlite3 as sql

#from signUpForm import SignupForm

app = Flask(__name__)
##
# @route: HOME PAGE
# @request methods: 'GET'
# @description: handle session, if registered redirect to user page,
#               otherwise display login page
#

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')    
    return terminate_session()
def terminate_session():
    session['logged_in'] == False
    session.pop('logged_in', None)
    flash('One does not simpley manually change the route...')
    time.sleep(2) 
    return redirect (url_for('home'))
##
# @route: KEEP THIS ROUTE
# <TODO: MERGE ROUTES:>
#
@app.route('/api/validate/', methods = ['POST', 'GET'])
def validateRoute():
    if request.method == 'POST':
        POST_USERNAME = str(request.form['user'])
        POST_PASSWORD = str(request.form['password'])
        if check_for_user(POST_USERNAME, POST_PASSWORD) == True:
            session['logged_in'] = True
            user_id = get_user_id(POST_USERNAME, POST_PASSWORD)
            return jsonify({"Status":"ok", "Route":url_for('home'), "user_id": user_id})
        else:
            print ('wrong')
            flash('wrong password!')
            return 'wrong password'
    elif request.method == 'GET':
        if session['logged_in'] == True:
            return redirect(url_for('home'))
        
        

@app.route('/api/register/', methods = ['POST', 'GET'])
def registerRoute():
    if request.method == 'POST':
        POST_USERNAME = str(request.form['user'])
        POST_PASSWORD = str(request.form['password'])
        POST_EMAIL = str(request.form['email'])
        if check_email(POST_EMAIL) == True:
            flash('Already Registered')
        else:
            add_user(POST_USERNAME, POST_PASSWORD, POST_EMAIL)
    if request.method == 'GET':
        return redirect(url_for('home'))
    return jsonify({"Status":"ok", "Route": url_for('home')})
###########################################################
@app.route('/result', methods = ['POST', 'GET'])
def result():
    #TODO:
    if not session.get('logged_in'):
        return render_template('login.html')
    rows = get_content()
    return render_template('list.html', rows = rows)

#REGISTER ROUTE: REMOVE SOON
@app.route('/register', methods = ['GET'])
def register():
    return render_template('register.html')

##  
# @route: CONTENT
# @requests: 'POST' used by data collector
#            'GET' used by registered users
# @description: <TODO:>
#
@app.route('/api/users/<user>/', methods = ['GET'])
def welcome(user):
    if not session.get('logged_in'):
        return redirect(url_for('home'))
    print session['logged_in']
    return render_template('user.html')
@app.route('/logout')
def logout():
    session['logged_in'] == False
    session.pop('logged_in', None)
    return redirect(url_for('home'))
#@app.route('/api/messages/', methods=['GET', 'POST'])
#def messages():
#    if request.method == 'POST':
#        content = request.json
#        add_to_table(content)
#        return jsonify({"Status":"ok"})
#    elif request.method == 'GET':
#        #check session:
#        if not session.get('logged_in'):
#            return redirect(url_for('home')) 
#        else:
#            #fix content display
#            return result()


#Debug Route
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port = 8080 )