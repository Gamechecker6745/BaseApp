from imports import *


class BaseObject:
    tagged = {}
    all = []

    def __init__(self, app, parent, position, scripts, children=tuple(), tag=None):
        if self not in BaseObject.all:
            BaseObject.all.append(self)
        self.app = app
        self.scripts = scripts
        self.cache = {}

        self.tag = tag
        if tag is not None:
            BaseObject.tagged[tag] = self

        self.parent = parent

        self.children = children
        for child in self.children:
            child.parent = self

        self.visible = True
        self._position = np.array(position)

    def run(self):
        for script in self.scripts:
            try:
                runpy.run_module('scripts.' + script, init_globals={'start': True,
                                                                    'app': self.app,
                                                                    'self': self,
                                                                    'tag': BaseObject.tagged})
            except ImportError:
                warnings.warn(f"An error occurred when running {script}.")

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, val):
        self._position = val

    @position.deleter
    def position(self):
        del self._position

    def get_g_pos(self):
        final_pos = np.array((0, 0), 'float64')
        obj = self.parent

        while obj is not self.app.DM.camera:
            final_pos += obj.position
            obj = obj.parent

        final_pos -= self.app.DM.camera.position
        return final_pos + self.position

    def update(self):
        if self.children is not None:
            for child in self.children:
                child.update()

        for script in self.scripts:
            try:
                runpy.run_module('scripts.' + script, {'start': False,
                                                       'app': self.app,
                                                       'self': self,
                                                       'tag': BaseObject.tagged})
            except ImportError:
                warnings.warn(f"An error occurred when running {script}.")

    def display(self):
        for child in self.children:
            if self.visible and child.visible:
                child.display()

    def hovering(self):
        return False
