# Author: Tiffany Patafio, September 2018
##############################
# Code written to retrieve and report the next stop of all busses on a given line
##############################
# put your API key and bus line as input argument:
# i.e. run the code as
#      python get_bus_info_tp1600.py <APIKEY> <Bus line> <outputfile.csv>
#
#making Python 2 & 3 compatible, importing packages
from __future__ import print_function
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import json
import os
import sys

# this line checks the number of arguments and produces an error
if not len(sys.argv)==4:
    print("Invalid number of arguments run as: python get_bus_info_tp1600.py <APIKEY> <Bus line> <outputfile.csv>")
    sys.exit()
    
    
# this line pulls the results and puts them into a data dictionary
key=sys.argv[1]
bus=sys.argv[2]
filenm=sys.argv[3]
page="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(key, bus)
response=urllib.urlopen(page)
data=response.read().decode("utf-8")
dataDict=json.loads(data)

#the following code opens the filename specified for writing
fout = open(filenm, "w")

#the following processes the data to pull out the appropriate values for writing to file
buses=dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
fout.write('Latitude,Longitude,Stop Name,Stop Status \n')
for i in range(0,len(buses)):
    try:
        status=dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    except KeyError:
        status='N/A'
    try:
        stop=dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    except KeyError:
        stop='N/A'
    lat=dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    long=dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    fout.write('%s,%s,%s,%s\n'%(lat,long, stop, status))
print('Success, check your files for', filenm)
