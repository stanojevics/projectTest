import sqlite3 as sql
import datetime
from datetime import datetime, time
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
def check_for_user(user_name_post, password_post):
    with sql.connect('SmartServiceDevelopmentProjectdb.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE user_name=? and password = ?", (user_name_post, password_post))
        if len(cur.fetchall()) != 0:
            #print cur.fetchall()
            return True
        return False
def check_email(email_post):
    with sql.connect('SmartServiceDevelopmentProjectdb.db') as con:
        cur= con.cursor()
        cur.execute('SELECT * FROM users WHERE email=?', (email_post,))
        if len(cur.fetchall()) != 0:
            return True
        return False
def add_user(username_post, password_post, email_post):
    with sql.connect('SmartServiceDevelopmentProjectdb.db') as con:
        cur = con.cursor()
        cur.execute('INSERT INTO users (user_name, password, email) VALUES (?,?,?)', (username_post, password_post, email_post))

        con.commit()
    con.close()