from datetime import date
from datetime import datetime
from pvlib import solarposition
import json


class PvlibSolarPos():
    
    
    def get_solarposition(arg_time,arg_lat,arg_long):
        
        return_data = {}
        solarpos = solarposition.get_solarposition(
            time = arg_time, 
            latitude = arg_lat, 
            longitude = arg_long,
            altitude = None,
            pressure = None)
         
        solarpos_data = json.loads(solarpos.to_json())
         
        zenith_dict = solarpos_data["zenith"]
        elevation_dict = solarpos_data["elevation"]
        azimuth_dict = solarpos_data["azimuth"]
         
        azimuth = list(azimuth_dict.values())[0]
        zenith = list(zenith_dict.values())[0]
         
        return_data['zenith'] = zenith
        return_data['azimuth'] = azimuth
         
        return return_data
         
    
        
        
        
        
        
        
