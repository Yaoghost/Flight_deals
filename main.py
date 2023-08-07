import requests
from datetime import datetime, timedelta
from CheckPrice import flightPrice
from SheetManager import Sheet
from Alerter import Alert

# get cities name with sheet
sheet = Sheet()
sheet = sheet.getData()   # stores now a dict of cyties and prices

# get flight price with getPrice() dont forget to include the city name for object declared

for city, lowestPrice in sheet.items():
    print(city)
    flight_price = flightPrice(city_name=city).getPrice()
    print(flight_price[0])
    if flight_price[0] <= lowestPrice:    # item at index 0 is the price and 1 is the currency
        alert = Alert(flight_price[0], lowestPrice, city, flight_price[1])
        alert.send()

