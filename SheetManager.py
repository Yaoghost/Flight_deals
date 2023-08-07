import requests

class Sheet:

    def __init__(self):
        self.SHEET_ENDPOINT = ""

    def getData(self):

        sheet_data = requests.get(url=self.SHEET_ENDPOINT)
        sheet_data = sheet_data.json()
        j = 0
        flight_desired = {}
        for item in sheet_data.get('sheet1', []):
            city_name = item.get('city')
            lowest_price = item.get('lowestPrice')
            if city_name is not None and lowest_price is not None:
                flight_desired[city_name] = lowest_price
        return flight_desired
