from flask import Flask, request, session, render_template, url_for, flash
import requests

from random import choice, randint, uniform
from datetime import datetime, timedelta

app = Flask(__name__)


def api_insight():
    api_get = requests.get("https://api.nasa.gov/insight_weather/?api_key=ZTlhs6euFl3voDLilUFxmBarheLUICgNEbdc7TA3&feedtype=json&ver=1.0").json()
    try:
        sol = api_get[api_get["sol_keys"][0]]
    except:
        return ["No Weather Data Available!"]
    text = ""
    at = sol.get("AT")
    hws = sol.get("HWS")
    pre = sol.get("PRE")
    if at:
        text += f"Atmospheric Pressure: {at['av']}"
    if hws:
        text += f"Wind Speed: {hws['av']}"
    if pre:
        text += f"Atmospheric Pressure: {pre['av']}"
    return [text]


def api_marsroverphotos():
    text = ""
    photos = []
    for i in range(6):
        rover = choice(["curiosity", "opportunity", "spirit"])
        sol_dict = choice(requests.get(f"https://api.nasa.gov/mars-photos/api/v1/manifests/{rover}?api_key=ZTlhs6euFl3voDLilUFxmBarheLUICgNEbdc7TA3").json()["photo_manifest"]["photos"])
        sol = sol_dict["sol"]
        camera = choice(sol_dict["cameras"])

        photo_dict = choice(requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?sol={sol}&camera={camera}&api_key=ZTlhs6euFl3voDLilUFxmBarheLUICgNEbdc7TA3").json()["photos"])
        photo = photo_dict["img_src"]
        photos.append(photo)
        text += f"Image {i + 1}: Taken from {rover.title()}'s {photo_dict['camera']['full_name']} after {sol + 1} SOLs from landing (on {photo_dict['earth_date']})! "
    photos.insert(0, text)
    return photos

def api_apod():
    apod_dict = requests.get("https://api.nasa.gov/planetary/apod?api_key=ZTlhs6euFl3voDLilUFxmBarheLUICgNEbdc7TA3").json()
    return [apod_dict["explanation"], apod_dict["hdurl"]]

def api_exoplanet():
    num_planets = randint(5, 20)
    exoplanets_total = requests.get("https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=pl_hostname,pl_discmethod&order=dec&format=json").json()
    exoplanets = ""
    for i in range(num_planets):
        exoplanet = choice(exoplanets_total)
        exoplanets += f"You discovered exoplanet {exoplanet['pl_hostname']} through {exoplanet['pl_discmethod']}! "
    return [exoplanets]

def api_eonet():
    events_api = requests.get("https://eonet.sci.gsfc.nasa.gov/api/v3/events?status=open&limit=6").json()["events"]
    events = ""
    for i in range(6):
        event = choice(events_api)
        events += f"{event['title']} - {', '.join([x['title'] for x in event['categories']])}"
    return [events]

def api_epic():
    epic_api = requests.get("https://api.nasa.gov/EPIC/api/natural?api_key=ZTlhs6euFl3voDLilUFxmBarheLUICgNEbdc7TA3").json()
    text = "Images were taken by NASA's EPIC camera onboard the NOAA DSCOVR spacecraft."
    images = []
    for i in range(3):
        epic = choice(epic_api)
        date_ = epic['date'].split(" ")[0].replace("-", "/")
        images.append(f"https://epic.gsfc.nasa.gov/archive/natural/{date_}/png/{epic['image']}.png")
    images.insert(0, text)
    return images

def api_tle():
    num_satelites = randint(30, 80)
    satelites_total = requests.get("https://tle.ivanstanojevic.me/api/tle").json()["member"] 
    satelites = "New Satellites: "
    for i in range(num_satelites):
        satelite = choice(satelites_total)
        satelites += f"Satelite {satelite['name']}, "
    return [satelites]


apis = [
    ["Insight API", api_insight, "perseverance"],
    ["Mars Rover Photos API", api_marsroverphotos, "perseverance"],
    ["APOD API", api_apod, "outerspace"],
    ["Exoplanet API", api_exoplanet, "outerspace"],
    ["EONET API", api_eonet, "earth"],
    ["EPIC API", api_epic, "earth"],
    ["TLE API", api_tle, "earth"]
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/perseverance")
def perserverance():
    return render_template("perseverance.html")

@app.route("/outerspace")
def outerspace():
    return render_template("outerspace.html")

@app.route("/earth")
def earth():
    return render_template("earth.html")

@app.route("/api/<int:num>")
def api(num):
    return render_template("api.html", api=apis[num][0], result=apis[num][1](), story=apis[num][2])

if __name__ == "__main__":
  app.run(host="0.0.0.0")
