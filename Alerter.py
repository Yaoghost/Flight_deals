from twilio.rest import Client
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

class Alert:
    def __init__(self, flight_price, lowestPrice, destination, currency):
        self.flight_price = flight_price
        self.lowestPrice = lowestPrice
        self.destination = destination
        self.difference = self.lowestPrice - self.flight_price
        self.currency = currency
    def send(self):
        message = client.messages.create(
            from_='',
            body=f"ALERT❗ A flight from Wichita to {self.destination}, for {self.flight_price} {self.currency} compared to {self.lowestPrice} {self.currency} has been found! You're about to save {self.difference}❗",
            to=''
        )
