import requests
import ast


def get_twitch_access_token():
    with open('twitch_credentials.json', mode='r') as infile:
        credentials = ast.literal_eval(infile.read())

    request_url = 'https://id.twitch.tv/oauth2/token'
    request_json = {
                        "client_id": str(credentials['client_id']),
                        "client_secret": str(credentials['client_secret']),
                        "grant_type": "client_credentials",
                    }
    response = requests.post(request_url, json=request_json)
    access_token = response.json()['access_token']
    expires_in = response.json()['expires_in']

    return access_token, expires_in


def get_twitch_streams(access_token, client_id, channels_to_query):
    live_channels = []
    REQUEST_URL = 'https://api.twitch.tv/helix/streams'
    headers = {
                "Authorization": "Bearer {0}".format(access_token),
                "Client-Id": client_id,
              }
    payload = {
                "user_login": [str(channel) for channel in channels_to_query],
                "type": "live",
              }
    response = requests.get(REQUEST_URL, headers=headers, params=payload)
    for r in response.json()['data']:
        live_channels.append(r['user_name'])

    return live_channels
    


