from manim_imports_ext import *

class MonotonicStack(AlgoScene):
    def scale(self, s):
        self.camera.frame.set_width(self.camera.frame.get_width()/s)
        self.camera.frame.set_height(self.camera.frame.get_height()/s)

    def compare(self, arr, indexa, indexb):
        # 比较二者
        a = arr.submobjects[indexa].copy()
        self.play(ApplyMethod(a.move_to, UP*1.3+LEFT/2))

        b = arr.submobjects[indexb].copy()
        self.play(ApplyMethod(b.move_to, UP*1.3+RIGHT/2))

        va = self.datas[indexa]
        vb = self.datas[indexb]

        if va > vb:
            self.show_message("%d比栈顶%d大，%d出栈, %d入栈" % (va, vb, vb, va))
        else:
            self.show_message("%d比栈顶%d小，%d入栈" % (va, vb, va))

        self.wait()
        self.play(FadeOut(a))
        self.play(FadeOut(b))
        
    def show_message(self, msg):
        m = Text(msg, font=AlgoFontName).scale(0.5).shift(DOWN*1.5)
        self.play(Transform(self.message, m))

    def construct(self):
        self.scale(1)
        self.datas = [73, 74, 75, 71, 69, 72, 76, 73]
        self.message = Text("单调栈", font=AlgoFontName).scale(0.5).shift(DOWN*1.5)
        self.play(Write(self.message))

        arr = AlgoVector(self, self.datas)
        arr.to_edge(edge=UP)
        for i in range(arr.size()):
            arr.set_sub(i, str(i))

        res = AlgoVector(self, [0, 0, 0, 0, 0, 0, 0, 0])
        res.next_to(arr, direction=DOWN)
        res.set_color("#666666")

        stack = AlgoStack(self, [])

        self.play(ShowCreation(arr))
        self.play(ShowCreation(res))
        self.play(ShowCreation(stack))

        arrow = arr.add_arrow()

        for i in range(arr.size()):
            arr.move_arrow(arrow, i)
            
            if not stack.empty():
                self.compare(arr, i, stack.top_data())

            while not stack.empty() and arr.get(i) > arr.get(stack.top_data()):
                index = stack.top_data()
                stack.pop()
                self.wait()
                res.set(index, i - index)
                res.next_to(arr, direction=DOWN)
                self.wait()
                if not stack.empty():
                    self.compare(arr, i, stack.top_data())

            stack.push(i)
            self.wait()
        self.show_message("完成单调栈，谢谢观看！")
        self.wait(5)
