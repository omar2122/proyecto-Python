from flask import Flask, render_template, request
import requests

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
                "temp": respuesta["main"]["temp"],
                "desc": respuesta["weather"][0]["description"]
            }

    return render_template("index.html", clima=clima)

app.run(debug=True)