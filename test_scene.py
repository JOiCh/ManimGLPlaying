from manimlib import *
# from manim.mobject.svg.tex_mobject import StringMobject
# import random
import numpy as np

# 漸變效果
class TextAnimation(Scene):
    def construct(self):
        # myTemplate = TexTemplate()
        # myTemplate.add_to_preamble(r"\usepackage{amsfonts}")
        # tex_template=myTemplate,
        # font_size=144,


        money = Tex(r"\$\$\$",color=YELLOW).scale(5)
        ss4 = Tex("S","E","S","A","M","E","4","=","4",",","9","8","0","y","e","n", color=BLUE).scale(2)
        ss5 = Tex("5",",","9","8","0","y","e","n","?", font="Arial", color=WHITE).scale(2)
        yen= SVGMobject("円円円円円").scale(1.5)
        # yen = Tex(r"$\textyen$}")

        # a = Tex(r"$$$")
        # b = Tex(r"SESAME4=4{,}980\yen")

        # self.add(a)
        # self.wait()
        # self.play(TransformMatchingTex(a, b, key_map={"^2": "\\sqrt{"}))
        # self.wait()

        # a = Text("$$$").scale(2)
        # b = Text("SESAME4 = 4,980円").scale(2)
        # self.add(a)
        # self.wait()
        # self.play(TransformMatchingShapes(a, b, path_arc=PI/2))
        # self.wait()
        # self.play(TransformMatchingShapes(b, a, path_arc=PI/2))
        # self.wait()

        # start_text = "$$$"
        # end_text = "SESAME4 = 4,980円"
        # third = "5,980円↑　どう？"
        
        # a = Text(start_text, font_size=96).set_color(YELLOW).scale(3)
        # b = Text(end_text).set_color_by_gradient(WHITE, "#28AEB1").scale(2)
        # c = Text(third).scale(3)

        # VGroup(a, b).arrange(UP, buff=1)
        # self.play(Write(a, run_time=3))
        # self.wait()
        # self.play(TransformMatchingShapes(a, b, path_arc=PI/2))
        # self.play(TransformMatchingShapes(b, c, path_arc=PI/2), run_time=4)
        # self.wait()
        # self.play(FadeOut(c, shift=DOWN))

        # tex = Tex(r"\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}")
        # kw = {
        #     "isolate": [
        #         "\\int_{0}^{\\infty} \\mathrm{e}^{- t}",
        #         "\\mathrm{d} t",
        #         "c_{0}",
        #         "c_{1} t",
        #         "c_{2} t^{2}",
        #         "c_{n} t^{n}"
        #     ],=
        #     "tex_to_color_map": {
        #         "\\mathrm{e}": MAROON_A,
        #         "c_{0}": BLUE,
        #         "c_{1}": BLUE,
        #         "c_{2}": BLUE,
        #         "c_{n}": BLUE
        #     }
        # }

        
        # self.play(Write(money),run_time=3)
        # self.wait()
        # self.play(TransformMatchingTex(money, ss5, key_map={r"\$\$\$": "="},path_arc=PI/2), run_time=2)
        # # self.play(TransformMatchingTex(tex2, tex3, key_map={"=": "?"},path_arc=PI/2), run_time=4)
        # # 播放动画
        # self.play(*[MoveToTarget(letter) for letter in ss4], *[MoveToTarget(letter) for letter in ss5])
       
        # self.play(TransformMatchingStrings(ss4, ss5), run_time=4)

        # 遍历每个字母并将其随机移动
        # for letter in ss4:
        #     letter.generate_target()
        #     letter.target.apply_complex_function(lambda z: np.exp(1j*np.random.uniform(0,2*np.pi))*z)

        # for letter in ss5:
        #     letter.generate_target()
        #     letter.target.apply_complex_function(lambda z: np.exp(1j*np.random.uniform(0,2*np.pi))*z)

        # rotating_letters = [ss4[1], ss4[2], ss4[4], ss4[5], ss4[12], ss4[10]]
        # #  讓字母逆時針旋轉
        # # self.play(*[Rotating(rotating_letters[i], radians=-2 * PI, about_point=ss4.get_center())
        # #             for i in range(len(rotating_letters))])
        # self.play(*[MoveToTarget(letter) for letter in ss4], *[MoveToTarget(letter) for letter in ss5])
        # self.play(TransformMatchingStrings(ss4, ss5), run_time=4)

        # 基本盤
        kw = {
            "run_time": 2, 
            "path_arc":PI /2,
        }

        # for letter in ss4:
        #     letter

        self.play(Write(money),run_time=3)
        self.play(Write(yen))
        
        self.wait()
        # self.play(TransformMatchingTex(money, ss4, key_map={r"\$\$\$": "="},path_arc=PI/2), run_time=2)
        # self.play(TransformMatchingTex(ss4, ss5, key_map={"=": "?"},path_arc=PI/2), run_time=4)
        
        self.play(TransformMatchingTex(
        money, ss4.set_color_by_tex_to_color_map({
                "E":PINK,
                "A": WHITE,
                "M": "#FDEA8E",
                "S": "#28AEB1",
        }),  
        key_map={
            r"\$\$\$": "=",
        }, **kw)
        )
        self.wait()
        self.play(
            TransformMatchingTex(ss4, ss5,
            key_map={
                "=": "?",
                "4":"5",
                "E":"9",
                "y":"n",
                "8":"0",
                "0":"e"
            }, **kw),
        )
        self.wait()
        self.play(FadeOut(ss5, RIGHT))

        