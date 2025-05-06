from manim import *

class G(Scene):
    def construct(self):
        p = [LEFT + DOWN, RIGHT + DOWN, RIGHT + UP, LEFT + UP]
        v = [MathTex(f"v_{{{i+1}}}").scale(0.5).next_to(p[i], p[i]-p[(i+1)%4], buff=0.3) for i in range(4)]
        e = VGroup()
        l = [3, 4, 3, 4]
        w = [1, 2, 1, 2]
        el = [MathTex(f"e_{{{i+1}}}").scale(0.5) for i in range(4)]
        wl = [MathTex(str(l[i])).scale(0.5) for i in range(4)]

        for i in range(4):
            ln = Line(p[i], p[(i+1)%4], color=WHITE, stroke_width=4)
            e.add(ln)
            el[i].move_to(ln.get_center() + 0.3 * ln.copy().rotate(PI/2).get_unit_vector())
            wl[i].move_to(ln.get_center() - 0.3 * ln.copy().rotate(PI/2).get_unit_vector())

        r1 = MathTex("r_1", "5").arrange(DOWN, buff=0.1).scale(0.6).move_to(ORIGIN)
        r2 = MathTex("r_2", "6").arrange(DOWN, buff=0.1).scale(0.6).next_to(p[2], RIGHT, buff=0.8)

        self.add(e, *v, *el, *wl, r1, r2)
