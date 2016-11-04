import requests
import json

def lambda_handler(event, context):
    url = "http://ec2-52-91-51-209.compute-1.amazonaws.com:5000/api/sensors"
    data = {'station_name':'bunn', 'sensor_data':'click'}
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    
    print r.status_code, r.text
    return r.status_code, r.text
