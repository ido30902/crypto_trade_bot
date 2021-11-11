from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import os
from dotenv import load_dotenv, main
import json
import websocket

api_key = os.getenv('API_KEY')
api_secret = os.getenv('SECRET')
client = Client(api_key, api_secret)


def main():

    load_dotenv()
    
    ws = websocket.WebSocketApp(os.getenv('SOCKET') , on_open=on_open, on_close=on_close, on_message=on_message, on_error=on_error)
    ws.run_forever()
  
def on_open(ws):
    print('Connection opened')

def on_close(ws):
    print('Connection closed')

def on_message(ws,message):
    
    money, quantity = get_json_data()

    response = json.loads(message)

    price = response['k'].get('c')

    avg_price = client.get_avg_price(symbol='LUNAUSDT').get('price')

    if avg_price < price and quantity > 0:
        print(f'Sell at {price}')

        money = money + float(quantity) * float(price)
        print_stats(money, quantity)

    if avg_price > price and money > 0:
        print(f'Buy at {price}')
        quantity = float(money) / float(price)
        money = 0 

        print_stats(money, quantity)

    


def on_error(ws,error):
    print('Error received ' + str(error))


def get_json_data():
    with open('data.json') as json_file:
        data = json.load(json_file)
        return (data['money'],data['quantity'])
    
def update_json_data(money, quantity):
    with open('data.json', 'w') as outfile:
        json.dump({'money': money, 'quantity': quantity}, outfile)

def buy(quantity, price):
    client.order_limit_buy(symbol='LUNAUSDT', quantity=quantity, price=price)

def print_stats(money, quantity):
    print(f'Money: {money}')
    print(f'Holding quantity: {quantity}')

if __name__ == '__main__':
    main()





    