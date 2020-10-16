# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 13:04:55 2020

@author: Kevin Nem
"""

import numpy as np
import pandas as pd

liquids_df= pd.read_csv('Liquids_China_Myanmar.csv')
liquids_df['Seller (origin)'].count()
liquids_df['Other seller'] = liquids_df['Seller (origin)'].str.contains(',')
liquids_df['Seller exists'] = liquids_df['Seller (origin)'].notnull()


liquids_df['date'] = pd.to_datetime(liquids_df['Date (origin)'])
liquids_df.groupby(pd.Grouper(key='date', freq='1M'))['Seller (origin)'].count()
liquids_df.groupby(pd.Grouper(key='date', freq='1M'))['Seller exists'].count()
liquids_df.groupby(pd.Grouper(key='date', freq='1M'))['Other seller'].count()
