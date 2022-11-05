from typing import Union

from fastapi import FastAPI
from dotenv import dotenv_values
import requests


config = dotenv_values("secrets.env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
app = FastAPI()


@app.get("/")
def read_root():
    return {"MERCHANT_ID": config['MERCHANT_ID']}


@app.get("/v1/get_order_fee")
def get_order_fee():
    payload = '''{
        "pickup": {
            "location": {
                "formatted_address": "Arkadiankatu 3-6"
            }
        },
        "dropoff": {
            "location": {
                "formatted_address": "Otakaari 24, 02150 Espoo"
            }
        }
    }'''

    auth_token = config['API_TOKEN_KEY']
    headers = {'Authorization': 'Bearer ' + auth_token,
            'Content-Type': 'application/json'}
    endpoint = "delivery-fee"
    url = f"https://daas-public-api.development.dev.woltapi.com/merchants/{config['MERCHANT_ID']}/{endpoint}"
    r = requests.post(url, data=payload, headers=headers)  # params=payload,
    return {"rc": str(r), "rt": str(r.text)}


@app.get("/v1/place_order")
def place_order():
    payload = '''{
        "pickup": {
            "location": {
                "formatted_address": "Arkadiankatu 3-6"
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
            "formatted_address": "Otakaari 24, 02150 Espoo"
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
    }'''

    auth_token = config['API_TOKEN_KEY']
    headers = {'Authorization': 'Bearer ' + auth_token,
            'Content-Type': 'application/json'}
    endpoint = "delivery-order"
    url = f"https://daas-public-api.development.dev.woltapi.com/merchants/{config['MERCHANT_ID']}/{endpoint}"
    r = requests.post(url, data=payload, headers=headers)  # params=payload,
    return {"rc": str(r), "rt": str(r.text)}
