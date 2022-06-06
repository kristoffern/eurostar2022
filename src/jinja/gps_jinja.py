import random
from jinja2 import Template

gps_coords = []
lat_pos = 50
long_pos = 10

for i in range(10):
	lat_pos += random.random()/200 
	long_pos += random.random()/200 

	gps_coords.append({"lat_pos": lat_pos, "long_pos": long_pos})

t = Template("Type,Latitude,Longitude\n{% for coord in gps_coords %}T,{{coord['lat_pos']}},{{coord['long_pos']}}\n" "{% endfor %}")
output = t.render(gps_coords=gps_coords)

print(output)