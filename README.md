#Executive Summary

These scripts are meant to eventually work with the SocrataRequest object and store a normalized table of GIS location tied to address. The advantage of starting with the public csv file that the site addresses have the same style while the CO business database has variations based on how someone registers a business inputs the information. There may be major differences between the data that google has and the data that Socrata has on businesses, meaning we will have to develop a flexible work-around. 

##Data Sources

T most up-to-date csv of commercial properties can be found here: 

http://data.denvergov.org/dataset/city-and-county-of-denver-real-property-apartment-and-commercial-characteristics

For testing purposes, test_data.csv is shortened to 64 rows so we don't hit the Google Maps API limit in a single test. You will also notice "test_" prepended file names that correspond to the unittests. 

##Installation 

This repository requires Python 3.4 and the following:

```
sqlite3 for windows

googlemaps Python package (pip install googlemaps)
```

An executable for sqlite3 is included for conveneince's sake. 

##Goals

* Eventually, it would be good to move to PostgreSQL, as it has a native column definition that works really well with GIS data (i.e. GPS location)
* We'll need to store this information so that we don't end up relying on the Google Maps API on the backend of ChurnOver. That could be too costly. Ideally, as an address comes in, this database would be the first place that it would look - grab the coordinates, and then use those coordinates for use with Socrata.
..* To this end, feel free to get your own Maps API key at https://console.developers.google.com
* Ultimately bring in the 'basics' that any real estate brokerage firm would expect from a data service. 


