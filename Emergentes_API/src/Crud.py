from database import get_db
from flask import make_response
#GETS ADMIN

def get_admin(username):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT username,password FROM admins WHERE username = ?"
    cursor.execute(statement, [username])
    return cursor.fetchone()


def get_pass_admin(username):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT password FROM admins WHERE username = ?"
    cursor.execute(statement, [username])
    return cursor.fetchone()



def get_admins():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT username, password FROM admins"
    cursor.execute(query)
    return cursor.fetchall()



#Muestra todo, muestra uno, edita, elimina. COMPANY
def insert_company(id, company_name, company_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO company(id, company_name, company_api_key) VALUES (?, ?, ?)"
    cursor.execute(statement, [id, company_name, company_api_key])
    db.commit()
    return make_response("created", 201)


def update_company(id, company_name, api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE company SET company_name = ?, company_api_key = ? WHERE id = ?"
    cursor.execute(statement, [company_name, api_key,id])
    db.commit()
    return True


def delete_company(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM company WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_company(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, company_name, company_api_key FROM company WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_companys():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, company_name, company_api_key FROM company"
    cursor.execute(query)
    return cursor.fetchall()


#CRUD location

def insert_location(company_id,location_id, location_name,location_country,location_city,location_meta):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO location(company_id,location_id, location_name,location_country,location_city,location_meta) VALUES (?, ?, ?, ?,?,?)"
    cursor.execute(statement, [company_id,location_id, location_name,location_country,location_city,location_meta])
    db.commit()
    return True


def update_location(company_id,location_id, location_name,location_country,location_city,location_meta):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE location SET company_id = ?,location_name = ?, location_country = ?,location_city = ?, location_meta = ? WHERE location_id = ?"
    cursor.execute(statement, [company_id, location_name, location_country, location_city, location_meta,location_id])
    db.commit()
    return True




#CRUD SENSOR

def insert_sensor(location_id, sensor_id,sensor_name,sensor_category,sensor_meta,sensor_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO sensor(location_id, sensor_id,sensor_name,sensor_category,sensor_meta,sensor_api_key) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [location_id, sensor_id, sensor_name, sensor_category, sensor_meta, sensor_api_key])
    db.commit()
    return True


def update_sensor(location_id, sensor_id,sensor_name,sensor_category,sensor_meta,sensor_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE sensor SET location_id = ?, sensor_name = ?, sensor_category= ?,sensor_meta = ?,sensor_api_key = ? WHERE sensor_id = ?"
    cursor.execute(statement, [location_id,sensor_name,sensor_category,sensor_meta,sensor_api_key,sensor_id])
    db.commit()
    return True


def delete_sensor(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM sensor WHERE sensor_id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_sensor(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT location_id, sensor_id,sensor_name,sensor_category,sensor_meta,sensor_api_key FROM sensor WHERE sensor_id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_sensors():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT location_id, sensor_id, sensor_name, sensor_category, sensor_meta, sensor_api_key FROM sensor"
    cursor.execute(query)
    return cursor.fetchall()













def delete_location(location_id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM location WHERE location_id = ?"
    cursor.execute(statement, [location_id])
    db.commit()
    return True


def get_location(location_id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT company_id,location_id, location_name,location_country,location_city,location_meta FROM location WHERE location_id = ?"
    cursor.execute(statement, [location_id])
    return cursor.fetchone()


def get_locations():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT company_id,location_id, location_name,location_country,location_city,location_meta FROM location"
    cursor.execute(query)
    return cursor.fetchall()

#CRUD SENSOR

def insert_sensor(location_id,id, name,category,meta,api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO sensor(location_id,sensor_id, sensor_name,sensor_category,sensor_meta,sensor_api_key) VALUES (?, ?, ?, ?, ? , ?)"
    cursor.execute(statement, [location_id,id, name,category,meta,api_key])
    db.commit()
    return True


def update_sensor(location_id, id, name,category,meta,api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE sensor SET location_id = ?, sensor_name = ?, sensor_category = ?,sensor_meta = ?, sensor_api_key = ? WHERE sensor_id = ?"
    cursor.execute(statement, [location_id,name,category,meta,api_key,id])
    db.commit()
    return True


def delete_sensor(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM sensor WHERE sensor_id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_sensor(sensor_id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT location_id, sensor_id, sensor_name, sensor_category , sensor_meta, sensor_api_key FROM sensor WHERE sensor_id = ?"
    cursor.execute(statement, [sensor_id])
    return cursor.fetchone()


def get_id_sensor(sensor_id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT sensor_api_key FROM sensor WHERE sensor_id = ?"
    cursor.execute(statement, [sensor_id])
    return cursor.fetchone()



def get_sensors():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT location_id, sensor_id, sensor_name,sensor_category,sensor_meta,sensor_api_key FROM sensor"
    cursor.execute(query)
    return cursor.fetchall()

#CRUD SENSOR_DATA

def insert_sdata(sensor_id, sensor_magnitude, sensor_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO sensor_data(sensor_id, sensor_magnitude,sensor_api_key) VALUES (?, ?, ?)"
    cursor.execute(statement, [sensor_id,sensor_magnitude,sensor_api_key])
    db.commit()
    return True


def update_sdata(sensor_id,sensor_magnitude,sensor_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE sensor_data SET sensor_magnitude = ?, sensor_api_key = ? WHERE sensor_id = ?"
    cursor.execute(statement, [sensor_magnitude,sensor_api_key, sensor_id])
    db.commit()
    return True




def delete_sdata(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM sensor_data WHERE sensor_id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_sdata(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT sensor_id, sensor_magnitude, sensor_api_key FROM sensor_data WHERE sensor_id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()



def get_sdatas():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT sensor_id, sensor_magnitude, sensor_api_key FROM sensor_data"
    cursor.execute(query)
    return cursor.fetchall()