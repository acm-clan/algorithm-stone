from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from algomanim.empty_animation import is_empty_anim
from gui.video_player import VIDEO_BASE_WIDTH
from gui.anim_utils import format_anim_block_str


# Scrollbar base height
BAR_BASE_HEIGHT = 125

# Box width constraints
BOX_MIN_WIDTH = 80
BOX_MAX_WIDTH = 240

# Add-text button takes up 1/8 of the box
TEXT_BTN_FRAC = 8


class AnimationBar(QWidget):

    def __init__(self, video_player=None, gui_window=None, parent=None):
        super().__init__(parent)

        self.video_player = video_player
        self.gui_window = gui_window

        self.anims = []
        self.anim_boxes = []
        self.anim_box_list = QHBoxLayout()
        self.anim_box_list.setContentsMargins(0, 0, 0, 0)

        # multiblock edits
        self.curr_position = 0

        # Set up scrollbar for boxes
        self.scroll_area = QScrollArea()
        self.scroll_area.setMinimumSize(VIDEO_BASE_WIDTH, BAR_BASE_HEIGHT)

        # Arrange widget contents
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.scroll_area)

        self.setLayout(main_layout)

    def link_video_player(self, video_player):
        self.video_player = video_player

    def link_gui_window(self, gui_window):
        self.gui_window = gui_window

    def fill_bar(self, anims):
        # this may not be exactly anims if there are some hidden animations
        self.anims = []
        self.anim_boxes = []
        self.anim_box_list = QHBoxLayout()
        self.anim_box_list.setContentsMargins(0, 0, 0, 0)

        # track index separately
        index = 0
        for anim in anims:
            if anim.metadata.animated:
                self.anims.append(anim)
                # only display if animated or empty
                anim_box = self.create_anim_box(index, anim)
                self.anim_box_list.addWidget(anim_box)
                self.anim_boxes.append(anim_box)
                index += 1

        # Group boxes together
        anim_group_box = QGroupBox()
        anim_group_box.setStyleSheet("border-style: none")
        anim_group_box.setLayout(self.anim_box_list)

        # Show boxes in scroll area
        self.scroll_area.setWidget(anim_group_box)

    @staticmethod
    def get_anim_box_size(runtime):
        height = BAR_BASE_HEIGHT - 15  # prevent height overflow

        width = max(int(150 * runtime), BOX_MIN_WIDTH)
        width = min(width, BOX_MAX_WIDTH)  # prevent box from getting too long

        return width, height

    def create_anim_box(self, index, anim_meta_block):
        """
        Create a single anim box from the properties of anim
        """

        anim_box = QGroupBox()
        anim_box.setStyleSheet("border-style: none; background-color: white; color: black")

        anim_box_layout = QGridLayout()
        anim_box_layout.setContentsMargins(0, 0, 0, 0)

        # Animation label using metadata
        desc = format_anim_block_str(anim_meta_block)

        anim_lbl = QLabel(desc)
        anim_lbl.setAlignment(Qt.AlignCenter)  # center-align text
        anim_lbl.setWordWrap(True)  # will not wrap if there is no whitespace
        anim_box_layout.addWidget(anim_lbl, 0, 0, 1, TEXT_BTN_FRAC - 1)

        if is_empty_anim(anim_meta_block):
            # To close this "add custom animation" box
            close_button = QPushButton(text='×')
            close_button.setToolTip("Close")
            close_button.setStyleSheet("border:1px solid black;")
            close_button.clicked.connect(lambda event: self.gui_window.delete_empty_anim(index))

            anim_box_layout.addWidget(close_button, 0, TEXT_BTN_FRAC, alignment=Qt.AlignRight)
        elif anim_meta_block.start_position() != anim_meta_block.end_position():
            # Create text animation button for per animation block
            add_anim_button = QPushButton(text='+')
            add_anim_button.setToolTip("Add custom animation")
            add_anim_button.setStyleSheet("border:1px solid black;")

            add_anim_button.clicked.connect(lambda event:
                self.add_anim(index + 1, anim_meta_block.end_index()))

            anim_box_layout.addWidget(add_anim_button, 0, TEXT_BTN_FRAC, alignment=Qt.AlignRight)

        # Size and layout box
        runtime = anim_meta_block.runtime
        width, height = AnimationBar.get_anim_box_size(runtime)

        anim_box.setFixedHeight(height)
        anim_box.setFixedWidth(width)
        anim_box.setLayout(anim_box_layout)

        # Clicking on anim box jumps video to anim
        anim_box.mouseReleaseEvent = lambda event: \
            self.set_mouse_clicked(anim_meta_block)

        return anim_box

    def set_mouse_clicked(self, anim):
        mb_selected = self.gui_window.anim_clicked(anim)
        if not mb_selected and not is_empty_anim(anim):
            self.video_player.set_media_position(anim.start_position())

    def set_active_lbl(self, index):
        self.anim_boxes[index].setStyleSheet("background-color: #2980b9; color: white")
        self.scroll_area.ensureWidgetVisible(self.anim_boxes[index])

    def set_inactive_lbl(self, index):
        self.anim_boxes[index].setStyleSheet("background-color: white; color: black")

    def media_position_changed(self, position):
        self.curr_position = position
        for (i, anim) in enumerate(self.anims):
            if is_empty_anim(anim):
                continue
            start_position = anim.start_position()
            end_position = anim.end_position()
            if (start_position <= position < end_position) or \
                (start_position == position and start_position == end_position):
                self.set_active_lbl(i)
                self.gui_window.change_panel_anim(anim)
            else:
                self.set_inactive_lbl(i)

    def set_multiblock_selection_mode(self, selected):
        if selected:
            for anim_box in self.anim_boxes:
                anim_box.setStyleSheet("background-color: gray; color: black")
        else:
            self.media_position_changed(self.curr_position)

    def set_animation_group(self, start_anim, end_anim):
        start_idx = self.anims.index(start_anim)
        end_idx = self.anims.index(end_anim)
        for i in range(0, len(self.anims)):
            if start_idx <= i <= end_idx:
                self.set_active_lbl(i)
            else:
                self.set_inactive_lbl(i)

    def add_anim(self, index, position):
        self.gui_window.add_empty_anim(index, position)
        self.set_active_lbl(index)
