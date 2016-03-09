import urllib
import re

print "Please type date in DD/MM/YYYY format "
d = raw_input("Day: ")
m = raw_input("Month: ")
y = raw_input("Year: ")
link = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/"+d+"-"+m+"-"+y+".json"
data = urllib.urlopen(link).read()

x = re.findall('\d+', data)
draws = 157
for i in range(draws):
    for j in range(0, 7):
        k = i*20
        del x[k]
for i in range(80):
    crowd = 0
    number = i+1
    for j in range(len(x)):
        if int(x[j]) == number:
            crowd = crowd+1
    print number, ": ", crowd
raw_input()
