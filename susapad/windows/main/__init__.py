
import dataclasses as ds
import time

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from susapad.controller import susapad, exception
from susapad.windows import settings, insider
from susapad.windows.main import widgets
from susapad import base_widgets as base


class MainWindow(base.BaseWindow):

    def __init__(self, susapad, language: dict):

        ## Configuration
        super().__init__(susapad)

        self.settings_window = None
        self.susapad = susapad
        self.language = language

        ## Configure Layout
        self.main_widget = widgets.WindowLayout(self, self.language)
        self.layout.addWidget(self.main_widget)

        ## Startup
        self.connect_to_susapad()


    @QtCore.Slot()
    def connect_to_susapad(self):
        port = "COM5" if self.susapad.debug else self.susapad.find()
        if "" == port:
            self.main_widget.group_button.main.set_found(False)
            self.main_widget.group_header.status.setText(
                self.language["status"]["not-found"])
            exception.susapad_not_found(self, self.language["error"]["not-found"])
        else:
            if not self.susapad.debug:
                self.susapad.connect(port)

            self.main_widget.group_button.main.set_found(True)
            if self.susapad.insider:
                self.main_widget.group_header.status.setText(
                    self.language["status"]["insider-connected"].format(port = port))
            else:
                self.main_widget.group_header.status.setText(
                    self.language["status"]["connected"].format(port = port))

    @QtCore.Slot()
    def open_settings_window(self):
        if self.susapad.insider and not self.settings_window:
            self.settings_window = insider.SettingsWindow(self, self.language)
            self.settings_window.show()
        elif not self.settings_window:
            self.settings_window = settings.SettingsWindow(self, self.language)
            self.settings_window.show()

    @QtCore.Slot()
    def close_settings_window(self):
        self.settings_window.close()
        self.settings_window = None
