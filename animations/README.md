### 视频教程

python3 -m manimlib kmp.py -w

一句话系列
- [x] 一句话记住单调栈
- [ ] 一句话记住Knuth随机算法
- [ ] 一句话记住快速排序
- [ ] 红黑树

### 安装说明

使用[manimgl](https://3b1b.github.io/manim/)进行开发

下载Adobe开源字体https://mirrors.tuna.tsinghua.edu.cn/adobe-fonts/

等宽字体Monospaced Font，用于数字字母  

serif 是有衬线字体，意思是在字的笔画开始、结束的地方有额外的装饰，而且笔画的粗细会有所不同。相反的，sans serif 就没有这些额外的装饰，而且笔画的粗细差不多。  

serif 字体容易识别，它强调了每个字母笔画的开始和结束，因此易读性比较高，sans serif 则比较醒目。  

在中文阅读的情况下，适合使用 serif 字体（如宋体）进行排版，易于换行阅读的识别性，避免发生行间的阅读错误。  

### 带颜色和公式的字体混合
带颜色和公式的字体混合例子

``` python
class TestTexScene(AlgoScene):
    def construct(self):
        self.show_diff()
        self.wait(2)

    def show_diff(self):
        kw = {
            "tex_to_color_map": {
                "x_0": BLUE_D,
                "y_0": BLUE_B,
                "{t}": GREY_B,
                "O(2)": BLUE_D,
                "前缀和": BLUE_D,
                "单点": BLUE_D,
            }
        }

        s = VGroup(
            TexText("1 前缀和：数组不变，区间求和$O(1)$", font="", color=BLACK, **kw),
            Tex("\\text {1 前缀和：数组不变，区间求和} O(2)", color=BLACK, **kw),
            TexText("2 树状数组：用于区间求和，单点修改 $O(logn)$", color=BLACK, **kw),
            TexText("3 线段树：用于区间求和，区间最大值，区间修改，单点修改 $O(logn)$", color=BLACK, **kw),
            Tex("x({t}) = \\cos(t) x_0 - \\sin(t) y_0", color=BLACK, **kw),
        )

        s.arrange(direction=DOWN, aligned_edge=LEFT, buff=0.1)
        s.scale(0.5).center()
        self.add(s)
```
