from imports import *
from constants import Constants as Cs

from game_objects import BaseObject


class Container(BaseObject):
    def __init__(self, app, parent, position, scripts=tuple(), children=tuple(), tag=None):
        super().__init__(app, parent, position, scripts, children, tag=tag)
