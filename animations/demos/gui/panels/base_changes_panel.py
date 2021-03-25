from PyQt5.QtWidgets import *

# Scrollbar minimum width
SCROLL_WIDTH = 300


class BaseChangesPanel(QWidget):

    def __init__(self, parent=None, gui_window=None):
        super().__init__(parent)
        self.gui_window = gui_window

        # Set up scrollbar
        self.scroll_area = QScrollArea()
        self.scroll_area.setMinimumWidth(SCROLL_WIDTH)

        # Buttons
        self.reset_button = QPushButton("Reset changes")
        self.apply_button = QPushButton("Apply changes and render")

        if gui_window is not None:
            self.reset_button.clicked.connect(gui_window.reset_changes)
            self.apply_button.clicked.connect(gui_window.apply_changes)

        # Arrange widget contents
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.scroll_area)
        self.main_layout.addWidget(self.reset_button)
        self.main_layout.addWidget(self.apply_button)

        self.setLayout(self.main_layout)

    def link_gui_window(self, gui_window):
        self.gui_window = gui_window
        self.reset_button.clicked.connect(gui_window.reset_changes)
        self.apply_button.clicked.connect(gui_window.apply_changes)
