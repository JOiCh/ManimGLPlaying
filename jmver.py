from manimlib import *
# from manim import Wiggle
# import numpy as np
class Jmver(Scene):
   
   def construct(self):

       eq1 = Text("$$$？", font="Open Sense").scale(1.5)
       eq2 = Text("SESAME4 = 4,980円").scale(1)
       eq3 = Text("5,980円")
       eq4 = Text("↑")
       eq5 = Text("どう？").scale(2)
       eq3.next_to(eq2,LEFT, buff=-2)
       eq4.next_to(eq3,RIGHT, buff=0.3)
       eq5.next_to(eq4,RIGHT, buff=1.5)
       for i in range(2):
           self.play(ApplyWave(eq1))
       self.play(Transform(eq1, eq2), run_time = 1)
       self.play(ApplyWave(eq1))
       self.wait(1)
       self.remove(eq1)
       self.play(TransformMatchingShapes(eq2, eq3, path_arc = PI/2), run_time = 1)
    #    print("TransformMatchingShapes完成")
       self.wait()
       self.add(eq4)
    #    print("增加箭頭完成")
    #    print("wiggle開始")
       self.add(eq5)
       self.play(
            *[WiggleOutThenIn(mob) for mob in eq5]
        )
    #    print("wiggle結束")

       