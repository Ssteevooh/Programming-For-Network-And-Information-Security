import requests
import urllib.parse
from datetime import datetime, timedelta

main_api = "https://api.sunrise-sunset.org/json?"

while True:
    HowUTC = input("Manual UTC type 1 or Automated UTC type 2 or Postal code type 3 or type quit/q to end it ")
    if HowUTC == "quit" or HowUTC == "q":
        break

    if HowUTC == "1":

        lat = input("Give latitude ")
        lng = input("Give longitude ")
        Manual_UTC = input("Is your current UTC + or - ? ")

        url = main_api + urllib.parse.urlencode({"lat": lat, "lng": lng})

        json_data = requests.get(url).json()

        Sunrise = (json_data["results"]["sunrise"])
        Sunset = (json_data["results"]["sunset"])

        # Convert 12h to 24h
        format = ("%I:%M:%S %p")
        Sunrise_1 = datetime.strptime(Sunrise, format)
        Sunset_1 = datetime.strptime(Sunset, format)

        if Manual_UTC == "+":
            Hours = int(input("How many hours to add? "))
            Sunrise_done = datetime.strftime(Sunrise_1 + timedelta(hours=Hours), "%H:%M:%S")
            Sunset_done = datetime.strftime(Sunset_1 + timedelta(hours=Hours), "%H:%M:%S")
        elif Manual_UTC == "-":
            Hours = int(input("How many hours to subtrack? "))
            Sunrise_done = datetime.strftime(Sunrise_1 - timedelta(hours=Hours), "%H:%M:%S")
            Sunset_done = datetime.strftime(Sunset_1 - timedelta(hours=Hours), "%H:%M:%S")

        print("URL:" + (url))
        print("Given latitude is " + (lat) + " and given longitude is " + (lng))
        print("Sunrise " + (Sunrise_done))
        print("Sunset " + (Sunset_done))

    elif HowUTC == "2":

        lat = input("Give latitude ")
        lng = input("Give longitude ")

        url = main_api + urllib.parse.urlencode({"lat": lat, "lng": lng})

        json_data = requests.get(url).json()

        Sunrise = (json_data["results"]["sunrise"])
        Sunset = (json_data["results"]["sunset"])

        # Convert 12h to 24h
        format = ("%I:%M:%S %p")
        Sunrise_1 = datetime.strptime(Sunrise, format)
        Sunset_1 = datetime.strptime(Sunset, format)

        time_now = datetime.now()
        utc_now = datetime.utcnow()

        if time_now > utc_now:
            Autotime = time_now - utc_now
            Sunrise_auto = Sunrise_1 + Autotime
            Sunset_auto = Sunset_1 + Autotime
            Sunrise_done = datetime.strftime(Sunrise_auto, "%H:%M:%S")
            Sunset_done = datetime.strftime(Sunset_auto, "%H:%M:%S")
        elif time_now < utc_now:
            Autotime = utc_now - time_now
            Sunrise_auto = Sunrise_1 - Autotime
            Sunset_auto = Sunset_1 - Autotime
            Sunrise_done = datetime.strftime(Sunrise_auto, "%H:%M:%S")
            Sunset_done = datetime.strftime(Sunset_auto, "%H:%M:%S")

        print("URL:" + (url))
        print("Given latitude is " + (lat) + " and given longitude is " + (lng))
        print("Sunrise " + (Sunrise_done))
        print("Sunset " + (Sunset_done))

    elif HowUTC == "3":

        country_code = "FI"
        postal_code = input("What is the postal code ")

        bring_api_url = "https://api.bring.com/pickuppoint/api/pickuppoint/%s/postalCode/%s.json" % (country_code, postal_code)

        json_data2 = requests.get(bring_api_url).json()

        lat = json_data2["pickupPoint"][0]["latitude"]
        lng = json_data2["pickupPoint"][0]["longitude"]

        url = main_api + urllib.parse.urlencode({"lat": lat, "lng": lng})

        json_data = requests.get(url).json()

        Sunrise = json_data["results"]["sunrise"]
        Sunset = json_data["results"]["sunset"]

        # Convert 12h to 24h
        format = ("%I:%M:%S %p")
        Sunrise_1 = datetime.strptime(Sunrise, format)
        Sunset_1 = datetime.strptime(Sunset, format)

        time_now = datetime.now()
        utc_now = datetime.utcnow()

        if time_now > utc_now:
            Autotime = time_now - utc_now
            Sunrise_auto = Sunrise_1 + Autotime
            Sunset_auto = Sunset_1 + Autotime
            Sunrise_done = datetime.strftime(Sunrise_auto, "%H:%M:%S")
            Sunset_done = datetime.strftime(Sunset_auto, "%H:%M:%S")
        elif time_now < utc_now:
            Autotime = utc_now - time_now
            Sunrise_auto = Sunrise_1 - Autotime
            Sunset_auto = Sunset_1 - Autotime
            Sunrise_done = datetime.strftime(Sunrise_auto, "%H:%M:%S")
            Sunset_done = datetime.strftime(Sunset_auto, "%H:%M:%S")

        print("URL:" + (url))
        print("BRING_URL:" + (bring_api_url))
        print("Given latitude is " + (lat) + " and given longitude is " + (lng))
        print("Sunrise " + (Sunrise_done))
        print("Sunset " + (Sunset_done))
