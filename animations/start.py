from manimlib import *
sys.path.insert(0, './')
sys.path.insert(0, './src')
from algo_vector import *
from algo_stack import *

class MonotonicStack(Scene):
    def scale(self, s):
        self.camera.frame.set_width(self.camera.frame.get_width()/s)
        self.camera.frame.set_height(self.camera.frame.get_height()/s)

    def construct(self):
        self.scale(1)
        arr = AlgoVector(self, [73, 74, 75, 71, 69, 72, 76, 73])
        arr.to_edge(edge=UP)

        res = AlgoVector(self, [0, 0, 0, 0, 0, 0, 0, 0])
        res.next_to(arr, direction=DOWN)

        stack = AlgoStack(self, [])

        self.add(arr, res, stack)
        self.play(ShowCreation(arr))
        self.play(ShowCreation(res))
        self.play(ShowCreation(stack))

        arrow = arr.add_arrow()

        for i in range(arr.size()):
            arr.move_arrow(arrow, i)
            while not stack.empty() and arr.get_node_data(i) > arr.get_node_data(stack.top_data()):
                index = stack.top_data()
                stack.pop()
                self.wait()
                res.set_node_data(index, i - index)
                res.next_to(arr, direction=DOWN)
                self.wait()
            stack.push(i)
            self.wait(1)
        
        self.wait(5)


        

