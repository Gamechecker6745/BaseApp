from imports import *
from utils import Utils as Ut

from game_objects import BaseObject


class Text(BaseObject):
    def __init__(self, app, parent, position, string, font, colour, align=0, scripts=tuple(), children=tuple(), tag=None):
        super().__init__(app, parent, position, scripts, children, tag=tag)

        self.align = align
        self._colour = colour
        if len(colour) == 3:
            self._colour += (255,)

        self.font = font
        self._text = string
        self.surface = self.font.render(self.text, True, self.colour)
        self.buffer_surface = pg.Surface(self.surface.get_size(), pg.SRCALPHA)
        self.aligned_position = Ut.align_position(self.surface.get_size(), self.position, self.align)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, val):
        self._position = val
        self.aligned_position = Ut.align_position(self.surface.get_size(), self.position, self.align)

    @position.deleter
    def position(self):
        del self._position

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, val):
        self._text = val
        self.surface = self.font.render(self.text, True, self.colour)
        self.buffer_surface = pg.Surface(self.surface.get_size(), pg.SRCALPHA)
        self.aligned_position = Ut.align_position(self.surface.get_size(), self.position, self.align)

    @text.deleter
    def text(self):
        del self._text

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, val):
        self._colour = val
        if len(val) == 3:
            self._colour += (255,)

        self.surface = self.font.render(self.text, True, self.colour)

    @colour.deleter
    def colour(self):
        del self._colour

    def update(self):
        super().update()
        self.aligned_position = Ut.align_position(self.surface.get_size(), self.position, self.align)

    def display(self):
        super().display()
        self.buffer_surface.blit(self.surface, (0, 0))
        self.buffer_surface.set_alpha(self.colour[3])
        self.app.DM.surface.blit(self.buffer_surface, self.aligned_position + self.get_g_pos() - self.position)
        self.buffer_surface.fill((0, 0, 0, 0))

    def hovering(self):
        return self.surface.get_rect().collidepoint(self.app.IM.mouse_pos - self.aligned_position - self.get_g_pos() + self.position)
