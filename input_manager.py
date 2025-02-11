from imports import *
from constants import Constants as Cs


class InputManager:
    def __init__(self, app):
        self.app = app

        self.events = []
        self.event_types = []
        self.event_keys = []

        self.mouse_pos = (0, 0)
        self.mouse_state = None
        self.mouse_clicks = [False, False, False]
        self.mousewheel = None

        self.keyboard_state = None
        self.unicode = None

    def update(self):
        self.events = pg.event.get()
        self.event_types = map(lambda x: x.type, self.events)

        self.event_keys.clear()

        self.mouse_pos = pg.mouse.get_pos() * np.array(Cs.DIMENSIONS) / np.array(self.app.DM.screen.get_size())
        self.mouse_state = pg.mouse.get_pressed()
        self.mouse_clicks = [False, False, False]
        self.mousewheel = 0

        self.keyboard_state = pg.key.get_pressed()
        self.unicode = None

        for event in self.events:
            try:
                self.event_keys.append(event.key)
            except AttributeError:
                pass

            match event.type:
                case pg.QUIT:
                    self.app.running = False

                case pg.MOUSEBUTTONDOWN:
                    match event.button:
                        case 1:
                            self.mouse_clicks[0] = True
                            break
                        case 2:
                            self.mouse_clicks[1] = True
                            break
                        case 3:
                            self.mouse_clicks[2] = True
                            break

                case pg.MOUSEWHEEL:
                    self.mousewheel = event.y

                case pg.KEYDOWN:
                    self.unicode = event.unicode

    def on_exit(self):
        pass
