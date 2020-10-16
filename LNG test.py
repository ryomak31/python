# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 17:10:37 2020

@author: Kevin Nem
"""

#import library
import requests
import json
import io
import pandas as pd
# import datetime as dt
# import sys

#Connecting to the database & setting connexion parameters
base_url = "https://api-lng.kpler.com/v1"
credentials = {'email': 'knem@kpler.com', 'password': 'knem31270'}
headers_login ={'Content-type':'application/json'}
response = requests.post(base_url + '/login', data=json.dumps(credentials), headers= headers_login)
print(response.status_code)

if response.status_code != 200:
    raise Exception('Failed to authenticate')
else:
    token = response.json()['token']
    headers ={'Authorization':token}
    print('Fetching data')


response = requests.get(base_url + '/trades?startDate=2009-01-01&fromZones=United States&toZones=Europe&columns=all&withIntracountry=false' , headers=headers,)
response.status_code

buff = io.StringIO(response.content.decode('UTF-8'))
lng = pd.read_csv(buff, delimiter=';')
lng.to_csv('United2.csv', index =False)
print('Done')
