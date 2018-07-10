"""
The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data,
and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as
within Google Maps.

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
http://py4e-data.dr-chuck.net/geojson?

You can test to see if your program is working with a location of "South Federal University" which will have a place_id
of "ChIJJ8oO7_B_bIcR2AlhC8nKlok".

Test for MSU : you get place_id -> ChIJ94cTgAb2jw0R93FrXChdBDU
"""

import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys for this API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

address = input('Enter location: ')
url = serviceurl + urllib.parse.urlencode({'address': address})

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)
else:
    # print(json.dumps(js, indent=4))
    place_id = js["results"][0]["place_id"]
    print(place_id)
