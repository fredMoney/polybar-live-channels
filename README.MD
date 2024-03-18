# polybar-live-channels

Shows Twitch channels that are live on polybar. Default max is 3

### Requirements:

- Python 3

- Twitch API key (trying to get rid of this)

- Nerd Fonts

### `channel_list.txt` usage:

    On a new line, insert the identifier ('t' for Twitch, 'y' for YouTube) followed by the channel name (found in the URL). Order matters.

### Polybar config:

```
# polybar-live-channels
# Shows which channels are live
[module/live-channels]
type = custom/script
exec = ~/Documents/polybar-live-channels/print_channels.sh
tail = true
interval = 1800
```

### Roadmap:

- Use fuzzy search for channel names

- Make it work for YouTube
