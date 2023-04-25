from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt


class BaseWindow(QtWidgets.QWidget):

    def __init__(self, susapad, parent = None):

        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self._configure_shadows()
        self.resize(500, 200)

        self.parent = parent
        self.susapad = susapad
        self.oldPos = None

        self.layout = QtWidgets.QVBoxLayout(self)
        
    
    def _configure_shadows(self):
        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setOffset(QtCore.QPoint(0,0))
        shadow.setBlurRadius(30)
        shadow.setColor(QtGui.QColor(0,0,0))
        self.setGraphicsEffect(shadow)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.oldPos is not None:
            delta = event.globalPos() - self.oldPos
            self.move(self.pos() + delta)
            self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.oldPos = None
