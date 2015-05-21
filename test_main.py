import unittest
import sqlite3
import csv

from pprint import pprint

import googlemaps

from main import create_tables, get_location, put_location
from settings import GMAPS_API


class TestMain(unittest.TestCase):
	
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_creates_table_defs(self):
		create_tables(test=True)
		db = sqlite3.connect("test_db.db")
		cursor = db.cursor()
		cursor.execute("SELECT COUNT(*) FROM comm_properties")
		result = cursor.fetchone()
		db.close()
		self.assertEqual(result, (64,), "Incorrect number of rows in test_db")
	def test_connects_with_maps_api(self):
		"""
		Eventually to be thrown into the churn SocrataRequest
		for more accurate address searching.
		"""
		db = sqlite3.connect('test_db.db')
		cursor = db.cursor()
		cursor.execute(
			"""SELECT SITE_NBR, 
			SITE_DIR, SITE_NAME, SITE_MODE FROM comm_properties"""
		)
		data = cursor.fetchone()
		observed = get_location(data)
		expected = (
			39.7733071, 
			-104.8108087, 
			'4005 Chambers Road, Denver, CO 80239, USA'
		)
		db.close()
		pprint(observed)
		self.assertEqual(observed, expected, 
			"Maps API shows different result than expected."
		)
	def test_puts_address_and_gps_data(self):
		"""
		Stores Maps API data and normalized address in 
		a separate database. Data filtering function. 
		"""

		##########################
		db = sqlite3.connect('test_db.db')
		cursor = db.cursor()
		put_location(cursor)
		db.commit()
		##########################
		where = 39.7733071, -104.8108087
		cursor.execute(
			"""
			SELECT pin, lat, lng, address FROM location where lat=? and lng=?
			""",
			where
		)
		##########################
		value = cursor.fetchone()
		self.assertEqual(value, 
			(163000684, 39.7733071, -104.8108087, 
				'4005 Chambers Road, Denver, CO 80239, USA')
		)
		##########################
		db.close()


if __name__ == '__main__':
	unittest.main()
