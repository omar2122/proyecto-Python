from flask import Flask, render_template, request
import requests
import math

app = Flask(__name__)

api_key = "ac215244e0eced8937d362007a6935a8"

@app.route("/", methods=["GET","POST"])
def index():
    clima = None
    
    if request.method == "POST":
        ciudad = request.form["ciudad"]
        print("Ciudad recibida:", ciudad)
        url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
        print("URL:", url)
        respuesta = requests.get(url).json()
        print(respuesta)

        if respuesta.get("cod") == 200:
            clima = {
                "ciudad": respuesta["name"],
                "temp": round(respuesta["main"]["temp"]),
                "feels_like": round(respuesta["main"]["feels_like"]),
                "temp_min": math.floor(respuesta["main"]["temp_min"]),
                "temp_max": math.ceil(respuesta["main"]["temp_max"]),
                "humidity": respuesta["main"]["humidity"],
                "wind": round(respuesta["wind"]["speed"]),
                "desc": respuesta["weather"][0]["description"],
                "weather_id": respuesta["weather"][0]["id"],
                "icon": respuesta["weather"][0]["icon"]
            }

    return render_template("index.html", clima=clima)

app.run(debug=True)