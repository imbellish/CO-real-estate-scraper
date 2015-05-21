import unittest
import sqlite3
import csv

import googlemaps

from main import create_tables, get_location
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
		print(result)

	def test_gets_gps_data(self):
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
		location = get_location(data)
		print(location)



if __name__ == '__main__':
	unittest.main()
