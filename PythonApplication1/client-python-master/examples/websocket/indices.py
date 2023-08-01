from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage, Market
from typing import List

client = WebSocketClient(market=Market.Indices)

# aggregates (per minute)
# client.subscribe("AM.*") # all aggregates
client.subscribe("AM.I:SPX")  # Standard & Poor's 500
client.subscribe("AM.I:DJI")  # Dow Jones Industrial Average
client.subscribe("AM.I:NDX")  # Nasdaq-100
client.subscribe("AM.I:VIX")  # Volatility Index

# single index
# client.subscribe("V.*") # all tickers
# client.subscribe("V.I:SPX") # Standard & Poor's 500
# client.subscribe("V.I:DJI") # Dow Jones Industrial Average
# client.subscribe("V.I:NDX") # Nasdaq-100
# client.subscribe("V.I:VIX") # Volatility Index


def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        print(m)


client.run(handle_msg)
