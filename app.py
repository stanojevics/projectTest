# imports from flask module:
from flask import Flask, redirect, render_template, request, jsonify, url_for, session, abort, flash
import datetime
from datetime import datetime, time
import time
from time import sleep
from dbhandling import validate_password, change_password, add_to_table, check_for_user, check_email, add_user, get_content, get_user_id
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
#fix:DONE!
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')    
    print session['logged_in']
    return redirect(url_for('welcome', user = session['logged_in']))

##
# @route: KEEP THIS ROUTE
# <TODO: MERGE ROUTES:>
#
@app.route('/api/register/', methods = ['POST', 'GET'])
def registerRoute():
    if request.method == 'POST':
        if str(request.form['flag'])=='login':
            
            rsp =  jsonify({'Status':'change to login', 'Route':url_for('home')})
        elif str(request.form['flag'])=='register':
            if check_email(str(request.form['email'])) == True:
                flash ('Already Registered')
                rsp = jsonify({'Status': 'already registered', 'Route':url_for('home')})
            else:
                add_user(
                    str(request.form['user']),
                    str(request.form['password']),
                    str(request.form['email'])
                )
                rsp =  jsonify({'Status':'ok', 'Route':url_for('home')})
    if request.method == 'GET':
        if not session.get('logged_in'):
            return render_template('register.html')
        return redirect (url_for('home'))
    return rsp

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
@app.route('/api/users/<user>/settings', methods = ['GET', 'POST'])
def settings(user):
    if request.method == 'GET':
        if not session.get('logged_in'):
            return redirect(url_for('home'))
        print session['logged_in']
        return render_template('settings.html')

@app.route('/api/messages/', methods=['GET', 'POST'])
def messages():
    if request.method == 'POST':
        content = request.json
        add_to_table(content)
        return jsonify({"Status":"ok"})
    elif request.method == 'GET':
            #fix content display
            return result()
def result():
    #TODO:
    if not session.get('logged_in'):
        return redirect(url_for('home'))
    rows = get_content()
    return render_template('list.html', rows = rows)

##
# @route: startup route, login/register request handling
# @requests: 'POST' 'GET'
# @description: handles incoming 'POST' and 'GET' requests
#               in case of 'POST' with login flag:
#                           checks the submitted user info and generates
#                           json response in case of success to the front-end,
#                           containing route, on which the user is redirected
#               in case of 'POST' with register flag:
#                           returns json response to the front-end,
#                           containing the route for registration event,
#                           on which user is redirected
#               in case of 'GET': thoughts and prayers...
#
@app.route('/api/validate/', methods = ['POST', 'GET'])
def validate():
    if request.method == 'POST':
        #register case: redirect to register route
        print request.form['flag']
        if str(request.form['flag']) == 'register':
            return jsonify({'Status':'ok', 'Route': request.form['request_url']})
        #login case: redirect to user/redirect to home
        elif str(request.form['flag']) == 'login':
            if check_for_user(str(request.form['user']), str(request.form['password'])) == True:
                user_id = get_user_id(str(request.form['user']), str(request.form['password']))
                session['logged_in'] = user_id
                return jsonify({"Status":"ok", "Route":url_for('welcome', user = user_id)})
            else:
                print ('wrong')
                flash('wrong password!')
                return jsonify({"Status":"ok", "Route":url_for('home')})
        #messages: redirect to messages
        elif str(request.form['flag']) == 'messages':
            return jsonify({'Status':'ok', 'Route':url_for('messages')})
        #logout case: redirect to validate
        elif str(request.form['flag']) == 'logout':
            session['logged_in'] = False
            return jsonify({'Status':session['logged_in'], 'Route':url_for('validate')})
        elif str(request.form['flag']) == 'profile':
            return jsonify({'Status':'ok', 'Route':url_for('home')})
        elif str(request.form['flag']) == 'settings':
            return jsonify({'Status': 'ok', 'Route':request.form['request_url']+session['logged_in']+'/settings'})
        elif str(request.form['flag']) == 'change-password':
            if validate_password(session['logged_in'], request.form['oldPassword']) == True:
                change_password(session['logged_in'],request.form['newPassword'])
                return jsonify({'Status': 'ok','Route':url_for('home')})
            else:
                return jsonify({'Status': 'wrong password', 'Route': url_for('home')})
        else:
                print ('bad request')
                flash('bad request')
                return 'wrong password'
    #customer is a monkey
    #monkeys tend to break stuff
    #protect yourself
    #protection in my case: 
    #   holding a wooden shield, in front of rocket launcher
    #solution: thoughts and prayers
    #idiot proof/customer proof/child proof case:
    elif request.method == 'GET':
        return redirect(url_for('home'))
            
#Debug Route
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port = 8080 )