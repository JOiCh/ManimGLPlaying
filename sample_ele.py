from manimlib import *

TEX_TEXT_TO_REPLACE = r"\text"
TEX_USE_CTEX = False

class Cir2(Scene):
    def construct(self):

        # self.renderer.tex_template.add_to_preamble(r"\usepackage{circuitikz}")

        c = Tex(r"""
            \begin{circuitikz}[american]
                \draw (0,0) to [battery2, v=$1.5V$] (0,2)
                  to[short, i=$I_0$] (2,2)
                  to[R] (2,0)
                  to[short] (0,0)
                  ;
            \end{circuitikz}""",
            )
        
        self.add(c)
        self.wait(3)
