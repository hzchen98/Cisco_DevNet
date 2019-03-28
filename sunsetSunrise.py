# -*- coding: utf-8 -*-
# Mostrar el horario de salida y puesta de sol según la coordenada

import requests

# coodenadas Madrid
ciudad = "Madrid"
latitud = 40.4168
longitud = -3.7038

api_web = "https://api.sunrise-sunset.org/json?lat=%s&lng=%s" % (latitud, longitud)

url_requests = api_web

response = requests.get(url_requests).json()

times = response['results']

print("Hora de salida y puesta de sol y otros de la ciudad", ciudad)

for text, time in times.items():
	print(text, ":", time)