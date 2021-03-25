# pylint: disable=no-name-in-module
# pylint: disable=import-error
# Known issue where CI runner cannot import QtMultimedia, QtMultimediaWidgets.
# No solution possible on user side.

from PyQt5.QtCore import Qt, QUrl, QSizeF
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QGraphicsVideoItem
from PyQt5.QtWidgets import *

# 16:9 ratio
VIDEO_WIDTH_RATIO = 16
VIDEO_HEIGHT_RATIO = 9

VIDEO_BASE_WIDTH = 640
VIDEO_BASE_HEIGHT = 360

VIEW_OFFSET = 5


class VideoPlayerWidget(QWidget):
    def __init__(self, position_changed_callback=None, parent=None):
        super().__init__(parent)

        self.video_fp = ""
        self.position_changed_callback = position_changed_callback

        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # Supporting infrastructure to display media player
        video_item = QGraphicsVideoItem()
        video_item.setSize(QSizeF(VIDEO_BASE_WIDTH, VIDEO_BASE_HEIGHT))

        scene = QGraphicsScene(self)
        scene.addItem(video_item)

        graphics_view = QGraphicsView(scene)
        # Offset prevents scrollbars from appearing on video window
        graphics_view.setMinimumSize(VIDEO_BASE_WIDTH + VIEW_OFFSET,
                                     VIDEO_BASE_HEIGHT + VIEW_OFFSET)
        # Ensure view scales up in increments of 16:9 ratio
        graphics_view.setBaseSize(VIDEO_BASE_WIDTH, VIDEO_BASE_HEIGHT)
        graphics_view.setSizeIncrement(VIDEO_WIDTH_RATIO, VIDEO_HEIGHT_RATIO)

        # Play button
        self.play_button = QPushButton()
        self.play_button.setEnabled(False)
        self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.play_button.clicked.connect(self.play)

        # Video scrubber
        self.position_slider = QSlider(Qt.Horizontal)
        self.position_slider.setRange(0, 0)
        self.position_slider.valueChanged.connect(self.slider_position_changed)

        self.error_label = QLabel()
        self.error_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # Wire up media player
        self.media_player.setVideoOutput(video_item)
        self.media_player.stateChanged.connect(self.media_state_changed)
        self.media_player.positionChanged.connect(self.media_position_changed)
        self.media_player.durationChanged.connect(self.media_duration_changed)
        self.media_player.error.connect(self.handle_error)

        # Arrange video controls
        control_layout = QHBoxLayout()
        control_layout.addWidget(self.play_button)
        control_layout.addWidget(self.position_slider)

        # Arrange widget contents
        main_layout = QVBoxLayout()
        main_layout.addWidget(graphics_view)
        main_layout.addLayout(control_layout)
        main_layout.addWidget(self.error_label)

        self.setLayout(main_layout)

    # Display the video stored at video_fp
    def open_video(self, video_fp):
        self.video_fp = video_fp
        self.media_player.setMedia(
            QMediaContent(QUrl.fromLocalFile(str(self.video_fp))))

        # Enable play button and un-grey it
        self.play_button.setEnabled(True)
        self.play_button.setStyleSheet("QPushButton::enabled")

        # Show first scene of video
        self.media_player.play()
        self.media_player.pause()

    def play(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()

    def slider_position_changed(self, position):
        self.set_media_position(position)

    def media_state_changed(self, state):
        del state  # unused

        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.play_button.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.play_button.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))

    def set_media_position(self, position):
        self.media_player.setPosition(position)

    def media_position_changed(self, position):
        self.position_changed_callback(position)
        self.position_slider.blockSignals(True)
        self.position_slider.setValue(position)
        self.position_slider.blockSignals(False)

    def media_duration_changed(self, duration):
        self.position_slider.setRange(0, duration)

    def handle_error(self):
        self.play_button.setEnabled(False)
        self.error_label.setText("Error: " + self.media_player.errorString())
