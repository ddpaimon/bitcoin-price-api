from exchanges.coinapult import Coinapult
from twilio.rest import Client
from config import AppConfig
import time

tclient = Client(AppConfig.account_sid, AppConfig.auth_token)
old_value = 0

while True:
    new_value = Coinapult().get_current_price()
    diff = new_value - old_value
    if abs(diff) > AppConfig.odds:
        old_value = new_value
        prefix = "Up" if diff > 0 else "Down"
        for client in AppConfig.to_:
            message = tclient.messages.create(
                    client,
                    from_=AppConfig.from_,
                    body=prefix+": "+str(new_value)+" | Diff: "+str(diff))
    time.sleep(AppConfig.interval)
