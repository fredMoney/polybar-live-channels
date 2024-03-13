# (DONE)grab channel list from file
# (DONE)split list into 2 lists for twitch and youtube
# call apis and retrieve live channels
#   twitch DONEEEEEE
#   youtube
# merge live channels into 1 list and order based on file orderings
# return first 3 channels
# clean this shit up
import twitch

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


def format_channels(channels):
    message = ''.join(str(channel)+ '󱜠 ' for channel in channels)
    return message

# MAIN
with open('channel_list.txt', mode='r') as infile:
    channels = infile.read().splitlines()
ttv_c, yt_c = split_channels(channels)

access_token, expires_in = twitch.get_twitch_access_token()
with open('tokens.txt', mode='w') as ofile:
    ofile.writelines([access_token, '\n', str(expires_in)])
live_channels = twitch.get_twitch_streams(access_token, '74wu0uvvktrybwf259qa49r624hzwg', ttv_c)

print(format_channels(live_channels))