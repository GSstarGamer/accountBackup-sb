import requests
from dotenv import load_dotenv
import os
import base64
import base64
from discord_protos import FrecencyUserSettings


load_dotenv()
token = os.getenv('TOKEN')


def discordEP(endpoint: str, type: str, json_data: dict = None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Authorization': token
    }
    if endpoint.startswith('/'):
        endpoint = endpoint[1:]
    if type == 'post':
        return requests.post('https://discord.com/api/v10/' +
                             endpoint, headers=headers, json_data=json_data)

    elif type == 'get':
        return requests.get('https://discord.com/api/v10/' +
                            endpoint, headers=headers, data=json_data).json()


# friends = [friend["user"]
#            for friend in discordEP('users/@me/relationships', 'get')]

data = discordEP(
    '/users/@me/settings-proto/2', 'get')
gifs = [i for i in FrecencyUserSettings.FromString(
    base64.b64decode(data['settings'])).favorite_gifs.gifs]
