# app = main app, game_object = source object, start = state, tag = tagged objects
from imports import *


def init():  # runs once at the start of the program
    ...


def update():  # runs once on every tick
    if self.hovering():
        self.colour = (255, 0, 0)
    else:
        self.colour = (0, 255, 0)


if start:
    init()
else:
    update()
