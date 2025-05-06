from manim import *

class GraphTheoryExplanation(Scene):
    def construct(self):
        
        title = Text("Graph Theory Basics", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        node_label = Text("Node (Vertex)", font_size=30).shift(UP * 2.5)
        node = Dot(radius=0.15, color=BLUE).move_to(ORIGIN)
        node_name = Text("A").next_to(node, DOWN)
        self.play(FadeIn(node), Write(node_label), Write(node_name))
        self.wait(1)
        self.play(FadeOut(node_label))

        node2 = Dot(radius=0.15, color=BLUE).shift(RIGHT * 3)
        node2_name = Text("B").next_to(node2, DOWN)
        edge = Line(node.get_center(), node2.get_center())
        conn_label = Text("Edge (Connection)", font_size=30).shift(DOWN * 2.5)

        self.play(FadeIn(node2), Write(node2_name))
        self.play(Create(edge), Write(conn_label))
        self.wait(1)

        self.play(FadeOut(conn_label), FadeOut(title))

        undirected_title = Text("Undirected Graph", font_size=40).to_edge(UP)
        self.play(Write(undirected_title))
        self.wait(0.5)

        self.wait(1)

        self.play(FadeOut(undirected_title), FadeOut(edge), FadeOut(node), FadeOut(node2),
                  FadeOut(node_name), FadeOut(node2_name))

        directed_title = Text("Directed Graph", font_size=40).to_edge(UP)
        self.play(Write(directed_title))

        nodeA = Dot(radius=0.15, color=GREEN).move_to(LEFT * 2)
        nodeB = Dot(radius=0.15, color=GREEN).move_to(RIGHT * 2)
        nameA = Text("A").next_to(nodeA, DOWN)
        nameB = Text("B").next_to(nodeB, DOWN)
        arrow = Arrow(nodeA.get_center(), nodeB.get_center(), buff=0.1)

        self.play(FadeIn(nodeA), FadeIn(nodeB), Write(nameA), Write(nameB))
        self.play(Create(arrow))
        self.wait(1)

        ex = Text("A → B (One-way connection)", font_size=30).next_to(arrow, DOWN * 1.5).scale(0.5)
        self.play(Write(ex))
        self.wait(2)

        self.play(FadeOut(directed_title), FadeOut(nodeA), FadeOut(nodeB),
                  FadeOut(nameA), FadeOut(nameB), FadeOut(arrow), FadeOut(ex))
