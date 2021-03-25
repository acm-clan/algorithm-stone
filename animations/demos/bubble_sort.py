from manimlib import *

class BubbleSortScene(Scene):
    CONFIG = {"camera_config": {"background_color": "#000000 "}}

    arr = [12, 8, 9, 2, 4, 18, 1]
    ANIMATION_TIME = 0.5

    def highlightNeighboringNumbers(self, nums, j, scale=2.0, color=RED):
        self.play(
            nums[j].scale, scale,
            nums[j].set_color, color,
            nums[j+1].scale, scale,
            nums[j+1].set_color, color,
            run_time=self.ANIMATION_TIME
        )
        self.wait()

    def construct(self):
        title = Text("Bubble Sort", color=GOLD).scale(2)
        title.to_corner(UL)

        self.play(
            ShowCreation(title)
        )
        self.wait()

        N = len(self.arr)
        list_of_squares = [Square().scale(0.6) for i in self.arr]

        # unpack squares and add it to VGroup
        squares = VGroup(*list_of_squares)

        squares.arrange(buff=0.)

        nums = [Text(str(i)) for i in self.arr]
        for i in range(N):
            nums[i].move_to(squares[i].get_center())

        self.add(squares, *nums)
        self.wait(2)

        for i in range(N):
            for j in range(N-i-1):

                self.highlightNeighboringNumbers(nums, j)

                if self.arr[j] > self.arr[j+1]:

                    self.play(
                        Swap(nums[j], nums[j+1])
                    )

                    # swap numbers
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

                    # swap TextMobjects
                    nums[j], nums[j+1] = nums[j+1], nums[j]

                # back transformation
                self.highlightNeighboringNumbers(
                    nums, j, scale=0.5, color=WHITE)

        self.wait(5)
