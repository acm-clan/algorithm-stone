from manimlib import *

class AlgoLogoShield(VMobject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def init_points(self):
        start = ORIGIN

        self.append_points(Line([3., -1., 0.], [0.0, 0., 0.]).get_points())
        self.append_points(Line([0.0, 0., 0.], [-3., -1., 0.]).get_points())

        v = CubicBezier(
            [-3, -1, 0], 
            [-3.06, -3.51, 0], 
            [-2.14, -5.19, 0], 
            [0, -6.5, 0],
        )

        v2 = CubicBezier(
            [0, -6.5, 0],
            [2.14, -5.19, 0], 
            [3.06, -3.51, 0], 
            [3, -1, 0], 
            )
            
        self.append_points(v.get_points())
        self.append_points(v2.get_points())
        self.center()

class AlgoLogo(VGroup):
    def __init__(self, *vmobjects, **kwargs):
        super().__init__(*vmobjects, **kwargs)
        self.add(AlgoLogoShield(fill_color="#4386f7", fill_opacity = 1, stroke_width=0).scale(1.06), 
        AlgoLogoShield(fill_color="#fff", fill_opacity = 1, stroke_width=0, stroke_opacity=0).scale(1.00),
        AlgoLogoShield(fill_color="#4386f7", fill_opacity = 1, stroke_width=0, stroke_opacity=0).scale(0.96))

        text = Text("A", font="Caladea").scale(5.4)
        text.shift(UP*1.2)
        self.add(text)

        vertices = [
            [-3.5, -3.75, 0],
            [-3.25, -4.25, 0],
            [-3.5, -4.75, 0],
            [3.5, -4.75, 0],
            [3.25, -4.25, 0],
            [3.5, -3.75, 0],
        ]
        
        back_flag = Polygon(*vertices, fill_color="#4386f7", fill_opacity = 1, stroke_width=0)
        back_flag.shift(UP*3.25)
        self.add(back_flag)

        fore_flag = Rectangle(6, 1, fill_color="#4386f7", fill_opacity = 1, stroke_color="#fff", stroke_width=2, stroke_opacity=1)
        fore_flag.shift(DOWN*1.2)
        self.add(fore_flag)

        self.center()

