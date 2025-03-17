import requests

API_PATH: str = "https://api.fogos.pt/v2"


def fires(location: str) -> dict:
    api: str = f"{API_PATH}/incidents/active"
    response: requests.Response = requests.get(api)
    json = response.json()
    if response.status_code != 200 or not json["success"]:
        raise Exception
    fires: list[dict] = json["data"]
    fires = [
        fire
        for fire in fires
        if (location in fire["location"] and fire["active"])
    ]
    return fires
