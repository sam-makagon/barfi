import requests
import json

url = "http://localhost:5000/api/sensors"
data = {'station_name':'bunn', 'sensor_data':'click'}
headers = {'Content-type': 'application/json'}
r = requests.post(url, data=json.dumps(data), headers=headers)

print r.status_code, r.text
