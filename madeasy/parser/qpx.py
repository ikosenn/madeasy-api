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
    headers = {'Content-Type': 'application/json'}
    return requests.post(API_URL, data=json.dumps(payload), headers=headers)


def strip_payload(origi, origin, destination, origin_id, destination_id):
    new_payload = {}
    legs = []
    new_payload['command_type'] = 'book'
    new_payload['origin'] = origin
    new_payload['destination'] = destination
    new_payload['origin_id'] = origin_id
    new_payload['destination_id'] = destination_id
    new_payload["legs"] = legs
    tripOptions = origi['trips']['tripOption']
    for tripOption in tripOptions:
        segments = []
        temp = {
            "price": tripOption['saleTotal']
        }
        for s in tripOption['slice']:
            for seg in s['segment']:
                temp_seg = {
                    "airline": seg['flight']['carrier'],
                    "flight_number": seg['flight']['number']
                }
                for mguu in seg['leg']:
                    temp_seg['start_time'] = mguu['departureTime']
                    temp_seg['stop_time'] = mguu['arrivalTime']
                    temp_seg['stop_airport'] = mguu['destination']
                    temp_seg['start_airport'] = mguu['origin']
                segments.append(temp_seg)
        temp['segments'] = segments
        legs.append(temp)

    return new_payload


def get_flight_details(payload, origin, destination,
                       origin_id, destination_id):
    res = make_request(payload).json()
    return strip_payload(res, origin, destination, origin_id, destination_id)
