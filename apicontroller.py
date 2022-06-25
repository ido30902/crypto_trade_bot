import json
from binance.client import Client
from dotenv import load_dotenv
import os
import websocket

class APIController:
    
    def __init__(self):
        load_dotenv()
        self.client = Client(os.getenv("API_KEY"),os.getenv("SECRET"))
    
    def get_coin_price(self,coin):
        return self.client.get_avg_price(symbol=coin)

    def buy_coin(self,coin,amount):
        return self.client.order_market_buy(symbol=coin, quantity=amount)

    def sell_coin(self,coin,amount):
        return self.client.order_market_sell(symbol=coin, quantity=amount)
    
    

class StreamManager:
    def __init__(self):
        self.ws = websocket.WebSocketApp(os.getenv('SOCKET') , 
                    on_message = lambda ws,msg: self.on_message(ws, msg),
                    on_error   = lambda ws,msg: self.on_error(ws, msg),
                    on_close   = lambda ws:     self.on_close(ws),
                    on_open    = lambda ws:     self.on_open(ws))

    def start_stream(self):
        self.ws.run_forever()
        print('Stream started')

    def stop_stream(self):
        self.ws.stop()
        print('Stream stopped')

    def on_open(self,ws):
        print('Connection opened')

    def on_close(self,ws):
        print('Connection closed')

    def on_message(self,ws,message):
        price = json.loads(message)['k']['c']
        print(f'price is {price}')
         
    def on_error(self,ws,error):
        print('Error received ' + str(error))