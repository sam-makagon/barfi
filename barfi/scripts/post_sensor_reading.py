import requests
import json

#url = "http://ec2-52-91-51-209.compute-1.amazonaws.com:5000/api/sensors"
url = "http://localhost:5000/api/sensors"
data = {'station_name':'bunn', 'sensor_data':'click'}
headers = {'Content-type': 'application/json'}
r = requests.post(url, data=json.dumps(data), headers=headers)

print r.status_code, r.text
