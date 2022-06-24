from binance.client import Client
from dotenv import load_dotenv
import os

class APIController:
    def __init__(self):
        load_dotenv()
        self.client = Client(os.getenv("API_KEY"),os.getenv("SECRET"))
    

    