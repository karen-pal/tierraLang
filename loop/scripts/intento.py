#!/usr/bin/env python3
import mpv

def my_log(loglevel, component, message):
    print('[{}] {}: {}'.format(loglevel, component, message))

_player = mpv.MPV(log_handler=my_log, ytdl=False, input_default_bindings=False, input_vo_keyboard=True)
@_player.on_key_press('s')
def advance():
    distance = _player.time_pos - soft_tejido["time"]
    if distance<0:
        distance = abs(distance)
    print(distance)
    _player.seek(distance)
    a.player.playlist_append(soft_tejido["file"])
    a.player.playlist_pos=2

@_player.on_key_press('a')
def backward():
    a.player.playlist_pos=1

#videos = ["/home/rgbellion/Videos/simplescreenrecorder3.mp4",'../tierras/pampa1.mp4',"../tierras/pampa2.mp4"]

soft_tejido = {"time":13,"file":"videos/soft.mp4"}
tejido = {"file":"videos/hydra_short.mp4", "spawns":soft_tejido}
eclipse = {"file":"videos/pampa_eclipse.mp4","spawns":soft_tejido}
videos = [tejido,eclipse]

def make_videos():
    return videos

from dataclasses import dataclass,field
from typing import Any, List
@dataclass
class Loopera():
    playlist: List[str] = field(default_factory=make_videos)
    player: Any = _player
    def run(self):
        self.player.fullscreen = False
        self.player.loop_playlist = 'inf'
        # Option access, in general these require the core to reinitialize
        self.player['vo'] = 'gpu'
        for video in self.playlist:
            self.player.playlist_append(video["file"])
        self.player.playlist_pos=0
        self.player.wait_for_playback()
        self.player.wait_for_property('idle-active')
        del self.player



a = Loopera()
a.run()





