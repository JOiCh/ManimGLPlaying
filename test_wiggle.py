from manimlib import *
# from manim.mobject.svg.tex_mobject import StringMobject
# import random
import numpy as np

class WiggleOutThenInExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2) 

        self.add(mobjects)

        self.play(
            *[WiggleOutThenIn(mob) for mob in mobjects]
        )

        self.wait()