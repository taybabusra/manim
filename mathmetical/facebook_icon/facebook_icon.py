
from manim import *
class Facebook_icon(Scene):
    def construct(self):
        #creating circle
        circle = Circle(radius=1.6,color=DARK_BLUE,fill_opacity =1.0)
        #text f
        icon =Text("f",font='Calibri').scale(6.0)\
                                                  .set_color(WHITE)\
                                                  .move_to(circle)\
                                                  .shift(DOWN*0.35)
        self.play(
            GrowFromCenter(circle),
            Write(icon),
            runtime =1.2 
        )
        self.wait()
        group = VGroup(circle,icon)
        
        self.play(
            group.animate.shift(UP+LEFT*2),
            runtime =1.2
        )
        self.wait()
        