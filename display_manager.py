from imports import *
from constants import Constants as Cs
from utils import Utils as Ut

from game_objects import *


class DisplayManager:
    def __init__(self, app):
        self.app = app

        self.screen = pg.display.set_mode(Cs.DIMENSIONS, pg.RESIZABLE)
        self.surface = pg.Surface(Cs.DIMENSIONS)

        self.images = {filepath: Ut.load_image('assets/images/' + filepath) for filepath in Ut.files_in_directory('assets/images')}

        pg.display.set_caption(Cs.CAPTION)
        pg.display.set_icon(self.images['icon.ico'])

        self.scene = 'Menu'

        self.camera = Container(self.app, None, (0, 0))

        self.scene_objects = {
            'Menu': [Mesh(self.app, self.camera, Cs.CENTRE, [-100, -100, -100, 100, 100, 100, 100, -100], [0, 1, 2, 0, 2, 3], 'WIP.png', scripts=['test'])]
        }

    def run(self):
        for obj in BaseObject.all:
            obj.run()

    def update(self):
        self.surface.fill(pg.color.Color('black'))

        for game_object in [self.camera] + list(reversed(self.scene_objects[self.scene])):
            game_object.update()
            if game_object.visible:
                game_object.display()

        final_surface = pg.transform.scale(self.surface, self.screen.get_size())
        self.screen.blit(final_surface, (0, 0))

        pg.display.flip()

    def on_exit(self):
        pass
