from manimlib.imports import *
from manimlib.mobject  import *


class Scene(Scene):
    def construct(self):
        rect=Polygon(ORIGIN, UP*2, UP*2+RIGHT*4, RIGHT*4)
        a = UL
        self.play(ShowCreation(rect))
        Dot1 = Dot(rect.get_corner(a))
        self.play(ShowCreation(Dot1))
        self.wait(3)
