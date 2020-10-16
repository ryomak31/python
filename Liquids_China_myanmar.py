#import library
import requests
import json
import io
import pandas as pd
# import datetime as dt
# import sys

#Connecting to the database & setting connexion parameters
lng = "https://api-lng.kpler.com/v1"

base_url = "https://api.kpler.com/v1"
credentials = {'email': 'knem+1@kpler.com', 'password': 'kplerkpler'}
headers_login ={'Content-type':'application/json'}
response = requests.post(base_url + '/login', data=json.dumps(credentials), headers= headers_login)
print(response.status_code)

if response.status_code != 200:
    raise Exception('Failed to authenticate')
else:
    token = response.json()['token']
    headers ={'Authorization':token}
    print('Fetching data')

response = requests.get(base_url + '/trades?toZones=China,Myanmar&products=crude/co&withIntracountry=false&startDate=2018-01-01&hash=fdf16ca659a8c41c29a6cce0d09625a8' , headers=headers,)
response.status_code

buff = io.StringIO(response.content.decode('UTF-8'))
liquids = pd.read_csv(buff, delimiter=';')
liquids.to_csv('Liquids_China_Myanmar.csv', index =False)
print('Done')
