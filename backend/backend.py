from typing import Union

from fastapi import FastAPI
from dotenv import dotenv_values
import requests


config = dotenv_values("secrets.env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
app = FastAPI()


@app.get("/")
def read_root():
    return "<h1>Wolt Api 2.0</<h1>"


@app.get("/v1/get_order_fee")
def get_order_fee(pickup="Arkadiankatu 3-6", dropoff="Otakaari 24, 02150 Espoo"):
    payload = '''{
        "pickup": {
            "location": {
                "formatted_address": "%s"
            }
        },
        "dropoff": {
            "location": {
                "formatted_address": "%s"
            }
        }
    }'''%(pickup, dropoff)

    auth_token = config['API_TOKEN_KEY']
    headers = {'Authorization': 'Bearer ' + auth_token,
            'Content-Type': 'application/json'}
    endpoint = "delivery-fee"
    url = f"https://daas-public-api.development.dev.woltapi.com/merchants/{config['MERCHANT_ID']}/{endpoint}"
    r = requests.post(url, data=payload, headers=headers)  # params=payload,
    return {"fee": r.json()['fee']['amount']}


@app.get("/v1/place_order")
def place_order(pickup="Arkadiankatu 3-6", dropoff="Otakaari 24, 02150 Espoo"):
    payload = '''{
        "pickup": {
            "location": {
                "formatted_address": "%s"
            },
            "comment": "The box is in front of the door",
            "contact_details": {
            "name": "John Doe",
            "phone_number": "+358123456789",
            "send_tracking_link_sms": false
            }
        },
        "dropoff": {
            "location": {
            "formatted_address": "%s"
            },
            "contact_details": {
            "name": "John Doe's wife",
            "phone_number": "+358123456789",
            "send_tracking_link_sms": false
            },
            "comment": "Leave at the door, please"
        },
        "customer_support": {
            "email": "string",
            "phone_number": "string",
            "url": "string"
        },
        "merchant_order_reference_id": null,
        "is_no_contact": true,
        "contents": [
            {
            "count": 1,
            "description": "plastic bag",
            "identifier": "12345",
            "tags": []
            }
        ],
        "tips": [],
        "min_preparation_time_minutes": 10,
        "scheduled_dropoff_time": null
    }'''%(pickup, dropoff)

    auth_token = config['API_TOKEN_KEY']
    headers = {'Authorization': 'Bearer ' + auth_token,
            'Content-Type': 'application/json'}
    endpoint = "delivery-order"
    url = f"https://daas-public-api.development.dev.woltapi.com/merchants/{config['MERCHANT_ID']}/{endpoint}"
    r = requests.post(url, data=payload, headers=headers)  # params=payload,
    return {"dropoff_eta": r.json()['dropoff']['eta'],
        "order_id": r.json()['wolt_order_reference_id']}


@app.get("/v1/get_driveby_offer")
def get_driveby_offer(order_id):
        
        # get users interests
        # get available merchants on existing order route
        # get best match of interests and available stores
        
        return {"merchant": "R-Kionsi",
            "item": "Vitamin Well",
            "fee": "1"}
