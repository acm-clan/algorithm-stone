from manim_imports_ext import *

class KmpScene(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = "ababcabaab"

    def get_next(self):
        t = self.data
        n = len(t)
        next = np.zeros(n, dtype=int)
        next[0] = -1

        vector_string = AlgoVector(self, list(t))
        self.add(vector_string)
        text = AlgoText("pattern", color=BLUE).next_to(vector_string, direction=LEFT)
        self.add(text)

        vector_index = AlgoVector(self, range(0, n))
        self.add(vector_index)
        vector_index.next_to(vector_string, direction=UP)
        text = AlgoText("index", color=BLUE).next_to(vector_index, direction=LEFT)
        self.add(text)

        vector_next = AlgoVector(self, next)
        self.add(vector_next)
        vector_next.next_to(vector_string, direction=DOWN)
        text = AlgoText("next", color=BLUE).next_to(vector_next, direction=LEFT)
        self.add(text)

        cursor_j = vector_index.add_arrow(0, color=RED, text="j")
        cursor_k = vector_index.add_arrow(-1, color=BLUE, text="k")

        j = 0
        k = -1

        while j<len(t)-1:
            if k==-1 or t[j] == t[k]:
                if t[j] == t[k] and k != -1:
                    self.play(ApplyMethod(vector_string.get_node(j).set_color, BLUE), 
                        ApplyMethod(vector_string.get_node(k).set_color, BLUE))
                    self.show_message("比较后相等，前进一步")
                    self.play(ApplyMethod(vector_string.get_node(j).set_color, ALGO_NODE_COLOR), 
                        ApplyMethod(vector_string.get_node(k).set_color, ALGO_NODE_COLOR))
                if k == -1:
                    self.show_message("k=-1，前进一步")
                j+=1
                k+=1
                next[j] = k
                
                vector_index.move_arrow(cursor_j, j, run_time=0.5)
                vector_index.move_arrow(cursor_k, k, run_time=0.5)

                vector_next.set(j, str(k))
                if k>0:
                    self.play(vector_next.submobjects[j].set_color, BLUE)
                else:
                    self.play(vector_next.submobjects[j].set_color, RED)
                
                self.update_frame()
            else:
                self.play(ApplyMethod(vector_string.get_node(j).set_color, RED), 
                        ApplyMethod(vector_string.get_node(k).set_color, RED))
                self.show_message("比较后不相等，回溯一步")
                self.play(ApplyMethod(vector_string.get_node(j).set_color, ALGO_NODE_COLOR), 
                    ApplyMethod(vector_string.get_node(k).set_color, ALGO_NODE_COLOR))

                node = vector_next.get_node(k)
                old_k = k
                k = next[k]
                if k != -1:
                    arrow = Arrow(vector_next.get_node(old_k).get_center(),
                        vector_next.get_node(k).get_center(), path_arc=-np.pi*0.5, thickness=0.03, color=GREEN)
                else:
                    arrow = Arrow(vector_next.get_node(old_k).get_center(),
                        vector_next.get_node(old_k).get_center()+LEFT, path_arc=-np.pi*0.5, thickness=0.03, color=GREEN)
                arrow.set_color(BLUE)
                self.play(ShowCreation(arrow), run_time=0.5)
                self.wait()

                vector_index.move_arrow(cursor_k, k, run_time=0.5)

                self.play(FadeOut(arrow))

        self.show_message("next表计算完成")
        self.next = next
        print(next)

    def construct(self):
        # self.start_logo()
        self.init_message("KMP算法")
        self.get_next()
        self.wait(2)
