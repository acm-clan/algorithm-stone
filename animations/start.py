from manimlib import *
sys.path.insert(0, './')
sys.path.insert(0, './src')
from algo_vector import *
from algo_stack import *

class MonotonicStack(Scene):
    CONFIG = {
            "camera_class": ThreeDCamera,
        }
    def show(self, arr, offset):
        list_of_squares = [Square().scale(0.6) for i in arr]
        squares = VGroup(*list_of_squares)
        squares.arrange(buff=0.)
        squares.shift(offset)

        self.play(ShowCreation(squares))

        nums = [Text(str(i), font_size=20) for i in arr]
        for i in range(len(arr)):
            nums[i].move_to(squares[i].get_center())
            self.add(nums[i])

        self.wait(5)

    def construct(self):
        # self.show([73, 74, 75, 71, 69, 72, 76, 73], UP*3)
        # 
        arr = AlgoVector([73, 74, 75, 71, 69, 72, 76, 73])
        arr.to_edge(edge=UP)
        res = AlgoVector([0, 0, 0, 0, 0, 0, 0, 0])
        res.next_to(arr, direction=DOWN)

        stack = AlgoStack([])

        # res.light()
        self.add(arr, res, stack)
        self.play(ShowCreation(arr))
        self.play(ShowCreation(res))
        self.play(ShowCreation(stack))

        for i in range(arr.size()):
            while not stack.empty() and arr.get_node_data(i) > arr.get_node_data(stack.top_data()):
                index = stack.top_data()
                stack.pop()
                res.set_node_data(index, i - index)
                self.wait(1)
            stack.push(i)
            self.wait(1)
        
        self.wait(5)


        

