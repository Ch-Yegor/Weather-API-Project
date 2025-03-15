import os

import requests
import sys

from flask import Flask, jsonify, redirect, render_template, request
from dotenv import load_dotenv

import json

import redis
from redis.cache import CacheConfig

import datetime

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv("API_KEY")

redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

def apology(message, code=400):

    def escape(s):
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s
    
    data = []
    words = []
    script = False
    return render_template("index.html", data=data, words=words, script=script, top=code, bottom=escape(message)), code

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city_name = request.form.get("city")

        city_json = redis_client.get(f"{city_name}")

        if city_json is None:
            response = requests.request("GET", f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city_name}?unitGroup=metric&key={API_KEY}&contentType=json")
            if response.status_code == 400:
                return apology("incorrect city name :(", response.status_code)
            elif response.status_code != 200:
                return apology("API is down :(", response.status_code)
            json_data = response.json()
            redis_client.set(f"{city_name}", json.dumps(json_data), ex=1800)
            city_json = redis_client.get(f"{city_name}")

        data = json.loads(city_json)
        days = data["days"]
        
        date_string = datetime.datetime.strptime(days[0]['datetime'], "%Y-%m-%d").strftime("%d.%m.%Y")
        tempmax = str(days[0]['tempmax']) + "°C"
        tempmin = str(days[0]['tempmin']) + "°C"
        precipprob = str(days[0]['precipprob']) + "%"
        humidity = str(days[0]['humidity']) + "%"
        windspeed = str(days[0]['windspeed']) + "km/h"
        description = days[0]['description']

        temp = str(data["currentConditions"]["temp"]) + "°C"
        feelslike = str(data["currentConditions"]["feelslike"]) + "°C"
        icon = data["currentConditions"]["icon"]

        words = ["Feels like", "Precipitation", "Max temp", "Min temp", "Humidity", "Wind speed"]

        script = True

        return render_template("index.html", data=data, datetime=date_string, tempmax=tempmax, tempmin=tempmin, precipprob=precipprob, humidity=humidity, windspeed=windspeed, description=description, temp=temp, feelslike=feelslike, icon=icon, words=words, script=script)

    data = []
    words = []
    script = False
    return render_template("index.html", data=data, words=words, script=script)