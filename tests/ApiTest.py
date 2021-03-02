# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from datetime import datetime
import pytz

#url = "http://54.86.136.32:8080//checkglare"

url = "http://localhost:8080//checkglare"


for x in range(0, 24):
    
    epoch_time = datetime( 2021,2,13,x,0, tzinfo=pytz.timezone('US/Pacific')).timestamp()
    
    img_data = {
            'lat': '49.2827',
            
            'long': '123.1207',
            
            'epoch': epoch_time,
            
            'orientation': '90.0'}
    
    res = requests.post(url, data = img_data)
    
    print(res.text)





