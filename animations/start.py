from manimlib import *
sys.path.insert(0, './')
sys.path.insert(0, './src')
from algo_vector import *

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
        # res = Vector([0, 0, 0, 0, 0, 0, 0, 0])
        # indexes = Stack()
        # for i in range(len(arr)):
        #     while !indexes.empty() and arr[i] > arr[indexes.top()]:
        #         index = indexes.top()
        #         indexes.pop()
        #         res[index] = i - index
        #     indexes.push(i)
        # res.light()
        self.add(arr)
        self.play(ShowCreation(arr))
        self.wait(5)


        

