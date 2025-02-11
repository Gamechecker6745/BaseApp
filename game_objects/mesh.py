from imports import *
from constants import Constants as Cs

from game_objects import BaseObject


class Mesh(BaseObject):
    def __init__(self, app, parent, position, vertices, edges, colour, scripts=tuple(), children=tuple(), tag=None):
        if len(vertices) % 2 != 0 or len(edges) % 3 != 0:
            raise Exception("Invalid input to mesh.")

        super().__init__(app, parent, position, scripts, children, tag=tag)

        self.vertices = [np.array((vertices[idx], vertices[idx+1])) for idx in range(0, len(vertices) - 1, 2)]
        self.points = vertices

        self.surface = pg.Surface(Cs.DIMENSIONS, pg.SRCALPHA)

        self.edges = edges
        self.triangles = self.generate_triangles(edges)

        self.colour = colour

    def generate_vertices(self,  val):
        return [(val[idx], val[idx+1]) + self.get_g_pos() for idx in range(0, len(val) - 1, 2)]

    def generate_triangles(self, edges):
        return [np.array((edges[idx], edges[idx+1], edges[idx+2])) for idx in range(0, len(edges), 3)]

    def update(self):
        super().update()
        self.vertices = self.generate_vertices(self.points)

    def display(self):
        for triangle in self.triangles:
            pg.draw.polygon(self.surface, self.colour, (self.vertices[triangle[0]], self.vertices[triangle[1]], self.vertices[triangle[2]]))
            self.app.DM.surface.blit(self.surface, (0, 0))

        super().display()

    def hovering_triangle(self, points):
        turns = self.orient(points[0], points[1], self.app.IM.mouse_pos) + \
                self.orient(points[1], points[2], self.app.IM.mouse_pos) + \
                self.orient(points[2], points[0], self.app.IM.mouse_pos)

        return abs(turns) == 3

    def hovering(self):
        for triangle in self.triangles:
            if self.hovering_triangle((self.vertices[triangle[0]], self.vertices[triangle[1]], self.vertices[triangle[2]])):
                return True
        return False

    @staticmethod
    def orient(A, B, C):  # True = right orient, False = left orient
        AB = np.array(B - A)
        AC = np.array(C - A)
        return 1 if (AB[0] * AC[1] - AB[1] * AC[0]) > 0 else -1
