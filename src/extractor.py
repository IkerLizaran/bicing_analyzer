import requests
from dotenv import load_dotenv
import os
import logging
import time

def get_data():
    api_address_data = "https://opendata-ajuntament.barcelona.cat/data/dataset/estat-estacions-bicing/resource/1b215493-9e63-4a12-8980-2d7e0fa19f85/download"

    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
    my_token = os.getenv("TOKEN_BICING")
    if my_token is None:
        logging.error("TOKEN_BICING not found in .env")
        return None

    my_header = {
        "Authorization" : my_token
    }
    try:
        for attempt in range(3):
            response_data = requests.get(api_address_data, headers=my_header, timeout=15)

            if response_data.status_code == 200:
                try:
                    return response_data.json()
                except ValueError:
                    logging.warning("response_data couldn't return json format") 
            else:
                logging.warning(f"Bicing data API returned status code {response_data.status_code}")
            
            if attempt < 2:
                time.sleep(5)

        logging.error("Bicing data API is not responding")
        return None
        
    except Exception as error:
        logging.error(f"The following exception ocurred: {error}")
        return None

def get_locations():
    api_address_locations = "https://opendata-ajuntament.barcelona.cat/data/ca/dataset/informacio-estacions-bicing/resource/f60e9291-5aaa-417d-9b91-612a9de800aa/download"

    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

    my_token = os.getenv("TOKEN_BICING")
    if my_token is None:
        logging.error("TOKEN_BICING not found in .env")
        return None

    my_header = {
        "Authorization" : my_token
    }
    try:
        for attempt in range(3):
            response_location = requests.get(api_address_locations, headers=my_header, timeout=15)

            if response_location.status_code == 200:
                try:
                    return response_location.json()
                except ValueError:
                    logging.warning("response_location couldn't return json format")
            else:
                logging.warning(f"Bicing locations API returned status code {response_location.status_code}")

            if attempt < 2:
                time.sleep(5)

        logging.error("Bicing locations API is not responding")
        return None
        
    except Exception as error:
        logging.error(f"The following exception ocurred: {error}")
        return None