import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv("C:\Programming\EnviornmentVariables\.env.txt")
PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
USERNAME = "nostaw"
GRAPH = "graphic1"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# create this account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graphic1",
    "name": "Rowing Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# Create a graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

date = datetime.now()
formatted_date = date.strftime("%Y%m%d")
# print(formatted_date)

pixel_create_config = {
    "date": formatted_date,
    "quantity": input("How many kilometers did you row today? "),
}

# Post a pixel
pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
response = requests.post(url=pixel_create_endpoint, json=pixel_create_config, headers=headers)
print(response.text)

pixel_update_config = {
    "quantity": "5.2",
}

# Update a pixel with put()
# pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{formatted_date}"
# response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)

# Delete a pixel
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{formatted_date}"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
