from manimlib.imports import *

class Image(Scene):
    def construct(self):
        self.wait()
        image = ImageMobject("/home/hrushikesh/Desktop/Books/Manim/My_Projects/Symmetry/Images/College.jpg")
        image.scale(2.5)

        name_clg = TextMobject("Fergusson College (Autonomous), Pune").scale(1.5)
        name_dept = TextMobject(r"\text{Department of Mathematics}", color = BLUE_D)
        name_clg.move_to(ORIGIN + UP*3.3)
        name_dept.move_to(ORIGIN + DOWN*3)

        self.play(FadeIn(image , run_time = 3))
        self.wait()
        self.play(Write(name_clg))
        self.wait()
        self.play(Write(name_dept))
        self.wait(2)

class Opening_Quote(Scene):
    def construct(self):

        def color_red(text,a,b):
            for mob in text.submobjects[a:b]:
                mob.set_color(RED)

        def color_blue(text,a,b):
            for mob in text.submobjects[a:b]:
                mob.set_color(BLUE)

        def color_green(text,a,b):
            for mob in text.submobjects[a:b]:
                mob.set_color(GREEN)

        words = Text(
            """
            "The Mathematical Sciences particularly exhibit order ,
            symmetry and limitation and these are the greatest
            form of the beautiful"
            """,
            font = 'TeX Gyre Schola'
        )

        words.set_width(2*(FRAME_X_RADIUS-1))
        words.to_edge(UP)
        color_blue(words, 16, 38)
        color_red(words,59,65)
        color_red(words,66,88)
        color_red(words,92,103)
        color_green(words, 154, 164)

        author = TextMobject("-ARISTOTLE")
        author.set_color(YELLOW)
        author.next_to(words, DOWN)

        self.play(Write(words, run_time=10))
        self.wait()
        self.play(Write(author, run_time = 3))
        self.wait()

class First_Scene_What(Scene):
    def construct(self):
        order = TextMobject("Order").set_color(RED).scale(1.5)
        sym = TextMobject("Symmetry").set_color(RED).scale(1.5)
        lim = TextMobject("Limitation").set_color(RED).scale(1.5)

        order.move_to(ORIGIN + UP*2.5 + LEFT*4)
        sym.move_to(ORIGIN + UP*2.5 + LEFT*0.4)
        lim.move_to(ORIGIN + UP*2.5 + RIGHT*4)

        self.wait()
        self.play(FadeIn(order))
        self.wait()
        self.play(FadeIn(sym))
        self.wait()
        self.play(FadeIn(lim))

        Sym = TexMobject(r"Symmetry").move_to(UP*3).scale(2)
        self.wait(3)
        line = Line(UP*2.5 + LEFT*8, UP*2.5 + RIGHT*8)
        self.play(FadeOut(order), FadeOut(lim))
        self.play(ReplacementTransform(sym, Sym), ShowCreation(line))
        self.wait()


        what = TextMobject("What ?").set_color(RED).move_to(LEFT*6 + UP*2)
        self.play(Write(what, runtime = 2))
        self.wait()

        sym1 = TextMobject("General").set_color(BLUE_E).scale(0.7)
        sym2 = TextMobject("Language").set_color(BLUE_E).scale(0.7).move_to(DOWN*0.4)
        sym = VGroup(sym1, sym2)
        sym.move_to(LEFT*6 + UP)
        self.play(FadeInFromDown(sym))
        self.wait(3)

        trees = SVGMobject("My_Projects/Symmetry/SVG/Asymmetric.svg",
        color = WHITE, fill_opacity=0, stroke_width=1).scale(1.5)
        self.play(ShowCreation(trees, run_time=3))
        self.wait(2)
        self.play(trees.scale, 0.3, trees.shift, UP+ RIGHT*5)
        self.wait(2)

        fly = SVGMobject("My_Projects/Symmetry/SVG/BFly.svg",
        color = WHITE, fill_opacity=0, stroke_width=1).scale(1.5)
        line = Line(UP*2, DOWN*2)
        dline = DashedVMobject(line)
        self.play(ShowCreation(fly, run_time=10))
        self.wait(2)
        self.play(ShowCreation(dline))
        self.wait(2)
        group1 = VGroup(fly, dline)
        self.play(group1.shift, LEFT*3)
        self.wait(2)
        self.play(trees.scale, 2, trees.shift, DOWN+ LEFT*3)
        self.wait(5)
        self.play(FadeOut(trees), FadeOut(group1))
        self.wait()

class Second_Scene_What(Scene):
    def construct(self):
        #Objects from Last Scene
        Sym = TexMobject(r"Symmetry").move_to(UP*3).scale(2)
        underline = Line(UP*2.5 + LEFT*8, UP*2.5 + RIGHT*8)
        what = TextMobject("What ?").set_color(RED).move_to(LEFT*6 + UP*2)
        sym1 = TextMobject("General").set_color(BLUE_E).scale(0.7)
        sym2 = TextMobject("Language").set_color(BLUE_E).scale(0.7).move_to(DOWN*0.4)
        sym = VGroup(sym1, sym2)
        sym.move_to(LEFT*6 + UP)
        self.add(Sym, underline, what, sym)
        self.wait(2)


        #Begin with Geometrical Definition
        geom = TexMobject(r"Geometry").set_color(BLUE_E).move_to(LEFT*6)
        geom.scale(0.7)
        self.play(FadeInFromDown(geom))
        self.wait(3)

        #Start with an Isoceles Triangle
        iso = Polygon(UP, DOWN+LEFT, DOWN+RIGHT).set_color(GREEN_D)
        iso.set_fill(GREEN_D, opacity=1)
        self.play(DrawBorderThenFill(iso))
        self.wait(3)
        line2 = Line(UP*1.5, DOWN*1.5)
        dline2 = DashedVMobject(line2)
        self.play(ShowCreation(dline2))
        self.wait(3)
        group1 = VGroup(iso, dline2)
        self.play(group1.scale,0.3, group1.shift, RIGHT*5.5)
        self.wait(2)

        #Now an Equivlateral triangle
        triangle = Triangle().set_color(RED).set_fill(RED, opacity=1)
        self.play(DrawBorderThenFill(triangle))
        self.wait(3)
        line1 = Line(UP*1.5, DOWN*1.5)
        dline1 = DashedVMobject(line1)
        self.play(ShowCreation(dline1))
        lists = []
        boxes = [0]*3
        for i in range(1, 3):
            boxes[i]= dline1.copy().rotate(2*(PI/3)*i)
            self.play(ShowCreation(boxes[i]))
        self.wait()
        group2 = VGroup(triangle, dline1, boxes[1], boxes[2])
        self.play(group2.scale,0.3, group2.shift, DOWN*1.2 + RIGHT*5.5)
        self.wait(2)

        #Finally a star shape
        star = SVGMobject("My_Projects/Symmetry/SVG/Star.svg",
        color = WHITE, opacity=1, stroke_width=1).scale(1.5)
        self.wait()
        self.play(DrawBorderThenFill(star), run_time=3)
        self.wait()
        line = Line(UP*2, DOWN*2)
        dline2 = DashedVMobject(line)
        self.play(ShowCreation(dline2))
        self.wait()
        lists = []
        boxes = [0]*6
        for i in range(1, 6):
            boxes[i]= dline2.copy().rotate((PI/6)*i)
            self.play(ShowCreation(boxes[i]))
        self.wait(3)
        group3 = VGroup(star,dline2, boxes[1],boxes[2],boxes[3],boxes[4],boxes[5])
        self.play(group3.scale, 0.3, group3.shift, DOWN*2.5 + RIGHT*5.5)
        self.wait(2)


        #Reflection Symmetry
        refsym = TextMobject("Reflection Symmetry").move_to(UP*1.5 + RIGHT*5.5).scale(0.7)
        self.play(Write(refsym, run_time=2))
        self.wait()

        ref_group = VGroup(refsym, group1, group2, group3)
        ref_group.set_opacity(0.5)
        self.wait(4)

class Third_Scene_What(Scene):
    def construct(self):

        def Copy_animation(object, angles):
            n=0
            for i in angles:
                self.play(object.shift, LEFT*3)
                object1 = object.copy().set_color(RED).set_fill(RED)
                self.play(object1.shift, RIGHT*4.5)
                arrow = CurvedArrow(LEFT, RIGHT, angle= PI/4).move_to(DOWN*2+RIGHT*1.5)
                text = "{}^\circ".format(i)
                ang = TexMobject(text).next_to(arrow, DOWN)
                self.play(ShowCreation(arrow), Write(ang))
                self.play(Rotate(object1, i*DEGREES, run_time=2))
                self.play(FadeOut(arrow), FadeOut(ang))
                self.play(object.shift, RIGHT*3, object1.shift,LEFT*1.5)
                self.play(FadeOut(object1))
                n += 1

        #Create Last SCENE
        Sym = TexMobject(r"Symmetry").move_to(UP*3).scale(2)
        underline = Line(UP*2.5 + LEFT*8, UP*2.5 + RIGHT*8)
        what = TextMobject("What ?").set_color(RED).move_to(LEFT*6 + UP*2)
        sym1 = TextMobject("General").set_color(BLUE_E).scale(0.7)
        sym2 = TextMobject("Language").set_color(BLUE_E).scale(0.7).move_to(DOWN*0.4)
        sym = VGroup(sym1, sym2).move_to(LEFT*6 + UP)
        geom = TexMobject(r"Geometry").set_color(BLUE_E).move_to(LEFT*6).scale(0.7)

        iso = Polygon(UP, DOWN+LEFT, DOWN+RIGHT).set_color(GREEN_D)
        iso.set_fill(GREEN_D, opacity=1)
        line2 = Line(UP*1.5, DOWN*1.5)
        dline2 = DashedVMobject(line2)
        group1 = VGroup(iso, dline2).scale(0.3).shift(RIGHT*5.5)

        triangle = Triangle().set_color(RED).set_fill(RED, opacity=1)
        line1 = Line(UP*1.5, DOWN*1.5)
        dline1 = DashedVMobject(line1)
        lists = []
        boxes = [0]*3
        for i in range(1, 3):
            boxes[i]= dline1.copy().rotate(2*(PI/3)*i)
        group2 = VGroup(triangle, dline1, boxes[1], boxes[2])
        group2.scale(0.3).shift(DOWN*1.2 + RIGHT*5.5)

        star = SVGMobject("My_Projects/Symmetry/SVG/Star.svg",
        color = WHITE, opacity=1, stroke_width=1).scale(1.5)
        line = Line(UP*2, DOWN*2)
        dline2 = DashedVMobject(line)
        lists = []
        boxes = [0]*6
        for i in range(1, 6):
            boxes[i]= dline2.copy().rotate((PI/6)*i)
        group3 = VGroup(star,dline2, boxes[1],boxes[2],boxes[3],boxes[4],boxes[5])
        group3.scale(0.3).shift(DOWN*2.5 + RIGHT*5.5)

        refsym = TextMobject("Reflection Symmetry").move_to(UP*1.5 + RIGHT*5.5).scale(0.7)
        ref_group = VGroup(refsym, group1, group2, group3)
        ref_group.set_opacity(0.5)

        self.add(Sym, underline, what, sym, geom, ref_group)
        self.wait(2)
        #Done creating previous Scene

        #Start with Rotational symmetry
        #First Check that reflection symmetry fails
        hexa = SVGMobject("My_Projects/Symmetry/SVG/Rotate.svg", color=BLUE_D,
        fill_opacity = 0, stroke_width=1).scale(1.5)
        self.play(ShowCreation(hexa, run_time=4))
        self.wait(2)

        for i in [UP, RIGHT, np.array([1,0.57735,0])]:
            self.play(hexa.shift, LEFT*3)
            hexa1 = hexa.copy().set_color(RED)
            self.play(hexa1.shift, RIGHT*4.5)
            line = Line(RIGHT*1.5 + i*2, RIGHT*1.5 + i*(-2))
            dline = DashedVMobject(line)
            self.play(ShowCreation(dline))
            self.play(Rotate(hexa1, PI, i))
            group = VGroup(dline, hexa1)
            self.wait(2)
            self.play(hexa.shift, RIGHT*3, group.shift,LEFT*1.5)
            self.wait(2)
            self.play(FadeOut(group))

        #Now Introduce the Rotational symmetry
        Copy_animation(hexa, [60,120,180])
        self.wait(2)
        self.play(hexa.scale, 0.3, hexa.move_to, LEFT*5 + DOWN*2.5)
        self.wait(2)

        square = Square(color=GREEN, fill_opacity=1).set_fill(GREEN)
        self.play(DrawBorderThenFill(square), run_time=2)
        self.wait()
        Copy_animation(square, [90, 180, 270])
        self.wait(2)
        self.play(square.scale, 0.3, square.move_to, LEFT*5 + DOWN*3.5)
        self.wait(3)

        rotsym = TextMobject("Rotational Symmtery").move_to(LEFT*5 + DOWN).scale(0.7)
        self.play(Write(rotsym))
        self.wait(2)
        rot_group  = VGroup(rotsym, hexa, square)
        self.play(rot_group.scale, 1, rot_group.shift, RIGHT*4 + UP*2.5,
        ref_group.set_opacity, 1, ref_group.scale, 1,
        ref_group.shift, LEFT*2)
        self.wait(5)
        self.play(FadeOut(rot_group, run_time=5),FadeOut(ref_group, run_time=5))
        self.wait(3)

class Fourth_Scene_What(Scene):
    def construct(self):
        self.wait()
        abst = TextMobject("Abstract").move_to(UP*3).scale(1.5)
        self.play(FadeIn(abst))
        self.wait()

        name = TextMobject("Definition:", color=BLUE_D).move_to(UP + LEFT*5)
        self.play(FadeIn(name))
        self.wait()
        absdef = TextMobject("''Symmetry is a type of ", "invariance",", a property of a mathematical objects remains unchanged, ","under a set of ","operations ","or ","transformations", ".''")
        absdef[1].set_color(RED)
        absdef[4].set_color(GREEN)
        absdef[6].set_color(GREEN)
        absdef.scale(1.7).set_width(10).next_to(name, DOWN+RIGHT)
        self.play(Write(absdef, run_time=7))
        self.wait()
        inv = absdef[1].copy()
        op1 = absdef[4].copy()
        op2 = absdef[6].copy()
        self.play(FadeOut(abst), FadeOut(name))
        self.play(inv.scale, 1.5, inv.shift,UP*2.63+RIGHT*4)
        self.play(op1.scale, 1.5, op1.shift, UP*3+ LEFT*6)
        self.play(op2.scale, 1.5, op2.shift,UP*3 + LEFT*4.5)
        self.play(FadeOut(absdef), run_time=2)
        self.wait(2)

        square = Square(color=BLUE_D).move_to(LEFT*4)
        arrow1 = Arrow(DOWN*2.5+LEFT*4,LEFT*4+DOWN*1.5)
        text1 = TextMobject("Mathematical\\ Object").move_to(DOWN*3+LEFT*4).scale(0.7)
        self.play(ShowCreation(square))
        self.play(FadeInFromDown(arrow1), FadeInFromDown(text1))
        self.wait(2)

        arrow2 = Arrow(LEFT*2, ORIGIN)
        text2 = TextMobject("Rotate").move_to(LEFT + UP*0.5).scale(0.7)
        text3 = TexMobject(r"90^{\circ}").move_to(LEFT+DOWN*0.5).scale(0.7)
        arrow3 = Arrow(LEFT + UP*1.5, LEFT+UP*0.5)
        self.play(FadeIn(arrow2), FadeIn(text2),FadeIn(text3))
        self.play(ShowCreation(arrow3), op1.next_to, arrow3,UP,
        op1.scale, 0.7)
        self.wait(2)

        square2 = square.copy().set_color(RED)
        self.play(square2.shift, RIGHT*6)
        self.wait()
        self.play(op2.shift, UP*3)
        op2 = TextMobject("Transformation", color=GREEN).scale(0.7).move_to(RIGHT*2+DOWN*3)
        arrow4 = Arrow(DOWN*2.5+RIGHT*2,DOWN*1.5+RIGHT*2)
        self.play(FadeInFromDown(arrow4), FadeInFromDown(op2))
        self.play(Rotate(square2, PI/2))
        self.wait(2)

        arrow5 = Arrow(RIGHT*4, RIGHT*3)
        self.play(FadeIn(arrow5), inv.scale, 0.7, inv.next_to, arrow5,RIGHT,
        square.copy().shift, RIGHT*6)

        text4 = TexMobject(r"45^{\circ}").move_to(LEFT+DOWN*0.5).scale(0.7)
        self.play(FadeOut(text3))
        self.wait()
        self.play(FadeInFromLarge(text4))
        self.wait()
        self.play(FadeOut(arrow5),Rotate(square2, PI/4))
        self.play(ShowCreation(Cross(inv)))
        self.wait(3)

class Summary_What(Scene):
    def construct(self):

        def intro(object, pos):
            self.play(scene.set_opacity, 0.1, FadeInFromPoint(object, ORIGIN))
            self.wait()
            self.play(object.scale, 0.3, object.shift, pos,
            scene.set_opacity, 1)
            scene.add(object)
            self.wait()

        def DottedLines(object, angle, lines):
            line = Line(UP*2.5, DOWN*2.5)
            dline = DashedVMobject(line)
            dlines = [0]*(lines-1)
            for i in range(lines-1):
                dlines[i]= dline.copy().rotate(angle*(i+1))
            group = VGroup(object,dline)
            for x in dlines:
                group.add(x)
            return group

        #Title of the Scene
        title = TextMobject("Symmetry", "  -  ", "What", " ?").scale(1.5)
        title[2].set_color(RED)
        title.move_to(UP*3)

        #Headings
        heading1 = TexMobject("General \, Language", color=BLUE_D).scale(0.7)
        heading2 = TexMobject("Geometry", color=BLUE_D).scale(0.7)
        heading3 = TexMobject("Abstract", color=BLUE_D).scale(0.7)
        heading1.move_to(UP*1.5 + LEFT*4.5)
        heading2.move_to(UP*1.5)
        heading3.move_to(UP*1.5 + RIGHT*4)
        headings = VGroup(heading1, heading2, heading3)

        #Create Scene with title and headings
        self.wait()
        self.play(Write(title))
        self.play(FadeInFromDown(heading1), FadeInFromDown(heading2),
        FadeInFromDown(heading3))
        self.wait()

        #A group for whole scene, which will be updated throughout the animation
        scene = VGroup(title, headings)

        #import required SVG's, Draw shapes and created dotted lines and
        #play the animations

        global svg_group
        svg_group = []

        ##1st SVG Trees##
        trees = SVGMobject("My_Projects/Symmetry/SVG/Asymmetric.svg",
        color=GREEN_D, fill_opacity=1, stroke_width=1).scale(2)

        intro(trees, LEFT*4.5)
        svg_group.append(trees)

        ##2nd SVG - ButterFly##
        fly = SVGMobject("My_Projects/Symmetry/SVG/BFly.svg",
        color=GREEN_D, stroke_width=1, fill_opacity=1).scale(2)
        svg_group.append(fly)
        intro(fly, LEFT*4.5 + DOWN*2)

        ##3rd SVG - star##
        star = SVGMobject("My_Projects/Symmetry/SVG/Star.svg",
        color=WHITE, stroke_width=1, fill_opacity=1).scale(2)
        star_group = DottedLines(star, PI/6, 6)
        intro(star_group, ORIGIN)

        ##4th SVG - Hexa##
        hexa = SVGMobject("My_Projects/Symmetry/SVG/Rotate.svg",
        color=WHITE, stroke_width=1, fill_opacity=0).scale(2)
        svg_group.append(hexa)
        self.play(scene.set_opacity, 0.1, FadeInFromPoint(hexa, ORIGIN))
        self.wait()
        self.play(scene.set_opacity, 1, hexa.shift, DOWN*2, hexa.scale, 0.3)
        scene.add(hexa)
        self.wait(2)

        #For Abstract Definition
        self.play(scene.set_opacity, 0)
        inv = TextMobject("Invariance").move_to(UP*3+RIGHT*5)
        op1 = TextMobject("Operations").move_to(UP*3+ LEFT*5)
        op2 = TextMobject("Transformation").move_to(UP*3)
        self.add(op1)
        self.add(op2)
        self.add(inv)
        self.wait()

        square = Square(color=BLUE_D).move_to(LEFT*4)
        arrow1 = Arrow(DOWN*2.5+LEFT*4,LEFT*4+DOWN*1.5)
        text1 = TextMobject("Mathematical\\ Object").move_to(DOWN*3+LEFT*4).scale(0.5)
        self.play(ShowCreation(square))
        self.play(FadeInFromDown(arrow1), FadeInFromDown(text1))

        arrow2 = Arrow(LEFT*2, ORIGIN)
        text2 = TextMobject("Rotate").move_to(LEFT + UP*0.5).scale(0.7)
        text3 = TexMobject(r"90^{\circ}").move_to(LEFT+DOWN*0.5).scale(0.7)
        arrow3 = Arrow(LEFT + UP*1.5, LEFT+UP*0.5)
        self.play(FadeIn(arrow2), FadeIn(text2),FadeIn(text3))
        self.play(ShowCreation(arrow3),op1.scale, 0.5, op1.next_to, arrow3,UP)

        square2 = square.copy().set_color(RED)
        self.play(square2.shift, RIGHT*6)
        self.play(op2.shift, UP*3)
        op2 = TextMobject("Transformation").scale(0.5).move_to(RIGHT*2+DOWN*3)
        arrow4 = Arrow(DOWN*2.5+RIGHT*2,DOWN*1.5+RIGHT*2)
        self.play(FadeInFromDown(arrow4), FadeInFromDown(op2))
        self.play(Rotate(square2, PI/2))

        arrow5 = Arrow(RIGHT*4, RIGHT*3)
        square3 = square.copy()
        self.play(FadeIn(arrow5), inv.scale, 0.5, inv.next_to, arrow5,RIGHT,
        square3.shift, RIGHT*6)

        group = VGroup(arrow1, arrow2, arrow3, arrow4, arrow5, square, square2,
        square3, text2, text3)

        self.play(text1.move_to, text1.get_center()*0 +RIGHT*4, FadeOut(group),
        op1.move_to, op1.get_center()*0+RIGHT*4+DOWN*0.7,
        op2.move_to, op2.get_center()*0+RIGHT*4+DOWN*1.4,
        inv.move_to, inv.get_center()*0+RIGHT*4+DOWN*2.1, scene.set_opacity, 1)
        self.wait(3)

class First_Scene_How(Scene):
    def construct(self):

        how = TextMobject("HOW", " ?").scale(1.3).move_to(UP*3.5)
        how[0].set_color(RED)
        self.wait()
        self.play(Write(how), run_time=3)
        self.wait()

        line = Line(RIGHT*0.7+UP*3, RIGHT*0.7+DOWN*3)
        #self.play(ShowCreation(line))
        #self.wait()

        vis = TexMobject("Visual \, Representation", color=BLUE_D).scale(0.7)
        mat = TexMobject("Mathematical \, Representation", color=BLUE_D).scale(0.7)
        que = TexMobject(r"?", color = RED).scale(8).move_to(RIGHT*4)
        arrow = CurvedArrow(LEFT*4+DOWN*2.5, RIGHT*4+DOWN*2.5, angle=PI/4)
        mat.move_to(UP*2.5+RIGHT*4)
        vis.move_to(UP*2.5+LEFT*3)
        self.play(Write(vis))
        self.wait()

        ##Visiual Represntation of Symmetry
        inv = TextMobject("Invariance")
        op1 = TextMobject("Operations")
        self.wait()

        square = Square(color=BLUE_D).move_to(LEFT*5).scale(0.5)
        arrow1 = Arrow(DOWN*1.5+LEFT*5,LEFT*5+DOWN*0.5)
        text1 = TextMobject("Mathematical\\ Object").next_to(arrow1, DOWN*0.5).scale(0.5)
        self.play(ShowCreation(square))
        self.play(FadeInFromDown(arrow1), FadeInFromDown(text1))

        arrow2 = Arrow(LEFT*4, LEFT*3)
        text2 = TextMobject("Rotate").move_to(LEFT*3.5 + UP*0.5).scale(0.5)
        text3 = TexMobject(r"90^{\circ}").move_to(LEFT*3.5+DOWN*0.5).scale(0.5)
        arrow3 = Arrow(LEFT*3.5 + UP*1.5, LEFT*3.5+UP*0.5)
        self.play(FadeIn(arrow2), FadeIn(text2),FadeIn(text3), ShowCreation(line))
        op1.next_to(arrow3, UP).scale(0.5)
        self.play(ShowCreation(arrow3),FadeIn(op1), Write(mat))

        square2 = square.copy().set_color(RED)
        self.play(square2.shift, RIGHT*3)
        arrow4 = Arrow(DOWN*1.5+LEFT*2,DOWN*0.5+LEFT*2)
        op2 = TextMobject("Transformation").scale(0.5).next_to(arrow4, DOWN*0.5)
        self.play(FadeInFromDown(arrow4), FadeInFromDown(op2), ShowCreation(arrow))
        self.play(Rotate(square2, PI/2), Write(que))

        arrow5 = Arrow(LEFT*0.5, LEFT*1.5)
        square3 = square.copy()
        inv.move_to(LEFT*0.1).scale(0.5)
        self.play(FadeIn(arrow5), FadeInFromDown(inv), square3.shift, RIGHT*3)
        self.wait(3)
