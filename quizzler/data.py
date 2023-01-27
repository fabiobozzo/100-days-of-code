import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

api_response = requests.get(url="https://opentdb.com/api.php", params=parameters)
api_response.raise_for_status()
api_response_json = api_response.json()

question_data = api_response_json["results"]
