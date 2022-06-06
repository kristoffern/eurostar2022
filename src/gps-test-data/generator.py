'''
This is a simple example of how to generate a file containing GPS data points
To test and visualize the resulting test data file (route.csv), simply navigate
to: https://www.gpsvisualizer.com/
'''

import random

lat_pos = 55.637602926318344
long_pos = 12.578643285072149

gps_file = open('route.csv', 'w')
gps_file.write('Type,Latitude,Longitude\n')

for _ in range(100):

	north = random.choice([True, False])
	east = random.choice([True, False])

	if north:
		lat_pos += random.random()/200
	else:
		lat_pos -= random.random()/200

	if east:
		long_pos += random.random()/200
	else:
		long_pos -= random.random()/200

	gps_file.write("T,{},{}\n".format(lat_pos, long_pos))
