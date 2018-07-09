# Import database module:
# RUN ONLY ONCE: DONE
# DATABASE EXISTS : TRUE
# TABLE EXISTS : TRUE
import sqlite3
from datetime import datetime, time

conn = sqlite3.connect('SmartServiceDevelopmentProjectdb.db')
cur = conn.cursor()
#conn.execute("CREATE TABLE person (id integer primary key, firstname text, lastname text, dob date)")
def create_table():
    #cur.execute("CREATE TABLE IF NOT EXISTS test(productID INT AUTO_INCREMENT PRIMARY KEY, city TEXT, country TEXT)")
    conn.execute("CREATE TABLE IF NOT EXISTS temp_readings(id integer primary key, city text, country text, temperature_current text, temperature_min text, temperature_max text, [timestamp] timestamp)")
    conn.execute("CREATE TABLE IF NOT EXISTS users(id integer primary key, user_name text, password text, email text)")
def add_user_admin():
    import sqlite3 as sql
    with sql.connect('SmartServiceDevelopmentProjectdb.db') as con:
        cur = con.cursor()
        con.execute('INSERT INTO users (user_name, password, email) VALUES (?,?,?)', ('admin', 'admin', 'test@test.com'))
        con.commit()
    con.close()

create_table()
add_user_admin()
