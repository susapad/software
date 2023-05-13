
import serial
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt

from susapad import base_widgets as base

from . import widgets


class SettingsWindow(base.BaseWindow):

    def __init__(self, parent, language: dict):
        super().__init__(parent.susapad, parent)

        self.settings_widget = widgets.WindowLayout(self, parent, self.susapad, language)
        self.layout.addWidget(self.settings_widget)

        self.close_button = widgets.CloseButton(self, parent, language)
        self.close_button.move(420, 20)
