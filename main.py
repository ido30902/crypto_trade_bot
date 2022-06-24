import json
import websocket

from apicontroller import APIController

coin = 'LUNAUSDT'
money = 0


def main():

    controller = APIController()
    
    ws = websocket.WebSocketApp(os.getenv('SOCKET') , on_open=on_open, on_close=on_close, on_message=on_message, on_error=on_error)
    ws.run_forever()
  
def on_open(ws):
    print('Connection opened')

def on_close(ws):
    print('Connection closed')

def on_message(ws,message):
    pass
    


def on_error(ws,error):
    print('Error received ' + str(error))

    
if __name__ == '__main__':
    main()





    