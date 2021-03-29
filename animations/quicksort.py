from manimlib import *
sys.path.insert(0, './')
sys.path.insert(0, './src')
from algo_stack import *
from algo_vector import *

class QuickSort(Scene):
    def scale(self, s):
        self.camera.frame.set_width(self.camera.frame.get_width()/s)
        self.camera.frame.set_height(self.camera.frame.get_height()/s)

    def show_message(self, msg):
        m = Text(msg, font_size=24, font='微软雅黑').shift(DOWN*1.5)
        self.play(Transform(self.message, m))

    def partition(self, arr, low, high):
        anchor = arr.get(high)
        i = low - 1
        for j in range(low, high):
            if arr.get(j) <= anchor:
                i += 1
                self.show_message("交换%d %d"%(i, j))
                arr.swap(i, j)
                self.wait()
        self.show_message("交换%d %d"%(i+1, high))
        arr.swap(i+1, high)
        self.wait()
        return i+1

    def quick_sort(self, arr, low, high):
        if low >= high:
            return
        p = self.partition(arr, low, high)
        print("partion:", p, low, p-1, p+1, high)
        self.quick_sort(arr, low, p-1)
        self.quick_sort(arr, p+1, high)

    def construct(self):
        self.scale(1)
        self.datas = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
        self.message = Text("快速排序", font_size=24, font='微软雅黑').shift(DOWN*1.5)
        self.play(Write(self.message))

        arr = AlgoVector(self, self.datas)
        arr.to_edge(edge=UP)
        for i in range(arr.size()):
            arr.set_sub(i, str(i))

        self.play(ShowCreation(arr))
        self.quick_sort(arr, 0, arr.size()-1)
        self.show_message("完成快速排序，谢谢观看！")
        self.wait(5)
