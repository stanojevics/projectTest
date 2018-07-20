# Import database module:
# RUN ONLY ONCE: DONE
# DATABASE EXISTS : TRUE
# TABLE EXISTS : TRUE
import sqlite3
from datetime import datetime, time
import string
import random
conn = sqlite3.connect('SmartServiceDevelopmentProjectdb.db')
cur = conn.cursor()

def create_table():
    conn.execute("CREATE TABLE IF NOT EXISTS temp_readings(id integer primary key, city text, country text, temperature_current text, temperature_min text, temperature_max text, [timestamp] timestamp)")
    conn.execute("CREATE TABLE IF NOT EXISTS registered_users(id text primary key, user_name text, password text, email text)")
def add_user_admin():
    import sqlite3 as sql
    with sql.connect('SmartServiceDevelopmentProjectdb.db') as con:
        cur = con.cursor()
        chars = string.letters + string.digits
        pwdSize = 7
        id = '#' + ''.join((random.choice(chars)) for x in range(pwdSize))
        print id
        con.execute('INSERT INTO registered_users (id, user_name, password, email) VALUES (?,?,?,?)', (id,'admin', 'admin', 'test@test.com'))
        con.commit()
    con.close()

create_table()
add_user_admin()
