from manim import *

class GREquation(Scene):
    def construct(self):
        title = Tex(r"Some example equation manipulation using \LaTeX")
        #equation = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}")
        equation = MathTex("G_{\mu \nu}", "+", "\Lambda","g_{\mu \nu}", "=", "8 \pi", "T_{\mu \nu}")
        VGroup(title, equation).arrange(DOWN)
        self.play(Write(title),FadeIn(equation, shift=DOWN))
        self.wait(2)
        self.play(FadeOut(title),equation.animate.shift(UP*3.5))

        framebox1 = SurroundingRectangle(equation[3], buff = .1)
        self.play(Create(framebox1))
        g = Matrix([[-1,0,0,0],[0,r"\frac{a(t)^2}{1-kr^2}",0,0],[0,0,r"a(t)^2r^2",0],[0,0,0,r"a(t)^2r^2sin^2(\theta)"]],h_buff=2.2,v_buff=1.2,element_alignment_corner=[ 0., 0., 0.])
        g.scale(1)
        eq2 = MathTex("g_{\mu \nu} =")
        eq2.next_to(g, LEFT)
        self.play(Write(eq2), Write(g),run_time=0.5)
        self.wait(2)

        framebox2 = SurroundingRectangle(equation[6], buff = .1)
        T = Matrix([[r"\rho",0,0,0],[0,r"P \frac{a(t)^2}{1-kr^2}",0,0],[0,0,r"Pa(t)^2r^2",0],[0,0,0,r"Pa(t)^2r^2sin^2(\theta)"]],h_buff=2.2,v_buff=1.2,element_alignment_corner=[ 0., 0., 0.])
        eq3 = MathTex("T_{\mu \nu} =")
        eq3.next_to(T, LEFT)
        self.play(ReplacementTransform(framebox1,framebox2),ReplacementTransform(eq2,eq3),ReplacementTransform(g,T))
        self.wait(2)