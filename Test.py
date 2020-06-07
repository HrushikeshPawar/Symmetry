from manimlib.imports import *

class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))

class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 14,
        "height": FRAME_Y_RADIUS * 2,
        "width": 14,
        "grid_stroke": 0.5,
        "grid_color": WHITE,
        "axis_color": RED,
        "axis_stroke": 2,
        "labels_scale": 0.25,
        "labels_buff": 0,
        "number_decimals": 2
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((- self.width / 2, - self.height / 2, 0))
        vector_si = ORIGIN + np.array((- self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        divisions_x = self.width / columns
        divisions_y = self.height / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip([columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff)
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = Text(f"{coord_point}",font="Arial",stroke_width=0).scale(self.labels_scale)
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes, labels)

class Images(Scene):
    def construct(self):
        asym = ImageMobject("My_Projects/Symmetry/Images/star.png")
        self.play(FadeIn(asym, run_time = 3))
        self.wait(2)

class SVG(Scene):
    def construct(self):

        grid = ScreenGrid()
        self.play(ShowCreation(grid), run_time = 3)

        fly = SVGMobject("My_Projects/Symmetry/SVG/Star.svg",
        color = WHITE, fill_opacity=0, stroke_width=1).scale(2)
        self.wait()
        self.play(ShowCreation(fly), run_time=3)
        self.wait()
        line = Line(UP*2.5, DOWN*2.5)
        dline = DashedVMobject(line)#DashedLine(UP*3, DOWN*3)
        self.play(ShowCreation(dline))
        self.wait()

        lists = []
        boxes = [0]*6
        for i in range(1, 6):
            boxes[i]= dline.copy().rotate((PI/6)*i)
            self.play(ShowCreation(boxes[i]))
        self.wait(3)
        group = VGroup(fly,dline, boxes[1],boxes[2],boxes[3],boxes[4],boxes[5])
        self.play(group.scale, 0.3, group.shift, UP*2 + RIGHT*3)
        self.wait(3)
        #dline.scale, 0.3, dline.shift, UP*2 + RIGHT*3)
        """fly1 = fly.copy()
        self.play(fly1.shift, LEFT*2,
        fly.shift, RIGHT*2)
        #self.play(fly.rotate, (PI/3)*2)
        self.play(Rotate(fly,PI/3))
        self.wait(2)
        """

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
        #line = Line(UP*2.5 + LEFT*8, UP*2.5 + RIGHT*8)
        self.play(FadeOut(order), FadeOut(lim))
        self.play(ReplacementTransform(sym, Sym))
        self.wait()


        what = TextMobject(
                            "Symmetry",
                            "  -  ",
                            "What",
                            "  ? "
        ).move_to(UP*3).scale(2)
        what[2].set_color(RED)
        self.play(ReplacementTransform(Sym, what), runtime = 2)
        self.wait()

        sym = TextMobject("General  Language").set_color(BLUE_E)
        sym.move_to(UP*3)
        self.play(FadeOutAndShift(what, UP), FadeInFromDown(sym, run_time=2))
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
        self.wait(3)

class Second_Scene_What(Scene):
    def construct(self):
        #Objects from Last Scene
        sym = TextMobject("General  Language").set_color(BLUE_E)
        sym.move_to(UP*3)
        self.add(sym)
        self.wait(2)
        self.play(FadeOut(sym))


        #Begin with Geometrical Definition
        geom = TexMobject(r"Geometry").set_color(BLUE_E).move_to(UP*3)
        self.play(Write(geom), run_time=2)
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

class SecondScene(Scene):
    def construct(self):
        #Objects from Last Scene
        Sym = TexMobject(r"Symmetry").move_to(UP*3).scale(2)
        underline = Line(UP*2.5 + LEFT*8, UP*2.5 + RIGHT*8)
        what = TextMobject("What ?").set_color(RED).move_to(LEFT*6 + UP*2)
        self.add(Sym, underline, what)
        self.wait(2)


        #Begin with Geometrical Definition
        geom = TexMobject(r"Geometry").set_color(BLUE).move_to(LEFT*6 + UP)
        self.play(FadeInFromDown(geom))
        self.wait(3)

        #Start with a triangle
        triangle = Triangle().set_color(RED)
        self.play(ShowCreation(triangle))
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
        group1 = VGroup(triangle, dline1, boxes[1], boxes[2])
        self.play(group1.shift, LEFT*3)
        self.wait(3)

        iso = Polygon(UP, DOWN+LEFT, DOWN+RIGHT).set_color(GREEN_D)
        self.play(ShowCreation(iso))
        self.wait(3)
        line2 = Line(UP*1.5, DOWN*1.5)
        dline2 = DashedVMobject(line2)
        self.play(ShowCreation(dline2))
        self.wait(3)

        rect1 = Rectangle(height=2, width=1).set_fill(YELLOW, opacity=1)
        rect1.set_color(YELLOW).move_to(RIGHT*3)
        rect2 = Rectangle(height=2, width=1).set_fill(YELLOW, opacity=1)
        rect2.set_color(YELLOW).move_to(RIGHT*4)
        self.play(ShowCreation(rect1), ShowCreation(rect2))
        self.play(Rotating(rect1, radians=PI, axis = UP, about_edge = RIGHT,
         run_time = 2))
        rect1.set_color = RED
        self.wait(3)

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
        geom = TexMobject(r"Geometry").set_color(BLUE).move_to(UP*3)

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

        self.add(geom, ref_group)
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
        self.play(hexa.scale, 0.3, hexa.move_to, LEFT*5 + DOWN*1.5)
        self.wait(2)

        square = Square(color=GREEN, fill_opacity=1).set_fill(GREEN)
        self.play(DrawBorderThenFill(square), run_time=2)
        self.wait()
        Copy_animation(square, [90, 180, 270])
        self.wait(2)
        self.play(square.scale, 0.3, square.move_to, LEFT*5 + DOWN*3)
        self.wait(3)

        rotsym = TextMobject("Rotational Symmtery").move_to(LEFT*5).scale(0.7)
        self.play(Write(rotsym))
        self.wait(2)
        rot_group  = VGroup(rotsym, hexa, square)
        self.play(rot_group.scale, 1, rot_group.next_to, rot_group.get_center()*0 + LEFT*4,
        ref_group.set_opacity, 1, ref_group.scale, 1,
        ref_group.shift, LEFT*3.5)
        self.wait(5)
        self.play(FadeOut(rot_group, run_time=5),FadeOut(ref_group, run_time=5))
        self.wait(3)

class Rotation_What(Scene):
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
        #Done creating previous Scene

        hexa = SVGMobject("My_Projects/Symmetry/SVG/Rotate.svg", color=BLUE_D,
        fill_opacity = 0, stroke_width=1).scale(0.3).move_to(LEFT*5 + DOWN*2.5)
        self.add(hexa)
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
        self.wait(3)

class Abstract(Scene):
    def construct(self):
        #Create Last SCENE
        #Sym = TexMobject(r"Symmetry").move_to(UP*3).scale(2)
        #underline = Line(UP*2.5 + LEFT*8, UP*2.5 + RIGHT*8)
        #what = TextMobject("What ?").set_color(RED).move_to(LEFT*6 + UP*2)
        #sym1 = TextMobject("General").set_color(BLUE_E).scale(0.7)
        #sym2 = TextMobject("Language").set_color(BLUE_E).scale(0.7).move_to(DOWN*0.4)
        #sym = VGroup(sym1, sym2).move_to(LEFT*6 + UP)
        #geom = TexMobject(r"Geometry").set_color(BLUE_E).move_to(LEFT*6).scale(0.7)
        #self.add(Sym, underline, what, sym, geom)

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
        self.play(scene.set_opacity, 0.1)
        inv = TextMobject("Invariance").move_to(RIGHT*4+DOWN*2.1).scale(0.7)
        op1 = TextMobject("Operations").move_to(RIGHT*4+DOWN*0.7).scale(0.7)
        op2 = TextMobject("Transformation").move_to(RIGHT*4+DOWN*1.4).scale(0.7)
        #self.add(op1)
        #self.add(op2)
        #self.add(inv)
        self.wait()

        definition = TextMobject("''Symmetry is a type of ", "invariance",", a property of a mathematical objects remains unchanged, ","under a set of ","operations ","or ","transformations", ".''").scale(2)
        definition[1].set_color(RED)
        definition[4].set_color(GREEN)
        definition[6].set_color(GREEN)
        definition.scale(1.7).set_width(10)
        self.play(FadeInFrom(definition, run_time=3))
        self.wait()

        text1 = TextMobject("Mathematical Object").move_to(RIGHT*4).scale(0.7)
        self.play(FadeOut(definition), Write(text1), Write(inv), Write(op1), Write(op2), scene.set_opacity, 1, run_time=2)
        self.wait(3)

class How(Scene):
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

class How2(Scene):
    def construct(self):

        def update_one(obj):
            obj.move_to(line1.get_start())
        def update_two(obj):
            obj.move_to(line2.get_start())
        def update_three(obj):
            obj.move_to(line1.get_end())
        def update_four(obj):
            obj.move_to(line2.get_end())

        def CreateMatrix( a, b, c, d, pos1, pos2, pos3, pos4):
            pos = [pos1, pos2, pos3, pos4]
            num = [a, b, c, d]
            for i in range(4):
                if (pos[i]==one) or (pos[i]==four):
                    carrow = CurvedArrow(num[i].get_center(), pos[i].get_center(),
                    angle=PI/3).scale(0.9)
                elif (pos[i]==two) or (pos[i]==three):
                    carrow = CurvedArrow(num[i].get_center(), pos[i].get_center(),
                    angle=-PI/3).scale(0.9)

                self.play(ShowCreation(carrow))
                self.play(FadeOut(carrow))
                self.remove(carrow)
        ##  Creating and playing Text (Mathematical Representation)  ##
        mat = TextMobject("Mathematical Representation", color=BLUE_D)
        mat.move_to(UP*3.5+LEFT*3)
        self.wait()
        self.play(FadeIn(mat, UP*3.5+LEFT*3))
        self.wait()

        #Creating and placing Square
        square = Square().move_to(UP*1.5+LEFT*5).scale(0.5)
        self.play(ShowCreation(square))
        shape_fade=VGroup(square)

        #Creating Numbers
        one = TexMobject("1", color=GREEN).scale(0.5)
        one1 = one.copy().set_color(RED)
        two = TexMobject("2", color=GREEN).scale(0.5)
        two2 = two.copy().set_color(RED)
        three = TexMobject("3", color=GREEN).scale(0.5)
        three3 = three.copy().set_color(RED)
        four = TexMobject("4", color=GREEN).scale(0.5)
        four4 = four.copy().set_color(RED)
        text_fade=VGroup(one, one1, two, two2, three, three3, four, four4)

        #Creating lines and arrange numbers
        line1 = Line(square.get_corner(UL)+LEFT*0.15+UP*0.15,
                    square.get_corner(DR)+RIGHT*0.15+DOWN*0.15)
        line2 = Line(square.get_corner(DL)+LEFT*0.15+DOWN*0.15,
                    square.get_corner(UR)+RIGHT*0.15+UP*0.15)
        one.move_to(line1.get_start())
        two.move_to(line2.get_start())
        three.move_to(line1.get_end())
        four.move_to(line2.get_end())
        for i in [one, two, three, four]:
            self.play(Write(i))
        self.wait(2)


        square2 = square.copy()
        square2 = VGroup(square2, line1.set_opacity(0), line2.set_opacity(0))
        arrow = Arrow(UP*1.5+LEFT*4.3,UP*1.5+LEFT*2.7)
        rot = TextMobject("Rotate", color=YELLOW).scale(0.5).move_to(LEFT*3.5+UP*2)
        ang = TexMobject(r"180^\circ", color=YELLOW).scale(0.5).move_to(LEFT*3.5+UP)
        self.play(ShowCreation(arrow), Write(rot), Write(ang))
        one1.add_updater(update_one)
        two2.add_updater(update_two)
        three3.add_updater(update_three)
        four4.add_updater(update_four)
        self.add(one1, two2, three3, four4)
        self.play(square2.shift, RIGHT*3)
        self.wait()
        shape_fade.add(square2, arrow)
        text_fade.add(rot, ang)

        self.play(Rotate(square2, PI))
        self.wait(2)

        one_1 = one.copy().move_to(RIGHT*3+UP*2.5)
        two_1 = two.copy().move_to(RIGHT*3+UP*2)
        three_1 = three.copy().move_to(RIGHT*3+UP*1.5)
        four_1 = four.copy().move_to(RIGHT*3+UP)

        self.play(ShowCreation(one_1), ShowCreation(two_1), ShowCreation(three_1),
        ShowCreation(four_1))

        carrow1 = CurvedArrow(one1.get_center(), three.get_center(),
        angle=-PI/4).scale(0.9)
        carrow2 = CurvedArrow(two2.get_center(), four.get_center(),
        angle=PI/4).scale(0.9)
        carrow3 = CurvedArrow(three3.get_center(), one.get_center(),
        angle=PI/4).scale(0.9)
        carrow4 = CurvedArrow(four4.get_center(), two.get_center(),
        angle=-PI/4).scale(0.9)

        arrow1 = Arrow(RIGHT*3+UP*2.5, RIGHT*4+UP*2.5)
        arrow2 = Arrow(RIGHT*3+UP*2, RIGHT*4+UP*2)
        arrow3 = Arrow(RIGHT*3+UP*1.5, RIGHT*4+UP*1.5)
        arrow4 = Arrow(RIGHT*3+UP, RIGHT*4+UP)

        one_2 = one.copy().set_color(RED).move_to(one.get_center()*0+RIGHT*4+UP*1.5)
        two_2 = two.copy().set_color(RED).move_to(two.get_center()*0+RIGHT*4+UP)
        three_2 = three.copy().set_color(RED).move_to(three.get_center()*0+RIGHT*4+UP*2.5)
        four_2 = four.copy().set_color(RED).move_to(four.get_center()*0+RIGHT*4+UP*2)

        self.play(ShowCreation(carrow1))
        self.play(ShowCreation(arrow1), FadeInFromDown(three_2))
        self.wait()
        self.play(FadeOut(carrow1), ShowCreation(carrow2))
        self.play(ShowCreation(arrow2), FadeInFromDown(four_2))
        self.wait()
        self.play(FadeOut(carrow2), ShowCreation(carrow3))
        self.play(ShowCreation(arrow3), FadeInFromDown(one_2))
        self.wait()
        self.play(FadeOut(carrow3), ShowCreation(carrow4))
        self.play(ShowCreation(arrow4), FadeInFromDown(two_2))
        self.play(FadeOut(carrow4))
        self.wait()

        #2nd Example, Flip / Reflection

        square3 = VGroup(square.copy(), one.copy(), two.copy(), three.copy(), four.copy())
        arrow5 = Arrow(LEFT*4.3+DOWN*2, LEFT*2.7+DOWN*2)
        ref = TextMobject("Refl / Flip", color=YELLOW).scale(0.5).move_to(LEFT*3.5 + DOWN*1.5)
        ax = TextMobject("Y - axis", color=YELLOW).scale(0.5).move_to(LEFT*3.5 + DOWN*2.5)
        shape_fade.add(square3, arrow5)
        text_fade.add(ref, ax)


        self.play(square3.shift, DOWN*3.5)
        self.wait()
        self.play(ShowCreation(arrow5), Write(ref), Write(ax))
        self.wait()

        square4 = Square().scale(0.5).move_to(LEFT*5+DOWN*2)
        line3 = Line(square4.get_corner(UL)+LEFT*0.15+UP*0.15,
                    square4.get_corner(DR)+RIGHT*0.15+DOWN*0.15).set_opacity(0)
        line4 = Line(square4.get_corner(DL)+LEFT*0.15+DOWN*0.15,
                    square4.get_corner(UR)+RIGHT*0.15+UP*0.15).set_opacity(0)
        square4 = VGroup(square4, line3.set_opacity(0), line4.set_opacity(0))
        one3 = TexMobject(r"1", color=RED, opacity=0).scale(0.5).move_to(
                        line3.get_start())
        two3 = TexMobject(r"2", color=RED, opacity=0).scale(0.5).move_to(
                        line4.get_start())
        three3 = TexMobject(r"3", color=RED, opacity=0).scale(0.5).move_to(
                        line3.get_end())
        four3 = TexMobject(r"4", color=RED, opacity=0).scale(0.5).move_to(
                        line4.get_end())
        shape_fade.add(square4)
        text_fade.add(one3, two3, three3, four3)

        def update_one3(obj):
            obj.move_to(line3.get_start())
            obj.set_opacity(1)
        def update_two3(obj):
            obj.move_to(line4.get_start())
            obj.set_opacity(1)
        def update_three3(obj):
            obj.move_to(line3.get_end())
            obj.set_opacity(1)
        def update_four3(obj):
            obj.move_to(line4.get_end())
            obj.set_opacity(1)

        one3.add_updater(update_one3)
        two3.add_updater(update_two3)
        three3.add_updater(update_three3)
        four3.add_updater(update_four3)

        self.add(one3, two3, three3, four3)

        self.play(square4.shift, RIGHT*3)
        line = Line(LEFT*2+DOWN, LEFT*2+DOWN*3)
        dline = DashedVMobject(line)
        self.play(ShowCreation(dline))
        self.wait()
        self.play(square4.flip,np.array([0,-3,0]))
        self.wait(3)
        shape_fade.add(dline)

        one4 = one.copy().move_to(RIGHT*3+DOWN*1.5)
        two4 = two.copy().move_to(RIGHT*3+DOWN*2)
        three4 = three.copy().move_to(RIGHT*3+DOWN*2.5)
        four4 = four.copy().move_to(RIGHT*3+DOWN*3)
        arrow_1 = arrow1.copy().move_to(RIGHT*3.5+DOWN*1.5)
        arrow_2 = arrow2.copy().move_to(RIGHT*3.5+DOWN*2)
        arrow_3 = arrow3.copy().move_to(RIGHT*3.5+DOWN*2.5)
        arrow_4 = arrow4.copy().move_to(RIGHT*3.5+DOWN*3)

        self.play(ShowCreation(one4), ShowCreation(two4), ShowCreation(three4),
        ShowCreation(four4), ShowCreation(arrow_1), ShowCreation(arrow_2),
        ShowCreation(arrow_3), ShowCreation(arrow_4))
        self.wait()

        carrow_1 = CurvedArrow(square4.get_corner(UR), square3.get_corner(UR),
        angle=PI/4).scale(0.9)
        carrow_2 = CurvedArrow(square4.get_corner(DR), square3.get_corner(DR),
        angle=-PI/4).scale(0.9)
        carrow_3 = CurvedArrow(square4.get_corner(DL), square3.get_corner(DL),
        angle=-PI/4).scale(0.9)
        carrow_4 = CurvedArrow(square4.get_corner(UL), square3.get_corner(UL),
        angle=PI/4).scale(0.9)

        one5 = one.copy().set_color(RED).move_to(one.get_center()*0+RIGHT*4+DOWN*3)
        two5 = two.copy().set_color(RED).move_to(two.get_center()*0+RIGHT*4+DOWN*2.5)
        three5 = three.copy().set_color(RED).move_to(three.get_center()*0+RIGHT*4+DOWN*2)
        four5 = four.copy().set_color(RED).move_to(four.get_center()*0+RIGHT*4+DOWN*1.5)

        self.play(ShowCreation(carrow_1), ShowCreation(four5))
        self.play(FadeOut(carrow_1), ShowCreation(carrow_2), ShowCreation(three5))
        self.play(FadeOut(carrow_2), ShowCreation(carrow_3), ShowCreation(two5))
        self.play(FadeOut(carrow_3), ShowCreation(carrow_4), ShowCreation(one5))
        self.play(FadeOut(carrow_4))
        self.wait(3)
        self.play(FadeOut(shape_fade), FadeOut(text_fade))
        self.wait(3)

class How3(Scene):
    def construct(self):

        ##Construct Last Scene##
        mat = TextMobject("Mathematical Representation", color=BLUE_D)
        mat.move_to(UP*3.5+LEFT*3)

        one_g = TexMobject(r"1", color=GREEN_D).scale(0.5).move_to(RIGHT*3+UP*2.5)
        two_g = TexMobject(r"2", color=GREEN_D).scale(0.5).move_to(RIGHT*3+UP*2)
        three_g = TexMobject(r"3", color=GREEN_D).scale(0.5).move_to(RIGHT*3+UP*1.5)
        four_g = TexMobject(r"4", color=GREEN_D).scale(0.5).move_to(RIGHT*3+UP)

        arrow1 = Arrow(RIGHT*3+UP*2.5, RIGHT*4+UP*2.5)
        arrow2 = Arrow(RIGHT*3+UP*2, RIGHT*4+UP*2)
        arrow3 = Arrow(RIGHT*3+UP*1.5, RIGHT*4+UP*1.5)
        arrow4 = Arrow(RIGHT*3+UP, RIGHT*4+UP)

        one_r = TexMobject(r"1", color=RED).scale(0.5).move_to(RIGHT*4+UP*1.5)
        two_r = TexMobject(r"2", color=RED).scale(0.5).move_to(RIGHT*4+UP)
        three_r = TexMobject(r"3", color=RED).scale(0.5).move_to(RIGHT*4+UP*2.5)
        four_r = TexMobject(r"4", color=RED).scale(0.5).move_to(RIGHT*4+UP*2)

        num1 = VGroup(one_g, two_g, three_g, four_g, arrow1, arrow2, arrow3,
        arrow4, one_r, two_r, three_r, four_r)

        one_g1 = TexMobject(r"1", color=GREEN_D).scale(0.5).move_to(RIGHT*3+DOWN*1.5)
        two_g1 = TexMobject(r"2", color=GREEN_D).scale(0.5).move_to(RIGHT*3+DOWN*2)
        three_g1 = TexMobject(r"3", color=GREEN_D).scale(0.5).move_to(RIGHT*3+DOWN*2.5)
        four_g1 = TexMobject(r"4", color=GREEN_D).scale(0.5).move_to(RIGHT*3+DOWN*3)

        arrow_1 = Arrow(RIGHT*3+DOWN*1.5, RIGHT*4+DOWN*1.5)
        arrow_2 = Arrow(RIGHT*3+DOWN*2, RIGHT*4+DOWN*2)
        arrow_3 = Arrow(RIGHT*3+DOWN*2.5, RIGHT*4+DOWN*2.5)
        arrow_4 = Arrow(RIGHT*3+DOWN*3, RIGHT*4+DOWN*3)

        one_r1 = TexMobject(r"1", color=RED).scale(0.5).move_to(RIGHT*4+DOWN*3)
        two_r1 = TexMobject(r"2", color=RED).scale(0.5).move_to(RIGHT*4+DOWN*2.5)
        three_r1 = TexMobject(r"3", color=RED).scale(0.5).move_to(RIGHT*4+DOWN*2)
        four_r1 = TexMobject(r"4", color=RED).scale(0.5).move_to(RIGHT*4+DOWN*1.5)

        num2 = VGroup(one_g1, two_g1, three_g1, four_g1, arrow_1, arrow_2, arrow_3,
        arrow_4, one_r1, two_r1, three_r1, four_r1)

        self.add(mat, num1,  num2)
        self.wait()
        ## DONE CREATING LAST SCENE##

        ##NEW SCENE Starts##
        self.play(num1.scale, 1.4, num1.shift, LEFT*8, num2.scale, 1.4,
        num2.shift, LEFT*8, run_time=2)
        self.wait()

        ##Arrow pointing towards compact form##
        arrow11 = Arrow(LEFT*2+UP*1.75, UP*1.75, color=BLUE)
        self.play(ShowCreation(arrow11))
        self.wait()

        ##Matrix Representation##
        matrix1 = TexMobject(r"\begin{pmatrix} 1 & 2 & 3 & 4 \\ 3 & 4 & 1 & 2 \end{pmatrix}")
        for i in range(1,5):
            matrix1[0][i].set_color(GREEN_D).scale(0.75)
        for i in range(5,9):
            matrix1[0][i].set_color(RED).scale(0.75)

        matrix1.move_to(UP*1.75+RIGHT*2)
        self.play(Write(matrix1[0][0]), Write(matrix1[0][9]))
        self.wait()
        rnum1 = [three_r, four_r, one_r, two_r]
        gmatnum = [matrix1[0][1], matrix1[0][2], matrix1[0][3], matrix1[0][4]]
        self.play(*[FadeIn(mob) for mob in gmatnum])
        for i in range(5,9):
            self.play(Indicate(rnum1[i-5], scale_factor=2), Write(matrix1[0][i]))
        self.wait(2)
        ##1st Matrix done##

        ##2nd Matrix Represntation##
        ##2nd Arrow ##
        arrow12 = arrow11.copy().move_to(arrow11.get_center()*0 + LEFT+DOWN*2.25)
        self.play(ShowCreation(arrow12))
        self.wait()

        ##2nd Matrix##
        matrix2 = TexMobject(r"\begin{pmatrix} 1 & 2 & 3 & 4 \\ 4 & 3 & 2 & 1 \end{pmatrix}")
        for i in range(1,5):
            matrix2[0][i].set_color(GREEN_D).scale(0.75)
        for i in range(5,9):
            matrix2[0][i].set_color(RED).scale(0.75)

        matrix2.move_to(DOWN*2.25+RIGHT*2)
        self.play(Write(matrix2[0][0]), Write(matrix2[0][9]))
        self.wait()
        rnum2 = [four_r1, three_r1, two_r1, one_r1]
        gmatnum = [matrix2[0][1], matrix2[0][2], matrix2[0][3], matrix2[0][4]]
        self.play(*[FadeIn(mob) for mob in gmatnum])
        for i in range(5,9):
            self.play(Indicate(rnum2[i-5], scale_factor=2), Write(matrix2[0][i]), run_time=0.5)
        self.wait(2)

class Why(Scene):
    def construct(self):

        ##Function to Number Square##
        def NumSq(square):
            global one, two, three, four, square_group, line1, line2, SQ1Group
            line1 = Line(square.get_corner(UL)+UP*0.15+LEFT*0.15,
                            square.get_corner(DR)+DOWN*0.15+RIGHT*0.15)
            line2 = Line(square.get_corner(DL)+DOWN*0.15+LEFT*0.15,
                            square.get_corner(UR)+UP*0.15+RIGHT*0.15)
            one = TexMobject(r"1", color=GREEN).scale(0.5).move_to(line1.get_start())
            two = TexMobject(r"2", color=GREEN).scale(0.5).move_to(line2.get_start())
            three = TexMobject(r"3", color=GREEN).scale(0.5).move_to(line1.get_end())
            four = TexMobject(r"4", color=GREEN).scale(0.5).move_to(line2.get_end())
            square_group = VGroup(square, line1, line2)
            nos = [one, two, three, four]
            self.play(*[Write(num) for num in nos])
            SQ1Group = VGroup(square, one, two, three, four)

        def update_one(obj):
            obj.move_to(line1.get_start())
        def update_two(obj):
            obj.move_to(line2.get_start())
        def update_three(obj):
            obj.move_to(line1.get_end())
        def update_four(obj):
            obj.move_to(line2.get_end())

        def SquareRot(square, angle):
            global square2, one2, two2, three2, four2, SQ2Group
            square2 = square.copy()
            one2 = one.copy().set_color(RED).add_updater(update_one)
            two2 = two.copy().set_color(RED).add_updater(update_two)
            three2 = three.copy().set_color(RED).add_updater(update_three)
            four2 = four.copy().set_color(RED).add_updater(update_four)
            self.add(one2, two2, three2, four2)
            square2 = VGroup(square2, line1.set_opacity(0), line2.set_opacity(0))
            SQ2Group = VGroup(square2, one2, two2, three2, four2)
            self.play(SQ2Group.shift, RIGHT*4)
            self.play(Rotate(square2, angle), run_time=2)
            self.wait

        def SquareRefl(square, axis):
            global square3, one3, two3, three3, four3, SQ3Group, dline
            square3 = square.copy()
            one3 = one.copy().set_color(RED).add_updater(update_one)
            two3 = two.copy().set_color(RED).add_updater(update_two)
            three3 = three.copy().set_color(RED).add_updater(update_three)
            four3 = four.copy().set_color(RED).add_updater(update_four)
            self.add(one3, two3, three3, four3)
            square3 = VGroup(square3, line1.set_opacity(0), line2.set_opacity(0))
            SQ3Group = VGroup(square3, one3, two3, three3, four3)
            self.play(SQ3Group.shift, RIGHT*4)
            line = Line(ORIGIN, axis)
            line.move_to(line.get_center()*0 + LEFT+UP)
            dline = DashedVMobject(line)
            self.play(ShowCreation(dline))
            self.play(Rotate(square3, angle=PI, axis=axis), run_time=2)
            self.wait()

        def MatrixRep(a, b, c, d):
            str = "\\begin{pmatrix1} 1 & 2 & 3 & 4 \\\\ {} & {} & {} & {}\\end{pmatrix2}".format(a, b , c, d, pmatrix1 = "{pmatrix}", pmatrix2="{pmatrix}")
            matrix = TexMobject(str)
            for i in range(1,5):
                matrix[0][i].set_color(GREEN_D)
            for j in range(5,9):
                matrix[0][j].set_color(RED)

            return matrix

        def DrawArrow(angle):
            global arrow, rota, ang
            rota = TextMobject("Rotate").scale(0.5).move_to(UP*1.5+LEFT*3)
            arrow = Arrow(UP+LEFT*4, UP+LEFT*2)
            ang = TexMobject(r"{}^\circ".format(angle)).scale(0.5).move_to(UP*0.5+LEFT*3)
            text = [rota, ang]
            self.play(ShowCreation(arrow), *[Write(mob) for mob in text])
            #arrow_group = VGroup(arrow, ang, text)
            self.wait()

        def DrawArrow2(ax):
            global flip, axis, arrow
            flip = TextMobject("Flip").scale(0.5).move_to(UP*1.5+LEFT*3)
            arrow = Arrow(UP+LEFT*4, UP+LEFT*2)
            axis = TexMobject(r"{}".format(ax)).scale(0.5).move_to(UP*0.5+LEFT*3)
            text = [flip, axis]
            self.play(ShowCreation(arrow), *[Write(mob) for mob in text])
            self.wait()

        def clear_updaters(angle):
            line1.move_to(LEFT*5+UP).rotate(-angle)
            line2.move_to(LEFT*5+UP).rotate(-angle)

        def ReFlip(axis):
            line1.move_to(LEFT*5+UP)
            line2.move_to(LEFT*5+UP)
            line1.rotate(angle=PI, axis=axis)
            line2.rotate(angle=PI, axis=axis)


        why = TextMobject("WHY", "?").scale(1.5).move_to(UP*3)
        why[0].set_color(RED)
        self.wait()
        self.play(Write(why), run_time=2)
        self.wait()
        sym = TexMobject("All\,\, Symmetries\,\, of\,", "\,Square").move_to(UP*3)
        sym[1].set_color(RED)
        self.play(FadeOutAndShift(why, UP), FadeInFromDown(sym, run_time=2))
        self.wait(3)

        rot = TextMobject("Rotational Symmetries", color=BLUE_D).move_to(UP*3+LEFT*4)
        square = Square().scale(0.5).move_to(LEFT*5+UP)
        self.play(FadeOut(sym), TransformFromCopy(sym[1], square, run_time=2),
        FadeInFrom(rot, UP))
        self.wait()

        ## Add numbers to the square, and updater to numders##
        NumSq(square)
        self.wait(3)

        ## Square Transformation, Rotation by 0 degrees##
        DrawArrow(0)
        SquareRot(square, 0)
        matrix0 = MatrixRep(1, 2, 3, 4).move_to(LEFT*3.5+DOWN*2)
        gnum = [matrix0[0][i] for i in range(1,5)]
        rnum = [matrix0[0][i] for i in range(5,9)]
        self.play(*[Write(obj) for obj in [matrix0[0][0], matrix0[0][9]]])
        self.play(Indicate(SQ1Group, 2), *[Write(num) for num in gnum])
        self.play(Indicate(SQ2Group, 2), *[Write(num) for num in rnum])
        rho_0 = TexMobject(r"\rho_0 \, =", color=YELLOW).move_to(LEFT*6+DOWN*2)
        self.play(Write(rho_0))
        matrix0 = VGroup(matrix0, rho_0)
        clear_updaters(0)
        self.play(matrix0.scale, 0.5, matrix0.shift, RIGHT*9+UP*5.5,
                *[FadeOut(obj) for obj in [ang, arrow, rota]], FadeOut(SQ2Group))

        self.wait(2)

        ## Square Transformation, Rotation by 90 degrees##
        DrawArrow(90)
        SquareRot(square, PI/2)
        matrix1 = MatrixRep(2, 3, 4, 1).move_to(LEFT*3.5+DOWN*2)
        gnum = [matrix1[0][i] for i in range(1,5)]
        rnum = [matrix1[0][i] for i in range(5,9)]
        self.play(*[Write(obj) for obj in [matrix1[0][0], matrix1[0][9]]])
        self.play(Indicate(SQ1Group, 2), *[Write(num) for num in gnum])
        self.play(Indicate(SQ2Group, 2), *[Write(num) for num in rnum])
        rho_1 = TexMobject(r"\rho_1 \, =", color=YELLOW).move_to(LEFT*6+DOWN*2)
        self.play(Write(rho_1))
        matrix1 = VGroup(matrix1, rho_1)
        clear_updaters(PI/2)
        self.play(matrix1.scale, 0.5, matrix1.shift, RIGHT*9+UP*4.5,
                *[FadeOut(obj) for obj in [ang, arrow, rota]], FadeOut(SQ2Group))

        self.wait(2)

        ## Square Transformation, Rotation by 180 degrees##
        DrawArrow(180)
        SquareRot(square, PI)
        matrix2 = MatrixRep(3, 4, 1, 2).move_to(LEFT*3.5+DOWN*2)
        gnum = [matrix2[0][i] for i in range(1,5)]
        rnum = [matrix2[0][i] for i in range(5,9)]
        self.play(*[Write(obj) for obj in [matrix2[0][0], matrix2[0][9]]])
        self.play(Indicate(SQ1Group, 2), *[Write(num) for num in gnum])
        self.play(Indicate(SQ2Group, 2), *[Write(num) for num in rnum])
        rho_2 = TexMobject(r"\rho_2 \, =", color=YELLOW).move_to(LEFT*6+DOWN*2)
        self.play(Write(rho_2))
        matrix2 = VGroup(matrix2, rho_2)
        clear_updaters(PI)
        self.play(matrix2.scale, 0.5, matrix2.shift, RIGHT*9+UP*3.5,
                *[FadeOut(obj) for obj in [ang, arrow, rota]], FadeOut(SQ2Group))

        self.wait(2)

        ## Square Transformation, Rotation by 270 degrees##
        DrawArrow(270)
        SquareRot(square, 3*PI/2)
        matrix3 = MatrixRep(4, 1, 2, 3).move_to(LEFT*3.5+DOWN*2)
        gnum = [matrix3[0][i] for i in range(1,5)]
        rnum = [matrix3[0][i] for i in range(5,9)]
        self.play(*[Write(obj) for obj in [matrix3[0][0], matrix3[0][9]]])
        self.play(Indicate(SQ1Group, 2), *[Write(num) for num in gnum])
        self.play(Indicate(SQ2Group, 2), *[Write(num) for num in rnum])
        rho_3 = TexMobject(r"\rho_3 \, =", color=YELLOW).move_to(LEFT*6+DOWN*2)
        self.play(Write(rho_3))
        matrix3 = VGroup(matrix3, rho_3)
        self.play(matrix3.scale, 0.5, matrix3.shift, RIGHT*9+UP*2.5,
                *[FadeOut(obj) for obj in [ang, arrow, rota]], FadeOut(SQ2Group))
        clear_updaters(3*PI/2)
        self.wait(2)

        ## Square Transformation, Rotation by 270 degrees##
        DrawArrow(360)
        SquareRot(square, 0)
        matrix4 = MatrixRep(1, 2, 3, 4).move_to(LEFT*3.5+DOWN*2)
        gnum = [matrix4[0][i] for i in range(1,5)]
        rnum = [matrix4[0][i] for i in range(5,9)]
        self.play(*[Write(obj) for obj in [matrix4[0][0], matrix4[0][9]]])
        self.play(Indicate(SQ1Group, 2), *[Write(num) for num in gnum])
        self.play(Indicate(SQ2Group, 2), *[Write(num) for num in rnum])
        rho_4 = TexMobject(r"\rho_4 \, =", color=YELLOW).move_to(LEFT*6+DOWN*2)
        self.play(Write(rho_4))
        matrix4 = VGroup(matrix4, rho_4)
        self.play(Indicate(matrix4, 2), Indicate(matrix0, 4))
        self.play(FadeOut(matrix4), *[FadeOut(obj) for obj in [ang, arrow, rota]],
                    FadeOut(SQ2Group))
        clear_updaters(0)
        self.wait(2)

        ## Reflection Transformations##
        refl = TextMobject("Reflection Symmetries", color=BLUE_D).move_to(UP*3+LEFT*4)
        self.play(ReplacementTransform(rot, refl))

        ##Reflection along Y-AXIS##
        DrawArrow2("Y - Axis")
        SquareRefl(square, np.array([0,2,0]))
        matrix5 = MatrixRep(4, 3, 2, 1).move_to(LEFT*3.5+DOWN*2)
        gnum = [matrix5[0][i] for i in range(1,5)]
        rnum = [matrix5[0][i] for i in range(5,9)]
        self.play(*[Write(obj) for obj in [matrix5[0][0], matrix5[0][9]]])
        self.play(Indicate(SQ1Group, 2), *[Write(num) for num in gnum])
        self.play(Indicate(SQ3Group, 2), *[Write(num) for num in rnum])
        mu_1 = TexMobject(r"\mu_1 \, =", color=YELLOW).move_to(LEFT*6+DOWN*2)
        self.play(Write(mu_1))
        matrix5 = VGroup(matrix5, mu_1)
        self.play(matrix5.scale, 0.5, matrix5.shift, RIGHT*9+UP*1.5,
                *[FadeOut(obj) for obj in [axis, arrow, flip, dline]], FadeOut(SQ3Group))
        ReFlip(np.array([0,2,0]))
        self.wait(2)

        ##Reflection along X-AXIS##
        DrawArrow2("X - Axis")
        SquareRefl(square, np.array([2,0,0]))
        matrix6 = MatrixRep(2, 1, 4, 3).move_to(LEFT*3.5+DOWN*2)
        gnum = [matrix6[0][i] for i in range(1,5)]
        rnum = [matrix6[0][i] for i in range(5,9)]
        self.play(*[Write(obj) for obj in [matrix6[0][0], matrix6[0][9]]])
        self.play(Indicate(SQ1Group, 2), *[Write(num) for num in gnum])
        self.play(Indicate(SQ3Group, 2), *[Write(num) for num in rnum])
        mu_2 = TexMobject(r"\mu_2 \, =", color=YELLOW).move_to(LEFT*6+DOWN*2)
        self.play(Write(mu_2))
        matrix6 = VGroup(matrix6, mu_2)
        self.play(matrix6.scale, 0.5, matrix6.shift, RIGHT*9+UP*0.5,
                *[FadeOut(obj) for obj in [axis, arrow, flip, dline]], FadeOut(SQ3Group))
        ReFlip(np.array([2,0,0]))
        self.wait(2)

        ##Reflection along DIAGONAL 1, 3##
        DrawArrow2("Diag\, 1-3")
        SquareRefl(square, np.array([-2,2,0]))
        matrix7 = MatrixRep(1 , 4, 3, 2).move_to(LEFT*3.5+DOWN*2)
        gnum = [matrix7[0][i] for i in range(1,5)]
        rnum = [matrix7[0][i] for i in range(5,9)]
        self.play(*[Write(obj) for obj in [matrix7[0][0], matrix7[0][9]]])
        self.play(Indicate(SQ1Group, 2), *[Write(num) for num in gnum])
        self.play(Indicate(SQ3Group, 2), *[Write(num) for num in rnum])
        delta_1 = TexMobject(r"\delta_1 \, =", color=YELLOW).move_to(LEFT*6+DOWN*2)
        self.play(Write(delta_1))
        matrix7 = VGroup(matrix7, delta_1)
        self.play(matrix7.scale, 0.5, matrix7.shift, RIGHT*9+DOWN*0.5,
                *[FadeOut(obj) for obj in [axis, arrow, flip, dline]], FadeOut(SQ3Group))
        ReFlip(np.array([-2,2,0]))
        self.wait(2)

        ##Reflection along DIAGONAL 2, 4##
        DrawArrow2("Diag\, 2-4")
        SquareRefl(square, np.array([2,2,0]))
        matrix8 = MatrixRep(3 , 2, 1, 4).move_to(LEFT*3.5+DOWN*2)
        gnum = [matrix8[0][i] for i in range(1,5)]
        rnum = [matrix8[0][i] for i in range(5,9)]
        self.play(*[Write(obj) for obj in [matrix8[0][0], matrix8[0][9]]])
        self.play(Indicate(SQ1Group, 2), *[Write(num) for num in gnum])
        self.play(Indicate(SQ3Group, 2), *[Write(num) for num in rnum])
        delta_2 = TexMobject(r"\delta_2 \, =", color=YELLOW).move_to(LEFT*6+DOWN*2)
        self.play(Write(delta_2))
        matrix8 = VGroup(matrix8, delta_2)
        self.play(matrix8.scale, 0.5, matrix8.shift, RIGHT*9+DOWN*1.5,
                *[FadeOut(obj) for obj in [axis, arrow, flip, dline]], FadeOut(SQ3Group))
        ReFlip(np.array([2,2,0]))
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in [SQ1Group, refl]], run_time=2)
        self.wait(4)

class PreparationForTable(Scene):
    def construct(self):

        global group, Table_Group
        group = VGroup()
        Table_Group = VGroup()
        ## Function for Creating Tables (empty) ##
        def Table():

            global rho_0, rho_1, rho_2, rho_3, mu_1, mu_2, delta_1, delta_2, crho_0, crho_1, crho_2, crho_3, cmu_1, cmu_2, cdelta_1, cdelta_2, lines_remove

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
            circ = Letters("circ").move_to(UP*3.5+LEFT*6.5).set_color(YELLOW).scale(2)
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

            vlines = VertLines(up=UP*3.75, left=LEFT*6.25, down=DOWN*0.75, space=0.5, no=8)
            hlines = HoriLines(up=UP*3.25, left=LEFT*6.75, right=LEFT*2.25, space=0.5, no=8)
            self.play(Write(vlines), Write(hlines), run_time=3)
            self.play(Write(letters, run_time=3))
            self.wait()

        ## Function to Number Square ##
        def NumSq(square):
            global one, two, three, four, square_group, line1, line2, SQ1Group
            line1 = Line(square.get_corner(UL)+UP*0.15+LEFT*0.15,
                            square.get_corner(DR)+DOWN*0.15+RIGHT*0.15)
            line2 = Line(square.get_corner(DL)+DOWN*0.15+LEFT*0.15,
                            square.get_corner(UR)+UP*0.15+RIGHT*0.15)
            one = TexMobject(r"1", color=GREEN).scale(0.5).move_to(line1.get_start())
            two = TexMobject(r"2", color=GREEN).scale(0.5).move_to(line2.get_start())
            three = TexMobject(r"3", color=GREEN).scale(0.5).move_to(line1.get_end())
            four = TexMobject(r"4", color=GREEN).scale(0.5).move_to(line2.get_end())
            square_group = VGroup(square, line1, line2)
            nos = [one, two, three, four]
            self.play(*[Write(num) for num in nos])
            SQ1Group = VGroup(square, one, two, three, four)

        ## Updater Functions ##
        def update_one(obj):
            obj.move_to(line1.get_start())
        def update_two(obj):
            obj.move_to(line2.get_start())
        def update_three(obj):
            obj.move_to(line1.get_end())
        def update_four(obj):
            obj.move_to(line2.get_end())

        def SquareRot(square, angle, matrix):
            global one2, two2, three2, four2, SQ2Group
            square2 = square.copy()
            one2 = one.copy().set_color(RED).add_updater(update_one)
            two2 = two.copy().set_color(RED).add_updater(update_two)
            three2 = three.copy().set_color(RED).add_updater(update_three)
            four2 = four.copy().set_color(RED).add_updater(update_four)
            self.add(one2, two2, three2, four2)
            square2 = VGroup(square2, line1.set_opacity(0), line2.set_opacity(0))
            SQ2Group = VGroup(square2, one2, two2, three2, four2)
            self.play(SQ2Group.shift, RIGHT*2.5)
            self.play(Rotate(square2, angle), Write(matrix), run_time=2)
            group.add(SQ2Group)
            return square2

        def SquareRefl(square, axis, matrix):
            global one3, two3, three3, four3, SQ3Group, dline
            square3 = square.copy()
            one3 = one.copy().set_color(RED).add_updater(update_one)
            two3 = two.copy().set_color(RED).add_updater(update_two)
            three3 = three.copy().set_color(RED).add_updater(update_three)
            four3 = four.copy().set_color(RED).add_updater(update_four)
            self.add(one3, two3, three3, four3)
            square3 = VGroup(square3, line1.set_opacity(0), line2.set_opacity(0))
            SQ3Group = VGroup(square3, one3, two3, three3, four3)
            self.play(SQ3Group.shift, RIGHT*2.5)
            line = Line(ORIGIN, axis)
            line.move_to(line.get_center()*0 + SQ3Group.get_center())
            dline = DashedVMobject(line)
            self.play(ShowCreation(dline, run_time=0.5))
            self.play(Rotate(square3, angle=PI, axis=axis), Write(matrix))
            group.add(SQ3Group, dline)
            return square3

        def MatrixRep(a, b, c, d):
            str = "\\begin{pmatrix1} 1 & 2 & 3 & 4 \\\\ {} & {} & {} & {}\\end{pmatrix2}".format(a, b , c, d, pmatrix1 = "{pmatrix}", pmatrix2="{pmatrix}")
            matrix = TexMobject(str)
            for i in range(1,5):
                matrix[0][i].set_color(GREEN_D)
            for j in range(5,9):
                matrix[0][j].set_color(RED)
            group.add(matrix)
            return matrix

        def DrawArrow(obj, sym, col):
            global arrow_group1
            arrow = Arrow(ORIGIN, RIGHT).next_to(obj, RIGHT)
            symbol = TexMobject("\\{}".format(sym)).scale(0.5).next_to(arrow, UP*0.5)
            symbol.set_color(col)
            arrow_group = VGroup(arrow, symbol)
            #self.play(Write(arrow_group))
            group.add(arrow_group)
            return arrow_group

        def DrawArrow2(obj, sym, col):
            global arrow_group2
            arrow = Arrow(ORIGIN, DOWN).next_to(obj, DOWN)
            symbol = TexMobject("\\{}".format(sym)).scale(0.5).next_to(arrow, RIGHT*0.5)
            symbol.set_color(col)
            arrow_group2 = VGroup(arrow, symbol)
            group.add(arrow_group2)
            return arrow_group2

        def clear_updaters(angle):
            line1.move_to(LEFT*5.5+DOWN*2).rotate(-angle)
            line2.move_to(LEFT*5.5+DOWN*2).rotate(-angle)

        def ReFlip(axis):
            line1.rotate(angle=PI, axis=axis)
            line2.rotate(angle=PI, axis=axis)

        def Transform(obj, mat, sym, col, operation, a, b, c, d, angle=PI, axis=IN, rotate=True, refl=False):
            if(rotate==True and refl==False):
                self.play(WiggleOutThenIn(operation, scale_value=2))
                a1 = DrawArrow(obj, sym, col)
                a2 = DrawArrow2(mat, sym, col)
                self.play(ShowCreation(a1), ShowCreation(a2), run_time=0.5)
                matrix = MatrixRep(a, b, c, d).next_to(arrow_group2, DOWN).scale(0.7)
                square = SquareRot(obj, angle, matrix=matrix)
                one2.remove_updater(update_one)
                two2.remove_updater(update_two)
                three2.remove_updater(update_three)
                four2.remove_updater(update_four)
                return square, matrix

            if(rotate==False and refl==True):
                self.play(WiggleOutThenIn(operation, scale_value=2))
                a1 = DrawArrow(obj, sym, col)
                a2 = DrawArrow2(mat, sym, col)
                self.play(ShowCreation(a1), ShowCreation(a2))
                matrix = MatrixRep(a, b, c, d).next_to(arrow_group2, DOWN).scale(0.7)
                square = SquareRefl(square=obj, axis=axis, matrix=matrix)
                one3.remove_updater(update_one)
                two3.remove_updater(update_two)
                three3.remove_updater(update_three)
                four3.remove_updater(update_four)
                return square, matrix

        global matrices
        matrices = []
        def MatrixConst(a, b, c, d, name):
            str = "\\begin{pmatrix1} 1 & 2 & 3 & 4 \\\\ {} & {} & {} & {} \\end{pmatrix2}".format(a, b, c, d, pmatrix1="{pmatrix}", pmatrix2="{pmatrix}")
            matrix = TexMobject(str)
            matrices.append(matrix)
            for i in range(1,5):
                matrix[0][i].set_color(GREEN_D)
            for j in range(5,9):
                matrix[0][j].set_color(RED)
            obj = TexMobject("\\{}".format(name), "\\, =", color=YELLOW).move_to(LEFT*2.5)
            matrix = VGroup(matrix, obj)
            matrix.scale(0.5)
            return matrix

        ##Creating Last Scene##
        matrix0 = MatrixConst(1,2,3,4,"rho_0"). move_to(RIGHT*5.5 + UP*3.5)
        matrix1 = MatrixConst(2,3,4,1,"rho_1"). move_to(RIGHT*5.5 + UP*2.5)
        matrix2 = MatrixConst(3,4,1,2,"rho_2"). move_to(RIGHT*5.5 + UP*1.5)
        matrix3 = MatrixConst(4,1,2,3,"rho_3"). move_to(RIGHT*5.5 + UP*0.5)
        matrix4 = MatrixConst(4,3,2,1,"mu_1"). move_to(RIGHT*5.5 + DOWN*0.5)
        matrix5 = MatrixConst(2,1,4,3,"mu_2"). move_to(RIGHT*5.5 + DOWN*1.5)
        matrix6 = MatrixConst(1,4,3,2,"delta_1"). move_to(RIGHT*5.5 + DOWN*2.5)
        matrix7 = MatrixConst(3,2,1,4,"delta_2"). move_to(RIGHT*5.5 + DOWN*3.5)
        self.add(matrix0, matrix1, matrix2, matrix3, matrix4, matrix5, matrix6, matrix7)
        matrix_group = VGroup(matrix0, matrix1, matrix2, matrix3, matrix4, matrix5, matrix6, matrix7)
        Table_Group.add(matrix_group)
        self.wait(2)
        ## DONE Creating Last Scene ##

        self.play(matrix_group.set_opacity, 0.1, matrix3.set_opacity, 1, matrix3.shift, LEFT*9.5+UP*2, matrix3.scale, 2 )
        self.wait(2)

        Scene_Group = VGroup()
        rho = matrix3[1][0].copy()
        self.play(rho.shift, DOWN*2)
        colon = TexMobject(":").next_to(rho, RIGHT*0.5)
        self.play(Write(colon))
        Scene_Group.add(rho, colon)

        curl1 = TexMobject("\\{\,1,\,2,\,3,\,4\,\\}").next_to(colon, RIGHT*0.5)
        self.play(Write(curl1[0][0]), Write(curl1[0][8]))
        self.play(*[Indicate(mob, 2) for mob in matrices[3][0][1:5]])
        self.play(*[Write(num) for num in curl1[0][1:8]])
        arrow = Arrow(UP*0.5+LEFT*3, UP*0.5+LEFT*1.5)
        self.play(ShowCreation(arrow))
        Scene_Group.add(curl1, arrow,)

        curl2 = TexMobject("\\{\,1,\,2,\,3,\,4\,\\}").next_to(arrow, RIGHT*0.5)
        self.play(*[Indicate(mob, 2) for mob in matrices[3][0][5:9]])
        self.play(Write(curl2))
        self.wait(2)
        Scene_Group.add(curl2)

        ran = [4, 1, 2, 3]
        for i in range(4):
            rho = matrix3[1][0].copy().shift(DOWN*(i+3))
            num = TexMobject("({})\,=".format(i+1)).next_to(rho, RIGHT*0.4)
            lhs = VGroup(rho, num)
            rhs = TexMobject("{}".format(ran[i])).next_to(lhs, RIGHT*0.5)
            domnum = VGroup(matrices[3][0][i+1], matrices[3][0][i+5])
            self.play(Indicate(domnum, 2), Write(lhs), Write(rhs))
            self.wait()
            Scene_Group.add(lhs, rhs)

        self.wait(2)
        self.play(FadeOut(Scene_Group),matrix3.shift, RIGHT*9.5+DOWN*2,
        matrix3.scale, 0.5)
        self.play(matrix_group.set_opacity, 1)
        self.wait()

        set1=TexMobject(r"G\,=\,\{\,\rho_0,\,\rho_1,\,\rho_2,\,\rho_3,\,\mu_1,\,\mu_2,\,\delta_1,\,\delta_2\,\}").move_to(UP*2.5+LEFT*2)
        self.play(Write(set1, run_time=2))
        self.wait()

        fun = TexMobject("\\text{Let }\ \ ", "\\circ\,:", r"\,G", r"\,\times\,", "G", r"\rightarrow\,", r"G","\ \ \ \ \\text{such that,}").next_to(set1, DOWN*4)
        fun[1].set_color(YELLOW)
        fun[2].set_color(GREEN_D)
        fun[4].set_color(GREEN_D)
        fun[6].set_color(RED)
                                #0          #1      #2    #3        #4         #5   #6
        apply = TexMobject("\\forall\\,", "f_1\\,", ",", "f_2\\,", "\\in\\,", "G", ",\\ \\ \\ ", "\\left(", "f_1", "\\circ", "f_2", "\\right)(x) \, = \," , "f_1", "(",
        "f_2", "(x))").next_to(fun, DOWN)
        apply[0].set_color(YELLOW)
        apply[1].set_color(BLUE_D)
        apply[3].set_color(RED)
        apply[4].set_color(YELLOW)
        apply[5].set_color(GREEN_D)
        apply[8].set_color(BLUE_D)
        apply[9].set_color(YELLOW)
        apply[10].set_color(RED)
        apply[12].set_color(BLUE_D)
        apply[14].set_color(RED)

        self.play(Write(fun))
        self.play(*[Write(obj, run_time=2) for obj in apply[:6]])
        self.wait()
        self.play(*[Write(obj) for obj in apply[6:12]], run_time=2)
        self.wait()
        self.play(*[Write(obj) for obj in apply[12:]], run_time=2)

        self.play(*[FadeOut(obj) for obj in [set1, fun, apply]])
        self.wait()

        ## Creating and labeling Table ##
        Table()
        self.wait()

        ## Permanant Matrix for Starting Position ##
        matrix = Dot().move_to(UP*5)
        Table_Group.add(matrix)


        ## Permanant Square for Starting Position ##
        square = Square().scale(0.5).move_to(LEFT*5.5+DOWN*2)
        self.play(ShowCreation(square), Write(matrix))
        NumSq(square)
        Table_Group.add(SQ1Group)


        ## Transform ro(ro(x)) ##
        T1 = obj=Transform(obj=square, mat=matrix, sym="rho_0", col=RED, angle=0, operation=crho_0, a=1, b=2, c=3, d=4)
        T2 = Transform(obj=T1[0], mat=T1[1], sym="rho_0", col=RED, angle=0, operation=rho_0, a=1, b=2, c=3, d=4)
        self.play(WiggleOutThenIn(matrix0, scale_value=2))
        char = rho_0.copy().shift(DOWN*0.5).set_color(RED)
        self.play(Write(char), FadeOut(group))
        clear_updaters(0)
        group = VGroup()
        self.wait()

        ## Transform ro(r1(x)) ##
        T1 = obj=Transform(obj=square, mat=matrix, sym="rho_1", col=RED, angle=PI/2, operation=crho_1, a=2, b=3, c=4, d=1)
        T2 = Transform(obj=T1[0], mat=T1[1], sym="rho_0", col=RED, angle=0, operation=rho_0, a=2, b=3, c=4, d=1)
        self.play(WiggleOutThenIn(matrix1, scale_value=2))
        char = rho_1.copy().shift(DOWN*0.5).set_color(ORANGE)
        self.play(Write(char), FadeOut(group))
        group = VGroup()
        clear_updaters(PI/2)
        self.wait()

        ## Transform r1(ro(x)) ##
        T1 = obj=Transform(obj=square, mat=matrix, sym="rho_0", col=RED, angle=0, operation=crho_0, a=1, b=2, c=3, d=4)
        T2 = Transform(obj=T1[0], mat=T1[1], sym="rho_1", col=RED, angle=PI/2, operation=rho_1, a=2, b=3, c=4, d=1)
        self.play(WiggleOutThenIn(matrix1, scale_value=2))
        char = crho_1.copy().shift(RIGHT*0.5).set_color(ORANGE)
        self.play(Write(char), FadeOut(group))
        group = VGroup()
        clear_updaters(PI/2)
        self.wait(3)


        ## Fill the necessary rows in table ##
        char1 = crho_2.copy().shift(RIGHT*0.5).set_color(YELLOW)
        char2 = crho_3.copy().shift(RIGHT*0.5).set_color(GREEN_D)
        char3 = cmu_1.copy().shift(RIGHT*0.5).set_color(GREEN_E)
        char4 = cmu_2.copy().shift(RIGHT*0.5).set_color(BLUE)
        char5 = cdelta_1.copy().shift(RIGHT*0.5).set_color(BLUE_D)
        char6 = cdelta_2.copy().shift(RIGHT*0.5).set_color(BLUE_E)
        char7 = rho_2.copy().shift(DOWN*0.5).set_color(YELLOW)
        char8 = rho_3.copy().shift(DOWN*0.5).set_color(GREEN_D)
        char9 = mu_1.copy().shift(DOWN*0.5).set_color(GREEN_E)
        char10 = mu_2.copy().shift(DOWN*0.5).set_color(BLUE)
        char11 = delta_1.copy().shift(DOWN*0.5).set_color(BLUE_D)
        char12 = delta_2.copy().shift(DOWN*0.5).set_color(BLUE_E)

        chars=[char1, char2, char3, char4, char5, char6, char7, char8, char9, char10, char11, char12]
        greek = [rho_2, rho_3, mu_1, mu_2, delta_1, delta_2, crho_2, crho_3, cmu_1, cmu_2, cdelta_1, cdelta_2]

        self.play(*[WiggleOutThenIn(mob, scale_value=2) for mob in greek])
        self.play(*[Write(mob, scale_value=2) for mob in chars])
        self.wait()

        char0 = crho_0.copy().shift(DOWN*0.5+RIGHT*2).set_color(RED)
        char1 = crho_1.copy().shift(DOWN*0.5+RIGHT*2).set_color(ORANGE)
        char2 = crho_2.copy().shift(DOWN*0.5+RIGHT*2).set_color(YELLOW)
        char3 = crho_3.copy().shift(UP*0.5+RIGHT).set_color(GREEN_D)
        char4 = crho_0.copy().shift(DOWN+RIGHT*1.5).set_color(RED)
        char5 = rho_0.copy().shift(DOWN*2+RIGHT*0.5).set_color(RED)
        char6 = rho_1.copy().shift(DOWN*2+RIGHT*0.5).set_color(ORANGE)
        char7 = rho_2.copy().shift(DOWN+LEFT*0.5).set_color(YELLOW)
        char8 = rho_3.copy().shift(DOWN+LEFT*0.5).set_color(GREEN_D)

        chars=[char1, char2, char3, char4, char5, char6, char7, char8, char0]
        greek = [rho_1, rho_2, rho_3, crho_1, crho_2, crho_3]
        self.play(*[WiggleOutThenIn(mob, scale_value=2) for mob in greek])
        self.play(*[Write(mob) for mob in chars])
        self.wait()

        ## Transform r1(mu1(x)) ##
        T1 = obj=Transform(obj=square, mat=matrix, sym="mu_1", col=RED, axis=np.array([0,3,0]), rotate=False, refl=True, operation=cmu_1, a=4, b=3, c=2, d=1)
        T2 = Transform(obj=T1[0], mat=T1[1], sym="rho_1", col=RED, angle=PI/2, operation=rho_1, a=1, b=4, c=3, d=2)
        self.play(WiggleOutThenIn(matrix6, scale_value=2, run_time=2))
        char = cdelta_1.copy().shift(RIGHT+UP).set_color(BLUE_D)
        self.play(Write(char), FadeOut(group))
        group = VGroup()
        clear_updaters(PI/2)
        ReFlip(axis=np.array([0,3,0]))
        self.wait()

        ## Transform mu1(r1(x)) ##
        T1 = obj=Transform(obj=square, mat=matrix, sym="rho_1", col=RED, angle=PI/2, operation=crho_1, a=2, b=3, c=4, d=1)
        T2 = Transform(obj=T1[0], mat=T1[1], sym="mu_1", col=RED, axis=np.array([0,1.5,0]), rotate=False, refl=True, operation=mu_1, a=3, b=2, c=1, d=4)
        self.play(WiggleOutThenIn(matrix7, scale_value=2, run_time=2))
        char = delta_2.copy().shift(DOWN+LEFT*1.5).set_color(BLUE_E)
        self.play(Write(char), FadeOut(group))
        group = VGroup()
        ReFlip(axis=np.array([0,1.5,0]))
        clear_updaters(PI/2)
        self.wait()

        ## Transform r2(mu1(x)) ##
        T1 = obj=Transform(obj=square, mat=matrix, sym="mu_1", col=RED, axis=np.array([0,3,0]), rotate=False, refl=True, operation=cmu_1, a=4, b=3, c=2, d=1)
        T2 = Transform(obj=T1[0], mat=T1[1], sym="rho_2", col=RED, angle=PI, operation=rho_2, a=2, b=1, c=4, d=3)
        self.play(WiggleOutThenIn(matrix5, scale_value=2, run_time=2))
        char = cmu_2.copy().shift(RIGHT*1.5+UP*0.5).set_color(BLUE)
        self.play(Write(char), FadeOut(group))
        group = VGroup()
        clear_updaters(PI)
        ReFlip(axis=np.array([0,3,0]))
        self.wait()

        ## Transform mu1(r2(x)) ##
        T1 = obj=Transform(obj=square, mat=matrix, sym="rho_2", col=RED, angle=PI, operation=crho_2, a=3, b=4, c=1, d=2)
        T2 = Transform(obj=T1[0], mat=T1[1], sym="mu_1", col=RED, axis=np.array([0,1.5,0]), rotate=False, refl=True, operation=mu_1, a=2, b=1, c=4, d=3)
        self.play(WiggleOutThenIn(matrix5, scale_value=2, run_time=2))
        char = mu_2.copy().shift(DOWN*1.5+LEFT*0.5).set_color(BLUE)
        self.play(Write(char), FadeOut(group))
        group = VGroup()
        ReFlip(axis=np.array([0,1.5,0]))
        clear_updaters(PI)
        self.wait()

        ## Transform r3(mu1(x)) ##
        T1 = obj=Transform(obj=square, mat=matrix, sym="mu_1", col=RED, axis=np.array([0,3,0]), rotate=False, refl=True, operation=cmu_1, a=4, b=3, c=2, d=1)
        T2 = Transform(obj=T1[0], mat=T1[1], sym="rho_3", col=RED, angle=3*PI/2, operation=rho_3, a=3, b=2, c=1, d=4)
        self.play(WiggleOutThenIn(matrix7, scale_value=2, run_time=2))
        char = cdelta_2.copy().shift(RIGHT*2+UP*1.5).set_color(BLUE_E)
        self.play(Write(char), FadeOut(group))
        group = VGroup()
        clear_updaters(3*PI/2)
        ReFlip(axis=np.array([0,3,0]))
        self.wait()

        ## Transform mu1(r3(x)) ##
        T1 = obj=Transform(obj=square, mat=matrix, sym="rho_3", col=RED, angle=3*PI/2, operation=crho_3, a=4, b=1, c=2, d=3)
        T2 = Transform(obj=T1[0], mat=T1[1], sym="mu_1", col=RED, axis=np.array([0,1.5,0]), rotate=False, refl=True, operation=mu_1, a=1, b=4, c=3, d=2)
        self.play(WiggleOutThenIn(matrix6, scale_value=2, run_time=2))
        char = delta_1.copy().shift(DOWN*2+LEFT).set_color(BLUE_D)
        self.play(Write(char), FadeOut(group))
        group = VGroup()
        ReFlip(axis=np.array([0,1.5,0]))
        clear_updaters(3*PI/2)
        self.wait()

        ## FILL in the remaining sections ##
        char0 = cdelta_2.copy().shift(UP+RIGHT).set_color(BLUE_E)
        char1 = cmu_1.copy().shift(DOWN*0.5+RIGHT*1.5).set_color(GREEN_E)
        char2 = cdelta_1.copy().shift(UP*0.5+RIGHT*2).set_color(BLUE_D)
        char3 = cmu_2.copy().shift(DOWN*0.5+RIGHT).set_color(BLUE)
        char4 = cdelta_2.copy().shift(UP*0.5+RIGHT*1.5).set_color(BLUE_E)
        char5 = cmu_1.copy().shift(DOWN+RIGHT*2).set_color(GREEN_E)
        char6 = cmu_1.copy().shift(DOWN*1.5+RIGHT).set_color(GREEN_E)
        char7 = cdelta_1.copy().shift(DOWN*0.5+RIGHT*1.5).set_color(BLUE_D)
        char8 = cmu_2.copy().shift(DOWN+RIGHT*2).set_color(BLUE)
        char9 = mu_1.copy().shift(DOWN+RIGHT).set_color(GREEN_E)
        char10 = delta_1.copy().shift(DOWN+LEFT*0.5).set_color(BLUE_D)
        char11 = mu_2.copy().shift(DOWN+RIGHT).set_color(BLUE)
        char12 = mu_1.copy().shift(DOWN*1.5+RIGHT*0.5).set_color(GREEN_E)
        char13 = delta_2.copy().shift(DOWN*1.5+LEFT*0.5).set_color(BLUE_E)
        char14 = delta_1.copy().shift(DOWN*1.5+RIGHT*0.5).set_color(BLUE_D)
        char15 = delta_2.copy().shift(DOWN*2+LEFT).set_color(BLUE_E)
        char16 = mu_2.copy().shift(DOWN*2+RIGHT*0.5).set_color(BLUE)
        char17 = mu_1.copy().shift(DOWN*2+RIGHT*1.5).set_color(GREEN_E)


        chars=[char1, char2, char3, char4, char5, char6, char7, char8, char0]
        greek = [rho_1, rho_2, rho_3, cmu_2, cdelta_1, cdelta_2]
        self.play(*[WiggleOutThenIn(mob, scale_value=2) for mob in greek])
        self.play(*[Write(mob) for mob in chars])
        self.wait()
        chars=[char9, char12, char13, char14, char15, char16, char17, char11, char10]
        greek = [crho_1, crho_2, crho_3, mu_2, delta_1, delta_2]
        self.play(*[WiggleOutThenIn(mob, scale_value=2) for mob in greek])
        self.play(*[Write(mob) for mob in chars])
        self.wait(3)


        ## Transform mu1(mu1(x)) ##
        T1 = obj=Transform(obj=square, mat=matrix, sym="mu_1", col=RED, axis=np.array([0,3,0]), rotate=False, refl=True, operation=cmu_1, a=4, b=3, c=2, d=1)
        T2 = Transform(obj=T1[0], mat=T1[1], sym="mu_1", col=RED, axis=np.array([-0,1.5,0]), rotate=False, refl=True, operation=mu_1, a=1, b=2, c=3, d=4)
        self.play(WiggleOutThenIn(matrix0, scale_value=2, run_time=2))
        char = crho_0.copy().shift(DOWN*2+RIGHT*2.5).set_color(RED)
        self.play(Write(char), FadeOut(group))
        group = VGroup()
        ReFlip(axis=np.array([0,1.5,0]))
        ReFlip(axis=np.array([0,3,0]))
        clear_updaters(0)
        self.wait()

        ## Transform mu2(mu2(x)) ##
        T1 = obj=Transform(obj=square, mat=matrix, sym="mu_2", col=RED, axis=np.array([-2,0,0]), rotate=False, refl=True, operation=cmu_2, a=2, b=1, c=4, d=3)
        T2 = Transform(obj=T1[0], mat=T1[1], sym="mu_2", col=RED, axis=np.array([2,0,0]), rotate=False, refl=True, operation=mu_2, a=1, b=2, c=3, d=4)
        self.play(WiggleOutThenIn(matrix0, scale_value=2, run_time=2))
        char = crho_0.copy().shift(DOWN*2.5+RIGHT*3).set_color(RED)
        self.play(Write(char), FadeOut(group))
        group = VGroup()
        ReFlip(axis=np.array([0,1.5,0]))
        ReFlip(axis=np.array([0,3,0]))
        clear_updaters(0)
        self.wait()

        ## FILL in the remaining sections ##
        char0 = rho_0.copy().shift(DOWN*3.5+RIGHT*3).set_color(RED)
        char1 = rho_0.copy().shift(DOWN*4+RIGHT*3.5).set_color(RED)
        chars=[char1, char0]
        greek = [cdelta_1, cdelta_2, delta_1, delta_2]
        self.play(*[WiggleOutThenIn(mob, scale_value=2) for mob in greek])
        self.play(*[Write(mob) for mob in chars])
        self.wait()
        self.wait()


        ## Transform mu2(mu1(x)) ##
        T1 = obj=Transform(obj=square, mat=matrix, sym="mu_1", col=RED, axis=np.array([0,3,0]), rotate=False, refl=True, operation=cmu_1, a=4, b=3, c=2, d=1)
        T2 = Transform(obj=T1[0], mat=T1[1], sym="mu_2", col=RED, axis=np.array([-2,0,0]), rotate=False, refl=True, operation=mu_2, a=3, b=4, c=1, d=2)
        self.play(WiggleOutThenIn(matrix2, scale_value=2, run_time=2))
        char = crho_2.copy().shift(DOWN+RIGHT*3).set_color(YELLOW)
        self.play(Write(char), FadeOut(group))
        group = VGroup()
        ReFlip(axis=np.array([-2,0,0]))
        ReFlip(axis=np.array([0,3,0]))
        clear_updaters(0)
        self.wait()

        ## Transform mu1(mu2(x)) ##
        T1 = obj=Transform(obj=square, mat=matrix, sym="mu_2", col=RED, axis=np.array([-2,0,0]), rotate=False, refl=True, operation=cmu_2, a=2, b=1, c=4, d=3)
        T2 = Transform(obj=T1[0], mat=T1[1], sym="mu_1", col=RED, axis=np.array([-0,1.5,0]), rotate=False, refl=True, operation=mu_1, a=3, b=4, c=1, d=2)
        self.play(WiggleOutThenIn(matrix2, scale_value=2, run_time=2))
        char = rho_2.copy().shift(DOWN*3+RIGHT).set_color(YELLOW)
        self.play(Write(char), FadeOut(group))
        group = VGroup()
        ReFlip(axis=np.array([0,1.5,0]))
        ReFlip(axis=np.array([-2,0,0]))
        clear_updaters(0)
        self.wait()


        ## Transform delta1(mu2(x)) ##
        T1 = obj=Transform(obj=square, mat=matrix, sym="mu_2", col=RED, axis=np.array([-2,0,0]), rotate=False, refl=True, operation=cmu_2, a=2, b=1, c=4, d=3)
        T2 = Transform(obj=T1[0], mat=T1[1], sym="delta_1", col=RED, axis=np.array([-2,2,0]), rotate=False, refl=True, operation=delta_1, a=4, b=1, c=2, d=3)
        self.play(WiggleOutThenIn(matrix3, scale_value=2, run_time=2))
        char = rho_3.copy().shift(DOWN*3+RIGHT*1.5).set_color(GREEN_D)
        self.play(Write(char), FadeOut(group))
        group = VGroup()
        ReFlip(axis=np.array([-2,2,0]))
        ReFlip(axis=np.array([-2,0,0]))
        clear_updaters(0)
        self.wait()

        ## Transform mu2(delta1(x)) ##
        T1 = obj=Transform(obj=square, mat=matrix, sym="delta_1", col=RED, axis=np.array([-2,2,0]), rotate=False, refl=True, operation=cdelta_1, a=1, b=4, c=3, d=2)
        T2 = Transform(obj=T1[0], mat=T1[1], sym="mu_2", col=RED, axis=np.array([-2,0,0]), rotate=False, refl=True, operation=mu_2, a=2, b=3, c=4, d=1)
        self.play(WiggleOutThenIn(matrix1, scale_value=2, run_time=2))
        char = rho_1.copy().shift(DOWN*3.5+RIGHT*2).set_color(ORANGE)
        self.play(Write(char), FadeOut(group))
        group = VGroup()
        ReFlip(axis=np.array([-2,0,0]))
        ReFlip(axis=np.array([-2,2,0]))
        clear_updaters(0)
        self.wait()

        ## Transform mu1(delta1(x)) ##
        T1 = obj=Transform(obj=square, mat=matrix, sym="delta_1", col=RED, axis=np.array([-2,2,0]), rotate=False, refl=True, operation=cdelta_1, a=1, b=4, c=3, d=2)
        T2 = Transform(obj=T1[0], mat=T1[1], sym="mu_1", col=RED, axis=np.array([-0,1.5,0]), rotate=False, refl=True, operation=mu_1, a=4, b=1, c=2, d=3)
        self.play(WiggleOutThenIn(matrix3, scale_value=2, run_time=2))
        char = rho_3.copy().shift(DOWN*3.5+RIGHT*0.5).set_color(GREEN_D)
        self.play(Write(char), FadeOut(group))
        group = VGroup()
        ReFlip(axis=np.array([0,1.5,0]))
        ReFlip(axis=np.array([-2,2,0]))
        clear_updaters(0)
        self.wait()

        ## Transform delta1(mu1x)) ##
        T1 = obj=Transform(obj=square, mat=matrix, sym="mu_1", col=RED, axis=np.array([0,3,0]), rotate=False, refl=True, operation=cmu_2, a=4, b=3, c=2, d=1)
        T2 = Transform(obj=T1[0], mat=T1[1], sym="delta_1", col=RED, axis=np.array([-2,2,0]), rotate=False, refl=True, operation=delta_1, a=2, b=3, c=4, d=1)
        self.play(WiggleOutThenIn(matrix1, scale_value=2, run_time=2))
        char = rho_1.copy().shift(DOWN*2.5+RIGHT*2.5).set_color(YELLOW)
        self.play(Write(char), FadeOut(group))
        group = VGroup()
        ReFlip(axis=np.array([-2,2,0]))
        ReFlip(axis=np.array([0,3,0]))
        clear_updaters(0)
        self.wait()


        ## FILL in the remaining sections ##
        char0 = crho_1.copy().shift(DOWN*3+RIGHT*2.5).set_color(ORANGE)
        char1 = crho_3.copy().shift(DOWN*2+RIGHT*3).set_color(GREEN_D)
        char2 = crho_2.copy().shift(DOWN*2.5+RIGHT*3.5).set_color(YELLOW)
        char3 = rho_3.copy().shift(DOWN*2.5+RIGHT*2).set_color(GREEN_D)
        char4 = rho_1.copy().shift(DOWN*3+RIGHT*3).set_color(ORANGE)
        char5 = rho_2.copy().shift(DOWN*3.5+RIGHT*2.5).set_color(YELLOW)

        chars=[char1, char0, char2]
        greek = [cdelta_2, mu_1, mu_2, delta_1]
        self.play(*[WiggleOutThenIn(mob, scale_value=2) for mob in greek])
        self.play(*[Write(mob) for mob in chars])
        chars=[char3, char4, char5]
        greek = [delta_2, cmu_1, cmu_2, cdelta_1]
        self.play(*[WiggleOutThenIn(mob, scale_value=2) for mob in greek])
        self.play(*[Write(mob) for mob in chars])
        self.wait(2)
        self.play(FadeOutAndShiftDown(Table_Group))
        self.wait(3)

class Properties(Scene):
    def construct(self):

        ## Creating Last Scene

        global Table_Group, Properties, Fade
        Table_Group, Properties, Fade, Words = VGroup(), VGroup(), VGroup(), VGroup()
        ###~ CREATING LAST SCENE ~###
        ##Function to Create Table ##
        def Table():

            global circ, rho_0, rho_1, rho_2, rho_3, mu_1, mu_2, delta_1, delta_2, crho_0, crho_1, crho_2, crho_3, cmu_1, cmu_2, cdelta_1, cdelta_2, lines_remove, hletters, vletters

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

            letters, hletters, vletters = VGroup(), VGroup(), VGroup()
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
            hletters.add(rho_0, rho_1, rho_2, rho_3, mu_1, mu_2, delta_1, delta_2)


            crho_0 = Letters("rho_0").move_to(UP*3+LEFT*6.5)
            crho_1 = Letters("rho_1").move_to(UP*2.5+LEFT*6.5)
            crho_2 = Letters("rho_2").move_to(UP*2+LEFT*6.5)
            crho_3 = Letters("rho_3").move_to(UP*1.5+LEFT*6.5)
            cmu_1 = Letters("mu_1").move_to(UP+LEFT*6.5)
            cmu_2 = Letters("mu_2").move_to(UP*0.5+LEFT*6.5)
            cdelta_1 = Letters("delta_1").move_to(LEFT*6.5)
            cdelta_2 = Letters("delta_2").move_to(DOWN*0.5+LEFT*6.5)
            letters.add(crho_0, crho_1, crho_2, crho_3, cmu_1, cmu_2, cdelta_1, cdelta_2)
            vletters.add(crho_0, crho_1, crho_2, crho_3, cmu_1, cmu_2, cdelta_1, cdelta_2)

            vlines = VertLines(up=UP*3.75, left=LEFT*6.25, down=DOWN*0.75, space=0.5, no=8)
            hlines = HoriLines(up=UP*3.25, left=LEFT*6.75, right=LEFT*2.25, space=0.5, no=8)
            Table_Group.add(letters, vlines, hlines)

        def Characters():
            global Chars, hchars, vchars, identity, char15, char20, char28, char59, char45, char61, char55, char54
            char0 = rho_0.copy().shift(DOWN*0.5).set_color(RED)
            char1 = rho_1.copy().shift(DOWN*0.5).set_color(ORANGE)
            char2 = crho_1.copy().shift(RIGHT*0.5).set_color(ORANGE)
            char3 = crho_2.copy().shift(RIGHT*0.5).set_color(YELLOW)
            char4 = crho_3.copy().shift(RIGHT*0.5).set_color(GREEN_D)
            char5 = cmu_1.copy().shift(RIGHT*0.5).set_color(GREEN_E)
            char6 = cmu_2.copy().shift(RIGHT*0.5).set_color(BLUE)
            char7 = cdelta_1.copy().shift(RIGHT*0.5).set_color(BLUE_D)
            char8 = cdelta_2.copy().shift(RIGHT*0.5).set_color(BLUE_E)
            char9 = rho_2.copy().shift(DOWN*0.5).set_color(YELLOW)
            char10 = rho_3.copy().shift(DOWN*0.5).set_color(GREEN_D)
            char11 = mu_1.copy().shift(DOWN*0.5).set_color(GREEN_E)
            char12 = mu_2.copy().shift(DOWN*0.5).set_color(BLUE)
            char13 = delta_1.copy().shift(DOWN*0.5).set_color(BLUE_D)
            char14 = delta_2.copy().shift(DOWN*0.5).set_color(BLUE_E)
            char15 = crho_0.copy().shift(DOWN*0.5+RIGHT*2).set_color(RED)
            char16 = crho_1.copy().shift(DOWN*0.5+RIGHT*2).set_color(ORANGE)
            char17 = crho_2.copy().shift(DOWN*0.5+RIGHT*2).set_color(YELLOW)
            char18 = crho_3.copy().shift(UP*0.5+RIGHT).set_color(GREEN_D)
            char19 = crho_0.copy().shift(DOWN+RIGHT*1.5).set_color(RED)
            char20 = rho_0.copy().shift(DOWN*2+RIGHT*0.5).set_color(RED)
            char21 = rho_1.copy().shift(DOWN*2+RIGHT*0.5).set_color(ORANGE)
            char22 = rho_2.copy().shift(DOWN+LEFT*0.5).set_color(YELLOW)
            char23 = rho_3.copy().shift(DOWN+LEFT*0.5).set_color(GREEN_D)
            char24 = cdelta_1.copy().shift(RIGHT+UP).set_color(BLUE_D)
            char25 = delta_2.copy().shift(DOWN+LEFT*1.5).set_color(BLUE_E)
            char26 = cmu_2.copy().shift(RIGHT*1.5+UP*0.5).set_color(BLUE)
            char27 = mu_2.copy().shift(DOWN*1.5+LEFT*0.5).set_color(BLUE)
            char28 = cdelta_2.copy().shift(RIGHT*2+UP*1.5).set_color(BLUE_E)
            char29 = delta_1.copy().shift(DOWN*2+LEFT).set_color(BLUE_D)
            char30 = cdelta_2.copy().shift(UP+RIGHT).set_color(BLUE_E)
            char31 = cmu_1.copy().shift(DOWN*0.5+RIGHT*1.5).set_color(GREEN_E)
            char32 = cdelta_1.copy().shift(UP*0.5+RIGHT*2).set_color(BLUE_D)
            char33 = cmu_2.copy().shift(DOWN*0.5+RIGHT).set_color(BLUE)
            char34 = cdelta_2.copy().shift(UP*0.5+RIGHT*1.5).set_color(BLUE_E)
            char35 = cmu_1.copy().shift(DOWN+RIGHT*2).set_color(GREEN_E)
            char36 = cmu_1.copy().shift(DOWN*1.5+RIGHT).set_color(GREEN_E)
            char37 = cdelta_1.copy().shift(DOWN*0.5+RIGHT*1.5).set_color(BLUE_D)
            char38 = cmu_2.copy().shift(DOWN+RIGHT*2).set_color(BLUE)
            char39 = mu_1.copy().shift(DOWN+RIGHT).set_color(GREEN_E)
            char40 = delta_1.copy().shift(DOWN+LEFT*0.5).set_color(BLUE_D)
            char41 = mu_2.copy().shift(DOWN+RIGHT).set_color(BLUE)
            char42 = mu_1.copy().shift(DOWN*1.5+RIGHT*0.5).set_color(GREEN_E)
            char43 = delta_2.copy().shift(DOWN*1.5+LEFT*0.5).set_color(BLUE_E)
            char44 = delta_1.copy().shift(DOWN*1.5+RIGHT*0.5).set_color(BLUE_D)
            char45 = delta_2.copy().shift(DOWN*2+LEFT).set_color(BLUE_E)
            char46 = mu_2.copy().shift(DOWN*2+RIGHT*0.5).set_color(BLUE)
            char47 = mu_1.copy().shift(DOWN*2+RIGHT*1.5).set_color(GREEN_E)
            char48 = crho_0.copy().shift(DOWN*2+RIGHT*2.5).set_color(RED)
            char49 = crho_0.copy().shift(DOWN*2.5+RIGHT*3).set_color(RED)
            char50 = rho_0.copy().shift(DOWN*3.5+RIGHT*3).set_color(RED)
            char51 = rho_0.copy().shift(DOWN*4+RIGHT*3.5).set_color(RED)
            char52 = crho_2.copy().shift(DOWN+RIGHT*3).set_color(YELLOW)
            char53 = rho_2.copy().shift(DOWN*3+RIGHT).set_color(YELLOW)
            char54 = rho_3.copy().shift(DOWN*3+RIGHT*1.5).set_color(GREEN_D)
            char55 = rho_1.copy().shift(DOWN*3.5+RIGHT*2).set_color(ORANGE)
            char56 = rho_3.copy().shift(DOWN*3.5+RIGHT*0.5).set_color(GREEN_D)
            char57 = rho_1.copy().shift(DOWN*2.5+RIGHT*2.5).set_color(YELLOW)
            char58 = crho_1.copy().shift(DOWN*3+RIGHT*2.5).set_color(ORANGE)
            char59 = crho_3.copy().shift(DOWN*2+RIGHT*3).set_color(GREEN_D)
            char60 = crho_2.copy().shift(DOWN*2.5+RIGHT*3.5).set_color(YELLOW)
            char61 = rho_3.copy().shift(DOWN*2.5+RIGHT*2).set_color(GREEN_D)
            char62 = rho_1.copy().shift(DOWN*3+RIGHT*3).set_color(ORANGE)
            char63 = rho_2.copy().shift(DOWN*3.5+RIGHT*2.5).set_color(YELLOW)

            Table_Group.add(char0,char1,char2,char3,char4,char5,char6,char7,char8,char9,char10,char11,char12,char13,char14,char15,char16,char17,char18,char19,char20,char21,char22,char23,char24,char25,char26,char27,char28,char29,char30,char31,char32,char33,char34,char35,char36,char37,char38,char39,char40,char41,char42,char43,char44,char45,char46,char47,char48,char49,char50,char51,char52,char53,char54,char55,char56,char57,char58,char59,char60,char61,char62,char63)

            Chars = VGroup(char0,char1,char2,char3,char4,char5,char6,char7,char8,char9,char10,char11,char12,char13,char14,char15,char16,char17,char18,char19,char20,char21,char22,char23,char24,char25,char26,char27,char28,char29,char30,char31,char32,char33,char34,char35,char36,char37,char38,char39,char40,char41,char42,char43,char44,char45,char46,char47,char48,char49,char50,char51,char52,char53,char54,char55,char56,char57,char58,char59,char60,char61,char62,char63)

            hchars = VGroup(char0, char1, char9, char10, char11, char12, char13, char14,)
            vchars = VGroup(char0, char2, char3, char4, char5, char6, char7, char8)
            identity = VGroup(char0, char15, char19, char20, char48, char49, char50, char51)

        def CreateProperties():
            global prop, prop1, prop1_1, prop2, prop2_1, prop3, prop3_1, prop4, prop4_1, prop5, prop5_1, Property_Group, Properties
            ## 1st Property - CLOSED ##
            Property_Group, Properties = VGroup(), VGroup()
            prop = TextMobject("Properties :- ", color=GOLD).scale(1.5).move_to(LEFT*4+UP*2.5)
            # Coloring The Required Characteres #
            prop1 = TexMobject(
                                "1. \\ \\ \\ \\",                   #0
                                "\\text{If    }\\ \\",              #1
                                "f_1",                              #2
                                ",",                                #3
                                "f_2\\,",                           #4
                                "\\in\\,",                          #5
                                "G",                                #6
                                "\\ \\ \\text{,  then    } \\ \\",  #7
                                "f_1",                              #8
                                "\\circ",                           #9
                                "f_2\\,",                           #10
                                "\\in",                             #11
                                "G"                                 #12
            ).scale(0.7)
            prop1[2].set_color(BLUE_D)
            prop1[4].set_color(RED)
            prop1[5].set_color(YELLOW)
            prop1[6].set_color(GREEN_E)
            prop1[8].set_color(BLUE_D)
            prop1[9].set_color(YELLOW)
            prop1[10].set_color(RED)
            prop1[11].set_color(YELLOW)
            prop1[12].set_color(GREEN)
            prop1.move_to(LEFT*3.5+UP*1.5)
            # Writing Property 1 in Words #
            prop1_1 = TexMobject(
                                    "(\\, \\text{ i.e }",   #0
                                    "G",                    #1
                                    "\\text{ is}\\ \\ ",    #2
                                    "Closed",               #3
                                    "\\ \\ \\text{under }", #4
                                    "\\circ",               #5
                                    "\\text{ operation.}",  #6
                                    "\\,)"                  #7
            ).scale(0.7)
            prop1_1.next_to(prop1, RIGHT*2)
            prop1_1[1].set_color(GREEN_D)
            prop1_1[3].set_color(RED)
            prop1_1[5].set_color(YELLOW)
            # Add both to the Group Properties
            Properties.add(prop, prop1.set_opacity(0), prop1_1.set_opacity(0))

            ## 2nd Property ##
            prop2 = TexMobject(
                                "2. \\ \\ \\ \\",           #0
                                "\\ \\ \\forall\\,",        #1
                                "f \\,",                    #2
                                "\\in\\,",                  #3
                                "G",                        #4
                                ",\\ \\",                   #5
                                "f",                        #6
                                "\\circ",                   #7
                                "\\rho_0",                  #8
                                "\\ \\ = \\ \\,",           #9
                                "\\rho_0",                  #10
                                "\\circ",                   #11
                                "f",                        #12
                                "\\ \\ = \\ \\,",           #13
                                "f"                         #14
            ).scale(0.7)
            prop2[1].set_color(YELLOW)
            prop2[2].set_color(BLUE_D)
            prop2[3].set_color(YELLOW)
            prop2[4].set_color(GREEN_D)
            prop2[6].set_color(BLUE_D)
            prop2[7].set_color(YELLOW)
            prop2[8].set_color(RED)
            prop2[10].set_color(RED)
            prop2[11].set_color(YELLOW)
            prop2[12].set_color(BLUE_D)
            prop2[14].set_color(BLUE_D)
            #   Property 2 in words #
            prop2_1 = TexMobject(
                                    "(\\,\\text{ i.e }",            #0
                                    "\\text{ Existence of }",       #1
                                    "Identity",                     #2
                                    "\\text{ element}",              #3
                                    "\\,)"                          #4
            ).scale(0.7)
            #   Set Color#
            prop2_1[1].set_color(RED)
            #  Move to Required Position    #
            prop2[0].next_to(prop1[0], DOWN*2)
            prop2[1:].next_to(prop2[0])
            prop2_1.next_to(prop2, RIGHT*2)
            # Add both to the Group Properties
            Properties.add(prop2.set_opacity(0), prop2_1.set_opacity(0))

            ##  3rd Property   ##
            prop3 = TexMobject(
                                "3. \\ \\ \\ \\",   #0
                                "\\forall\\,",      #1
                                "f\\,",             #2
                                "\\in\\,",          #3
                                "G",                #4
                                ",\\ \\",           #5
                                "\\exists\\,",      #6
                                "f^{-1}\\,",        #7
                                "\\in\\,",          #8
                                "G",                #9
                                "\\ \\ \\text{ such that }",    #10
                                "f",                #11
                                "\\circ",           #12
                                "f^{-1}",           #13
                                "\\ \\ = \\ \\",    #14
                                "f^{-1}",           #15
                                "\\circ",           #16
                                "f",                #17
                                "\\ \\ = \\ \\",    #18
                                "\\rho_0"           #19
                                ).scale(0.7)
            prop3[1].set_color(YELLOW)
            prop3[2].set_color(BLUE_D)
            prop3[3].set_color(YELLOW)
            prop3[4].set_color(GREEN_D)
            prop3[6].set_color(YELLOW)#exists
            prop3[7].set_color("#d65435")
            prop3[8].set_color(YELLOW)
            prop3[9].set_color(GREEN_D)
            prop3[11].set_color(BLUE_D)
            prop3[12].set_color(GOLD)
            prop3[13].set_color("#d65435")
            prop3[15].set_color("#d65435")
            prop3[16].set_color(GOLD)
            prop3[17].set_color(BLUE_D)
            prop3[19].set_color(RED)
            prop3[0].next_to(prop2[0], DOWN*2)
            prop3[1:].next_to(prop3[0])
            #   Property 3 in WOrds #
            prop3_1 = TexMobject(
                                    "(\\,",                         #0
                                    "\\text{i.e}\\ \\",             #1
                                    "\\text{Existence  of} \\ \\",  #2
                                    "Inverse",                      #3
                                    "\\ \\ )"                       #4
            ).scale(0.7)
            prop3_1[2].set_color(RED)
            prop3_1.next_to(prop3, DOWN*0.7)
            Properties.add(prop3.set_opacity(0), prop3_1.set_opacity(0))

            ##  4th Property  ##
            prop4 = TexMobject(
                                "4.\\ \\ \\ \\ ",               #0
                                "\\text{If}\\ \\",          #1
                                "f_1",                      #2
                                ",\\,",                     #3
                                "f_2",                      #4
                                ",\\,",                     #5
                                "f_3",                      #6
                                "\\,\\in\\,",               #7
                                "G",                        #8
                                "\\ \\ \\ \\ \\text{then}", #9
                                "\\ \\ \\ \\ (",            #10
                                "f_1",                      #11
                                "\\circ",                   #12
                                "f_2",                      #13
                                ")",                        #14
                                "\\circ",                   #15
                                "f_3",                      #16
                                "\\ \\ = \\ \\",            #17
                                "f_1",                      #18
                                "\\circ",                   #19
                                "(",                        #20
                                "f_2",                      #21
                                "\\circ",                   #22
                                "f_3",                      #23
                                ")"                         #24
            ).scale(0.7)
            prop4[2].set_color(RED)
            prop4[4].set_color(GREEN_E)
            prop4[6].set_color(BLUE_D)
            prop4[7].set_color(YELLOW)
            prop4[8].set_color(GREEN_D)
            prop4[11].set_color(RED)
            prop4[12].set_color(GOLD)
            prop4[13].set_color(GREEN_E)
            prop4[15].set_color(GOLD)
            prop4[16].set_color(BLUE_D)
            prop4[18].set_color(RED)
            prop4[19].set_color(GOLD)
            prop4[21].set_color(GREEN_E)
            prop4[22].set_color(GOLD)
            prop4[23].set_color(BLUE_D)
            prop4[0].next_to(prop3[0], DOWN*4)
            prop4[1:].next_to(prop4[0])
            #   Propert4 in Words   #
            prop4_1 = TexMobject(
                                    "(\\, \\text{i.e  }",
                                    "Associativity",
                                    "\\,)"
            ).scale(0.7)
            prop4_1[1].set_color(RED)
            prop4_1.next_to(prop4, RIGHT*2)
            Properties.add(prop4.set_opacity(0), prop4_1.set_opacity(0))

            ## 5th Propperty  ##
            prop5 = TexMobject(
                                "5.\\ \\",              #0
                                "\exists\\,",           #1
                                "f_1\\,",               #2
                                ",",                    #3
                                "f_2\\,",               #4
                                "\\in\\,",              #5
                                "G",                    #6
                                "\\text{ such that }",  #7
                                "f_1",                  #8
                                "\\circ",               #9
                                "f_2",                  #10
                                "\\neq",                #11
                                "f_2",                  #12
                                "\\circ",               #13
                                "f_1"                   #14
            ).scale(0.7)
            prop5[1].set_color(YELLOW)
            prop5[2].set_color(BLUE_D)
            prop5[4].set_color(RED)
            prop5[5].set_color(YELLOW)
            prop5[6].set_color(GREEN_D)
            prop5[8].set_color(BLUE_D)
            prop5[9].set_color(YELLOW)
            prop5[10].set_color(RED)
            prop5[12].set_color(RED)
            prop5[13].set_color(YELLOW)
            prop5[14].set_color(BLUE_D)
            # Property 5 in Words #
            prop5_1 = TexMobject(
                                    "(\\, i.e\\ \\",    #0
                                    "G",                #1
                                    "\\text{ is }",     #2
                                    "Non-Abelian",      #3
                                    ")"                 #4
            ).scale(0.7)
            prop5_1[1].set_color(GREEN_D)
            prop5_1[3].set_color(RED)
            #   Move to required position   #
            prop5[0].next_to(prop4[0], DOWN*2)
            prop5[1:].next_to(prop5[0])
            prop5_1.next_to(prop5, RIGHT*2)
            Properties.add(prop5.set_opacity(0), prop5_1.set_opacity(0))

        def Property1():
            self.play(WiggleOutThenIn(Chars, scale_value=2, run_time=3))
            self.play(FadeOutAndShiftDown(Table_Group))
            self.play(Write(prop.set_opacity(1)))
            self.wait()
            self.play(Write(prop1[:7].set_opacity(1), run_time=2))
            self.wait()
            self.play(Write(prop1[7:].set_opacity(1), run_time=2))
            self.wait()
            self.play(Write(prop1_1.set_opacity(1), run_time=2))
            self.wait(3)
            self.play(FadeOutAndShift(Properties, UP),  FadeInFromDown(Table_Group, run_time=2))
            self.wait(2)
            Fade.add(prop, prop1, prop1_1[0], prop1_1[7])

        def Property2():
            self.play(WiggleOutThenIn(crho_0, scale_value=2))
            self.play(WiggleOutThenIn(hletters, run_time=2))
            self.play(Indicate(hchars, scale_factor=1.5), run_time=2)
            self.wait()
            self.play(WiggleOutThenIn(vletters, run_time=2))
            self.play(WiggleOutThenIn(rho_0, scale_value=2))
            self.play(Indicate(vchars, scale_factor=1.5), run_time=2)
            self.wait()
            self.play(FadeOutAndShiftDown(Table_Group), FadeInFrom(Properties, UP, run_time=2))
            self.wait()
            self.play(Write(prop2[:6].set_opacity(1), run_time=2))
            self.wait()
            self.play(Write(prop2[6:9].set_opacity(1)))
            self.wait()
            self.play(Write(prop2[9:13].set_opacity(1)))
            self.wait()
            self.play(Write(prop2[13:].set_opacity(1)))
            self.wait()
            self.play(Write(prop2_1.set_opacity(1)))
            self.wait(3)
            self.play(FadeOutAndShift(Properties, UP),  FadeInFromDown(Table_Group, DOWN, run_time=2))
            Fade.add(prop2, prop2_1[0], prop2_1[4])

        def Property3():
            self.play(WiggleOutThenIn(identity, rum_time=2))
            self.play(WiggleOutThenIn(crho_1, scale_value=2, rum_time=2), WiggleOutThenIn(rho_3, scale_value=2, rum_time=2))
            self.wait()
            self.play(Indicate(char15, scale_factor=2, run_time=2))
            self.wait()
            self.play(WiggleOutThenIn(rho_1, scale_value=2, rum_time=2), WiggleOutThenIn(crho_3, scale_value=2, rum_time=2))
            self.wait()
            self.play(Indicate(char20, scale_factor=2, run_time=2))
            self.wait()
            self.play(WiggleOutThenIn(identity, rum_time=2))
            self.wait()
            self.play(FadeOutAndShiftDown(Table_Group), FadeInFrom(Properties, UP, run_tim=2))
            self.wait()
            self.play(Write(prop3[:5].set_opacity(1)))
            self.wait()
            self.play(Write(prop3[5:10].set_opacity(1)))
            self.wait()
            self.play(Write(prop3[10:14].set_opacity(1)))
            self.wait()
            self.play(Write(prop3[14:18].set_opacity(1)))
            self.wait()
            self.play(Write(prop3[18:].set_opacity(1)))
            self.wait()
            self.play(Write(prop3_1.set_opacity(1)))
            self.wait()
            self.play(FadeOutAndShift(Properties, UP), FadeInFrom(Table_Group, DOWN,run_time=2))
            self.wait()
            Fade.add(prop3, prop3_1[0:2], prop3_1[4])

        def Property4():
            # Setting up the Pitch
            comp1 = TexMobject(
                                "(\\,",             #0
                                "\\mu_1",           #1
                                "\\circ",           #2
                                "\\rho_3",          #3
                                "\\,)",             #4
                                "\\circ",           #5
                                "\\mu_2",           #6
                                "\\ \\ = \\ \\",    #7
                                "\\rho_3"           #8
            ).scale(0.7)
            comp1[1].set_color(GREEN_E)
            comp1[2].set_color(GOLD)
            comp1[3].set_color(GREEN_D)
            comp1[5].set_color(GOLD)
            comp1[6].set_color(BLUE)
            comp1[8].set_color(GREEN_D)

            comp2 = TexMobject(
                                "\\mu_1",           #0
                                "\\circ",           #1
                                "(\\,",             #2
                                "\\rho_3",          #3
                                "\\circ",           #4
                                "\\mu_2",           #5
                                "\\,)",             #6
                                "\\ \\ = \\ \\",    #7
                                "\\rho_3"           #8
            ).scale(0.7)
            comp2[0].set_color(GREEN_E)
            comp2[1].set_color(GOLD)
            comp2[3].set_color(GREEN_D)
            comp2[4].set_color(GOLD)
            comp2[5].set_color(BLUE)
            comp2[8].set_color(GREEN_D)

            comp1.move_to(UP*2.5+LEFT*5.3)
            comp2.move_to(UP + LEFT*5.3)

            self.play(WiggleOutThenIn(cmu_1, scale_value=2, run_time=2), WiggleOutThenIn(rho_3, scale_value=2, run_time=2), Write(comp1[:5],run_time=2))
            self.play(Indicate(char28, scale_factor=2, run_time=3))
            self.play(WiggleOutThenIn(cdelta_2, scale_value=2, run_time=2), WiggleOutThenIn(mu_2, scale_value=2, run_time=2), Write(comp1[5:7],run_time=2))
            self.play(Indicate(char59, scale_factor=2, run_time=3), Write(comp1[7:], run_time=2))
            self.wait(2)

            self.play(WiggleOutThenIn(crho_3, scale_value=2, run_time=2), WiggleOutThenIn(mu_2, scale_value=2, run_time=2), Write(comp2[2:7],run_time=2))
            self.play(Indicate(char45, scale_factor=2, run_time=3))
            self.play(WiggleOutThenIn(cmu_1, scale_value=2, run_time=2), WiggleOutThenIn(delta_2, scale_value=2, run_time=2), Write(comp2[:2],run_time=2))
            self.play(Indicate(char61, scale_factor=2, run_time=3), Write(comp2[7:], run_time=2))
            self.wait(2)

            self.play(FadeOutAndShiftDown(Table_Group), FadeOut(comp1), FadeOut(comp2), FadeInFrom(Properties, UP, run_time=2))
            self.play(Write(prop4[:9].set_opacity(1)))
            self.wait()
            self.play(Write(prop4[9:17].set_opacity(1)))
            self.wait()
            self.play(Write(prop4[17:].set_opacity(1)))
            self.wait()
            self.play(Write(prop4_1.set_opacity(1)))
            self.wait(2)
            self.play(FadeOutAndShift(Properties, UP), FadeInFrom(Table_Group, run_time=2))
            self.wait(2)
            Fade.add(prop4, prop4_1[0], prop4_1[2])

        def Property5():
            num = TexMobject(
                            "Nos : \\ \\",
                            "a",
                            "\\cdot",
                            "b",
                            "\\ \\ = \\ \\",
                            "b",
                            "\\cdot",
                            "a"
            ).scale(0.7)
            num[0].set_color(GOLD)
            num[1].set_color(RED)
            num[3].set_color(BLUE)
            num[5].set_color(BLUE)
            num[7].set_color(RED)
            num.move_to(LEFT*5.3+UP*2.5)

            lhs = TexMobject(
                                "\\delta_1",
                                "\\circ",
                                "\\mu_2",
                                "\\ \\ = \\ \\",
                                "\\rho_1"
            ).scale(0.7).move_to(LEFT*5.3+UP*1.5)
            lhs[0].set_color(BLUE_D)
            lhs[1].set_color(GOLD)
            lhs[2].set_color(BLUE)
            lhs[4].set_color(ORANGE)

            rhs = TexMobject(
                                "\\mu_2",
                                "\\circ",
                                "\\delta_1",
                                "\\ \\ = \\ \\",
                                "\\rho_3"
            ).scale(0.7).move_to(LEFT*5.3+UP*0.5)
            rhs[0].set_color(BLUE)
            rhs[1].set_color(GOLD)
            rhs[2].set_color(BLUE_D)
            rhs[4].set_color(GREEN_D)

            neq = TexMobject(
                                "\\delta_1",
                                "\\circ",
                                "\\mu_2",
                                "\\ \\ \\neq \\ \\",
                                "\\mu_2",
                                "\\circ",
                                "\\delta_1",
            ).scale(0.7).move_to(LEFT*5.3+DOWN*0.5)
            neq[0].set_color(BLUE_D)
            neq[1].set_color(GOLD)
            neq[2].set_color(BLUE)
            neq[4].set_color(BLUE)
            neq[5].set_color(GOLD)
            neq[6].set_color(BLUE_D)

            self.play(Write(num, run_time=2))
            self.play(WiggleOutThenIn(cdelta_1, scale_value=2, run_time=2),
                        WiggleOutThenIn(mu_2, scale_value=2, run_time=2))
            self.play(Write(lhs[:3], run_time=2))
            self.wait()
            self.play(Indicate(char55, scale_factor=2, run_time=2), Write(lhs[3:], run_time=2))
            self.play(WiggleOutThenIn(delta_1, scale_value=2, run_time=2),
                        WiggleOutThenIn(cmu_2, scale_value=2, run_time=2))
            self.play(Write(rhs[:3], run_time=2))
            self.wait()
            self.play(Indicate(char54, scale_factor=2, run_time=2), Write(rhs[3:], run_time=2))
            self.wait()
            self.play(Write(neq, run_time=2))
            self.wait()
            self.play(FadeOutAndShiftDown(Table_Group), FadeOut(num), FadeOut(lhs), FadeOut(rhs), FadeOut(neq), FadeInFrom(Properties, UP, run_time=2))
            self.wait()
            self.play(Write(prop5[:7].set_opacity(1), run_time=2))
            self.wait()
            self.play(Write(prop5[7:11].set_opacity(1), run_time=2))
            self.wait()
            self.play(Write(prop5[11:].set_opacity(1), run_time=2))
            self.wait()
            self.play(Write(prop5_1.set_opacity(1)))
            Fade.add(prop5, prop5_1[0], prop5_1[5])


        ## Creating and Labeling Table ##
        #Table()
        Table()
        ## Filling in the table ##
        Characters()

        ## Zoom in on the Table and place it in Center ##
        self.add(Table_Group)
        self.wait(2)
        self.play(Table_Group.move_to, Table_Group.get_center()*0, Table_Group.scale, 1.4286)
        self.wait(3)

        ## Writing all Properties in Hidden Way ##
        CreateProperties()



        ## 1st Property ##
        Property1()

        ## 2nd Property ##
        Property2()

        ##  3rd Property ##
        Property3()

        ## 4th Property ##
        Property4()

        ##  5th Property  ##
        Property5()

        ##  FADE AND ALIGN WORDS  ##
        num1 = TexMobject("1.\\ \\ \\ \\").scale(0.7).move_to(UP*2.5+LEFT*5)
        num2 = TexMobject("2.\\ \\ \\ \\").scale(0.7).move_to(UP*1.5+LEFT*5)
        num3 = TexMobject("3.\\ \\ \\ \\").scale(0.7).move_to(UP*0.5+LEFT*5)
        num4 = TexMobject("4.\\ \\ \\ \\").scale(0.7).move_to(DOWN*0.5+LEFT*5)
        num5 = TexMobject("5.\\ \\ \\ \\").scale(0.7).move_to(DOWN*1.5+LEFT*5)
        num = VGroup(num1, num2, num3, num4, num5)
        self.play(FadeOut(Fade))
        self.remove(Fade)
        Fade.set_opacity(0)
        self.play(Write(num), prop1_1[1:7].move_to, prop1_1[1:7].next_to(num1),
        prop2_1[1:4].move_to, prop2_1[1:4].next_to(num2),
        prop3_1[2:4].move_to, prop3_1[2:4].next_to(num3),
        prop4_1[1].move_to,   prop4_1[1].next_to(num4),
        prop5_1[1:5].move_to, prop5_1[1:5].next_to(num5), run_time=3)
        self.wait(3)
        group1 = VGroup(num1, num2, num3, num4, prop1_1, prop2_1, prop3_1, prop4_1)
        group2 = VGroup(num1, num2, num3, num4, num5, prop1_1, prop2_1, prop3_1, prop4_1, prop5_1)
        self.play(group2.shift, RIGHT*5)
        braces1 = Brace(group1, LEFT)
        braces2 = Brace(group2, LEFT)
        text1 = braces1.get_text("GROUP")
        text2 = braces2.get_text("Non - Abelian Group")
        text1.set_color(GOLD)
        text2.set_color(GOLD)

        self.play(ShowCreation(braces1), Write(text1), run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(braces1, braces2, run_time=2),
                    ReplacementTransform(text1, text2, run_time=2))
        self.wait(3)

class Rectangle(Scene):
    def construct(self):

        global group
        group = VGroup()

        ## Function to Number Square ##
        def NumReq(rectangle):
            global one, two, three, four, rectangle_group, line1, line2, RQ1Group
            line1 = Line(rectangle.get_corner(UL)+UP*0.15+LEFT*0.15,
                            rectangle.get_corner(DR)+DOWN*0.15+RIGHT*0.15)
            line2 = Line(rectangle.get_corner(DL)+DOWN*0.15+LEFT*0.15,
                            rectangle.get_corner(UR)+UP*0.15+RIGHT*0.15)
            one = TexMobject(r"1", color=GREEN).scale(0.5).move_to(line1.get_start())
            two = TexMobject(r"2", color=GREEN).scale(0.5).move_to(line2.get_start())
            three = TexMobject(r"3", color=GREEN).scale(0.5).move_to(line1.get_end())
            four = TexMobject(r"4", color=GREEN).scale(0.5).move_to(line2.get_end())
            rectangle_group = VGroup(rectangle, line1.set_opacity(0), line2.set_opacity(0))
            nos = [one, two, three, four]
            self.play(*[Write(num) for num in nos])
            RQ1Group = VGroup(rectangle_group, one, two, three, four,)
            group.add(RQ1Group)

        ## Updater Functions ##
        def update_one(obj):
            obj.move_to(line1.get_start())
        def update_two(obj):
            obj.move_to(line2.get_start())
        def update_three(obj):
            obj.move_to(line1.get_end())
        def update_four(obj):
            obj.move_to(line2.get_end())

        def RectangleRot(rectangle, angle, matrix, pos, sym):
            global one2, two2, three2, four2, RQ2Group

            #  Copy rectangle  #
            rectangle2 = rectangle.copy()

            #  Copy Numbers  #
            one2 = one.copy().set_color(RED).add_updater(update_one)
            two2 = two.copy().set_color(RED).add_updater(update_two)
            three2 = three.copy().set_color(RED).add_updater(update_three)
            four2 = four.copy().set_color(RED).add_updater(update_four)
            self.add(one2, two2, three2, four2)

            #  Create Required Groups  #
            rectangle2 = VGroup(rectangle2, line1.set_opacity(0), line2.set_opacity(0))
            RQ2Group = VGroup(rectangle2, one2, two2, three2, four2)

            # Performed Required Action  #
            self.play(RQ2Group.shift, RIGHT*4.5)
            self.play(Rotate(rectangle2, angle))
            matrix = CreateMatrix(obj=rectangle, matrix=matrix, a=one2, b=two2, c=three2,
                    d=four2,pos1=pos[0], pos2=pos[1], pos3=pos[2], pos4=pos[3], sym=sym)

            return rectangle2, matrix

        def CheckRot(rectangle, angle, op, value):
            rectangle2 = rectangle.copy()
            one2 = one.copy().set_color(RED).add_updater(update_one)
            two2 = two.copy().set_color(RED).add_updater(update_two)
            three2 = three.copy().set_color(RED).add_updater(update_three)
            four2 = four.copy().set_color(RED).add_updater(update_four)
            self.add(one2, two2, three2, four2)
            rectangle2 = VGroup(rectangle2, line1.set_opacity(0), line2.set_opacity(0))
            RQ2Group = VGroup(rectangle2, one2, two2, three2, four2)
            arrow = DrawArrow(rectangle, op=op, value=value)
            self.play(ShowCreation(arrow))
            self.play(RQ2Group.shift, RIGHT*4.5)
            self.play(Rotate(rectangle2, angle), run_time=2)
            self.wait()
            copy = rectangle.copy().set_color(RED)
            self.play(copy.shift, RIGHT*4.5)
            self.wait()
            group.add(RQ2Group, rectangle2)
            return copy, rectangle2, arrow

        def RectangleRefl(rectangle, axis, matrix, pos, sym):
            global one3, two3, three3, four3, RQ3Group, dline

            #  Copy Rectangle  #
            rectangle3 = rectangle.copy()

            #  Copy Numbers  #
            one3 = one.copy().set_color(RED).add_updater(update_one)
            two3 = two.copy().set_color(RED).add_updater(update_two)
            three3 = three.copy().set_color(RED).add_updater(update_three)
            four3 = four.copy().set_color(RED).add_updater(update_four)
            self.add(one3, two3, three3, four3)

            #  Create Required Groups  #
            rectangle3 = VGroup(rectangle3, line1.set_opacity(0), line2.set_opacity(0))
            RQ3Group = VGroup(rectangle3, one3, two3, three3, four3)

            #  Create Line  #
            self.play(RQ3Group.shift, RIGHT*4.5)
            line = Line(ORIGIN, axis).scale(2.5)
            line.move_to(line.get_center()*0 + RQ3Group.get_center())
            dline = DashedVMobject(line)

            #  Perform Required Action  #
            self.play(ShowCreation(dline, run_time=0.5))
            self.play(Rotate(rectangle3, angle=PI, axis=axis))
            matrix = CreateMatrix(obj=rectangle, matrix=matrix, a=one3, b=two3, c=three3,
                    d=four3, pos1=pos[0], pos2=pos[1], pos3=pos[2], pos4=pos[3], sym=sym)

            return rectangle3, matrix

        def CheckRefl(rectangle, axis, op, value):
            global dline
            #  Copy Rectangle  #
            rectangle3 = rectangle.copy()

            #  Copy Numbers  #
            one3 = one.copy().set_color(RED).add_updater(update_one)
            two3 = two.copy().set_color(RED).add_updater(update_two)
            three3 = three.copy().set_color(RED).add_updater(update_three)
            four3 = four.copy().set_color(RED).add_updater(update_four)
            self.add(one3, two3, three3, four3)

            #  Create Required Groups  #
            rectangle3 = VGroup(rectangle3, line1.set_opacity(0), line2.set_opacity(0))
            RQ3Group = VGroup(rectangle3, one3, two3, three3, four3)

            #  Draw Arrow  #
            arrow = DrawArrow(rectangle, op=op, value=value)
            self.play(ShowCreation(arrow))

            #  Create Line  #
            self.play(RQ3Group.shift, RIGHT*4.5)
            line = Line(ORIGIN, axis).scale(2)
            line.move_to(line.get_center()*0 + RQ3Group.get_center())
            dline = DashedVMobject(line)


            #  Perform Required Action  #
            self.play(ShowCreation(dline, run_time=0.5))
            self.play(Rotate(rectangle3, angle=PI, axis=axis))

            copy = rectangle.copy().set_color(RED)
            self.play(copy.shift, RIGHT*4.5)
            self.wait()
            group.add(RQ3Group, rectangle3)
            return copy, rectangle3, arrow

        def MatrixRep(a, b, c, d):
            str = "\\begin{pmatrix1} 1 & 2 & 3 & 4 \\\\ {} & {} & {} & {}\\end{pmatrix2}".format(a, b , c, d, pmatrix1 = "{pmatrix}", pmatrix2="{pmatrix}")
            matrix = TexMobject(str)
            for i in range(1,5):
                matrix[0][i].set_color(GREEN_D)
            for j in range(5,9):
                matrix[0][j].set_color(RED)

            return matrix

        def CreateMatrix(obj, matrix, a, b, c, d, pos1, pos2, pos3, pos4, sym):

            self.play(Write(matrix[0][0]), Write(matrix[0][9]))
            self.play(Write(matrix[0][1:5]))
            pos = [pos1, pos2, pos3, pos4]
            num = [a, b, c, d]
            for i in range(4):
                if (pos[i]==one) or (pos[i]==four):
                    carrow = CurvedArrow(num[i].get_center(), pos[i].get_center(),
                    angle=PI/3).scale(0.9)
                elif (pos[i]==two) or (pos[i]==three):
                    carrow = CurvedArrow(num[i].get_center(), pos[i].get_center(),
                    angle=-PI/3).scale(0.9)

                self.play(ShowCreation(carrow), Write(matrix[0][i+5]))
                self.play(FadeOut(carrow))
                self.remove(carrow)

            symbol = TexMobject("\\{}".format(sym), "\\ \\ =").scale(0.7).next_to(matrix, LEFT)
            self.wait()
            self.play(Write(symbol))
            matrix = VGroup(matrix, symbol)
            return matrix

        def DrawArrow(obj, op, value):
            global arrow_group1
            arrow = Arrow(ORIGIN, RIGHT*2).next_to(obj, RIGHT*1.5)
            operation = TexMobject("{}".format(op)).scale(0.5).next_to(arrow, UP*0.5)
            value = TexMobject("{}".format(value)).scale(0.5).next_to(arrow, DOWN*0.5)
            arrow_group = VGroup(arrow, operation, value)
            return arrow_group

        def clear_updaters(angle):
            line1.move_to(LEFT*4).rotate(-angle)
            line2.move_to(LEFT*4).rotate(-angle)

        def ReFlip(axis):
            line1.rotate(angle=PI, axis=axis)
            line2.rotate(angle=PI, axis=axis)

        def Transform(obj, op, value, a=1, b=2, c=3, d=4, sym="rho_0", angle=PI, axis=IN, rotate=True, refl=False, check=False, pos=[], i=2):
            if(rotate==True and refl==False and check==False):
                a1 = DrawArrow(obj, op, value)
                self.play(ShowCreation(a1), run_time=0.5)
                matrix = MatrixRep(a, b, c, d).next_to(obj, DOWN*5).scale(0.8)
                shape = RectangleRot(rectangle=obj, angle=angle, pos=pos, matrix=matrix, sym=sym)
                rectangle = shape[0]
                matrix = shape[1]
                one2.remove_updater(update_one)
                two2.remove_updater(update_two)
                three2.remove_updater(update_three)
                four2.remove_updater(update_four)
                self.play(FadeOut(a1), FadeOut(RQ2Group))
                clear_updaters(angle)
                self.play(matrix.scale, 0.7, matrix.shift, RIGHT*9+UP*i)
                return rectangle, matrix

            elif(rotate==False and refl==True and check==False):
                a1 = DrawArrow(obj, op, value)
                self.play(ShowCreation(a1), run_time=0.5)
                matrix = MatrixRep(a, b, c, d).next_to(obj, DOWN*5).scale(0.8)
                shape = RectangleRefl(rectangle=obj, axis=axis, pos=pos, matrix=matrix, sym=sym)
                rectangle = shape[0]
                matrix = shape[1]
                one3.remove_updater(update_one)
                two3.remove_updater(update_two)
                three3.remove_updater(update_three)
                four3.remove_updater(update_four)
                self.play(FadeOut(a1), FadeOut(RQ3Group), FadeOut(dline))
                ReFlip(axis)
                clear_updaters(0)
                self.play(matrix.scale, 0.7, matrix.shift, RIGHT*9+UP*i)
                return rectangle, matrix

            elif(rotate==False and refl==False and check==True):
                obj = CheckRot(obj, angle, op, value)
                self.play(FadeOut(obj[0]), FadeOut(obj[1]), FadeOut(obj[2]))
                clear_updaters(angle)

            elif(rotate==False and refl==True and check==True):
                obj = CheckRefl(obj, axis, op, value)
                self.play(FadeOut(obj[0]), FadeOut(obj[1]), FadeOut(obj[2]), FadeOut(dline))
                ReFlip(axis)
                clear_updaters(0)




        ##  START  ##
        #  Creating Title  #
        title = TextMobject("All \\, Symmetries \\, of \\, ", "Rectangle").move_to(UP*3)
        title[1].set_color(RED)
        self.play(Write(title, run_time=2))
        self.wait(3)

        #  Starting with Rotational Symmetries  #
        title2 = TextMobject("Rotational \\ \\ Symmetries").move_to(LEFT*3+UP*3)
        shape = Polygon(ORIGIN, UP*2, UP*2+RIGHT*4, RIGHT*4,
                        color=WHITE).scale(0.5).move_to(LEFT*4)
        self.play(FadeOut(title, run_time=0.5), FadeInFrom(title2, LEFT),
                    TransformFromCopy(title[1], shape, run_time=2))
        self.wait()

        #  Numbering the Base - Rectangle  #
        NumReq(shape)
        self.wait(3)

        #  First Rotation - 0 degrees  #
        Transform(obj=shape, op="Rotate", value="0^\\circ", angle=0, a=1, b=2, c=3, d=4, pos=[one, two, three, four], sym="rho_0", i=4)
        self.wait(2)

        #  90 degrees  #
        Transform(obj=shape, op="Rotate", value="90^\\circ", angle=PI/2, rotate=False, refl=False, check=True)
        self.wait(2)

        #  Second Rotation - 180 degrees  #
        Transform(obj=shape, op="Rotate", value="180^\\circ", angle=PI, a=3, b=4, c=1, d=2, pos=[three, four, one, two], sym="rho_1", i=3)
        self.wait(2)

        #  270 degrees  #
        Transform(obj=shape, op="Rotate", value="270^\\circ", angle=3*PI/2, rotate=False, refl=False, check=True)
        self.wait(2)

        #  Starting with Reflection Symmetries  #
        title3 = TextMobject("Reflection \\ \\ Symmetries").move_to(LEFT*3+UP*3)
        self.play(ReplacementTransform(title2, title3), run_time=2)
        self.wait()

        #  First Reflection - Y - Axis  #
        Transform(obj=shape, op="Flip", value="Y - Axis", axis=UP, a=4, b=3, c=2, d=1, pos=[four, three, two, one], sym="mu_1", i=2, rotate=False, refl=True)
        self.wait(2)

        #  Second Reflection -- X - Axis  #
        Transform(obj=shape, op="Flip", value="X - Axis", axis=RIGHT, a=2, b=1, c=4, d=3, pos=[two, one, four, three], sym="mu_2", i=1, rotate=False, refl=True)
        self.wait(2)

        #  1 - 3 Diagonal  #
        Transform(obj=shape, op="Flip", value="1-3\\, Diag", axis=np.array([-2,1,0]), a=2, b=1, c=4, d=3, pos=[two, one, four, three], sym="mu_2", i=1, rotate=False, refl=True, check=True)
        self.wait(2)

        #  2 - 4 Diagonal  #
        Transform(obj=shape, op="Flip", value="2-4\\, Diag", axis=np.array([2,1,0]), a=2, b=1, c=4, d=3, pos=[two, one, four, three], sym="mu_2", i=1, rotate=False, refl=True, check=True)
        self.wait(3)

class Rectangle2(Scene):
    def construct(self):

        #  Fuction to Create Table  ##
        def Table():
            global rho_0, rho_1, mu_1, mu_2, crho_0, crho_1, cmu_1, cmu_2, lines_remove

            def Letters(obj):
                return TexMobject("\\{}".format(obj)).scale(0.7)

            def VertLines(up, left, down, space, no):
                lines = VGroup()
                for i in range(4):
                    lines.add(Line(up+(left - i*LEFT*space),
                    down+(left - i*LEFT*space), stroke_width=0.7))
                return lines

            def HoriLines(up, left, right, space, no):
                lines = VGroup()
                for i in range(4):
                    lines.add(Line(left+(up - i*UP*space),
                    right+(up - i*UP*space), stroke_width=0.7))
                return lines

            letters = VGroup()
            circ = Letters("circ").move_to(UP*3.25+LEFT*6.25).set_color(YELLOW).scale(2)
            rho_0 = Letters("rho_0").move_to(UP*3.25+LEFT*5.55)
            rho_1 = Letters("rho_1").move_to(UP*3.25+LEFT*4.85)
            mu_1 = Letters("mu_1").move_to(UP*3.25+LEFT*4.15)
            mu_2 = Letters("mu_2").move_to(UP*3.25+LEFT*3.45)
            letters.add(circ, rho_0, rho_1, mu_1, mu_2)


            crho_0 = Letters("rho_0").move_to(UP*2.55+LEFT*6.25)
            crho_1 = Letters("rho_1").move_to(UP*1.85+LEFT*6.25)
            cmu_1 = Letters("mu_1").move_to(UP*1.15+LEFT*6.25)
            cmu_2 = Letters("mu_2").move_to(UP*0.45+LEFT*6.25)
            letters.add(crho_0, crho_1, cmu_1, cmu_2)

            vlines = VertLines(up=UP*3.6, left=LEFT*5.9, down=UP*0.1, space=0.7, no=4)
            hlines = HoriLines(up=UP*2.9, left=LEFT*6.6, right=LEFT*3.1, space=0.7, no=4)
            self.play(Write(vlines), Write(hlines), run_time=3)
            self.play(Write(letters, run_time=3))
            Table_Group.add(vlines, hlines, letters)
            self.wait()

        ##  Function to Number Rectangle  ##
        def NumReq(rectangle, play=True, col=GREEN):
            global one, two, three, four, rectangle_group, line1, line2, RQ1Group
            line1 = Line(rectangle.get_corner(UL)+UP*0.15+LEFT*0.15,
                            rectangle.get_corner(DR)+DOWN*0.15+RIGHT*0.15)
            line2 = Line(rectangle.get_corner(DL)+DOWN*0.15+LEFT*0.15,
                            rectangle.get_corner(UR)+UP*0.15+RIGHT*0.15)
            one = TexMobject(r"1", color=col).scale(0.5).move_to(line1.get_start())
            two = TexMobject(r"2", color=col).scale(0.5).move_to(line2.get_start())
            three = TexMobject(r"3", color=col).scale(0.5).move_to(line1.get_end())
            four = TexMobject(r"4", color=col).scale(0.5).move_to(line2.get_end())
            rectangle_group = VGroup(rectangle, line1.set_opacity(0), line2.set_opacity(0))
            nos = [one, two, three, four]

            if play != False :
                self.play(*[Write(num) for num in nos])
            RQ1Group = VGroup(rectangle_group, one, two, three, four,)
            return RQ1Group

        ##  Updater Functions  ##
        def update_one(obj):
            obj.move_to(line1.get_start())
        def update_two(obj):
            obj.move_to(line2.get_start())
        def update_three(obj):
            obj.move_to(line1.get_end())
        def update_four(obj):
            obj.move_to(line2.get_end())

        def RectangleRot(rectangle, angle, matrix):
            global one2, two2, three2, four2, RQ2Group

            #  Copy rectangle  #
            rectangle2 = rectangle.copy()

            #  Copy Numbers  #
            one2 = one.copy().set_color(RED).add_updater(update_one)
            two2 = two.copy().set_color(RED).add_updater(update_two)
            three2 = three.copy().set_color(RED).add_updater(update_three)
            four2 = four.copy().set_color(RED).add_updater(update_four)
            self.add(one2, two2, three2, four2)

            #  Create Required Groups  #
            rectangle2 = VGroup(rectangle2, line1.set_opacity(0), line2.set_opacity(0))
            RQ2Group = VGroup(rectangle2, one2, two2, three2, four2)

            # Performed Required Action  #
            self.play(RQ2Group.shift, RIGHT*4.5)
            self.play(Rotate(rectangle2, angle), Write(matrix, run_time=2))
            group.add(RQ2Group)
            return rectangle2

        def RectangleRefl(rectangle, axis, matrix):
            global one3, two3, three3, four3, RQ3Group, dline

            #  Copy Rectangle  #
            rectangle3 = rectangle.copy()

            #  Copy Numbers  #
            one3 = one.copy().set_color(RED).add_updater(update_one)
            two3 = two.copy().set_color(RED).add_updater(update_two)
            three3 = three.copy().set_color(RED).add_updater(update_three)
            four3 = four.copy().set_color(RED).add_updater(update_four)
            self.add(one3, two3, three3, four3)

            #  Create Required Groups  #
            rectangle3 = VGroup(rectangle3, line1.set_opacity(0), line2.set_opacity(0))
            RQ3Group = VGroup(rectangle3, one3, two3, three3, four3)

            #  Create Line  #
            self.play(RQ3Group.shift, RIGHT*4.5)
            line = Line(ORIGIN, axis).scale(2.5)
            line.move_to(line.get_center()*0 + RQ3Group.get_center())
            dline = DashedVMobject(line)

            #  Perform Required Action  #
            self.play(ShowCreation(dline, run_time=0.5))
            self.play(Rotate(rectangle3, angle=PI, axis=axis), Write(matrix, run_time=2))
            group.add(RQ3Group, dline)
            return rectangle3

        def MatrixRep(a, b, c, d):
            str = "\\begin{pmatrix1} 1 & 2 & 3 & 4 \\\\ {} & {} & {} & {}\\end{pmatrix2}".format(a, b , c, d, pmatrix1 = "{pmatrix}", pmatrix2="{pmatrix}")
            matrix = TexMobject(str)
            for i in range(1,5):
                matrix[0][i].set_color(GREEN_D)
            for j in range(5,9):
                matrix[0][j].set_color(RED)
            group.add(matrix)
            return matrix

        def MatrixConst(a, b, c, d):
            str = "\\begin{pmatrix1} 1 & 2 & 3 & 4 \\\\ {} & {} & {} & {}\\end{pmatrix2}".format(a, b , c, d, pmatrix1 = "{pmatrix}", pmatrix2="{pmatrix}")
            matrix = TexMobject(str)
            for i in range(1,5):
                matrix[0][i].set_color(GREEN_D)
            for j in range(5,9):
                matrix[0][j].set_color(RED)
            return matrix

        def CreateMatrix(obj, matrix, a, b, c, d, pos1, pos2, pos3, pos4, sym):
            self.play(Write(matrix[0][0]), Write(matrix[0][9]))
            self.play(Write(matrix[0][1:5]))
            pos = [pos1, pos2, pos3, pos4]
            num = [a, b, c, d]
            for i in range(4):
                if (pos[i]==one) or (pos[i]==four):
                    carrow = CurvedArrow(num[i].get_center(), pos[i].get_center(),
                    angle=PI/3).scale(0.9)
                elif (pos[i]==two) or (pos[i]==three):
                    carrow = CurvedArrow(num[i].get_center(), pos[i].get_center(),
                    angle=-PI/3).scale(0.9)

                self.play(ShowCreation(carrow), Write(matrix[0][i+5]))
                self.play(FadeOut(carrow))
                self.remove(carrow)

            symbol = TexMobject("\\{}".format(sym), "\\ \\ =").scale(0.7).next_to(matrix, LEFT)
            self.wait()
            self.play(Write(symbol))
            matrix = VGroup(matrix, symbol)
            return matrix

        def DrawArrow(obj, op, col):
            global arrow_group1
            arrow = Arrow(ORIGIN, RIGHT*2).next_to(obj, RIGHT*1.5)
            operation = TexMobject("{}".format(op)).scale(0.5).next_to(arrow, UP*0.5)
            operation.set_color(col)
            arrow_group = VGroup(arrow, operation)
            group.add(arrow_group)
            return arrow_group

        def DrawArrow2(obj, op, col):
            global arrow_group2
            arrow = Arrow(ORIGIN, DOWN).next_to(obj, DOWN*1.5)
            symbol = TexMobject("{}".format(op)).scale(0.5).next_to(arrow, RIGHT*0.5)
            symbol.set_color(col)
            arrow_group2 = VGroup(arrow, symbol)
            group.add(arrow_group2)
            return arrow_group2

        def clear_updaters(angle):
            line1.move_to(LEFT*5.5+DOWN*2).rotate(-angle)
            line2.move_to(LEFT*5.5+DOWN*2).rotate(-angle)

        def ReFlip(axis):
            line1.rotate(angle=PI, axis=axis)
            line2.rotate(angle=PI, axis=axis)

        def Transform(obj, mat, op, operation, col=RED, a=1, b=2, c=3, d=4, angle=PI, axis=IN, rotate=True, refl=False, opac=1):
            if(rotate==True and refl==False):
                self.play(WiggleOutThenIn(operation, scale_value=2))
                a1 = DrawArrow(obj=obj, op=op, col=col)
                a2 = DrawArrow2(obj=mat, op=op, col=col).set_opacity(opac)
                self.play(ShowCreation(a1), ShowCreation(a2), run_time=0.5)
                matrix = MatrixRep(a, b, c, d).next_to(mat, DOWN*5).scale(0.7)
                rectangle = RectangleRot(rectangle=obj, angle=angle, matrix=matrix)
                one2.remove_updater(update_one)
                two2.remove_updater(update_two)
                three2.remove_updater(update_three)
                four2.remove_updater(update_four)
                return rectangle, matrix

            elif(rotate==False and refl==True):
                self.play(WiggleOutThenIn(operation, scale_value=2))
                a1 = DrawArrow(obj=obj, op=op, col=col)
                a2 = DrawArrow2(obj=mat, op=op, col=col).set_opacity(opac)
                self.play(ShowCreation(a1), ShowCreation(a2), run_time=0.5)
                matrix = MatrixRep(a, b, c, d).next_to(mat, DOWN*5).scale(0.7)
                rectangle = RectangleRefl(rectangle=obj, axis=axis, matrix=matrix)
                one3.remove_updater(update_one)
                two3.remove_updater(update_two)
                three3.remove_updater(update_three)
                four3.remove_updater(update_four)
                return rectangle, matrix

        def LastScene():
            global matrix0, matrix1, matrix2, matrix3
            ##   Creating the Last Scene   ##
            title = TextMobject("Reflection \\ \\ Symmetries").move_to(LEFT*3+UP*3)
            shape = Polygon(ORIGIN, UP*2, UP*2+RIGHT*4, RIGHT*4,
                            color=WHITE).scale(0.5).move_to(LEFT*4)

            #  Numbering the Base - Rectangle  #
            rect = NumReq(shape, play=False, col=RED)

            matrix0 = MatrixConst(1, 2, 3, 4).scale(0.8)
            matrix0 = VGroup(matrix0,TexMobject("\\rho_0\\ \\ =").scale(0.7).next_to(matrix0, LEFT)).move_to(RIGHT*4.5+UP*1.5)
            matrix1 = MatrixConst(3, 4, 1, 2).scale(0.8)
            matrix1 = VGroup(matrix1, TexMobject("\\rho_1\\ \\ =").scale(0.7).next_to(matrix1, LEFT)).move_to(RIGHT*4.5+UP*0.5)
            matrix2 = MatrixConst(4, 1, 3, 2).scale(0.8)
            matrix2 = VGroup(matrix2, TexMobject("\\mu_1\\ \\ =").scale(0.7).next_to(matrix2, LEFT)).move_to(RIGHT*4.5+DOWN*0.5)
            matrix3 = MatrixConst(2, 1, 4, 3).scale(0.8)
            matrix3 = VGroup(matrix3, TexMobject("\\mu_2\\ \\ =").scale(0.7).next_to(matrix3, LEFT)).move_to(RIGHT*4.5+DOWN*1.5)
            matrices = VGroup(matrix0.scale(0.7), matrix1.scale(0.7), matrix2.scale(0.7), matrix3.scale(0.7))
            self.add(title, rect, matrices)
            self.wait(3)
            self.play(FadeOut(rect), FadeOut(title), matrices.shift, UP*2+RIGHT*0.5)
            self.wait()
            Matrix_Group.add(matrices)
            return matrices


        global Table_Group, group, Matrix_Group
        Table_Group, group, Matrix_Group = VGroup(), VGroup(), VGroup()
        ##  Creating  Last  Scene  ##
        matrices = LastScene()
        ##  Done  Creating Last Scene  ##


        Table()
        #self.play(matrices.scale, 1.1, matrices.shift, UP+RIGHT*0.5)
        self.wait()


        matrix = Dot().move_to(UP*5)

        ## Permanant Square for Starting Position ##
        rectangle = Polygon(ORIGIN, UP*2, UP*2+RIGHT*4, RIGHT*4, color=WHITE).scale(0.5).move_to(LEFT*5.5+DOWN*2)
        self.play(ShowCreation(rectangle), ShowCreation(matrix))
        Matrix_Group.add(NumReq(rectangle))
        self.wait(3)

        ##  Fill the First rows and Coloums  ##
        char0 = rho_0.copy().set_color(RED).shift(DOWN*0.7)
        char1 = rho_1.copy().set_color(YELLOW).shift(DOWN*0.7)
        char2 = mu_1.copy().set_color(GREEN_E).shift(DOWN*0.7)
        char3 = mu_2.copy().set_color(BLUE_E).shift(DOWN*0.7)
        char4 = crho_1.copy().set_color(YELLOW).shift(RIGHT*0.7)
        char5 = cmu_1.copy().set_color(GREEN_E).shift(RIGHT*0.7)
        char6 = cmu_2.copy().set_color(BLUE_E).shift(RIGHT*0.7)
        chars = VGroup(char0, char1, char2, char3, char4, char5, char6)
        Table_Group.add(char0, char1, char2, char3, char4, char5, char6)
        self.play(Write(chars, run_time=3))
        self.wait(2)

        ## Transform r1(r1(x)) ##
        T1 = obj=Transform(obj=rectangle, mat=matrix, op="\\rho_1", col=YELLOW, angle=PI, operation=crho_1, a=3, b=4, c=1, d=2, opac=0)
        T2 = Transform(obj=T1[0], mat=T1[1], op="\\rho_1", col=YELLOW, angle=PI, operation=rho_1, a=1, b=2, c=3, d=4)
        self.play(WiggleOutThenIn(matrix0, scale_value=2))
        char = rho_0.copy().shift(DOWN*1.4 + RIGHT*0.7).set_color(RED)
        self.play(Write(char), FadeOut(group))
        clear_updaters(0)
        group = VGroup()
        Table_Group.add(char)
        self.wait()

        ## Transform mu_1(r1(x)) ##
        T1 = obj=Transform(obj=rectangle, mat=matrix, op="\\rho_1", col=YELLOW, angle=PI, operation=crho_1, a=3, b=4, c=1, d=2, opac=0)
        T2 = Transform(obj=T1[0], mat=T1[1], op="\\mu_1", col=GREEN_E, axis=UP, operation=mu_1, a=2, b=1, c=4, d=3, rotate=False, refl=True)
        self.play(WiggleOutThenIn(matrix3, scale_value=2))
        char = mu_2.copy().shift(DOWN*1.4 + LEFT*0.7).set_color(BLUE_E)
        self.play(Write(char), FadeOut(group))
        ReFlip(axis=UP)
        clear_updaters(angle=PI)
        Table_Group.add(char)
        group = VGroup()
        self.wait()

        ## Transform r1(mu1(x)) ##
        T1 = obj=Transform(obj=rectangle, mat=matrix, op="\\mu_1", col=GREEN_E, axis=UP, operation=cmu_1, a=4, b=3, c=2, d=1, opac=0, rotate=False, refl=True)
        T2 = Transform(obj=T1[0], mat=T1[1], op="\\rho_1", col=YELLOW, angle=PI, operation=rho_1, a=2, b=1, c=4, d=3)
        self.play(WiggleOutThenIn(matrix3, scale_value=2))
        char = cmu_2.copy().shift(UP*0.7 + RIGHT*1.4).set_color(BLUE_E)
        self.play(Write(char), FadeOut(group))
        clear_updaters(angle=PI)
        ReFlip(axis=UP)
        Table_Group.add(char)
        group = VGroup()
        self.wait()

        ## Transform mu_2(r1(x)) ##
        T1 = obj=Transform(obj=rectangle, mat=matrix, op="\\rho_1", col=YELLOW, angle=PI, operation=crho_1, a=3, b=4, c=1, d=2, opac=0)
        T2 = Transform(obj=T1[0], mat=T1[1], op="\\mu_2", col=BLUE_E, axis=RIGHT, operation=mu_2, a=4, b=3, c=2, d=1, rotate=False, refl=True)
        self.play(WiggleOutThenIn(matrix2, scale_value=2))
        char = mu_1.copy().shift(DOWN*1.4 + RIGHT*0.7).set_color(GREEN_E)
        self.play(Write(char), FadeOut(group))
        ReFlip(axis=RIGHT)
        clear_updaters(angle=PI)
        Table_Group.add(char)
        group = VGroup()
        self.wait()

        ## Transform r1(mu2(x)) ##
        T1 = obj=Transform(obj=rectangle, mat=matrix, op="\\mu_2", col=BLUE_E, axis=RIGHT, operation=cmu_2, a=2, b=1, c=4, d=3, opac=0, rotate=False, refl=True)
        T2 = Transform(obj=T1[0], mat=T1[1], op="\\rho_1", col=YELLOW, angle=PI, operation=rho_1, a=4, b=3, c=2, d=1)
        self.play(WiggleOutThenIn(matrix2, scale_value=2))
        char = cmu_1.copy().shift(DOWN*0.7 + RIGHT*1.4).set_color(GREEN_E)
        self.play(Write(char), FadeOut(group))
        clear_updaters(angle=PI)
        ReFlip(axis=RIGHT)
        Table_Group.add(char)
        group = VGroup()
        self.wait()

        ## Transform mu_2(mu1(x)) ##
        T1 = obj=Transform(obj=rectangle, mat=matrix, op="\\mu_1", col=GREEN_E, axis=UP, operation=cmu_1, a=4, b=3, c=2, d=1, opac=0, rotate=False, refl=True)
        T2 = Transform(obj=T1[0], mat=T1[1], op="\\mu_2", col=BLUE_E, axis=RIGHT, operation=mu_2, a=3, b=4, c=1, d=2, rotate=False, refl=True)
        self.play(WiggleOutThenIn(matrix1, scale_value=2))
        char = rho_1.copy().shift(DOWN*2.1 + RIGHT*1.4).set_color(YELLOW)
        self.play(Write(char), FadeOut(group))
        ReFlip(axis=RIGHT)
        ReFlip(axis=UP)
        clear_updaters(angle=0)
        group = VGroup()
        Table_Group.add(char)
        self.wait()

        ## Transform mu1(mu2(x)) ##
        T1 = obj=Transform(obj=rectangle, mat=matrix, op="\\mu_2", col=BLUE_E, axis=RIGHT, operation=cmu_2, a=2, b=1, c=4, d=3, opac=0, rotate=False, refl=True)
        T2 = Transform(obj=T1[0], mat=T1[1], op="\\mu_1", col=GREEN_E, axis=UP, operation=mu_1, a=3, b=4, c=1, d=2, rotate=False, refl=True)
        self.play(WiggleOutThenIn(matrix1, scale_value=2))
        char = crho_1.copy().shift(DOWN*1.4 + RIGHT*2.1).set_color(YELLOW)
        self.play(Write(char), FadeOut(group))
        ReFlip(axis=UP)
        ReFlip(axis=RIGHT)
        clear_updaters(angle=PI)
        group = VGroup()
        Table_Group.add(char)
        self.wait()

        ##  Fill the First rows and Coloums  ##
        char0 = rho_0.copy().set_color(RED).shift(DOWN*2.1 + RIGHT*1.4)
        char1 = rho_0.copy().set_color(RED).shift(DOWN*2.8 + RIGHT*2.1)
        chars = VGroup(char0, char1)
        self.play(Write(chars, run_time=2))
        Table_Group.add(char0, char1)
        self.wait(3)

        self.play(FadeOut(Matrix_Group), Table_Group.next_to, Table_Group.get_center()*0+LEFT*2)
        self.wait(3)

class RectProperties(Scene):
    def construct(self):

        #  Fuction to Create Table  ##
        def Table():
            global rho_0, rho_1, mu_1, mu_2, crho_0, crho_1, cmu_1, cmu_2, lines_remove

            def Letters(obj):
                return TexMobject("\\{}".format(obj)).scale(0.7)

            def VertLines(up, left, down, space, no):
                lines = VGroup()
                for i in range(4):
                    lines.add(Line(up+(left - i*LEFT*space),
                    down+(left - i*LEFT*space), stroke_width=0.7))
                return lines

            def HoriLines(up, left, right, space, no):
                lines = VGroup()
                for i in range(4):
                    lines.add(Line(left+(up - i*UP*space),
                    right+(up - i*UP*space), stroke_width=0.7))
                return lines

            letters = VGroup()
            circ = Letters("circ").move_to(UP*3.25+LEFT*6.25).set_color(YELLOW).scale(2)
            rho_0 = Letters("rho_0").move_to(UP*3.25+LEFT*5.55)
            rho_1 = Letters("rho_1").move_to(UP*3.25+LEFT*4.85)
            mu_1 = Letters("mu_1").move_to(UP*3.25+LEFT*4.15)
            mu_2 = Letters("mu_2").move_to(UP*3.25+LEFT*3.45)
            letters.add(circ, rho_0, rho_1, mu_1, mu_2)


            crho_0 = Letters("rho_0").move_to(UP*2.55+LEFT*6.25)
            crho_1 = Letters("rho_1").move_to(UP*1.85+LEFT*6.25)
            cmu_1 = Letters("mu_1").move_to(UP*1.15+LEFT*6.25)
            cmu_2 = Letters("mu_2").move_to(UP*0.45+LEFT*6.25)
            letters.add(crho_0, crho_1, cmu_1, cmu_2)

            vlines = VertLines(up=UP*3.6, left=LEFT*5.9, down=UP*0.1, space=0.7, no=4)
            hlines = HoriLines(up=UP*2.9, left=LEFT*6.6, right=LEFT*3.1, space=0.7, no=4)
            #self.play(Write(vlines), Write(hlines), run_time=3)
            #self.play(Write(letters, run_time=3))
            Table_Group.add(vlines, hlines, letters)
            self.wait()

        ##  Function to fill the Table with Characters  ##
        def Characters():
            global Chars, hchars, vchars, identity
            char0 = rho_0.copy().set_color(RED).shift(DOWN*0.7)
            char1 = rho_1.copy().set_color(YELLOW).shift(DOWN*0.7)
            char2 = mu_1.copy().set_color(GREEN_E).shift(DOWN*0.7)
            char3 = mu_2.copy().set_color(BLUE_E).shift(DOWN*0.7)
            char4 = crho_1.copy().set_color(YELLOW).shift(RIGHT*0.7)
            char5 = cmu_1.copy().set_color(GREEN_E).shift(RIGHT*0.7)
            char6 = cmu_2.copy().set_color(BLUE_E).shift(RIGHT*0.7)
            char7 = rho_0.copy().shift(DOWN*1.4 + RIGHT*0.7).set_color(RED)
            char8 = mu_2.copy().shift(DOWN*1.4 + LEFT*0.7).set_color(BLUE_E)
            char9 = cmu_2.copy().shift(UP*0.7 + RIGHT*1.4).set_color(BLUE_E)
            char10 = mu_1.copy().shift(DOWN*1.4 + RIGHT*0.7).set_color(GREEN_E)
            char11 = cmu_1.copy().shift(DOWN*0.7 + RIGHT*1.4).set_color(GREEN_E)
            char12 = rho_1.copy().shift(DOWN*2.1 + RIGHT*1.4).set_color(YELLOW)
            char13 = crho_1.copy().shift(DOWN*1.4 + RIGHT*2.1).set_color(YELLOW)
            char14 = rho_0.copy().set_color(RED).shift(DOWN*2.1 + RIGHT*1.4)
            char15 = rho_0.copy().set_color(RED).shift(DOWN*2.8 + RIGHT*2.1)

            Table_Group.add(char0,char1,char2,char3,char4,char5,char6,char7,char8,char9,char10,char11,char12,char13,char14,char15)

            Chars = VGroup(char0,char1,char2,char3,char4,char5,char6,char7,char8,char9,char10,char11,char12,char13,char14,char15)

            hchars = VGroup(char0, char1, char2, char3)
            vchars = VGroup(char0, char4, char5, char6)
            identity = VGroup(char0, char7, char14, char15)

        def CreateProperties():
            global prop, prop1, prop1_1, prop2, prop2_1, prop3, prop3_1, prop4, prop4_1, prop5, prop5_1, Property_Group, Properties
            ## 1st Property - CLOSED ##
            Property_Group, Properties = VGroup(), VGroup()
            prop = TextMobject("Properties :- ", color=GOLD).scale(1.5).move_to(LEFT*4+UP*2.5)
            # Coloring The Required Characteres #
            prop1 = TexMobject(
                                "1. \\ \\ \\ \\",                   #0
                                "\\text{If    }\\ \\",              #1
                                "f_1",                              #2
                                ",",                                #3
                                "f_2\\,",                           #4
                                "\\in\\,",                          #5
                                "G",                                #6
                                "\\ \\ \\text{,  then    } \\ \\",  #7
                                "f_1",                              #8
                                "\\circ",                           #9
                                "f_2\\,",                           #10
                                "\\in",                             #11
                                "G"                                 #12
            ).scale(0.7)
            prop1[2].set_color(BLUE_D)
            prop1[4].set_color(RED)
            prop1[5].set_color(YELLOW)
            prop1[6].set_color(GREEN_E)
            prop1[8].set_color(BLUE_D)
            prop1[9].set_color(YELLOW)
            prop1[10].set_color(RED)
            prop1[11].set_color(YELLOW)
            prop1[12].set_color(GREEN)
            prop1.move_to(LEFT*3.5+UP*1.5)
            # Writing Property 1 in Words #
            prop1_1 = TexMobject(
                                    "(\\, \\text{ i.e }",   #0
                                    "G",                    #1
                                    "\\text{ is}\\ \\ ",    #2
                                    "Closed",               #3
                                    "\\ \\ \\text{under }", #4
                                    "\\circ",               #5
                                    "\\text{ operation.}",  #6
                                    "\\,)"                  #7
            ).scale(0.7)
            prop1_1.next_to(prop1, RIGHT*2)
            prop1_1[1].set_color(GREEN_D)
            prop1_1[3].set_color(RED)
            prop1_1[5].set_color(YELLOW)
            # Add both to the Group Properties
            Properties.add(prop, prop1.set_opacity(0), prop1_1.set_opacity(0))

            ## 2nd Property ##
            prop2 = TexMobject(
                                "2. \\ \\ \\ \\",           #0
                                "\\ \\ \\forall\\,",        #1
                                "f \\,",                    #2
                                "\\in\\,",                  #3
                                "G",                        #4
                                ",\\ \\",                   #5
                                "f",                        #6
                                "\\circ",                   #7
                                "\\rho_0",                  #8
                                "\\ \\ = \\ \\,",           #9
                                "\\rho_0",                  #10
                                "\\circ",                   #11
                                "f",                        #12
                                "\\ \\ = \\ \\,",           #13
                                "f"                         #14
            ).scale(0.7)
            prop2[1].set_color(YELLOW)
            prop2[2].set_color(BLUE_D)
            prop2[3].set_color(YELLOW)
            prop2[4].set_color(GREEN_D)
            prop2[6].set_color(BLUE_D)
            prop2[7].set_color(YELLOW)
            prop2[8].set_color(RED)
            prop2[10].set_color(RED)
            prop2[11].set_color(YELLOW)
            prop2[12].set_color(BLUE_D)
            prop2[14].set_color(BLUE_D)
            #   Property 2 in words #
            prop2_1 = TexMobject(
                                    "(\\,\\text{ i.e }",            #0
                                    "\\text{ Existence of }",       #1
                                    "Identity",                     #2
                                    "\\text{ element}",             #3
                                    "\\,)"                          #4
            ).scale(0.7)
            #   Set Color#
            prop2_1[2].set_color(RED)
            #  Move to Required Position    #
            prop2[0].next_to(prop1[0], DOWN*2)
            prop2[1:].next_to(prop2[0])
            prop2_1.next_to(prop2, RIGHT*2)
            # Add both to the Group Properties
            Properties.add(prop2.set_opacity(0), prop2_1.set_opacity(0))

            ##  3rd Property   ##
            prop3 = TexMobject(
                                "3. \\ \\ \\ \\",   #0
                                "\\forall\\,",      #1
                                "f\\,",             #2
                                "\\in\\,",          #3
                                "G",                #4
                                ",\\ \\",           #5
                                "\\exists\\,",      #6
                                "f^{-1}\\,",        #7
                                "\\in\\,",          #8
                                "G",                #9
                                "\\ \\ \\text{ such that }",    #10
                                "f",                #11
                                "\\circ",           #12
                                "f^{-1}",           #13
                                "\\ \\ = \\ \\",    #14
                                "f^{-1}",           #15
                                "\\circ",           #16
                                "f",                #17
                                "\\ \\ = \\ \\",    #18
                                "\\rho_0"           #19
                                ).scale(0.7)
            prop3[1].set_color(YELLOW)
            prop3[2].set_color(BLUE_D)
            prop3[3].set_color(YELLOW)
            prop3[4].set_color(GREEN_D)
            prop3[6].set_color(YELLOW)#exists
            prop3[7].set_color("#d65435")
            prop3[8].set_color(YELLOW)
            prop3[9].set_color(GREEN_D)
            prop3[11].set_color(BLUE_D)
            prop3[12].set_color(GOLD)
            prop3[13].set_color("#d65435")
            prop3[15].set_color("#d65435")
            prop3[16].set_color(GOLD)
            prop3[17].set_color(BLUE_D)
            prop3[19].set_color(RED)
            prop3[0].next_to(prop2[0], DOWN*2)
            prop3[1:].next_to(prop3[0])
            #   Property 3 in WOrds #
            prop3_1 = TexMobject(
                                    "(\\,",                         #0
                                    "\\text{i.e}\\ \\",             #1
                                    "\\text{Existence  of} \\ \\",  #2
                                    "Inverse",                      #3
                                    "\\ \\ )"                       #4
            ).scale(0.7)
            prop3_1[3].set_color(RED)
            prop3_1.next_to(prop3, DOWN*0.7)
            Properties.add(prop3.set_opacity(0), prop3_1.set_opacity(0))

            ##  4th Property  ##
            prop4 = TexMobject(
                                "4.\\ \\ \\ \\ ",               #0
                                "\\text{If}\\ \\",          #1
                                "f_1",                      #2
                                ",\\,",                     #3
                                "f_2",                      #4
                                ",\\,",                     #5
                                "f_3",                      #6
                                "\\,\\in\\,",               #7
                                "G",                        #8
                                "\\ \\ \\ \\ \\text{then}", #9
                                "\\ \\ \\ \\ (",            #10
                                "f_1",                      #11
                                "\\circ",                   #12
                                "f_2",                      #13
                                ")",                        #14
                                "\\circ",                   #15
                                "f_3",                      #16
                                "\\ \\ = \\ \\",            #17
                                "f_1",                      #18
                                "\\circ",                   #19
                                "(",                        #20
                                "f_2",                      #21
                                "\\circ",                   #22
                                "f_3",                      #23
                                ")"                         #24
            ).scale(0.7)
            prop4[2].set_color(RED)
            prop4[4].set_color(GREEN_E)
            prop4[6].set_color(BLUE_D)
            prop4[7].set_color(YELLOW)
            prop4[8].set_color(GREEN_D)
            prop4[11].set_color(RED)
            prop4[12].set_color(GOLD)
            prop4[13].set_color(GREEN_E)
            prop4[15].set_color(GOLD)
            prop4[16].set_color(BLUE_D)
            prop4[18].set_color(RED)
            prop4[19].set_color(GOLD)
            prop4[21].set_color(GREEN_E)
            prop4[22].set_color(GOLD)
            prop4[23].set_color(BLUE_D)
            prop4[0].next_to(prop3[0], DOWN*4)
            prop4[1:].next_to(prop4[0])
            #   Propert4 in Words   #
            prop4_1 = TexMobject(
                                    "(\\, \\text{i.e  }",
                                    "Associativity",
                                    "\\,)"
            ).scale(0.7)
            prop4_1[1].set_color(RED)
            prop4_1.next_to(prop4, RIGHT*2)
            Properties.add(prop4.set_opacity(0), prop4_1.set_opacity(0))

            ## 5th Propperty  ##
            prop5 = TexMobject(
                                "5.\\ \\",              #0
                                "\\forall\\,",          #1
                                "f_1\\,",               #2
                                ",",                    #3
                                "f_2\\,",               #4
                                "\\in\\,",              #5
                                "G",                    #6
                                ",\\ \\ \\ \\ \\ \\ \\",#7
                                "f_1",                  #8
                                "\\circ",               #9
                                "f_2",                  #10
                                "\\ \\ = \\ \\ ",       #11
                                "f_2",                  #12
                                "\\circ",               #13
                                "f_1"                   #14
            ).scale(0.7)
            prop5[1].set_color(YELLOW)
            prop5[2].set_color(BLUE_D)
            prop5[4].set_color(RED)
            prop5[5].set_color(YELLOW)
            prop5[6].set_color(GREEN_D)
            prop5[8].set_color(BLUE_D)
            prop5[9].set_color(YELLOW)
            prop5[10].set_color(RED)
            prop5[12].set_color(RED)
            prop5[13].set_color(YELLOW)
            prop5[14].set_color(BLUE_D)
            # Property 5 in Words #
            prop5_1 = TexMobject(
                                    "(\\, i.e\\ \\",    #0
                                    "G",                #1
                                    "\\text{ is }",     #2
                                    "Abelian",          #3
                                    ")"                 #4
            ).scale(0.7)
            prop5_1[1].set_color(GREEN_D)
            prop5_1[3].set_color(RED)
            #   Move to required position   #
            prop5[0].next_to(prop4[0], DOWN*2)
            prop5[1:].next_to(prop5[0])
            prop5_1.next_to(prop5, RIGHT*2)
            #Properties.add(prop5.set_opacity(0), prop5_1.set_opacity(0))

        def Property1():
            self.play(WiggleOutThenIn(Chars, scale_value=2, run_time=3))
            self.play(FadeOutAndShiftDown(Table_Group))
            self.play(Write(prop.set_opacity(1)))
            self.wait()
            self.play(Write(prop1[:7].set_opacity(1), run_time=2))
            self.wait()
            self.play(Write(prop1[7:].set_opacity(1), run_time=2))
            self.wait()
            self.play(Write(prop1_1.set_opacity(1), run_time=2))
            self.wait(3)
            self.play(FadeOutAndShift(Properties, UP),  FadeInFromDown(Table_Group, run_time=2))
            self.wait(2)

        def Property2():
            self.play(WiggleOutThenIn(crho_0, scale_value=2))
            self.play(WiggleOutThenIn(hletters, run_time=2))
            self.play(Indicate(hchars, scale_factor=1.5), run_time=2)
            self.wait()
            self.play(WiggleOutThenIn(vletters, run_time=2))
            self.play(WiggleOutThenIn(rho_0, scale_value=2))
            self.play(Indicate(vchars, scale_factor=1.5), run_time=2)
            self.wait()
            self.play(FadeOutAndShiftDown(Table_Group), FadeInFrom(Properties, UP, run_time=2))
            self.wait()
            self.play(Write(prop2[:6].set_opacity(1), run_time=2))
            self.wait()
            self.play(Write(prop2[6:9].set_opacity(1)))
            self.wait()
            self.play(Write(prop2[9:13].set_opacity(1)))
            self.wait()
            self.play(Write(prop2[13:].set_opacity(1)))
            self.wait()
            self.play(Write(prop2_1.set_opacity(1)))
            self.wait(3)
            self.play(FadeOutAndShift(Properties, UP),  FadeInFromDown(Table_Group, DOWN, run_time=2))

        def Property3():
            self.play(WiggleOutThenIn(identity, rum_time=2))
            self.play(WiggleOutThenIn(crho_1, scale_value=2, rum_time=2), WiggleOutThenIn(rho_3, scale_value=2, rum_time=2))
            self.wait()
            self.play(Indicate(char15, scale_factor=2, run_time=2))
            self.wait()
            self.play(WiggleOutThenIn(rho_1, scale_value=2, rum_time=2), WiggleOutThenIn(crho_3, scale_value=2, rum_time=2))
            self.wait()
            self.play(Indicate(char20, scale_factor=2, run_time=2))
            self.wait()
            self.play(WiggleOutThenIn(identity, rum_time=2))
            self.wait()
            self.play(FadeOutAndShiftDown(Table_Group), FadeInFrom(Properties, UP, run_tim=2))
            self.wait()
            self.play(Write(prop3[:5].set_opacity(1)))
            self.wait()
            self.play(Write(prop3[5:10].set_opacity(1)))
            self.wait()
            self.play(Write(prop3[10:14].set_opacity(1)))
            self.wait()
            self.play(Write(prop3[14:18].set_opacity(1)))
            self.wait()
            self.play(Write(prop3[18:].set_opacity(1)))
            self.wait()
            self.play(Write(prop3_1.set_opacity(1)))
            self.wait()
            self.play(FadeOutAndShift(Properties, UP), FadeInFrom(Table_Group, DOWN,run_time=2))
            self.wait()

        def Property4():
            # Setting up the Pitch
            comp1 = TexMobject(
                                "(\\,",             #0
                                "\\mu_1",           #1
                                "\\circ",           #2
                                "\\rho_3",          #3
                                "\\,)",             #4
                                "\\circ",           #5
                                "\\mu_2",           #6
                                "\\ \\ = \\ \\",    #7
                                "\\rho_3"           #8
            ).scale(0.7)
            comp1[1].set_color(GREEN_E)
            comp1[2].set_color(GOLD)
            comp1[3].set_color(GREEN_D)
            comp1[5].set_color(GOLD)
            comp1[6].set_color(BLUE)
            comp1[8].set_color(GREEN_D)

            comp2 = TexMobject(
                                "\\mu_1",           #0
                                "\\circ",           #1
                                "(\\,",             #2
                                "\\rho_3",          #3
                                "\\circ",           #4
                                "\\mu_2",           #5
                                "\\,)",             #6
                                "\\ \\ = \\ \\",    #7
                                "\\rho_3"           #8
            ).scale(0.7)
            comp2[0].set_color(GREEN_E)
            comp2[1].set_color(GOLD)
            comp2[3].set_color(GREEN_D)
            comp2[4].set_color(GOLD)
            comp2[5].set_color(BLUE)
            comp2[8].set_color(GREEN_D)

            comp1.move_to(UP*2.5+LEFT*5.3)
            comp2.move_to(UP + LEFT*5.3)

            self.play(WiggleOutThenIn(cmu_1, scale_value=2, run_time=2), WiggleOutThenIn(rho_3, scale_value=2, run_time=2), Write(comp1[:5],run_time=2))
            self.play(Indicate(char28, scale_factor=2, run_time=3))
            self.play(WiggleOutThenIn(cdelta_2, scale_value=2, run_time=2), WiggleOutThenIn(mu_2, scale_value=2, run_time=2), Write(comp1[5:7],run_time=2))
            self.play(Indicate(char59, scale_factor=2, run_time=3), Write(comp1[7:], run_time=2))
            self.wait(2)

            self.play(WiggleOutThenIn(crho_3, scale_value=2, run_time=2), WiggleOutThenIn(mu_2, scale_value=2, run_time=2), Write(comp2[2:7],run_time=2))
            self.play(Indicate(char45, scale_factor=2, run_time=3))
            self.play(WiggleOutThenIn(cmu_1, scale_value=2, run_time=2), WiggleOutThenIn(delta_2, scale_value=2, run_time=2), Write(comp2[:2],run_time=2))
            self.play(Indicate(char61, scale_factor=2, run_time=3), Write(comp2[7:], run_time=2))
            self.wait(2)

            self.play(FadeOutAndShiftDown(Table_Group), FadeOut(comp1), FadeOut(comp2), FadeInFrom(Properties, UP, run_time=2))
            self.play(Write(prop4[:9].set_opacity(1)))
            self.wait()
            self.play(Write(prop4[9:17].set_opacity(1)))
            self.wait()
            self.play(Write(prop4[17:].set_opacity(1)))
            self.wait()
            self.play(Write(prop4_1.set_opacity(1)))
            self.wait(2)
            self.play(FadeOutAndShift(Properties, UP), FadeInFrom(Table_Group, run_time=2))
            self.wait(2)

        def Property5():
            self.play(FadeOutAndShift(Properties, UP), FadeInFrom(Table_Group, run_time=2))
            self.wait(3)
            self.play(FadeOutAndShiftDown(Table_Group), FadeInFrom(Properties, UP, run_time=2))
            self.wait()
            self.play(Write(prop5[:7].set_opacity(1), run_time=2))
            self.wait()
            self.play(Write(prop5[7:11].set_opacity(1), run_time=2))
            self.wait()
            self.play(Write(prop5[11:].set_opacity(1), run_time=2))
            self.wait()
            self.play(Write(prop5_1.set_opacity(1)))




        global Table_Group, Fade
        Table_Group, Fade = VGroup(), VGroup()

        ## Creating and Labeling Table ##
        Table()
        ## Filling in the table ##
        Characters()
        #"""
        Table_Group.next_to(Table_Group.get_center()*0+LEFT*2)
        self.add(Table_Group)
        self.wait(3)
        CreateProperties()
        self.play(FadeOutAndShiftDown(Table_Group), FadeInFrom(Properties.set_opacity(1), UP, run_time=3))
        self.wait(3)
        Property5()
        self.wait(3)
        Fade.add(prop, prop1, prop1_1[0], prop1_1[7])
        Fade.add(prop2, prop2_1[0], prop2_1[4])
        Fade.add(prop3, prop3_1[0:2], prop3_1[4])
        Fade.add(prop4, prop4_1[0], prop4_1[2])
        Fade.add(prop5, prop5_1[0], prop5_1[4])

        ##  FADE AND ALIGN WORDS  ##
        num1 = TexMobject("1.\\ \\ \\ \\").scale(0.7).move_to(UP*2.5+LEFT*5)
        num2 = TexMobject("2.\\ \\ \\ \\").scale(0.7).move_to(UP*1.5+LEFT*5)
        num3 = TexMobject("3.\\ \\ \\ \\").scale(0.7).move_to(UP*0.5+LEFT*5)
        num4 = TexMobject("4.\\ \\ \\ \\").scale(0.7).move_to(DOWN*0.5+LEFT*5)
        num5 = TexMobject("5.\\ \\ \\ \\").scale(0.7).move_to(DOWN*2+LEFT*5)
        num = VGroup(num1, num2, num3, num4, num5)
        self.play(FadeOut(Fade))
        self.remove(Fade)
        Fade.set_opacity(0)
        self.play(Write(num),
        prop1_1[1:7].move_to, prop1_1[1:7].next_to(num1),
        prop2_1[1:4].move_to, prop2_1[1:4].next_to(num2),
        prop3_1[2:4].move_to, prop3_1[2:4].next_to(num3),
        prop4_1[1].move_to,   prop4_1[1].next_to(num4),
        prop5_1[1:4].move_to, prop5_1[1:4].next_to(num5))#, run_time=3)
        self.wait(3)
        group1 = VGroup(num1, num2, num3, num4, prop1_1, prop2_1, prop3_1, prop4_1)
        group2 = VGroup(num1, num2, num3, num4, num5, prop1_1, prop2_1, prop3_1, prop4_1, prop5_1)
        self.play(group2.shift, RIGHT*5)
        braces1 = Brace(group1, LEFT)
        braces2 = Brace(group2, LEFT)
        text1 = braces1.get_text("GROUP")
        text2 = braces2.get_text("Abelian Group")
        text1.set_color(GOLD)
        text2.set_color(GOLD)

        self.play(ShowCreation(braces1))
        self.play(Write(text1), run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(braces1, braces2),
                    ReplacementTransform(text1, text2, run_time=2))
        self.wait(3)
