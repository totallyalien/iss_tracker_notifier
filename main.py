import requests
import datetime as dt
import time
import math
import smtplib


LAT = 11.504776
LONG = 77.238396
MY_MAIL = "xyz@gmail.com"
PASSWORD = "XXXXXXXX"
TO_MAIL = "xxxxxx"

parameter = {
    "lat":LAT,
    "lng":LONG,
    "formatted":0
}

while(True):

    Sleep_time = 60*30
    sun_response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)
    data = sun_response.json()

    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_data = iss_response.json()


    sunrise = data["results"]['sunrise'].split("T")[1].split(":")
    sunset = data["results"]["sunset"].split("T")[1].split(":")


    now  = dt.datetime.now(dt.timezone.utc)


    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_long = float(iss_data["iss_position"]["longitude"])




    if (int(sunset[0])<now.hour) & (int(sunrise[0])<now.hour):
        if (math.dist([iss_lat],[LAT])<=5) & (math.dist([iss_long],[LONG])<=5):
            Sleep_time = 60*60*18
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=MY_MAIL,password=PASSWORD)
            connection.sendmail(from_addr=MY_MAIL,to_addrs=TO_MAIL,msg="Subject:ALERT \n\n INTERNATIONAL SPACE STATION IS AROUND YOU !")
            connection.close()
    time.sleep(Sleep_time)

