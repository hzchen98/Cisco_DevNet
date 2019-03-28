# -*- coding: utf-8 -*-
# Obtener cantidad de personas que hay en la estación espacial internacional

import requests

api_web = "http://api.open-notify.org/astros.json"

response = requests.get(api_web).json()

print("Existe %d persona actualmente en la estación espacial internacional." % response['number'])
print("Sus nombres son:")

for persona in response['people']:
	print("\t"+persona['name'])