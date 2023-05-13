
from PySide6 import QtCore

from susapad import base_widgets as base


class CloseButton(base.BaseFloatingButton):

    def __init__(self, window, main_window, language: dict):
        super().__init__(window, language["buttons"]["close"], "Escape")

        self.main_window = main_window

    @QtCore.Slot()
    def action(self):
        self.main_window.close_settings_window()

class SaveButton(base.BaseButton):

    def __init__(self, window, main_window, susapad, language: dict):
        super().__init__(language["insider-config"]["save"], "Enter", window)
        self.susapad = susapad
        self.main_window = main_window
        self.clicked.connect(self.action)

    @QtCore.Slot()
    def action(self):
        if self.susapad.insider_save():
            self.main_window.close_settings_window()
        else:
            self.__raise_alert()
