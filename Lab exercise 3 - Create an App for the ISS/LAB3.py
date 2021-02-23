import requests
from datetime import datetime, timedelta
from time import strftime, gmtime

while True:
    latitude = input("Give latitude ")
    if latitude == "quit" or latitude == "q":
        break
    longitude = input("Give longitude ")
    if longitude == "quit" or longitude == "q":
        break

    ISS_pass = "http://api.open-notify.org/iss-pass.json?lat=%s&lon=%s" % (latitude, longitude)
    ISS_location = "http://api.open-notify.org/iss-now.json"
    ISS_people = "http://api.open-notify.org/astros.json"

    UTC_offset = timedelta(hours=2)

    json_pass = requests.get(ISS_pass).json()
    json_location = requests.get(ISS_location).json()
    json_people = requests.get(ISS_people).json()

    numpas = 0

    date_time = datetime.fromtimestamp(json_pass["request"]["datetime"])
    for isspass in json_pass["response"]:
        duration = strftime("%H:%M:%S", gmtime(isspass["duration"]))
        isspass = datetime.fromtimestamp(isspass["risetime"]) + UTC_offset
        if date_time.day < isspass.day:
            break
        else:
            numpas = numpas + 1
            print("Pass number %d will be at %s and it will last for %s." % (numpas, isspass.isoformat(), duration))
    print("There are %d passes today" % (numpas))

    rise_time1 = json_pass["response"][0]["risetime"]
    location = json_location["iss_position"]["latitude"], json_location["iss_position"]["longitude"]
    number = json_people["number"]
    people = []
    for peeps in json_people["people"]:
        people.append(peeps["name"])

    print("There are", number, "of people in ISS")
    print("ISS current location is", location)
    print("Astros names are", people)
