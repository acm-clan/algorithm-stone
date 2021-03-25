from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *

from gui.custom_renderer import custom_renderer


class RenderProgressBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.progress_label = QLabel("Render progress:")

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 1)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.progress_label)
        main_layout.addWidget(self.progress_bar)

        self.setLayout(main_layout)

    def set_busy(self):
        self.progress_bar.setValue(0)
        self.progress_bar.setRange(0, 0)

    def set_idle(self):
        # Stop pulsation
        self.progress_bar.setRange(0, 1)
        self.progress_bar.setValue(1)


class VideoRenderThread(QThread):

    # pylint: disable=too-many-arguments
    # pylint: disable=broad-except

    task_finished = pyqtSignal(object)
    exceptioned = pyqtSignal(Exception)

    def __init__(self, file_path, scene_name, video_quality,
                 post_customize_fns, post_config_settings):
        super().__init__()

        self.post_config_settings = post_config_settings
        self.post_customize_fns = post_customize_fns
        self.video_quality = video_quality
        self.scene_name = scene_name
        self.file_path = file_path

    def run(self):
        try:
            scene = custom_renderer(self.file_path, self.scene_name, self.video_quality,
                                    self.post_customize_fns, self.post_config_settings)
            self.task_finished.emit(scene)
        except Exception as exception:
            self.exceptioned.emit(exception)
