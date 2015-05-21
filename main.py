import os
import googlemaps

from settings import GMAPS_API

def create_tables(test=False):

	if os.name == 'nt':	
		if test == True:
			os.system('test_import')
		else:
			os.system('import')
	if os.name == 'posix':
		if test == True:
			os.system('sh test_import.sh')
		else:
			os.system('sh import.sh')

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
	# parse geo_result to tuple
	result = (
		geo_result[0]['geometry']['location']['lat'],
		geo_result[0]['geometry']['location']['lng'], 
		geo_result[0]['formatted_address']
	)
	# location should be found here
	return result

def put_location(cursor):
	cursor.execute(
		"""SELECT PIN, SITE_NBR, 
		SITE_DIR, SITE_NAME, SITE_MODE FROM comm_properties"""
	)
	rows = cursor.fetchall()
	for row in rows:
		api_request = row[1:]
		data = get_location(api_request)
		data = (row[0], data[0], data[1], data[2])
		cursor.execute(
			"""
			INSERT INTO location VALUES (?, ?, ?, ?)
			""",
			data
		)
	


	


