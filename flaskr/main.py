from flask import Flask
from flask_restful import Resource, Api, reqparse
import requests
from datetime import datetime, date
from pvlib import solarposition
from pvlibSolarPos import PvlibSolarPos
from pySolar import PySolar
import json
import logging
import os
import pytz



app = Flask(__name__)
api = Api(app)

today = date.today()

log_dir = os.path.join(os.path.normpath(os.getcwd()+ os.sep + os.pardir),'logs') 

log_file_suffix = today.strftime("%Y%m%d")

log_file_name = os.path.join(log_dir, 'checkglare_api_'+log_file_suffix+'.log')

logging.basicConfig( filename = log_file_name, level=logging.INFO)


class Default(Resource):

    def get(self):
        
        return { "Info": "for Chek Glare API use /checkglare with post"}
    

class CheckGlare(Resource):
   
    def post(self):
        
        logging.info('In the API call processing')
        
        parser = reqparse.RequestParser()
        
        parser.add_argument('lat', type = float, help='Latitude')
        parser.add_argument('long', type = float, help='Longitude')
        parser.add_argument('epoch', type = float, help='epoch time')
        parser.add_argument('orientation', type = float, help='orientation')
        
        args = parser.parse_args()
        
        args_time = datetime.fromtimestamp(args["epoch"])
        
    
        
        logging.info(" API args vales are: epoch value: " + str(args["epoch"]))
        logging.info(" API args vales are: epoch converted into date: " + str(args_time))
        logging.info(" API API args vales are: latitude: " + str(args["lat"]))
        logging.info(" args vales are: longitude: " + str(args["long"]))
        logging.info(" args vales are: orientation: " + str(args["orientation"]))
        
    
        
        """
        # This call is using pvlibsolar library
        
        solarpos = PvlibSolarPos.get_solarposition(
            arg_time = args_time, 
            arg_lat = args["lat"], 
            arg_long = args["long"] )
        
        """
        
        # This call is using pySolar library
    
        solarpos = PySolar.get_solarposition(
            arg_time = args_time, 
            arg_lat = args["lat"], 
            arg_long = args["long"] )
        
        
        zenith = solarpos["zenith"]
        azimuth = solarpos["azimuth"]
        
        logging.info(" Solar Position zenith Value is: " + str(zenith))
        logging.info(" Solar Position azimuth Value is: " + str(azimuth))
        
        glare = False
        
        
        
        if ( (azimuth - args["orientation"]) < float(30) and  zenith > float(45)):
            glare = True
        
        logging.info(" The Glare query result is " + str(glare))
            
            
            
        return { "glare" : glare }
    
api.add_resource(Default, '/')
    
api.add_resource(CheckGlare, '/checkglare')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080, debug=True)
    
    
    
    

