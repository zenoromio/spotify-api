import requests
import base64
import json
from links import sferaebbasta

#clients from spotify app for developers
CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"

#get authorization token from spotify
def get_token():
    auth_string = CLIENT_ID + ":" + CLIENT_SECRET
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}

    results = requests.post(url, headers=headers, data=data)
    json_result = json.loads(results.content)
    token = json_result["access_token"]
    return token

token = get_token()

#get json data from spotify artist
def get_artist_data():
    artist_url = "https://api.spotify.com/v1/artists/" + sferaebbasta["url"]

    headers = {
        "Authorization": "Bearer " + token
    }

    results = requests.get(artist_url, headers=headers)
    json_result = json.loads(results.content)
    return json_result

sferaebbasta_data = get_artist_data()

#download profile pic of spotify artist
def get_artist_pfp(artist):
    image_url = artist["images"][0]["url"]
    image_data = requests.get(image_url).content

    with open("artist_pic.jpg", 'wb') as handler:
        handler.write(image_data)

#get json data from spotify album
def get_album():
    album_url = "https://api.spotify.com/v1/albums/" + sferaebbasta["Italiano"]

    headers = {
        "Authorization": "Bearer " + token
    }

    results = requests.get(album_url, headers=headers)
    json_result = json.loads(results.content)
    return json_result

songs = get_album()["tracks"]["items"]

for song in songs:
    print(song["name"])

