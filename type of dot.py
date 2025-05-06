from manim import *

class UsefulAnnotations(Scene):
    def construct(self):
        m0 = Dot()
        m1 = AnnotationDot()
        m2 = LabeledDot("ii").shift(DOWN)
        m3 = LabeledDot(MathTex(r"\alpha").set_color(ORANGE)).shift(DOWN*2)
        m4 = CurvedArrow(2*LEFT, 2*RIGHT, radius= -5).shift(UP)
        m5 = CurvedArrow(2*LEFT, 2*RIGHT, radius= 8)
        m6 = CurvedDoubleArrow(ORIGIN, 2*RIGHT)

        self.add(m0, m1, m2, m3, m4, m5, m6)
        # for i, mobj in enumerate(self.mobjects):
        #     mobj.shift(DOWN * (i-3))