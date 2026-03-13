import requests

api_key = "ac215244e0eced8937d362007a6935a8"

ciudad = input("Introduce una ciudad: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"

respuesta = requests.get(url)

datos = respuesta.json()
print("",'\n')
print("Ciudad:", datos["name"])
print("",'\n')

print("Temperatura:", datos["main"]["temp"], "°C")
print("Sensación térmica:", datos["main"]["feels_like"], "°C")
print("Temperatura mínima:", datos["main"]["temp_min"], "°C")
print("Temperatura máxima:", datos["main"]["temp_max"], "°C")
print("Humedad: ", datos["main"]["humidity"], "%")
print("Viento:", datos["wind"]["speed"], "Km/h")

print("Clima:", datos["weather"][0]["description"])
print("ID clima:", datos["weather"][0]["id"])
print("imagen Clima:", "https://openweathermap.org/img/wn/" + datos["weather"][0]["icon"] + "@2x.png")


