##
# @description: Handles Databases
# @author: Stanojevic Stefan - 1431858
# @date: Summer 2018
#
import sqlite3 as sql
from datetime import datetime, time
import string
import random
##
# @description: Adds 'POST' content, from datacollector
#               to the content database
# @params: content to be added (json format)
#
def add_to_table(content):
    with sql.connect('SmartServiceDevelopmentProjectdb.db') as con:
        cur = con.cursor()
        con.execute('INSERT INTO temp_readings (city, country, temperature_current, temperature_min, temperature_max, [timestamp]) VALUES (?,?,?,?,?,?)'
            , (content['name']
            ,content['sys']['country']
            ,content['main']['temp']
            ,content['main']['temp_min']
            ,content['main']['temp_max']
            ,datetime.now()) )
            
        con.commit()
    con.close()
##
# @description: checks if requested user exists in database
# @params: 'POST' username and 'POST' password
#
def check_for_user(user_name_post, password_post):
    with sql.connect('SmartServiceDevelopmentProjectdb.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM registered_users WHERE user_name=? and password = ?", (user_name_post, password_post))
        if len(cur.fetchall()) != 0:
            #print cur.fetchall()
            return True
        return False
##
# @description: check if requested email exists in database
# @params: 'POST' email
#
def check_email(email_post):
    with sql.connect('SmartServiceDevelopmentProjectdb.db') as con:
        cur= con.cursor()
        cur.execute('SELECT * FROM registered_users WHERE email=?', (email_post,))
        if len(cur.fetchall()) != 0:
            return True
        return False
##
# @description: get users id
# @params: 'POST' username 'POST' password
#
def get_user_id(username_post, password_post):
    with sql.connect('SmartServiceDevelopmentProjectdb.db') as con:
        cur= con.cursor()
        cur.execute('SELECT * FROM registered_users WHERE user_name=? and password = ?', (username_post, password_post,))
        return cur.fetchone()[0]
##
# @description: adds user to the database
# @params: username, password, email
#
def add_user(username_post, password_post, email_post):
    with sql.connect('SmartServiceDevelopmentProjectdb.db') as con:
        cur = con.cursor()
        id = id_generator()
        cur.execute('INSERT INTO registered_users (id, user_name, password, email) VALUES (?,?,?,?)', (id, username_post, password_post, email_post))

        con.commit()
    con.close()
##
# @description: generate ID for the user
# 
#
def id_generator():
    chars = string.letters + string.digits
    pwdSize = 7
    id = 'u.' + ''.join((random.choice(chars)) for x in range(pwdSize))
    if (check_for_existing_id(id)==True):
        id_generator()
    return id

def check_for_existing_id(id):
    with sql.connect('SmartServiceDevelopmentProjectdb.db') as con:
        cur = con.cursor()
        cur= con.cursor()
        cur.execute('SELECT * FROM registered_users WHERE id=?', (id,))
        if len(cur.fetchall()) != 0:
                return True
        return False

def get_content():
    conn = sql.connect('SmartServiceDevelopmentProjectdb.db') #connect to db
    conn.row_factory = sql.Row 
    cur = conn.cursor() #make a cursor
    cur.execute("SELECT * FROM temp_readings") #select everything with cursor
    rows = cur.fetchall() #save selected
    return rows

def change_password(id, newPassword):
     with sql.connect('SmartServiceDevelopmentProjectdb.db') as con:
        cur = con.cursor()
        cur= con.cursor()
        cur.execute('SELECT * FROM registered_users WHERE id=?', (id,))
        if len(cur.fetchall()) != 0:
                #insert into products (name, price) values ('sprite', 9)
                #cur.execute("INSERT INTO registered_users (name, price) values ('sprite', 9)")
                cur.execute("UPDATE registered_users SET password=? WHERE Id=?", (newPassword,id,))
                return True
        return False
def validate_password(id, oldPassword):
    with sql.connect('SmartServiceDevelopmentProjectdb.db') as con:
        cur = con.cursor()
        cur= con.cursor()
        cur.execute('SELECT * FROM registered_users WHERE id=? and password = ?', (id,oldPassword,))
        if len(cur.fetchall()) != 0:
                return True
        return False