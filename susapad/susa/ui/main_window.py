
import dataclasses as ds
import time

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt

from susapad.susa.controler import susapad
from .widgets import main_window


class MainWindow(QtWidgets.QWidget):

    def __init__(self):

        ## Configuration
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self._configure_shadows()
        self.resize(500, 200)

        ## Attribute
        self.oldPos = None
        self.susapad = susapad.SusaPad()

        ## Configure Layout
        self.main_widget = main_window.WindowLayout(self)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.main_widget)
        self.setLayout(self.layout)

        ## Startup

    
    @QtCore.Slot()
    def connect_to_susapad(self):
        port = self.susapad.find()
        if "" == port:
            self.main_widget.group_button.main.set_found(False)
            self.main_widget.group_header.status.setText("SusaPad não encontrado!")
        else:
            self.main_widget.group_button.main.set_found(True)
            self.main_widget.group_header.status.setText(f"SusaPad encontrado na porta {port}")

    @QtCore.Slot()
    def open_settings_window(self):
        pass

    ## Style Configuration

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
