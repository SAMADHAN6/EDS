from manim import *

class MovingDiGraph(Scene):
    def construct(self):
        vertices = [x for x in range(5)]
        edges = [(x, x+1) for x in range(4)] + [(4, 0)]

        layout = {
            0:[0,0,0],
            1: [1,0,0],
            2: [0,1,0],
            3: [0,4,0],
            4: [0,5,0]
        }

        
        g = DiGraph(vertices, edges)

        self.play(Create(g),run_time=4)
        self.wait()