import requests
import json

from django.conf import settings


QPX_REQUEST_PAYLOAD = {
    "request": {
        "passengers": {
            "kind": "qpxexpress#passengerCounts",
            "adultCount": 1
        },
        "slice": [

        ],
        "refundable": False,
        "solutions": 20
    }
}

API_URL = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key='
API_URL += settings.QPX_API_KEY


def make_request(payload):
    """
    make the request to the QPX API
    """
    print(API_URL)
    headers = {'Content-Type': 'application/json'}
    return requests.post(API_URL, data=json.dumps(payload), headers=headers)
