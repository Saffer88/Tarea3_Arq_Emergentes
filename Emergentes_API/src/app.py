from flask import Flask, jsonify, json, request
import Crud
from database import Create_tables

app = Flask(__name__)

@app.route('/')
def hola():
    h="Esta no es la ruta master"
    return h






#COMPANYS
#get all companys
@app.route('/api/v1/company', methods=["GET"])
def get_companys():
    companys = Crud.get_companys()
    return jsonify(companys)

#get one by id company
@app.route("/api/v1/company/<id>", methods=["GET"])
def get_company_by_id(id):
    company = Crud.get_company(id)
    return jsonify(company)

#edit, set company
@app.route("/api/v1/company", methods=["PUT"])
def update_company():
    company_details = request.get_json()
    id = company_details["id"]
    company_name = company_details["company_name"]
    company_api_key = company_details["company_api_key"]
    result = Crud.update_company(id, company_name, company_api_key)
    return jsonify(result)


#delete company
@app.route("/api/v1/company/<id>", methods=["DELETE"])
def delete_company(id):
    result = Crud.delete_company(id)
    return jsonify(result)


#insert company
@app.route("/api/v1/company", methods=["POST"])
def insert_company():
    company_details = request.get_json()
    id = company_details["id"]
    company_name = company_details["company_name"]
    company_api_key = company_details["company_api_key"]
    
    #result = Crud.insert_company(id, company_name, company_api_key)
    #return jsonify(result)
    pass_api_key = str(Crud.get_pass_admin('admin'))
    try:
        #if('1'=='1'):
        if pass_api_key == company_api_key:
            result = Crud.insert_company(id, company_name, company_api_key)
            return jsonify(result)
        else:
            print(repr(pass_api_key) ),
            print(repr(company_api_key))
            return jsonify({"error": "Api_key incorrecta"})
        
    except Exception as ex:
        return jsonify({"error": str(ex)})
    


#LOCATION
#get all companys
@app.route('/api/v1/location', methods=["GET"])
def get_location():
    companys = Crud.get_locations()
    return jsonify(companys)

#get one by id company
@app.route("/api/v1/location/<id>", methods=["GET"])
def get_location_by_id(id):
    company = Crud.get_location(id)
    return jsonify(company)

#edit, set company
@app.route("/api/v1/location", methods=["PUT"])
def update_location():
    company_details = request.get_json()
    company_id = company_details["company_id"]
    location_id = company_details["location_id"]
    location_name = company_details["location_name"]
    location_country = company_details["location_country"]
    location_city = company_details["location_city"]
    location_meta = company_details["location_meta"]
    result = Crud.update_location(company_id, location_id,location_name,location_country,location_city,location_meta)
    return jsonify(result)


#delete company
@app.route("/api/v1/location/<location_id>", methods=["DELETE"])
def delete_location(location_id):
    result = Crud.delete_location(location_id)
    return jsonify(result)


#insert company
@app.route("/api/v1/location", methods=["POST"])
def insert_location():
    company_details = request.get_json()
    company_id = company_details["company_id"]
    location_id = company_details["location_id"]
    location_name = company_details["location_name"]
    location_country = company_details["location_country"]
    location_city = company_details["location_city"]
    location_meta = company_details["location_meta"]
    result = Crud.insert_location(company_id, location_id,location_name,location_country,location_city,location_meta)
    return jsonify(result)





#SENSORS
#get all companys
@app.route('/api/v1/sensor', methods=["GET"])
def get_sensor():
    companys = Crud.get_sensors()
    return jsonify(companys)



#get one by id company
@app.route("/api/v1/sensor/<sensor_id>", methods=["GET"])
def get_sensor_by_id(sensor_id):
    company = Crud.get_sensor(sensor_id)
    return jsonify(company)


#edit, set company
@app.route("/api/v1/sensor", methods=["PUT"])
def update_sensor():
    company_details = request.get_json()
    location_id = company_details["location_id"]
    sensor_id = company_details["sensor_id"]
    sensor_name = company_details["sensor_name"]
    sensor_category = company_details["sensor_category"]
    sensor_meta = company_details["sensor_meta"]
    sensor_api_key = company_details["sensor_api_key"]
    result = Crud.update_sensor(location_id,sensor_id,sensor_name,sensor_category,sensor_meta,sensor_api_key)
    return jsonify(result)


#delete company
@app.route("/api/v1/sensor/<sensor_id>", methods=["DELETE"])
def delete_sensor(sensor_id):
    result = Crud.delete_sensor(sensor_id)
    return jsonify(result)


#insert company
@app.route("/api/v1/sensor", methods=["POST"])
def insert_sensor():
    company_details = request.get_json()
    location_id = company_details["location_id"]
    sensor_id = company_details["sensor_id"]
    sensor_name = company_details["sensor_name"]
    sensor_category = company_details["sensor_category"]
    sensor_meta = company_details["sensor_meta"]
    sensor_api_key = company_details["sensor_api_key"]
    pass_api_key = str(Crud.get_pass_admin('admin'))
    try:
        #if('1'=='1'):
        if pass_api_key == sensor_api_key:
            result = Crud.insert_sensor(location_id, sensor_id, sensor_name, sensor_category, sensor_meta, sensor_api_key)
            return jsonify(result)
        else:
            print(repr(pass_api_key) ),
            print(repr(sensor_api_key))
            return jsonify({"error": "Api_key incorrecta o se está ocupando un id ya existente"})
        
    except Exception as ex:
        return jsonify({"error": str(ex)})
    




#SENSOR_DATA
#get all companys
@app.route('/api/v1/sensor_data', methods=["GET"])
def get_sdatas():
    companys = Crud.get_sdatas()
    return jsonify(companys)

#get one by id company
@app.route("/api/v1/sensor_data/<sensor_id>", methods=["GET"])
def get_sensordata_by_id(sensor_id):
    company = Crud.get_sdata(sensor_id)
    return jsonify(company)

#edit, set company
@app.route("/api/v1/sensor_data", methods=["PUT"])
def update_sdata():
    company_details = request.get_json()
    sensor_magnitude = company_details["sensor_magnitude"]
    sensor_id = company_details["sensor_id"]
    sensor_api_key = company_details["sensor_api_key"]
    result = Crud.update_sdata(sensor_id, sensor_magnitude, sensor_api_key)
    return jsonify(result)


#delete company
@app.route("/api/v1/sensor_data/<id>", methods=["DELETE"])
def delete_sdata(id):
    result = Crud.delete_company(id)
    return jsonify(result)


    
    
@app.route("/api/v1/sensor_data/", methods=["POST"])
def insert_sdata():
    company_details = request.get_json()
    sensor_magnitude = company_details["sensor_magnitude"]
    sensor_id = company_details["sensor_id"]
    sensor_api_key = company_details["sensor_api_key"]
  

    pass_api_key = str(Crud.get_pass_admin('admin'))

    try:
        #if('1'=='1'):
        if (pass_api_key == sensor_api_key):
            result = Crud.insert_sdata(sensor_id,sensor_magnitude, sensor_api_key)
            return jsonify(result)
        else:
            print(repr(pass_api_key) ),
            print(repr(sensor_api_key))
            return jsonify({"error": "Api_key incorrecta o se está ocupando un id ya existente"})
        
    except Exception as ex:
        return jsonify({"error": str(ex)})



#GET ADMINS
@app.route('/api/v1/admin', methods=["GET"])
def get_admins():
    companys = Crud.get_admins()
    return jsonify(companys)

#get one by id company
@app.route("/api/v1/admin/<username>", methods=["GET"])
def get_admin_by_username(username):
    company = Crud.get_admin(username)
    return jsonify(company)



#MAIN
if __name__ == "__main__":
    Create_tables()
    print(Crud.get_pass_admin('admin'))
    app.run(host='0.0.0.0', port=8000, debug=True)
    