#!usr/bin/env python
# https://www.studytonight.com/network-programming-in-python/pygeoip-module
import pygeoip
ip = '31.10.154.43'

gi = pygeoip.GeoIP('hackingetico/geolitecity-data/GeoLiteCity.dat')
def printRecord(ip):
	rec = gi.record_by_name(ip)
	city = rec['city']
	country = rec['country_name']
	longitude = rec['longitude']
	lat = rec['latitude']
	print ('[+] Address: '  + ip + ' Geo-located ')
	print ('[+] ' +str(city)+ ', '+str(country))
	print ('[+] Latitude: ' +str(lat)+ ', Longitude: '+ str(longitude))

printRecord(ip)