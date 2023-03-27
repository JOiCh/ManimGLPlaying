from manimlib import *
# from manimlib.imports import *
# from manim import Wiggle
# import numpy as np

# class JOiver(Scene):
       
#    實驗中
  #  def construct(self):
  #     txt0 = "Everything you want to hear.円円円円円円円円円円円円円円円"
  #     mobjects_money = VGroup(
  #       Text("$"), Text("$"), Text("$")
  #     ).scale(2)
  #     mobjects_money.arrange(RIGHT, buff=.5)
  #   #   tripple_money = "$$$"
  #     ss4 = "SESAME4 = 4,980円"
  #     ss4_arr = ["S","E","S","A","M","E","4","=","4",",","9","8","0","円"]
  #     new_price = "5,980円"
  #     new_price_arr = ["5",",","9","8","0","円"]
  #     up = "↑"
  #     jp = "どう"
  #     question = "?"

  #     kw = {
  #           "run_time": 2, 
  #           "path_arc":PI /2,
  #     }


  #     self.play(ShowSubmobjectsOneByOne(mobjects_money, run_time = 1))
  #     mobjects_money.arrange(LEFT, buff=0)
  #     self.play(
  #       *[Uncreate(mob) for mob in mobjects_money], run_time = 1
  #     )

  #     el2 = Text(question).scale(8)
  #     el2.next_to(mobjects_money, RIGHT, buff = 1)
  #     self.play(FadeIn(el2,shift = UP), run_time = .5)
  #     self.wait(.5)

  #     el3 = Text(ss4)
  #     self.play(Transform(el2, el3), run_time = 1)
  #     self.play(ApplyWave(el2))
  #     self.remove(el2)

  #     el4 = Text(new_price)
  #     self.play(TransformMatchingShapes(el3, el4, path_arc=PI/2))

  #   #   mobjects_money2 = VGroup(
  #   #     el4, Text(up).scale(5), Text(jp), Text(question)
  #   #   ).scale(2)
      
  #   #   self.play(
  #   #      *[GrowFromPoint(mob, mob.get_center()) for mob in Text(up).scale(5)]
  #   #   )
  #     el6 = Text(jp)
  #     el5 = Text(up).scale(3)
  #     el4.next_to(el5, LEFT, buff= .3)
  #     el6.next_to(el5, RIGHT, buff= 2)
  #     self.wait()
  #     self.play(FadeIn(el5, shift = UP), run_time = 2)
      
  #     q2 = Text("?")
  #     q2.next_to(el6, RIGHT, buff= 0.5)
  #     gp2 = VGroup(el6,q2.scale(3))
  #   #   self.add(q2.scale(2))
  #     self.play(
  #           *[WiggleOutThenIn(mob) for mob in gp2 ]
  #     )

    # 電阻圖test
  # def construct(self):
  #       tex = Tex(r"\includegraphics{test.pdf}")
  #       self.play(Write(tex))
  #       self.wait()
   

class Cir(Scene):
    def construct(self):
        # 創建 circuitikz 環境下的 LaTeX 程式碼
        circuit = Tex(r"""
            \begin{circuitikz}[american]
                \draw (0,0) to [battery2, v=$1.5V$] (0,2)
                  to[short, i=$I_0$] (2,2)
                  to[R] (2,0)
                  to[short] (0,0)
                  ;
            \end{circuitikz}""")
        self.add(circuit)
        self.wait(3)