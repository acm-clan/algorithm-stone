from manimlib import *

class AlgoLogo(VMobject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def init_points(self):
        start = ORIGIN
        vertices = np.array([np.array([3., -1., 0.]), np.array([0.0, 0., 0.]), np.array([-3., -1., 0.])])

        v = get_quadratic_approximation_of_cubic(
            [-3, -1, 0], 
            [-3.06, -3.51, 0], 
            [-2.14, -5.19, 0], 
            [0, -6.5, 0],
        )

        v2 = get_quadratic_approximation_of_cubic(
            [0, -6.5, 0],
            [2.14, -5.19, 0], 
            [3.06, -3.51, 0], 
            [3, -1, 0], 
            )
            
        vertices = np.concatenate((vertices, v, v2))

        self.set_points(vertices)
        self.close_path()
        self.center()
