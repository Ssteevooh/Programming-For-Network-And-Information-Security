import requests
from datetime import datetime

print('This is Bitcoins price right now.')

main_api = "https://api.coindesk.com/v1/bpi/currentprice.json"
json_data = requests.get(main_api).json()

while True:
    Currency = input("Type USD or GBP or EUR to see Bitcoins price in that currency or type q to quit ")
    if Currency == "q":
        break

    if Currency == "USD":
        time = datetime.now()
        desc = (json_data["bpi"]["USD"]["description"])
        rate = (json_data["bpi"]["USD"]["rate"]) + "$"
        print("Today is", time)
        print("The currensy is", desc)
        print("Price for 1 Bitcoin is", rate)

    elif Currency == "GBP":
        time = datetime.now()
        desc = (json_data["bpi"]["GBP"]["description"])
        rate = (json_data["bpi"]["GBP"]["rate"]) + "£"
        print("Today is", time)
        print("The currensy is", desc)
        print("Price for 1 Bitcoin is", rate)

    elif Currency == "EUR":
        time = datetime.now()
        desc = (json_data["bpi"]["EUR"]["description"])
        rate = (json_data["bpi"]["EUR"]["rate"]) + "€"
        print("Today is", time)
        print("The currensy is", desc)
        print("Price for 1 Bitcoin is", rate)
