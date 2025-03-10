from manim import *

class Tutorial(Scene):
    def construct(self):
        circ = Circle(radius=3,stroke_color=PURE_RED,fill_color="#8FFE09",fill_opacity=0.5)
        rect = Rectangle(3,2,stroke_color=XKCD.BABYSHITGREEN)
        txt = VGroup(Text("Hello world"),Text("Hello",color=BLUE,font="Comic Sans MS"))
        self.play(AnimationGroup(DrawBorderThenFill(circ),Write(txt[0]),lag_ratio=0.5),run_time=1)
        self.wait(2)
        self.play(ReplacementTransform(txt[0],txt[1]))
        self.wait()
        self.play(txt[1].animate.shift(UP*3))
        self.wait() 
        Tex("")
        """         func = lambda pos: ((pos[0]*UR+pos[1]*LEFT) - pos)  
        mob= StreamLines(func,x_range=[-5,5,1], y_range=[-5,5,1],stroke_width=3)  
        self.play(Create(mob),run_time=4)
        self.wait() """