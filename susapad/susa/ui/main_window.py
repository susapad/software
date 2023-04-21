
import dataclasses as ds

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt


from susapad.susa.model.connection import ConnectionStatus
from .widgets import main_window


@ds.dataclass
class MainWindowState:
    connection: ConnectionStatus
    ports: list[str]
    susapad_comport: str



class MainWindow(QtWidgets.QWidget):

    def __init__(self):

        # Configuration
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self._configure_shadows()

        self.background_layer = main_window.WindowLayout(self)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.background_layer)
        self.setLayout(self.layout)


    # Action method

    @QtCore.Slot()
    def connect_susapad(self):
        pass


    # Configuration methods

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
