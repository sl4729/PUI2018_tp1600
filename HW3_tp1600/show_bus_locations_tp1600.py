# Author: Tiffany Patafio, September 2018
##############################
# Code written to retrieve and report information about active vehicles for a bus line
##############################
# put your API key and bus line as input argument:
# i.e. run the code as
#      python show_bus_locations_tp1600.py <APIKEY> <Bus line>
#
#making Python 2 & 3 compatible
from __future__ import print_function
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import json
import os
import sys

# this line checks the number of arguments and produces an error
if not len(sys.argv)==3:
    print("Invalid number of arguments run as: python show_bus_locations_tp1600.py <APIKEY> <Bus line>")
    sys.exit()
    
    
# this line pulls the results and puts them into a data dictionary
key=sys.argv[1]
bus=sys.argv[2]
page="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(key, bus)
response=urllib.urlopen(page)
data=response.read().decode("utf-8")
dataDict=json.loads(data)

#the following processes the data to pull out the appropriate values for printing
buses=dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
print('Bus line:',bus)
print('Number of buses:',len(buses))
ind=0
for i in buses:
    i=i['MonitoredVehicleJourney']
    print('Bus', ind, 'is at latitude', i['VehicleLocation']['Latitude'], 'and longitude', i['VehicleLocation']['Longitude'])
    ind+=1