import urllib.parse
import requests


main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "My key"
while True:
    orig = input("Starting location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    Units = input("select imperial or metric (i/m): ")
    if Units.upper() == "M":
        distancemultiplier = 1.61
        fuelmultiplier = 3.78
        Fuelunit = " ltr"
        Distanceunit = " km"
    elif Units.upper() == "I":
        distancemultiplier = 1.0
        fuelmultiplier = 1.0
        Fuelunit = " gal"
        Distanceunit = " mile"
    else:
        print("Invalid unit selection! \nUsing metric as default")
        distancemultiplier = 1.61
        fuelmultiplier = 3.78
        Fuelunit = " ltr"
        Distanceunit = " km"

    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("Directions from " + (orig) + " to " + (dest))
        print("Tunnels " + str(json_data["route"]["hasTunnel"]))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Distance:       " + str("{:.2f}".format((json_data["route"]["distance"])*distancemultiplier)) + Distanceunit)
        print("Fuel Used: " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*fuelmultiplier)) + Fuelunit)
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*distancemultiplier) + " %s)" % Distanceunit))
        print("=============================================\n")
    elif json_status == 402:
        print("\n****************************************************************")
        print("Status Code: " + str(json_status) + "; Invalid user input for one or both locations.")
        print("****************************************************************\n")
    else:
        print("\n************************************************************************")
        print("Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
