# https://codeclubprojects.org/en-GB/python/iss/

"""
In this project you will use a web service to find out the current location of the International Space Station (ISS)
and plot its location on a map.
"""

import json
import urllib.request
import turtle
import time

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(result)

print('People in Space : ', result['number'])

people = result['people']
print(people)

for p in people:
    print('{} in {}'.format(p['name'], p['craft']))

url = "http://api.open-notify.org/iss-now.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(result)

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('Latitude: ', lat)
print('Longitude: ', lon)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(float(lon), float(lat))

print("------------------------------------")

# Space Center, Houston
lat = 29.5502
lon = -95.097

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon, lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(result)

over = result['response'][1]['risetime']
print(over)

style = ('Arial', 6, 'bold')
location.write(time.ctime(over), font=style)

# to keep a Python script output window open for 10 seconds to see the output
import time

time.sleep(10)
