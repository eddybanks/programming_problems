import sys
import json
from geopy import distance

if len(sys.argv) > 1:
  iata_code = sys.argv[1] 
else:
  print("You need to include an IATA code as an argument")
  sys.exit()
chosen_port = {}
connecting_ports = []
with open('airports.json') as json_file:
  airports = json.load(json_file)
  for airport in airports:
    if iata_code == airport["IATA/FAA"]:
      chosen_port["airport"] = airport
      chosen_port['connecting_ports'] = []

  for airport in airports:
    if airport['Airport ID'] in chosen_port['airport']['destinations']:
      port = {"iata": airport['IATA/FAA'], "name": airport['Name'], "distance": distance.distance([airport['Latitude'], airport['Longitude']], 
        [chosen_port['airport']['Latitude'], chosen_port['airport']['Longitude']])}
      chosen_port['connecting_ports'].append(port)

ports_by_distance = sorted(chosen_port['connecting_ports'], key = lambda n: n["distance"])
if len(chosen_port) > 0:
  for port in ports_by_distance:
    print(port["iata"], port["name"], port["distance"])
else:
  print("The airport with IATA code '{}' does not exit!".format(iata_code))