
from manim import*
from itertools import combinations
class  graph(Scene):
	def construct(self):
		self.dots()
		pass

	def dots(self):
		pt=[ORIGIN,LEFT,RIGHT,LEFT*UP,ORIGIN*DOWN]
		s=VGroup(*[Dot(point=p).set_fill(color=RED,opacity=2) for p in pt])

		self.add(s)
		l=VGroup(*[Line(i,j) for i,j in combinations(pt,2)] )
		self.play(Create(l),run_time=5)


		



		  
	