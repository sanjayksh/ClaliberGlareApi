# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests

url = "http://127.0.0.1:5000/checkglare"

img_data = {
            'lat': '49.2699648',
            
            'long': '-123.1290368',
            
            'epoch': '1588704959.321',
            
            'orientation': '-10.2'
}

res = requests.post(url, data = img_data)

print(res.text)





