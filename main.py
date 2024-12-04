from twitch import TwitchQueryNameInterval

CWD = '/home/fredd/Documents/polybar-live-channels/'

def format_channels(channels):
    message = ''.join('󱜠 ' + str(channel)+ ' ' for channel in channels[:3])
    return message

def order_channels(channels, SORT_ORDER):
    ordered = sorted(channels, key=lambda x: SORT_ORDER[x])
    return ordered

# MAIN
twitch_handler = TwitchQueryNameInterval()
twitch_handler.get_credentials()
twitch_handler.get_twitch_access_token()
twitch_handler.import_channels(CWD + 'channel_list.txt')
twitch_handler.get_info()
print(format_channels(twitch_handler.info))
