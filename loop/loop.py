#!/usr/bin/env python3
import mpv

def my_log(loglevel, component, message):
    print('[{}] {}: {}'.format(loglevel, component, message))

player = mpv.MPV(log_handler=my_log, ytdl=False, input_default_bindings=True, input_vo_keyboard=True)

# Property access, these can be changed at runtime
@player.property_observer('time-pos')
def time_observer(_name, value):
    # Here, _value is either None if nothing is playing or a float containing
    # fractional seconds since the beginning of the file.
    print(round(value))
    if round(value) == soft_tejido["time"]:
        player.playlist_append(soft_tejido["file"])
        player.playlist_next()
        player.playlist_remove(soft_tejido["file"])

player.fullscreen = False
player.loop_playlist = 'inf'
# Option access, in general these require the core to reinitialize
player['vo'] = 'gpu'


@player.on_key_press('n')
def next_video():
    print(round(player.time_pos))
    if round(player.time_pos) == soft_tejido["time"] :
        player.playlist_append(soft_tejido["file"])
        player.playlist_next()
        player.playlist_remove(soft_tejido["file"])
        player.seek(13)
    else:
        player.playlist_append(soft_tejido["file"])

@player.on_key_press('p')
def wtf_seek():
    print("SEEK")
    player.seek(-2)


@player.on_key_press('s')
def my_s_binding():
    pillow_img = player.screenshot_raw()
    pillow_img.save('screenshot.png')

#videos = ["/home/rgbellion/Videos/simplescreenrecorder3.mp4",'../tierras/pampa1.mp4',"../tierras/pampa2.mp4"]

soft_tejido = {"time":13,"file":"videos/soft.mp4"}
tejido = {"file":"videos/hydra_short.mp4", "spawns":soft_tejido}
videos = [tejido]
for video in videos:
    player.playlist_append(video["file"])
player.playlist_pos=0
player.wait_for_playback()
player.wait_for_property('idle-active')
del player
