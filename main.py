import os
import googlemaps

from settings import GMAPS_API

def create_tables(test=False):
	if test == True:
		os.system('test_import')
	else:
		os.system('import')

def get_location(address):
	# https://developers.google.com/maps/documentation/geocoding/
	# https://github.com/googlemaps/google-maps-services-python
	address = list(address)
	searchfor = ""
	for word in address:
		searchfor += word + " "
	gmaps = googlemaps.Client(key=GMAPS_API)
	geo_result = gmaps.geocode(searchfor + "Denver, CO")
	# TODO parse geo_result
	return geo_result

	


