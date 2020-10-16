# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:55:41 2020

@author: Kevin Nem
"""

def download():
    base_url = "https://api.kpler.com/v1"
    credentials = {'email': 'knem@kpler.com', 'password': 'knem31270'}
    headers_login ={'Content-type':'application/json'}
    response = requests.post(base_url + '/login', data=json.dumps(credentials), headers= headers_login)
    print(response.status_code)