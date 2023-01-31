import requests

LAT = 11.504776
LONG = 77.238396

parameter = {
    "lat":LAT,
    "lng":LONG
}



response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)
print(response.json())