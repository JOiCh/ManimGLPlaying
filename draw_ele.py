from manimlib import *
# from manimlib.imports import TexMobject

class Ele(Scene):
  def construct(self):
        # tex = Tex(r"\includegraphics{images/test.pdf}") 
        img = ImageMobject("ele22.png")
        img.set_height(50)
        self.add(img)
        # 將圖片向右移動2個單位
        # img.shift(2*RIGHT)
        self.play(FadeIn(img, run_time = 1))
        self.wait()
        self.play(ApplyWave(img))
        self.play(ApplyWave(
            img,
            direction=RIGHT,
            time_width=10,
            amplitude=2
        ))
        self.play(ApplyWave(
            img,
            rate_func=linear,
            ripples=5
        ))

        # Write會失敗??研究中
        # self.play(Write(img))