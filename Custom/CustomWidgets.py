from PyQt5 import QtWidgets, QtGui, QtCore
from pathlib import Path

import os


class CustomLabel(QtWidgets.QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setMinimumSize(QtCore.QSize(50, 50))

    def setup(self):
        self.setPixmap(self.pixmap_idle.scaled(self.width(), self.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.layout.addWidget(self)

    def resizeEvent(self, event):
        self.setPixmap(self.pixmap_idle.scaled(self.width(), self.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.main_window.map_path.resize_text_path()
        self.main_window.osr_path.resize_text_path()


class CustomButtons(QtWidgets.QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setMinimumSize(QtCore.QSize(50, 50))

    def setup(self):
        self.setPixmap(self.pixmap_idle.scaled(self.width(), self.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.layout.addWidget(self)

    def enterEvent(self, event):
        self.setPixmap(self.pixmap_hover.scaled(self.width(), self.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def leaveEvent(self, event):
        self.setPixmap(self.pixmap_idle.scaled(self.width(), self.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def mouseReleaseEvent(self, event):
        self.setPixmap(self.pixmap_idle.scaled(self.width(), self.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def mousePressEvent(self, event):
        self.setPixmap(self.pixmap_clicked.scaled(self.width(), self.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        home_dir = str(Path.home())
        if self.file_extension is not None:
            if self.file_extension == "folder":
                beatmap_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Beatmap Folder ', home_dir)
                print(beatmap_path)
            elif self.file_extension == ".osr":
                replay_path = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open file', home_dir, ".osr (*.osr)")
                print(replay_path)

    def resizeEvent(self, event):
        self.setPixmap(self.pixmap_idle.scaled(self.width(), self.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))


    '''
    def resize(self):
        scale = self.main_window.height() / 469

        x = self.default_coordinates[0] * scale
        y = self.default_coordinates[1] * scale

        width = self.default_scale[0] * scale
        height = self.default_scale[1] * scale


        _pixmap = QtGui.QPixmap(self.pixmap_idle)
        self.setPixmap(_pixmap.scaled(
            width, height,
            QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.setGeometry(x, y, width, height)
        '''



