# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 20:20:20 2020

@author: knem
"""


import requests
import json

def kpler_login():
    base_url = "https://api-cpp.kpler.com"
    credentials = {'email': 'knem@kpler.com', 'password': 'knem31270'}
    headers_login ={'Content-type':'application/json'}
    response = requests.post(base_url + '/login', data=json.dumps(credentials), headers= headers_login)

kpler_login()