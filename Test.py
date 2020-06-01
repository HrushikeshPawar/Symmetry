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

        ##Creating and playing Text (Mathematical Representation)
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

        carrow1 = CurvedArrow(one.get_center(), square2.get_corner(UL),
        angle=-PI/4, buff=10).scale(0.9)
        carrow2 = CurvedArrow(two.get_center(), square2.get_corner(DL),
        angle=PI/4, buff=10).scale(0.9)
        carrow3 = CurvedArrow(three.get_center(), square2.get_corner(DR),
        angle=PI/4, buff=10).scale(0.9)
        carrow4 = CurvedArrow(four.get_center(), square2.get_corner(UR),
        angle=-PI/4, buff=10).scale(0.9)

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


        self.play(square3.shift, DOWN*3.5)#, one.copy().shift, DOWN*3.5,
        #two.copy().shift, DOWN*3.5, three.copy().shift, DOWN*3.5,
        #four.copy().shift, DOWN*3.5)
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

        carrow_1 = CurvedArrow(square3.get_corner(UL), square4.get_corner(UL),
        angle=-PI/4, buff=10).scale(0.9)
        carrow_2 = CurvedArrow(square3.get_corner(DL), square4.get_corner(DL),
        angle=PI/4, buff=10).scale(0.9)
        carrow_3 = CurvedArrow(square3.get_corner(DR), square4.get_corner(DR),
        angle=PI/4, buff=10).scale(0.9)
        carrow_4 = CurvedArrow(square3.get_corner(UR), square4.get_corner(UR),
        angle=-PI/4, buff=10).scale(0.9)

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