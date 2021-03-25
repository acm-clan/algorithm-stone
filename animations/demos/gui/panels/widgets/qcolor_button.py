from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPushButton, QColorDialog


class QColorButton(QPushButton):
    """
    Custom Qt Widget to show a chosen color.
    """

    colorChanged = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._style = 'border-style: outset;' \
            'border-width: 1px;'  \
            'border-radius: 20;'  \
            'border-color: black'
        self._color = None
        self.setMaximumWidth(32)
        self.pressed.connect(self.on_color_picker)
        self.setStyleSheet(self._style)

    def set_color(self, color):
        if color != self._color:
            self._color = color
            self.colorChanged.emit()

        if self._color:
            self.setStyleSheet(f'{self._style}; background-color: {self._color};')

    def get_color(self):
        return self._color

    # Show color picker dialog to select color
    def on_color_picker(self):
        dlg = QColorDialog()
        if self._color:
            dlg.setCurrentColor(QColor(self._color))

        if dlg.exec_():
            self.set_color(dlg.currentColor().name())

    def mouse_press_event(self, event):
        return self.mouse_press_event(event)
