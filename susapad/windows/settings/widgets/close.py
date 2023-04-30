
from PySide6 import QtCore

from susapad import base_widgets as base


class CloseButton(base.BaseFloatingButton):

    def __init__(self, window, main_window):
        super().__init__(window, "Fechar", "Escape")

        self.main_window = main_window

    @QtCore.Slot()
    def action(self):
        self.main_window.close_settings_window()
