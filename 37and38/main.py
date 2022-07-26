import requests
from datetime import datetime as dt

USERNAME = "angelanew"
TOKEN = "dahdjhadjhajdhada"
GRAPH_ID = "graph1"

if __name__ == "__main__":

    pixela_endpoint = "https://pixe.la/v1/users"

    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    #response = requests.post(url=pixela_endpoint, json=user_params)
    #print(response.text)

    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

    graph_config = {
        "id": GRAPH_ID,
        "name": "Cycling Graph",
        "unit": "Km",
        "type": "float",
        "color": "ajisai"
    }

    print(USERNAME)
    endpoint_graph = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

    headers = {
        "X-USER-TOKEN": TOKEN
    }

    today = dt(year=2022, month=8, day=16)
    #requests.post(url=graph_endpoint, json=graph_config, headers=headers)

    pixel_config = {
        "date": today.strftime("%Y%m%d"),
        "quantity": "15"
    }

    response = requests.post(url=endpoint_graph, json=pixel_config, headers=headers)
    print(response.text)
    print(response.status_code)

    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

    new_pixel_data = {
        "quantity": "4.5"
    }
    requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
    print(response.text)

    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
    response = requests.delete(url=delete_endpoint, headers=headers)

    print(response.text)