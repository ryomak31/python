# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 01:53:14 2020

@author: knem
"""

#import library
import requests
import json
import io
import pandas as pd
# import datetime as dt
# import sys

#Connecting to the database & setting connexion parameters
base_url = "https://api.kpler.com/v1"
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

response = requests.get(base_url + '/trades?startDate=2017-01-01&hash=fdf16ca659a8c41c29a6cce0d09625a8' , headers=headers,)
response.status_code

buff = io.StringIO(response.content.decode('UTF-8'))
liquids = pd.read_csv(buff, delimiter=';')
liquids.to_csv('Liquids_China_Myanmartest.csv', index =False)

# GetFleet query

# getfleet = requests.get(base_url +'/vessels?columns=all', headers=headers)
# getfleet.status_code

# if not getfleet.content:
#     print('No Data')
# else:
#     buff = io.StringIO(getfleet.content.decode('UTF-8'))
#     reader_df = pd.read_csv(buff, delimiter=';')
#     reader_df.to_csv('Liquids_GetVessel_' + dt.datetime.now().strftime("%F") + '.csv', index =False)
#     print('Done')


# # GetTrade query
# gettrade_2017 = requests.get(base_url + '/trades?&endDate=2017-12-31', headers=headers,)
# gettrade_2017.status_code

# if not gettrade_2017.content:
#     print('No Data')
# else:
#     buff = io.StringIO(gettrade_2017.content.decode('UTF-8'))
#     df_gettrade17 = pd.read_csv(buff, delimiter=';')
#     df_gettrade17.to_csv('Liquids_GetTrade_2017_' + dt.datetime.now().strftime("%F") + '.csv', index =False)
#     print('Done')
    
# df_gettrade17 =pd.read_csv('Liquids_GetTrade_2017_2020-09-14.csv')

# merged_df = df_gettrade17.append(df_gettrade18, ignore_index = True)
                                 

# gettrade_2018 = requests.get(base_url +'/trades?startDate=2018-01-01&endDate=2018-01-02', headers=headers,)
# gettrade_2018.status_code

# gettrade_2019 = requests.get(base_url +'/trades?startDate=2019-01-01&endDate=2019-12-31', headers=headers,)
# gettrade_2019.status_code
    
# gettrade_2020 = requests.get(base_url +'/trades?startDate=2020-01-01&endDate=2020-10-01', headers=headers,)
# gettrade_2020.status_code


gettrade = requests.get(base_url +'/trades?startDate=2020-01-01&endDate=2020-10-01', headers=headers,)
gettrade.status_code

# if not gettrade_2018.content:
#     print('No Data')
# else:
#     buff = io.StringIO(gettrade_2018.content.decode('UTF-8'))
#     df_gettrade18 = pd.read_csv(buff, delimiter=';')
#     df_gettrade18.to_csv('Liquids_GetTrade_2018_' + dt.datetime.now().strftime("%F") + '.csv', index =False)
#     print('Done')

# if not gettrade_2019.content:
#     print('No Data')
# else:
#     buff = io.StringIO(gettrade_2019.content.decode('UTF-8'))
#     df_gettrade19 = pd.read_csv(buff, delimiter=';')
#     df_gettrade19.to_csv('Liquids_GetTrade_2019_' + dt.datetime.now().strftime("%F") + '.csv', index =False)
#     print('Done')
    
# if not gettrade_all.content:
#     print('No Data')
# else:
#     buff = io.StringIO(gettrade_all.content.decode('UTF-8'))
#     df_gettrade_all = pd.read_csv(buff, delimiter=';')
#     df_gettrade19.to_csv('Liquids_GetTrade_All_' + dt.datetime.now().strftime("%F") + '.csv', index =False)
#     print('Done')





    
