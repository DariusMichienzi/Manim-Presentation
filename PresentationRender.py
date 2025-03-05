from manim import *

class Presentation(Scene):
    def construct(self):

        title = VGroup(Text("Developer Group Meeting",weight=BOLD),Text("Wins",weight=BOLD),Text("Issues",weight=BOLD))
        footer = VGroup(Tex(r"7\textsuperscript{th} March 2025"),Text("Darius Michienzi",slant=ITALIC))
        title.scale(1.8)
        footer.scale(0.5)
        footer[0].move_to([-5.5,-3.5,0])
        footer[1].move_to([5.5,-3.5,0])
        self.play(FadeIn(title[0],footer),run_time=1)

        self.wait(2)

        self.play(ReplacementTransform(title[0],title[1]),run_time=1)

        self.wait(2)

        self.play(ReplacementTransform(title[1],title[2]),run_time=1)

        self.wait(2)

        self.play(Unwrite(title[2]),run_time=1)
        self.remove(title)
        banner = ManimBanner()
        self.wait(0.2)
        self.play(banner.create())
        self.play(banner.expand())

        self.wait(2)

        subtitle = VGroup(Text("What is Manim?"),Text("Why Manim?"),Text("Drawbacks"),Text("Installation"),Text("Getting Started"))
        self.play(banner.animate.scale(0.5),run_time=0.5)
        self.play(banner.animate.move_to([3.8,2.8,0]),run_time=0.5)
        self.wait(0.5)
        subtitle.move_to([-3.5,2.5,0])
        self.play(Write(subtitle[0]),run_time=0.5)
        underline1 = Underline(subtitle[0])
        self.play(Write(underline1))

        self.wait(2)

        points1 = VGroup(Text("- Maths ANIMation library for python",t2w={"M": BOLD,"A": BOLD,"N": BOLD,"I": BOLD},t2c={"M": BLUE,"A": BLUE,"N": BLUE,"I": BLUE}),
                         Text("- Made by 3Blue1Brown for his YouTube Channel"),
                         Text("- MANIM Community is a community maintained version forked from the original",t2w={"MANIM Community":BOLD},t2c={"MANIM Community": YELLOW}),
                         Text(" This version is continually developed with new features and full documentation."),
                         Text("- There is also the additional package MANIM Slides used to make interactive presentations like this",t2w={"MANIM Slides":BOLD},t2c={"MANIM Slides": BLUE_E})
                         )
        points1.arrange(DOWN*3, center=False, aligned_edge=LEFT) 
        points1.move_to([0,0,0])
        points1.scale(0.5)
        self.play(Write(points1[0]))

        self.wait(2)

        b1blogo = ImageMobject("./PresImg/3B1B_Logo.webp")
        b1blogo.scale(0.2)
        b1blogo.move_to([1,1,0])
        self.play(AnimationGroup(Write(points1[1]),FadeIn(b1blogo),lag_ratio=0.5))

        self.wait(2)

        self.play(Write(points1[2]))
        self.play(Write(points1[3]))

        self.wait(2)

        slideslogo = ImageMobject("./PresImg/Manim_Slides.webp")
        slideslogo.scale(0.2)
        slideslogo.move_to([0,-2.5,0])
        self.play(AnimationGroup(Write(points1[4]),FadeIn(slideslogo),lag_ratio=0.5))

        self.wait(2)

        self.play(FadeOut(points1),FadeOut(slideslogo),FadeOut(b1blogo))
        underline2 = Underline(subtitle[1])
        self.play(ReplacementTransform(subtitle[0],subtitle[1]),ReplacementTransform(underline1,underline2))

        self.wait(2)

        points2 = VGroup(Text("- Surprisingly easy to make high quality professional looking animations and presentations"),
                         Text("- Highly customizable and intuitive"),
                         Text("- An excellent explanatory and visual tool for education"),
                         Text("- There is an active Community constantly working on updates and new features"),
                         )
        points2.arrange(DOWN*2, center=False, aligned_edge=LEFT) 
        points2.move_to([0,0.9,0])
        points2.scale(0.5)
        self.play(Write(points2[0]))

        self.wait(2)

        self.play(Write(points2[1]))

        self.wait(2)

        self.play(Write(points2[2]))

        self.wait(2)

        self.play(Write(points2[3]))

        self.wait(2)

        subtitle[2].move_to([-3.5,-0.5,0])
        underline3 = Underline(subtitle[2])
        self.play(Write(subtitle[2]),Write(underline3))

        self.wait(2)

        points3 = VGroup(Text("- Time to render can become an issue. This presentation took !!! "),
                         Text("- A MANIM animation is very easy to spot in the default style",t2w={"MANIM": BOLD},t2c={"MANIM": BLUE}),
                         Text("- More time consuming to make presentations (mainly because of rendering)"),
                         Text("- Previewing slides or quick view rendering not easy to do"),
                         )
        points3.arrange(DOWN*2, center=False, aligned_edge=LEFT) 
        points3.move_to([-1,-2,0])
        points3.scale(0.5)
        self.play(Write(points3[0]))

        self.wait(2)

        self.play(Write(points3[1]))

        self.wait(2)

        self.play(Write(points3[2]))

        self.wait(2)

        self.play(Write(points3[3]))

        self.wait(2)

        underline4 = Underline(subtitle[3])
        self.play(FadeOut(points2),FadeOut(points3),FadeOut(subtitle[2]),FadeOut(underline3),ReplacementTransform(subtitle[1],subtitle[3]),ReplacementTransform(underline2,underline4))

        self.wait(2)

        points4 = VGroup(Tex("- Can be installed like any other python package"),
                         Tex("- using ", r"\verb|pip install manim|"),
                         Tex("- or ", r"\verb|pip install manim-slides|"),
                         Tex("- I would suggest using ", "VSCode. ", "There is an extension, ", "Manim Sideview",", that is very useful for quick access to Mobjects and a 'quick' rendering panel")
                         )
        points4.arrange(DOWN*2, center=False, aligned_edge=LEFT) 
        points4.move_to([-0.0,0.5,0])
        points4.scale(0.8)
        points4[1][1].set_color(BLUE)
        points4[2][1].set_color(BLUE)
        points4[3][1].set_color(YELLOW)
        points4[3][3].set_color(GREEN)
        sidelogo = ImageMobject("./PresImg/sideview.png")
        sidelogo.scale(0.1)
        sidelogo.move_to([0,-3,0])
        self.play(Write(points4[0]))
        self.wait()
        self.play(Write(points4[1]))
        self.wait()
        self.play(Write(points4[2]))
        self.wait()

        self.wait(2)

        self.play(AnimationGroup(Write(points4[3]),FadeIn(sidelogo),lag_ratio=0.5))

        self.wait(2)

        underline5 = Underline(subtitle[4])
        self.play(FadeOut(points4),FadeOut(sidelogo),ReplacementTransform(subtitle[3],subtitle[4]),ReplacementTransform(underline4,underline5))
    
        self.wait(2)

        self.play(subtitle[4].animate.shift(UP*0.8),underline5.animate.shift(UP*0.8))
        animcode = Code(code_file="ManimTest.py",language="python")
        rendercode = VGroup(Code(code_string="manim -pqh Tutorial.py Tutorial",language="console"),Code(code_string="manim -pqm Tutorial.py Tutorial",language="console"),Code(code_string="manim -pql Tutorial.py Tutorial",language="console"))
        presrendercode1 = VGroup(Code(code_string="manim-slide render Tutorial.py Tutorial",language="console"),
                                Code(code_string="manim-slides Tutorial",language="console")).arrange(RIGHT)
        
        presrendercode2 = VGroup(Code(code_string="manim-slide render Tutorial.py Tutorial",language="console"),
                                Code(code_string="manim-slides convert Tutorial slides.html --open",language="console")).arrange(RIGHT)
        
        prescode = Code(code_string="""from manim import *
from manim_slides import * 
                        
class Tutorial(Slide):
    def construct(self):
        circ = Circle(radius=2.4, stroke_color=PURE_RED,fill_color=RED,fill_opacity=0.5)
        rect = Rectangle(3,2, stroke_color=PURE_GREEN,fill_color=GREEN,fill_opacity=0.2)
        txt = VGroup(Tex("Hello World"),Tex("Hello",tex_template=TexFontTemplates.comic_sans))
        self.play(DrawBorderThenFill(circ), run_time=3)
        self.next_slide()
        self.play(Transform(circ,rect),run_time=0.5)
        self.play(Write(txt[0]))
        self.next_slide()
        self.play(ScaleInPlace(circ,0.5),
                  ScaleInPlace(txt[0],0.5),
                  Transform(txt[0],txt[1]),run_time=0.5)
        self.next_slide()""", language="python")
        animcode.scale(0.7)
        prescode.scale(0.7)
        rendercode.scale(0.7)
        presrendercode1.scale(0.7)
        presrendercode2.scale(0.7)

        animcode.move_to([0.09,0,0])
        prescode.move_to([0.09,0,0])
        rendercode.move_to([0,-3,0])
        presrendercode1.move_to([0,-3,0])
        presrendercode2.move_to([0,-3,0])


        self.play(AnimationGroup(Write(animcode),FadeIn(rendercode[0]),lag_ratio=0.5),run_time=1.5)
        
        self.wait(2)
        #self.next_slide(loop=True)
        
        self.play(Transform(rendercode[0],rendercode[1]))
        self.wait(0.5)
        self.play(Transform(rendercode[0],rendercode[2]))
        self.wait(0.5)
        self.play(Transform(rendercode[0],rendercode[0]))
        self.wait(0.5)

        self.wait(2)
        
        self.play(ReplacementTransform(animcode,prescode),ReplacementTransform(rendercode[0],presrendercode1),run_time=2.5  )

        self.wait(2)

        self.play(ReplacementTransform(presrendercode1,presrendercode2))

        self.wait(2)