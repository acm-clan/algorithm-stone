from manimlib import *

class AlgoLogo(VMobject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def init_points(self):
        start = ORIGIN
        self.vertices = get_quadratic_approximation_of_cubic(start, start+RIGHT*1+UP, start+RIGHT*2+UP, start+RIGHT*3)
        self.set_points(self.vertices)
        self.close_path()
