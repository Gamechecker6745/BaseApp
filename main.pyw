from imports import *
from constants import Constants as Cs

from input_manager import InputManager
from audio_manager import AudioManager
from display_manager import DisplayManager


class App:
    def __init__(self) -> None:
        pg.init()
        self.running = False

        # managers
        self.IM = InputManager(self)
        self.AM = AudioManager(self)
        self.DM = DisplayManager(self)

        # time
        self.clock = pg.time.Clock()
        self.run_time = 0
        self.delta_time = 0
        self.fps = 0

    def run(self) -> None:
        self.running = True
        self.DM.run()

        while self.running:
            self.update()
        self.on_exit()

    def update(self) -> None:
        self.delta_time = self.clock.tick(Cs.FRAMERATE) / 1000
        self.run_time += self.delta_time
        self.fps = self.clock.get_fps()

        self.IM.update()
        self.AM.update()
        self.DM.update()

    def on_exit(self) -> None:
        self.IM.on_exit()
        self.AM.on_exit()
        self.DM.on_exit()

        pg.quit()


if __name__ == '__main__':
    app = App()
    app.run()
