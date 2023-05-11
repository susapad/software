from __feature__ import true_property
from __feature__ import snake_case

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt


class BaseWindow(QtWidgets.QWidget):

    def __init__(self, susapad, parent = None):

        super().__init__()
        self.set_window_flags(Qt.FramelessWindowHint)
        self.set_attribute(Qt.WA_TranslucentBackground)
        self._configure_shadows()
        self.resize(500, 200)

        self.parent = parent
        self.susapad = susapad
        self.old_pos = None

        self.layout = QtWidgets.QVBoxLayout(self)


    def _configure_shadows(self):
        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.offset = QtCore.QPoint(0,0)
        shadow.blur_radius = 30
        shadow.color = QtGui.QColor(0,0,0)
        self.graphics_effect = shadow

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.global_pos()

    def mouseMoveEvent(self, event):
        if self.old_pos is not None:
            delta = event.global_pos() - self.old_pos
            self.move(self.pos + delta)
            self.old_pos = event.global_pos()

    def mouseReleaseEvent(self, event):
        self.old_pos = None
