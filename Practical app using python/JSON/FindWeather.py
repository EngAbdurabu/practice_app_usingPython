import requests, json

# section one
base_url = "https://api.openweathermap.org/data/2.5/weather?"
# section two
city_name = input("Enter the city name: ")
# section three
API_key = ""

# complate url
complate_url = base_url + "q="+ city_name+ "&units=metric" + "&appid=" + API_key

response = requests.get(complate_url)
# print(response.text)

x = json.loads(response.text)

if x['cod'] != "404":
	y = x['main']
	current_temperature = y['temp']
	current_pressure = y['pressure']
	current_humidity = y['humidity']

	z = x['weather']
	weather_description = z[0]["description"]

	print("The Temperature is : " + str(current_temperature) +
	      "\nThe Pressure is : " + str(current_pressure) +
	      "\nThe Humidity is : " + str(current_humidity) +
	      "\nThe weather description today: " + str(weather_description)
	)

else:
	print("The city not found ")

