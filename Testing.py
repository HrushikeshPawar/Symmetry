from manimlib.imports import *

class Test(Scene):
    def construct(self):
        abst = TextMobject("''Symmetry is a type of ", "invariance",", a property of a mathematical objects remains unchanged, ","under a set of ","operations ","or ","transformations.''")
        abst[1].set_color(RED)
        abst[4].set_color(GREEN)
        abst[6].set_color(GREEN)
        print(str(abst[1].get_tex_string()))
        cross = Cross(abst[1], stroke_width=0.1)
        self.play(ShowCreation(cross))
        self.wait()
