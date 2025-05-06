from manim import *

class ChangeGraphLayout(Scene):
    def construct(self):
        G = Graph([1, 2, 3, 4, 5], [(1, 2), (2, 3), (3, 4), (4, 5),(5,1)],
                  layout="circular"
                  )
        # self.add(G.animate.change_layout("circular"))
        # self.add(G.layout("circular"))
       
        self.add(G)
        # self.wait()