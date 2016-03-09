import urllib
import re

x = raw_input("Enter Latitude: ")
y = raw_input("Enter Longitude: ")

link = "http://api.openweathermap.org/data/2.5/weather?lat="+x+"&lon="+y+"&appid=1b6b39cb2dc261ce54833d45b82a8263"
data = urllib.urlopen(link).read()

x = data.split('"')
k = False
for i in range(len(x)):
    if x[i] == "main":
        if not k:
            weather = x[i+2]
            k = True
        else:
            temp = re.findall('\d+', x[i+3])

if weather == "rain":
    print "I'm singing in the rain!"
celcius = int(temp[0])-273
if celcius > 20:
    print "nice..."
elif celcius < 5:
    print "brrrr"

raw_input()
