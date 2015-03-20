#!/usr/bin/env python3

import math

# Introductory statement about program
print("This program will tell you the distance between two points when given the coordinates.")
print("")

# Allows user to change the radius of the sphere
print("Type 1 to change the radius of the sphere.")
print("Press Enter to continue without invoking the option.")
z = input("> ") # User types selection here
if z == "1": # If user types 1
	radius = float(input("What is the radius of the sphere in kilometers? "))
else: # If user types anything else
	radius = 6371 # Earth's radius
print("")

# Coordinate input and variables
latA = float(input("What is the latitude of Point A? "))
lonA = float(input("What is the longitude of Point A? "))
print("")
latB = float(input("What is the latitude of Point B? "))
lonB = float(input("What is the longitude of Point B? "))
print("")

latAr = math.radians(latA)
lonAr = math.radians(lonA)
latBr = math.radians(latB)
lonBr = math.radians(lonB)

# These are the calculations below to find the distance
a = math.radians(abs(90 - latB))
b = math.radians(abs(90 - latA))
c = math.radians(abs(lonA - lonB))
d = math.acos(math.cos(a) * math.cos(b) + math.sin(a) * math.sin(b) * math.cos(c)) * radius
print("The distance from Point A to Point B is", int(d), "kilometers or", int(d * 1.609344), "miles.") # Displays the result

# These are the calculations below to find the bearing
i = int(math.degrees(math.atan2(math.sin(lonBr - lonAr) * math.cos(latBr), math.cos(latAr) * math.sin(latBr) - math.sin(latAr) * math.cos(latBr) * math.cos(lonBr - lonAr)) % (2 * math.pi)))
print("The bearing from Point A to Point B is", str(i) + "°") # Displays the result
print("")

input("Press any key to exit") # Ends program when a key is pressed
exit()
