import sqlite3



def get_db():
    connection=sqlite3.connect("db/SESORESDB") 
    return connection


def Create_tables():

    tables=[
    ('''CREATE TABLE IF NOT EXISTS admins(
            username VARCHAR(30) PRIMARY KEY,
            password VARCHAR(30)
        )
            ''')
    ,
    ('''
        CREATE TABLE IF NOT EXISTS company(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name VARCHAR(30),
            company_api_key VARCHAR(30)
        )
            ''')
    ,
    ('''
        CREATE TABLE IF NOT EXISTS location(
            company_id INTEGER ,
            location_id INTEGER PRIMARY KEY AUTOINCREMENT,
            location_name VARCHAR(30),
            location_country VARCHAR(30),
            location_city VARCHAR(30),
            location_meta VARCHAR(30),
            FOREIGN KEY(company_id) REFERENCES company(id)
        )
            ''')
    ,
    ('''
        CREATE TABLE IF NOT EXISTS sensor(
            location_id INTEGER,
            sensor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_name VARCHAR(30),
            sensor_category VARCHAR(30),
            sensor_meta VARCHAR(30),
            sensor_api_key VARCHAR(30),
            FOREIGN KEY(location_id) REFERENCES location(id)
        )
            ''')
    ,
    ('''
        CREATE TABLE IF NOT EXISTS sensor_data(
            sensor_magnitude INTEGER,
            sensor_id INTEGER,
            sensor_api_key VARCHAR(30),
            FOREIGN KEY(sensor_id) REFERENCES sensor(id)
        )
            ''')
  
    ]


    try:
        nu='admin'
        np='PASSWORD'
        db = get_db()
        cursor = db.cursor()
        for table in tables:
            cursor.execute(table)
        cursor.execute("INSERT INTO admins(username, password) VALUES (?, ?)" , (nu, np) )
        db.commit()
        
        
    except Exception as ex:
        print(ex) 