from manimlib.imports import *

class Test(Scene):
    def construct(self):
        line = Line(ORIGIN, RIGHT)
        dot = Dot(line.get_start())
        self.add(line,dot)
        self.wait(5)
