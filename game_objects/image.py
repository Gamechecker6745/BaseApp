from imports import *
from utils import Utils as Ut

from game_objects import BaseObject


class Image(BaseObject):
    def __init__(self, app, parent, image_path, position, dimensions, alpha=255, scripts=tuple(), children=tuple(), tag=None):
        """File_path based assets/images"""

        super().__init__(app, parent, position, scripts, children, tag=tag)

        image = pg.image.load('assets/images/' + image_path)
        image = image.convert_alpha()

        self._alpha = alpha

        if dimensions is not None:
            self.surface = pg.Surface(dimensions, pg.SRCALPHA)
            self.surface.blit(pg.transform.scale(image, dimensions), (0, 0))
        else:
            self.surface = pg.Surface(image.get_size(), pg.SRCALPHA)
            self.surface.blit(image, (0, 0))

        self.surface.set_alpha(self.alpha)

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, val):
        self._alpha = val
        self.surface.set_alpha(self._alpha)

    @alpha.deleter
    def alpha(self):
        del self._alpha

    def display(self):
        super().display()

        self.app.DM.surface.blit(self.surface, self.get_g_pos())

    def hovering(self):
        return self.surface.get_rect().collidepoint(self.app.IM.mouse_pos - self.get_g_pos())
