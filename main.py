# (DONE)grab channel list from file
# (DONE)split list into 2 lists for twitch and youtube
# call apis and retrieve live channels
#   twitch DONEEEEEE
#   youtube
# merge live channels into 1 list 
# (DONE)and order based on file orderings
# (DONE)return first 3 channels
# clean this shit up
import twitch
import os

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
    ordered = sorted(channels, key=lambda x: SORT_ORDER[x.lower()])
    return ordered


# MAIN
channels, SORT_ORDER = import_channels()
ttv_c, yt_c = split_channels(channels)
access_token, expires_in = twitch.get_twitch_access_token()
with open(CWD+'tokens.txt', mode='w') as ofile:
    ofile.writelines([access_token, '\n', str(expires_in)])
live_channels = twitch.get_twitch_streams(access_token, '74wu0uvvktrybwf259qa49r624hzwg', ttv_c)
sorted_channels = order_channels(live_channels, SORT_ORDER)
print(format_channels(sorted_channels))
