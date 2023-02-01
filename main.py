import requests
import datetime as dt

LAT = 11.504776
LONG = 77.238396

parameter = {
    "lat":LAT,
    "lng":LONG,
    "formatted":0
}


sun_response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)
data = sun_response.json()

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_data = iss_response.json()


sunrise = data["results"]['sunrise'].split("T")
sunset = data["results"]["sunset"].split("T")


now  = dt.datetime.now()
print(now.time())

