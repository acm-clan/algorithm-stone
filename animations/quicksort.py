from manim_imports_ext import *

class QuickSort(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.partition_time = 0
        self.low_arrow = None
        self.current_arrow = None
        random.seed(1)

    def scale(self, s):
        self.camera.frame.set_width(self.camera.frame.get_width()/s)
        self.camera.frame.set_height(self.camera.frame.get_height()/s)
    
    def add_span(self, arr, low, high):
        l = arr.submobjects[low].get_bounding_box_point(DOWN)
        h = arr.submobjects[high].get_bounding_box_point(DOWN)
        color = self.rand_color()
        span = Line(l, h, color=color)
        delta = DOWN*self.partition_time*0.3
        span.shift(delta)
        span_left = Line(l, l+delta, color=color)
        span_right = Line(h, h+delta, color=color)
        self.play(ShowCreation(span), ShowCreation(span_left), ShowCreation(span_right))
        self.wait()

    def compare(self, arr, a, b):
        ca = arr.submobjects[a].copy()
        cb = arr.submobjects[b].copy()
        self.play(ApplyMethod(ca.move_to, ORIGIN+DOWN/2+LEFT),
        ApplyMethod(cb.move_to, ORIGIN+DOWN/2+RIGHT))
        t = None
        m = None
        if arr.get(a) > arr.get(b):
            t = Text(">", color=YELLOW).scale(0.5)
            m = self.create_serif_font("不需要移动").scale(0.5)
        else:
            t = Text("<=", color=YELLOW).scale(0.5)
            m = self.create_serif_font("交换放左边").scale(0.5)
        t.shift(DOWN/2)
        m.next_to(cb)
        self.add(t, m)
        self.play(ShowCreation(m))
        self.wait(1)
        self.play(FadeOut(ca, run_time=0.2), FadeOut(cb, run_time=0.2), FadeOut(t, run_time=0.2), FadeOut(m, run_time=0.2))

    def partition(self, arr, low, high):
        self.partition_time += 1
        # 增加一条横线
        self.add_span(arr, low, high)
        anchor = arr.get(high)
        # 高亮锚点
        self.play(ApplyMethod(arr.submobjects[high].set_color, BLUE))
        i = low - 1
        arr.move_arrow(self.low_arrow, low)

        for j in range(low, high):
            arr.move_arrow(self.current_arrow, j)
            self.compare(arr, j, high)
            if arr.get(j) <= anchor:
                i += 1
                arr.move_arrow(self.low_arrow, i)
                if i != j:
                    self.show_message("交换%d和%d"%(arr.get(i), arr.get(j)))
                    arr.swap(i, j)

        if i+1 != high:
            self.show_message("最后将锚点%d放到%d"%(arr.get(high), arr.get(i+1)))
            # 压暗锚点
            arr.swap(i+1, high)
        self.play(ApplyMethod(arr.submobjects[i+1].set_color, GREY))
        self.wait()
        return i+1

    def quick_sort(self, arr, low, high):
        if low >= high:
            return
        p = self.partition(arr, low, high)
        self.quick_sort(arr, low, p-1)
        self.quick_sort(arr, p+1, high)

    def construct(self):
        self.scale(1)
        self.add_sound("bg")
        # logo
        self.start_logo()

        # content

        self.init_message("快速排序")
        self.datas = [13, 19, 5, 12, 8, 7, 4, 21, 6, 11]

        arr = AlgoVector(self, self.datas)
        arr.to_edge(edge=UP)

        self.play(ShowCreation(arr))
        self.low_arrow = arr.add_arrow(0)
        self.low_arrow.set_color(self.rand_color())
        self.current_arrow = arr.add_arrow(0)
        self.current_arrow.set_color(self.rand_color())

        self.wait()
        self.quick_sort(arr, 0, arr.size()-1)
        # 
        self.show_message("一句话记忆：比锚点小的放左边")
        self.wait(5)

        self.show_message("完成快速排序，谢谢观看！")
        self.finish()
