# Calculates the distance between two cities and allows the user to specify a unit of distance.
# This program may require finding coordinates for the cities like latitude and longitude.

import sys
import math
global kmConversions
kmConversions = {
	'meter': 1000, 
	'millimeter': 1000000, 
	'mile':0.621371, 
	'feet':3280.84, 
	'inches': 39370.1, 
	'nautmile': 0.539957,
}

#Converts kilometer to other unit of distance.
def ConvertKmTo(distance, unit):
	"""
	Converts kilometers into any unit of distance defined in kmConversions and returns that value
	"""
	return distance * kmConversions[unit]
	
class Coord(object):
	"""
	Coordinate class for use with latitude and longtitude calculation and representations.
	"""
	def __init__(self, deg = 0, min = 0, sec = 0, sign = "+"):
		self.degree = deg
		self.minute = min
		self.second = sec
	def getCoord(self):
		return (self.degree, self.minute, self.second)
	def getDegree(self):
		return self.degree + self.minute/60 + self.second/60/60
	
class EarthCoord(object):
	"""
	Representation of the earth coordinates of a location on the planet earth
	"""
	def __init__(self, lat, long):
		if(len(list(lat)) != 4):
			lat = [0, 0, 0, '+']
		if(len(long) != 4):
			long = [0, 0, 0, '+']
		self.latitude = Coord(lat[0], lat[1], lat[2]) 	#[Degrees, Minutes, Seconds] Positive is Eastern, Negative is Western
		self.longitude = Coord(long[0], long[1], long[2])	#[Degrees, Minutes, Seconds] Positive is North, Negative is Southern
	def setLatitude(deg, min, sec):
		self.latitude.degree = deg
		self.latitude.minute = min
		self.latitude.second = sec
	def setLongitude(deg, min, sec):
		self.longitude.degree = deg
		self.longitude.minute = min
		self.longitude.second = sec
	# measures the distance between itself and another coordinate measured in kilometers
	def distance(self, coordinate):
		r = 6371 #Average Radius of the earth
		#implement Haversine Distance formula
		lat1 = math.radians(self.latitude.getDegree())
		lat2 = math.radians(coordinate.latitude.getDegree())
		deltaLat = math.radians(self.latitude.getDegree() - coordinate.latitude.getDegree())
		deltaLong = math.radians(self.longitude.getDegree() - coordinate.longitude.getDegree())
		a = math.sin(deltaLat/2) ** 2 + math.cos(lat1) * math.cos(lat2) * (math.sin(deltaLong/2) ** 2)
		c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
		distance = r * c
		return distance

#test Module
#module works, too lazy to make a UI for it.
if __name__ == '__main__':
	portland = EarthCoord([45,52,36,'+'],[122,67,50,'-'])
	denver = EarthCoord([39,73,92,'+'], [104,98,42,'-'])
	print("The distance from Portland to Denver is:")
	distance = portland.distance(denver)
	print(str( round(distance, 2 ) ) + " km")
	print(str( round(ConvertKmTo(distance, 'meter'), 2 ) ) + " m")
	print(str( round(ConvertKmTo(distance, 'millimeter'), 2 ) ) + " mm")
	print(str( round(ConvertKmTo(distance, 'mile'), 2 ) ) + " miles")
	print(str( round(ConvertKmTo(distance, 'feet'), 2 ) ) + " feet")
	print(str( round(ConvertKmTo(distance, 'inches'), 2 ) ) + " inches")
	print(str( round(ConvertKmTo(distance, 'nautmile'), 2 ) ) + " nautical miles")