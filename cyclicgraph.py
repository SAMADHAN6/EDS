from manim import *

class MovingDiGraph(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]

        # layout = {
        #     1: [1,0,0],
        #     2: [0,1,0],
        #     3: [0,0,1],
        #     4: [2,0,0]
        # }

        
        g = DiGraph(vertices, edges)

        self.play(Create(g),run_time=6)