from manimlib.imports import *

class Test(Scene):
    def construct(self):
        def MatrixRep(a, b, c, d):
            str = "\\begin{pmatrix1} 1 & 2 & 3 & 4 \\\\ {} & {} & {} & {}\\end{pmatrix2}".format(a, b , c, d, pmatrix1 = "{pmatrix}", pmatrix2="{pmatrix}")
            matrix = TexMobject(str)

            for i in range(1,5):
                matrix[0][i].set_color(GREEN_D)
            for j in range(5,9):
                matrix[0][j].set_color(RED)
            return matrix

        matrix = MatrixRep(1, 2, 3, 4)
        #self.play(Write(imp[0][0]), Write(imp[0][9]))
        #for i in range(1,5):
        #    self.play(Write(imp[0][i]))
        #self.wait(3)
        self.play(Write(matrix))
        self.wait(4)
