import requests
from datetime import datetime, timedelta

# ********** GET IATA CODE *********
class flightPrice:

    def __init__(self, city_name):
        self.today = datetime.now()
        self.date_string = self.today.strftime("%d/%m/%Y")
        self.six_months = self.today.strptime(self.date_string, "%d/%m/%Y") + timedelta(days=6 * 30)
        self.six_months_string = self.six_months.date().strftime("%d/%m/%Y")
        self.city_name = city_name

    def getPrice(self):
        # Empty strings to replace API keys and endpoints
        AIR_LABS_API_KEY = ""
        TEQUILA_ENDPOINT = ""
        TEQUILA_API_KEY = ""

        # The rest of the code remains unchanged
        data = requests.get(url=f"https://airlabs.co/api/v9/airports?city={self.city_name}&api_key={AIR_LABS_API_KEY}")
        data = data.json()
        search = True
        i = 0
        while search:
            if data["response"][i]["name"].find(self.city_name) != -1:   # find city name
                iata_code = data["response"][i]["iata_code"]
                search = False
            i = i + 1

        tequila_header = {
            "apikey": TEQUILA_API_KEY
        }
        tequila_params = {
            "fly_from": "FRA",
            "fly_to": iata_code,
            "date_from": self.date_string,
            "date_to": self.six_months_string
        }

        flight_data = requests.get(url=TEQUILA_ENDPOINT, params=tequila_params, headers=tequila_header)
        flight_data = flight_data.json()
        flight_price = flight_data["data"][5]["price"]
        currency_fli = flight_data["data"][5]["conversion"]

        for key, value in currency_fli.items():
            currency = key
        return (flight_price, currency)
