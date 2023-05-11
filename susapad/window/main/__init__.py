
import dataclasses as ds
import time

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from susapad.controller import susapad, exception
from susapad.window import settings
from susapad.window.main import component
from susapad import base_widgets as base

from . import ui


class MainWindow(base.BaseWindow):

    def __init__(self, susapad):
        super().__init__(susapad)

        self.settings_window = None
        self.susapad = susapad

        self.init_widgets()
        self.init_layout()

        self.connect_to_susapad()

    def init_widgets(self):
        self.ui = ui.MainUI(self)

    def init_layout(self):
        self.layout.addWidget(self.ui)


    @QtCore.Slot()
    def connect_to_susapad(self):
        port = "COM5" if self.susapad.debug else self.susapad.find()
        if "" == port:
            self.ui.main_button.set_found(False)
            self.ui.susapad_status.setText("SusaPad não encontrado!")
            exception.susapad_not_found(self)
        else:
            if not self.susapad.debug:
                self.susapad.connect(port)
            self.ui.main_button.set_found(True)
            self.ui.susapad_status.setText(f"SusaPad encontrado na porta {port}")

    @QtCore.Slot()
    def open_settings_window(self):
        if not self.settings_window:
            self.settings_window = settings.SettingsWindow(self)
            self.settings_window.show()

    @QtCore.Slot()
    def close_settings_window(self):
        self.settings_window.close()
        self.settings_window = None
