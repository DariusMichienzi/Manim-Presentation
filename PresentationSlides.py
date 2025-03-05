from manim import *

from manim_slides import Slide


class Presentation(Slide):
    def construct(self):
        self.wait_time_between_slides = 0.1

        title = VGroup(Text("Developer Group Meeting",weight=BOLD),Text("Wins",weight=BOLD),Text("Issues",weight=BOLD))
        footer = VGroup(Tex(r"7\textsuperscript{th} March 2025"),Text("Darius Michienzi",slant=ITALIC))
        title.scale(1.8)
        footer.scale(0.5)
        footer[0].move_to([-5.5,-3.5,0])
        footer[1].move_to([5.5,-3.5,0])
        self.play(FadeIn(title[0],footer),run_time=1)

        self.next_slide()

        self.play(ReplacementTransform(title[0],title[1]),run_time=1)

        self.next_slide()

        self.play(ReplacementTransform(title[1],title[2]),run_time=1)

        self.next_slide()

        self.play(Unwrite(title[2]),run_time=1)
        self.remove(title)
        banner = ManimBanner()
        self.wait(0.2)
        self.play(banner.create())
        self.play(banner.expand())

        self.next_slide()

        subtitle = VGroup(Text("What is Manim?"),Text("Why Manim?"),Text("Drawbacks"),Text("Installation"),Text("Getting Started"))
        self.play(banner.animate.scale(0.5),run_time=0.5)
        self.play(banner.animate.move_to([3.8,2.8,0]),run_time=0.5)
        self.wait(0.5)
        subtitle.move_to([-3.5,2.5,0])
        self.play(Write(subtitle[0]),run_time=0.5)
        underline1 = Underline(subtitle[0])
        self.play(Write(underline1))

        self.next_slide()

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

        self.next_slide()

        b1blogo = ImageMobject("3B1B_Logo.webp")
        b1blogo.scale(0.2)
        b1blogo.move_to([1,1,0])
        self.play(AnimationGroup(Write(points1[1]),FadeIn(b1blogo),lag_ratio=0.5))

        self.next_slide()

        self.play(Write(points1[2]))
        self.play(Write(points1[3]))

        self.next_slide()

        slideslogo = ImageMobject("Manim_Slides.webp")
        slideslogo.scale(0.2)
        slideslogo.move_to([0,-2.5,0])
        self.play(AnimationGroup(Write(points1[4]),FadeIn(slideslogo),lag_ratio=0.5))

        self.next_slide()

        self.play(FadeOut(points1),FadeOut(slideslogo),FadeOut(b1blogo))
        underline2 = Underline(subtitle[1])
        self.play(ReplacementTransform(subtitle[0],subtitle[1]),ReplacementTransform(underline1,underline2))

        self.next_slide()

        points2 = VGroup(Text("- Surprisingly easy to make high quality professional looking animations and presentations"),
                         Text("- Highly customizable and intuitive"),
                         Text("- An excellent explanatory and visual tool for education"),
                         Text("- There is an active Community constantly working on updates and new features"),
                         )
        points2.arrange(DOWN*2, center=False, aligned_edge=LEFT) 
        points2.move_to([0,0.9,0])
        points2.scale(0.5)
        self.play(Write(points2[0]))

        self.next_slide()

        self.play(Write(points2[1]))

        self.next_slide()

        self.play(Write(points2[2]))

        self.next_slide()

        self.play(Write(points2[3]))

        self.next_slide()

        subtitle[2].move_to([-3.5,-0.5,0])
        underline3 = Underline(subtitle[2])
        self.play(Write(subtitle[2]),Write(underline3))

        self.next_slide()

        points3 = VGroup(Text("- Time to render can become an issue. This presentation took !!! "),
                         Text("- A MANIM animation is very easy to spot in the default style",t2w={"MANIM": BOLD},t2c={"MANIM": BLUE}),
                         Text("- More time consuming to make presentations (mainly because of rendering)"),
                         Text("- Previewing slides or quick view rendering not easy to do"),
                         )
        points3.arrange(DOWN*2, center=False, aligned_edge=LEFT) 
        points3.move_to([-1,-2,0])
        points3.scale(0.5)
        self.play(Write(points3[0]))

        self.next_slide()

        self.play(Write(points3[1]))

        self.next_slide()

        self.play(Write(points3[2]))

        self.next_slide()

        self.play(Write(points3[3]))

        self.next_slide()

