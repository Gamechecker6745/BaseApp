from imports import *
from game_objects import BaseObject


class Circle(BaseObject):
    def __init__(self, app, parent, position, radius, colour, scripts=tuple(), children=tuple(), tag=None, width=0):
        super().__init__(app, parent, position, scripts, children=children, tag=tag)

        self.surface = pg.Surface((radius*2, radius*2), pg.SRCALPHA)
        self.centre = (radius, radius)

        self.radius = radius
        self.colour = colour
        if len(self.colour) == 3:
            self.colour += (255,)

        self.width = width
        self.rect = pg.Rect(1, 1, 1, 1)

    def display(self):
        pg.draw.circle(self.surface, self.colour, self.centre, self.radius, self.width)

        self.app.DM.surface.blit(self.surface, self.get_g_pos() - np.array(self.surface.get_size())/2)

    def hovering(self):
        delta_position = self.app.IM.mouse_pos - self.get_g_pos()

        if delta_position[0] ** 2 + delta_position[1] ** 2 <= self.radius ** 2:
            return True
        return False
