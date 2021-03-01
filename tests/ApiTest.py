# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from datetime import datetime

#url = "http://54.86.136.32:8080//checkglare"

url = "http://localhost:8080//checkglare"


epoch_time = datetime( 2021,2,13,8,0).timestamp()

print(' the epoch time value is ' + str(epoch_time))

img_data = {
            'lat': '49.2827',
            
            'long': '123.1207',
            
            'epoch': epoch_time,
            
            'orientation': '90.0'
}

res = requests.post(url, data = img_data)

print(res.text)





