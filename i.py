from manim import *

class dfs(Scene):
    def construct(self):
        v = ["A", "B", "C", "D", "E", "F"]
        e = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"), ("C", "F")]
        g = Graph(v, e, layout="spring", labels=True)
        self.play(Create(g))
        self.wait(1)

        p = ["A", "B", "D", "C", "E", "F"]
        s = set()

        for n in p:
            if n not in s:
                c = g[n]
                self.play(c.animate.set_fill(RED), run_time=0.5)
                # self.play(c.animate.set_color(YELLOW))
                s.add(n)
                self.wait(0.3)

        self.wait(1)
