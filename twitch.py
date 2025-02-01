import requests
from ast import literal_eval
from abc import abstractmethod

CWD = '/home/fredd/Documents/polybar-live-channels/'

class TwitchQuery():
    def __init__(self):
        self.credentials = {}
        self.access_token = ""
        self.expires_in = 0
        self.channels_to_query = []
        self.sort_order = {}
        self.info = []

    def get_credentials(self):
        with open(CWD+'twitch_credentials.json', mode='r') as infile:
            self.credentials = literal_eval(infile.read())

    def get_twitch_access_token(self):
        request_url = 'https://id.twitch.tv/oauth2/token'
        request_json = {
                            "client_id": str(self.credentials['client_id']),
                            "client_secret": str(self.credentials['client_secret']),
                            "grant_type": "client_credentials",
                        }
        response = requests.post(request_url, json=request_json)
        self.access_token = response.json()['access_token']
        self.expires_in = int(response.json()['expires_in'])

    def import_channels(self, location):
        with open(location, mode='r') as infile:
            self.channels_to_query = [channel.rstrip() for channel in infile]
        self.sort_order = {v:i for i,v in enumerate(self.channels_to_query)}

    @abstractmethod
    def get_info(self):
        pass

class TwitchQueryNameInterval(TwitchQuery):
    def __init__(self):
        super().__init__()

    def get_info(self):
        client_id = str(self.credentials['client_id'])
        REQUEST_URL = 'https://api.twitch.tv/helix/streams'
        headers = {
                    "Authorization": "Bearer {0}".format(self.access_token),
                    "Client-Id": client_id,
                  }
        payload = {
                    "user_login": [str(channel) for channel in self.channels_to_query],
                    "type": "live",
                  }
        response = requests.get(REQUEST_URL, headers=headers, params=payload)
        for r in response.json()['data']:
            self.info.append(r['user_name'])

        self.info = sorted(self.info, key=lambda channel: self.sort_order[channel])

class TwitchQueryMore(TwitchQuery):
    def __init__(self):
        super().__init__()

    def get_info(self):
        client_id = str(self.credentials['client_id'])
        REQUEST_URL = 'https://api.twitch.tv/helix/streams'
        headers = {
                    "Authorization": "Bearer {0}".format(self.access_token),
                    "Client-Id": client_id,
                  }
        payload = {
                    "user_login": [str(channel) for channel in self.channels_to_query],
                    "type": "live",
                  }
        response = requests.get(REQUEST_URL, headers=headers, params=payload)
        for r in response.json()['data']:
            self.info.append([r['user_name'], r['title'], r['game_name']])

        self.info = sorted(self.info, key=lambda channel: self.sort_order[channel])

