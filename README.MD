# polybar-live-channels

Shows channels that are live on polybar. Default max is 3. Currently only works for Twitch because their API is nice *(r than YouTube's).*

### Requirements:

- Python 3

- Twitch API key (trying to get rid of this)

- Nerd Fonts


`channel_list.txt` usage: 

    On a new line, insert the identifier ('t' for Twitch, 'y' for YouTube) followed by the channel name (found in the URL). Order matters.

polybar config:  

```
# polybar-live-channels
# Shows which channels are live
[module/live-channels]
type = custom/script
exec = ~/Documents/polybar-live-channels/print_channels.sh
tail = true
interval = 1800
```
