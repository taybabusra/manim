# Wikipedia: https://en.wikipedia.org/wiki/Rose_(mathematics)

from manim import *


class RosePattern(VMobject):
    #k = 3  # n / d
    #step_size=0.05  # step change in polar angle
    #theta= 2 * PI
    #radius = 2  # amplitude

    def __init__(self,k = 3,step_size=0.05,theta= 2 * PI,radius = 2,**kwargs):
        super().__init__(stroke_width=1,**kwargs)
        theta = np.arange(0, theta + step_size, step_size)

        # Equations:
        # x = a * cos(k * theta) * cos(theta)
        # y = a * cos(k * theta) * sin(theta)
        points = [
            np.array([
                radius * np.cos(k * t) * np.cos(t),
                radius * np.cos(k * t) * np.sin(t),
                0
            ]) for t in theta
        ]
        self.set_points_smoothly(points)


class RosePatternNutshell(Scene):
    num = 7 # intended to be a square
    offset= 2.3 # controls the spacing between the elements

    def construct(self):
        grps = VGroup()  # as there are going to be groups of Texs and RosePatterns
        texs = VGroup()
        patterns = VGroup()

        for n in range(self.num + 1):
            for d in range(self.num + 1):
                if n == 0 and d == 0:
                    tex = MathTex("k = {n \\over d}", font_size=25)
                    grps.add(tex)
                    texs.add(tex)
                if n == 0 and d != 0:
                    tex = MathTex(f"d = {d}", font_size=25)
                    grps.add(tex)
                    texs.add(tex)
                if n != 0 and d == 0:
                    tex = MathTex(f"n = {n}", font_size=25)
                    grps.add(tex)
                    texs.add(tex)
                if n != 0 and d != 0:
                    pattern = RosePattern(
                        k=n / d,
                        radius=self.camera.frame_width/ (2 * self.offset * (self.num + 1)),
                        #set(width=config.frame_width)
                        theta=2 * self.num * PI
                    )
                    grps.add(pattern)
                    patterns.add(pattern)

        colors = [ORANGE, TEAL, BLUE, GREEN, RED, MAROON, PURPLE, PINK]

        grps.arrange_in_grid(fill_rows_first=False)
        patterns.set_color_by_gradient(*colors)
        texs.set_color_by_gradient(*colors)

        self.play(*[Write(tex) for tex in texs])
        self.play(
            *[Create(pattern) for pattern in patterns],
            run_time=8,
            rate_func=linear
        )
        self.wait()