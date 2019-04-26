from googlegeocoder import GoogleGeocoder
import math
import csv


def getlatlong(address):
    geocoder = GoogleGeocoder("Google-Map-api-keys-xxxxxxxxxxxxx")
    search = geocoder.get(address)
    return(search[0].geometry.location.lat, search[0].geometry.location.lng)

def distance(originlat,originlong, destinationlat,destinationlong):
    lat1 = originlat
    lon1 = originlong
    lat2 = destinationlat
    lon2 = destinationlong
    radius = 6371 # for km = 6371 for mile = 3959
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

address_list = [
    "49 BENLAMOND AVE APT 1 M4E1Y8 ",
    "4801 KEELE STREET  M3J3A4 ",
    "111 ELIZABETH STREET  M5G 1P7 ",
    "19 BRANT STREET  M5V 2L2 ",
    "100 DYNAMIC DRIVE  M1V 5C4 ",
]



start_address = "young and dundas"
inlat,inlong = getlatlong(start_address)
output_data = [["address","lat","long","distance"]]

for i in address_list:
    row = []
    deslat,deslong = getlatlong(i)
    row.append(i)
    row.append(deslat)
    row.append(deslong)
    distance1 = distance(inlat,inlong,deslat,deslong)
    row.append(distance1)
    output_data.append(row)

with open("distance_output.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        for row in output_data:
            writer.writerow(row)
        f.close()