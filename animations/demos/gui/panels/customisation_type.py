# pylint: disable=no-value-for-parameter

from enum import Enum
from PyQt5.QtWidgets import QLineEdit

from gui.panels.widgets.input_color_button import InputColorButton
from gui.panels.widgets.input_text_box import InputTextBox
from gui.panels.widgets.qcolor_button import QColorButton

class CustomisationType(Enum):

    # pylint: disable=R0913
    def __init__(self, desc, get_widget, wrap_input_widget,
                 action_pair_customise, input_widget_index=0):
        super().__init__()
        self.desc = desc
        self.get_widget = get_widget
        self.wrap_input_widget = wrap_input_widget
        self.customise = action_pair_customise
        self.input_widget_index = input_widget_index

    @staticmethod
    def get_change_color_widget():
        return QColorButton()

    @staticmethod
    def get_change_runtime_widget():
        return QLineEdit()

    @staticmethod
    def action_pair_change_color(action_pair):
        return action_pair.set_color

    @staticmethod
    def action_pair_fast_forward(action_pair):
        return action_pair.set_runtime

    COLOR = (
        "Color",
        get_change_color_widget.__get__(Enum),
        InputColorButton,
        action_pair_change_color.__get__(Enum)
    )
    RUNTIME = (
        "Duration (s)",
        get_change_runtime_widget.__get__(Enum),
        InputTextBox,
        action_pair_fast_forward.__get__(Enum)
    )
