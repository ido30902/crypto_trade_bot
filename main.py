import json
from apicontroller import *

coin = 'XRPUSDT'

def main():

    controller = APIController()
    streamer = StreamManager()

    print(controller.get_coin_price(coin))

    streamer.start_stream()
    
    
    


    

    
if __name__ == '__main__':
    main()





    