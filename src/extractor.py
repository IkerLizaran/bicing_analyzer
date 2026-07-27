import requests
from dotenv import load_dotenv
import os
import pandas as pd
import json

def get_data():
    api_address_data = "https://opendata-ajuntament.barcelona.cat/data/dataset/estat-estacions-bicing/resource/1b215493-9e63-4a12-8980-2d7e0fa19f85/download"

    load_dotenv()
    my_token = os.getenv("TOKEN_BICING")

    my_header = {
        "Authorization" : my_token
    }
    try:
        response_data = requests.get(api_address_data, headers=my_header)

        if response_data.status_code == 200:
            json_bicing = response_data.json()
            return json_bicing
        else:
            return None

    except Exception as e:
        print(e)
        return None

def get_locations():
    api_address_locations = "https://opendata-ajuntament.barcelona.cat/data/ca/dataset/informacio-estacions-bicing/resource/f60e9291-5aaa-417d-9b91-612a9de800aa/download"

    load_dotenv()

    my_token = os.getenv("TOKEN_BICING")

    my_header = {
        "Authorization" : my_token
    }
    try:
        response_location = requests.get(api_address_locations, headers=my_header)

        if response_location.status_code == 200:
            return response_location.json()
        else:
            return None
    except Exception as e:
        print(e)
        return None