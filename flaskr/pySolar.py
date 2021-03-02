from pysolar import solar
import datetime
import pytz



class PySolar():
        
        def get_solarposition(arg_time,arg_lat,arg_long):
            
            return_data = {}
            
            
            arg_date = datetime.datetime(2021, 2, 18, 15, 13, 1, 130320, tzinfo=pytz.timezone("America/Los_Angeles"))
            
            zenith = (90 - solar.get_altitude(arg_lat, arg_long, arg_date))
            
            azimuth = solar.get_azimuth(arg_lat, arg_long, arg_date)
            
            return_data['zenith'] = zenith
            return_data['azimuth'] = azimuth
         
            return return_data