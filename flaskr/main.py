from flask import Flask
from flask_restful import Resource, Api, reqparse
import requests
from datetime import date
from datetime import datetime
from pvlib import solarposition
import json


app = Flask(__name__)
api = Api(app)


class Default(Resource):

    def get(self):
        
        return { "Info": "for Chek Glare API use /checkglare with post"}
    

class CheckGlare(Resource):
   
    def post(self):
        
        today = date.today()
        
        parser = reqparse.RequestParser()
        
        parser.add_argument('lat', type = float, help='Latitude')
        parser.add_argument('long', type = float, help='Longitude')
        parser.add_argument('epoch', type = float, help='epoch time')
        parser.add_argument('orientation', type = float, help='orientation')
        
        args = parser.parse_args()
        
        args_time = datetime.fromtimestamp(args["epoch"])
        
        print(" args vales are: time: " + str(args_time) )
        print(" args vales are: lat: " + str(args["lat"] ) )
        print(" args vales are: long: " + str(args["long"]) )
        
    
        solarpos = solarposition.get_solarposition(
            time = args_time, 
            latitude = args["lat"], 
            longitude = args["long"],
            altitude = None,
            pressure = None)
        
        solarpos_data = json.loads(solarpos.to_json())
        
        zenith = solarpos_data["zenith"]
        elevation = solarpos_data["elevation"]
        azimuth = solarpos_data["azimuth"]
        
        glare = False
        
        
        
        if ( ( list(azimuth.values())[0] - args["orientation"]) < float(30) and list(azimuth.values())[0] > float(45)):
            glare = True

        return { "glare" : glare }
    
api.add_resource(Default, '/')
    
api.add_resource(CheckGlare, '/checkglare')

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    

