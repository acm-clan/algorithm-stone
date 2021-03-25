from PyQt5.QtGui import QPainter, QFontMetrics
from PyQt5.QtCore import Qt

__author__ = 'Caroline Beyne'

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *


TITLE_MAX_WIDTH = 200


class FrameLayout(QWidget):
    def __init__(self, parent=None, title=None):
        QWidget.__init__(self, parent=parent)

        self._is_collasped = True
        self._title_frame = None
        self._content, self._content_layout = (None, None)

        self._main_v_layout = QVBoxLayout(self)
        self._main_v_layout.addWidget(self.initTitleFrame(title, self._is_collasped))
        self._main_v_layout.addWidget(self.initContent(self._is_collasped))

        self.initCollapsable()

    def initTitleFrame(self, title, collapsed):
        self._title_frame = self.TitleFrame(title=title, collapsed=collapsed)

        return self._title_frame

    def initContent(self, collapsed):
        self._content = QWidget()
        self._content_layout = QVBoxLayout()

        self._content.setLayout(self._content_layout)
        self._content.setVisible(not collapsed)

        return self._content

    def addLayout(self, layout):
        self._content_layout.addLayout(layout)

    def addWidget(self, widget):
        self._content_layout.addWidget(widget)

    def initCollapsable(self):
        self._title_frame.clicked.connect(self.toggleCollapsed)

    def toggleCollapsed(self):
        self._content.setVisible(self._is_collasped)
        self._is_collasped = not self._is_collasped
        self._title_frame._arrow.setArrow(int(self._is_collasped))


    ############################
    #           TITLE          #
    ############################
    class TitleFrame(QFrame):
        clicked = QtCore.pyqtSignal()

        def __init__(self, parent=None, title="", collapsed=False):
            QFrame.__init__(self, parent=parent)

            self.setMinimumHeight(24)
            self.move(QtCore.QPoint(24, 0))
            self.setStyleSheet("border:1px solid rgb(41, 41, 41); ")

            self._hlayout = QHBoxLayout(self)
            self._hlayout.setContentsMargins(0, 0, 0, 0)
            self._hlayout.setSpacing(0)

            self._arrow = None
            self._title = None

            self._hlayout.addWidget(self.initArrow(collapsed))
            self._hlayout.addWidget(self.initTitle(title))

        def initArrow(self, collapsed):
            self._arrow = FrameLayout.Arrow(collapsed=collapsed)
            self._arrow.setStyleSheet("border:0px")

            return self._arrow

        def initTitle(self, title=None):
            self._title = ElidedLabel(title)
            self._title.setMaximumWidth(TITLE_MAX_WIDTH)
            self._title.setMinimumHeight(24)
            self._title.move(QtCore.QPoint(24, 0))
            self._title.setStyleSheet("border:0px")

            return self._title

        def mousePressEvent(self, event):
            self.clicked.emit()

            return super(FrameLayout.TitleFrame, self).mousePressEvent(event)


    #############################
    #           ARROW           #
    #############################
    class Arrow(QFrame):
        def __init__(self, parent=None, collapsed=False):
            QFrame.__init__(self, parent=parent)

            self.setMaximumSize(24, 24)

            # horizontal == 0
            self._arrow_horizontal = (QtCore.QPointF(7.0, 8.0), QtCore.QPointF(17.0, 8.0), QtCore.QPointF(12.0, 13.0))
            # vertical == 1
            self._arrow_vertical = (QtCore.QPointF(8.0, 7.0), QtCore.QPointF(13.0, 12.0), QtCore.QPointF(8.0, 17.0))
            # arrow
            self._arrow = None
            self.setArrow(int(collapsed))

        def setArrow(self, arrow_dir):
            if arrow_dir:
                self._arrow = self._arrow_vertical
            else:
                self._arrow = self._arrow_horizontal

        def paintEvent(self, event):
            painter = QtGui.QPainter()
            painter.begin(self)
            painter.setBrush(QtGui.QColor(192, 192, 192))
            painter.setPen(QtGui.QColor(64, 64, 64))
            painter.drawPolygon(*self._arrow)
            painter.end()


# Extended QLabel which truncates text if it exceeds the max width of the widget
class ElidedLabel(QLabel):
    def paintEvent(self, event):
        painter = QPainter(self)

        metrics = QFontMetrics(self.font())
        elided = metrics.elidedText(self.text(), Qt.ElideRight, self.width())

        painter.drawText(self.rect(), self.alignment(), elided)
