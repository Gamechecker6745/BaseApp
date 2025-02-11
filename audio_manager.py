from imports import *
from constants import Constants as Cs
from utils import Utils as Ut


class AudioManager:
    def __init__(self, app):
        self.app = app

        self._volume = 1
        self._sound_volume = 0.5
        self._music_volume = 0.2

        self.sounds = Ut.files_in_directory('assets/audio/sounds')  # filepath: file path (audio folder)
        self.music = Ut.files_in_directory('assets/audio/music')  # filepath: file path (audio folder)

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value

    @volume.deleter
    def volume(self):
        del self._volume

    @property
    def sound_volume(self):
        return self._sound_volume

    @sound_volume.setter
    def sound_volume(self, value):
        self._sound_volume = value

    @sound_volume.deleter
    def sound_volume(self):
        del self._sound_volume

    @property
    def music_volume(self):
        return self._music_volume

    @music_volume.setter
    def music_volume(self, value):
        self._music_volume = value

    @music_volume.deleter
    def music_volume(self):
        del self._music_volume

    def play_sound(self, sound_name):
        try:
            self.sounds[sound_name].set_volume(self.sound_volume * self.volume)
            self.sounds[sound_name].play()
        except KeyError:
            warn("Sound not found")

    def play_music(self, music_name, loops=-1):
        try:
            pg.mixer.music.load(self.music[music_name])
            pg.mixer.music.set_volume(self.music_volume * self.volume)
            pg.mixer.music.play(loops)
        except KeyError:
            warn("Music not found")

    def update(self):
        pass

    def on_exit(self):
        pass
