from flask import Flask, render_template, request
import requests
import math

app = Flask(__name__)

api_key = "ac215244e0eced8937d362007a6935a8"

@app.route("/", methods=["GET","POST"])
def index():
    clima = None
    traducciones = {}

    
    
    if request.method == "POST":
        ciudad = request.form["ciudad"]
        print("Ciudad recibida:", ciudad)
        url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
        print("URL:", url)
        respuesta = requests.get(url).json()
        print(respuesta)

        if respuesta.get("cod") == 200:
            
            iconos = {
                "clear sky": "sun.png",
                "few clouds": "partly_cloudy.png",
                "scattered clouds": "clouds.png",
                "broken clouds": "clouds.png",
                "overcast clouds": "clouds.png",
                "rain": "rain.png",
                "moderate rain": "rain.png",
                "light rain": "rain.png",
                "snow": "snow.png",
                "thunderstorm": "thunderstorm.png",
                "wind": "wind.png"
            }

            traducciones = {
                "clear sky": "Cielo despejado",
                "few clouds": "Algunas nubes",
                "scattered clouds": "Nubes dispersas",
                "broken clouds": "Muy nublado",
                "overcast clouds": "Totalmente nublado",
                "rain": "Lluvia",
                "moderate rain": "Lluvia moderada",
                "light rain": "Lluvia ligera"             
            }
    
            descripcion = respuesta["weather"][0]["description"]
            icono = iconos.get(descripcion, "snow.png")            
            descripcion = traducciones.get(descripcion, descripcion)
            
            


            clima = {
                "ciudad": respuesta["name"],
                "temp": round(respuesta["main"]["temp"]),
                "feels_like": round(respuesta["main"]["feels_like"]),
                "temp_min": math.floor(respuesta["main"]["temp_min"]),
                "temp_max": math.ceil(respuesta["main"]["temp_max"]),
                "humidity": respuesta["main"]["humidity"],
                "wind": round(respuesta["wind"]["speed"]),
                #"desc": respuesta["weather"][0]["description"],
                "desc": descripcion,            
                "weather_id": respuesta["weather"][0]["id"],
                "icono": icono
                #"icon": respuesta["weather"][0]["icon"]
            }

    return render_template("index.html", clima=clima)

app.run(debug=True)