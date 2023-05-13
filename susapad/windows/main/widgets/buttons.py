from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

from susapad import base_widgets as base


class ActionButton(base.BaseButton):

    def __init__(self, main_window, language: dict):
        super().__init__(language["buttons"]["connect"], "Enter")
        self.language = language
        self.main_window = main_window
        self.found: bool = False
        self.set_found(main_window.susapad.serial)
        self.clicked.connect(self.action)

    def set_found(self, found: bool = True):
        if found:
            self.found = True
            self.setText(self.language["buttons"]["settings"])
        else:
            self.found = False
            self.setText(self.language["buttons"]["try-again"])

    @QtCore.Slot()
    def action(self):
        if self.found:
            self.main_window.open_settings_window()
        else:
            self.main_window.connect_to_susapad()


class CloseButton(base.BaseButton):

    def __init__(self, language):
        super().__init__(language["buttons"]["close"], "Escape")
        self.setAccessibleName("secondary")
        self.clicked.connect(self.close_application)

    @QtCore.Slot()
    def close_application(self):
        QtCore.QCoreApplication.instance().quit()
