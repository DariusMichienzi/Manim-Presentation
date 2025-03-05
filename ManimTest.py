from manim import *

class Tutorial(Scene):
    def construct(self):
        circ = Circle(radius=2.4, stroke_color=PURE_RED,fill_color=RED,fill_opacity=0.5)
        rect = Rectangle(3,2, stroke_color=PURE_GREEN,fill_color=GREEN,fill_opacity=0.2)
        txt = VGroup(Tex("Hello World"),Tex("Hello",tex_template=TexFontTemplates.comic_sans))
        self.play(DrawBorderThenFill(circ), run_time=3)
        self.wait(2)
        self.play(Transform(circ,rect),run_time=0.5)
        self.play(Write(txt[0]))
        self.wait(2)
        self.play(ScaleInPlace(circ,0.5),
                  ScaleInPlace(txt[0],0.5),
                  Transform(txt[0],txt[1]),run_time=0.5)
        self.wait(5)
