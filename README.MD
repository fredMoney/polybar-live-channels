<h1>polybar-live-channels</h1>
<p>Currently only works for Twitch because their API is nice<em>(r than Youtube's)</em>.</p>
<p>polybar config:</p>
<p><code># polybar-live-channels
# Shows which channels are live
[module/live-channels]
type = custom/script
exec = ~/Documents/polybar-live-channels/print_channels.sh
tail = true
interval = 1800</code></p>
