polybar config:

# polybar-live-channels
# Shows which channels are live
[module/live-channels]
type = custom/script
exec = ~/Documents/polybar-live-channels/print_channels.sh
tail = true
interval = 1800
