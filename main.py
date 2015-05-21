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
	
	# takes the tuple, (1115, N, Logan, ST)
	# and morphs it into an array/list
	address = list(address)
	searchfor = ""
	for word in address:
		# for each item in that list concatenates to string
		searchfor += word + " "
	# takes that string and calls the Maps API
	gmaps = googlemaps.Client(key=GMAPS_API)
	geo_result = gmaps.geocode(searchfor + "Denver, CO")
	# TODO parse geo_result
	# location should be found here
	return geo_result

	


