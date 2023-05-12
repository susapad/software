
from PySide6 import QtCore

from susapad import base_widgets as base


class CloseButton(base.BaseFloatingButton):

    def __init__(self, window, main_window):
        super().__init__(window, "Fechar", "Escape")

        self.main_window = main_window

    @QtCore.Slot()
    def action(self):
        self.main_window.close_settings_window()

class SaveButton(base.BaseButton):

    def __init__(self, window, main_window, susapad):
        super().__init__("Salvar", "Enter", window)
        self.susapad = susapad
        self.main_window = main_window
        self.clicked.connect(self.action)

    @QtCore.Slot()
    def action(self):
        if self.susapad.insider_save():
            self.main_window.close_settings_window()
        else:
            print("Algum problema ocorreu. Certifique-se que seu Susapad Insider está conectado.")
            self.__raise_alert()
