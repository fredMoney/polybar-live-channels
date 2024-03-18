import twitch
import math
import regex

CWD = '/home/fredd/Documents/polybar-live-channels/'

def split_channels(channels):
    twitch_channels = []
    youtube_channels = []

    for channel in channels:
        if channel[0] == 't':
            twitch_channels.append(channel[1:])
        elif channel[0] == 'y':
            youtube_channels.append(channel[1:])
        else:
            print('Invalid formatting: '.join(str(channel)))

    return twitch_channels, youtube_channels


def import_channels(location=CWD+'channel_list.txt'):
    with open(location, mode='r') as infile:
        channels = infile.read().splitlines()
    SORT_ORDER = {v[1:]:i for i,v in enumerate(channels)}
    return channels, SORT_ORDER


def format_channels(channels):
    message = ''.join(str(channel)+ '󱜠 ' for channel in channels[:3])
    return message


def order_channels(channels, SORT_ORDER):
    ordered = sorted(channels, key=lambda x: SORT_ORDER[x])
    return ordered


# MAIN
POLYBAR_INTERVAL = 600
access_token = None
uses = 0
channels, SORT_ORDER = import_channels()
ttv_c, yt_c = split_channels(channels)

with open(CWD+'tokens.txt', mode='r') as token_file:
    access_token = token_file.read()

with open(CWD+'remaining_uses.txt', mode='r') as uses_file:
    uses = int(uses_file.read())

if uses < 1 or access_token is None:
    access_token, expires_in = twitch.get_twitch_access_token()
    uses = int(math.floor(expires_in / POLYBAR_INTERVAL))

with open(CWD+'tokens.txt', mode='w') as ofile:
    ofile.writelines(access_token)
live_channels = twitch.get_twitch_streams(access_token, ttv_c)
uses = uses - 1

with open(CWD+'remaining_uses.txt', mode='w') as uses_file:
    uses_file.write(str(uses))

sorted_channels = order_channels(live_channels, SORT_ORDER)
print(format_channels(sorted_channels))
