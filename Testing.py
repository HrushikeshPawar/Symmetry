"""from manimlib.imports import *
from manimlib.mobject  import *
class Tables(Scene):
    def construct(self):

        def Table():
            def Letters(obj):
                return TexMobject("\\{}".format(obj)).scale(0.6)

            def VertLines(up, left, down, space, no):
                lines = VGroup()
                for i in range(8):
                    lines.add(Line(up+(left - i*LEFT*space),
                    down+(left - i*LEFT*space), stroke_width=0.7))
                return lines

            def HoriLines(up, left, right, space, no):
                lines = VGroup()
                for i in range(8):
                    lines.add(Line(left+(up - i*UP*space),
                    right+(up - i*UP*space), stroke_width=0.7))
                return lines

            letters = VGroup()
            circ = Letters("circ").move_to(UP*3.5+LEFT*6.5).set_color(YELLOW)
            rho_0 = Letters("rho_0").move_to(UP*3.5+LEFT*6)
            rho_1 = Letters("rho_1").move_to(UP*3.5+LEFT*5.5)
            rho_2 = Letters("rho_2").move_to(UP*3.5+LEFT*5)
            rho_3 = Letters("rho_3").move_to(UP*3.5+LEFT*4.5)
            mu_1 = Letters("mu_1").move_to(UP*3.5+LEFT*4)
            mu_2 = Letters("mu_2").move_to(UP*3.5+LEFT*3.5)
            delta_1 = Letters("delta_1").move_to(UP*3.5+LEFT*3)
            delta_2 = Letters("delta_2").move_to(UP*3.5+LEFT*2.5)
            letters.add(circ, rho_0, rho_1, rho_2, rho_3, mu_1, mu_2, delta_1, delta_2)


            crho_0 = Letters("rho_0").move_to(UP*3+LEFT*6.5)
            crho_1 = Letters("rho_1").move_to(UP*2.5+LEFT*6.5)
            crho_2 = Letters("rho_2").move_to(UP*2+LEFT*6.5)
            crho_3 = Letters("rho_3").move_to(UP*1.5+LEFT*6.5)
            cmu_1 = Letters("mu_1").move_to(UP+LEFT*6.5)
            cmu_2 = Letters("mu_2").move_to(UP*0.5+LEFT*6.5)
            cdelta_1 = Letters("delta_1").move_to(LEFT*6.5)
            cdelta_2 = Letters("delta_2").move_to(DOWN*0.5+LEFT*6.5)
            letters.add(crho_0, crho_1, crho_2, crho_3, cmu_1, cmu_2, cdelta_1, cdelta_2)
            self.play(Write(letters, run_time=3))

            vlines = VertLines(up=UP*3.75, left=LEFT*6.25, down=DOWN*0.75, space=0.5, no=8)
            hlines = HoriLines(up=UP*3.25, left=LEFT*6.75, right=LEFT*2.25, space=0.5, no=8)
            self.play(Write(vlines), Write(hlines), run_time=3)
            self.wait(3)
"""
for i in range(64):
    print("char{}".format(i))
