import requests

client_id = 'e6d19f348578489bbb0f89150a260b75'
client_secret = '17ab1ffbac7e41e985e125fa4631e35c'


def get_token():
    grant_type = 'client_credentials'
    body_params = {'grant_type': grant_type}
    url = 'https://accounts.spotify.com/api/token'
    response = requests.post(url, data=body_params, auth=(client_id, client_secret))
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        return "Error: " + response.text
