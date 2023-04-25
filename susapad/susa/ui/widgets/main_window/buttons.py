from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt

from susapad.susa.ui.widgets.common import button


class ActionButton(button.BaseButton):

    def __init__(self, window):
        super().__init__("Conectar", "Enter")
        self.window = window
        self.found: bool = False
        self.set_found(window.susapad.serial)
        self.clicked.connect(self.action)

    def set_found(self, found: bool = True):
        if found:
            self.found = True
            self.setText("Configurar")
        else:
            self.found = False
            self.setText("Tentar novamente!")

    @QtCore.Slot()
    def action(self):
        if self.found:
            self.window.open_settings_window()
        else:
            self.window.connect_to_susapad()


class CloseButton(button.BaseButton):

    def __init__(self):
        super().__init__("Fechar", "Escape")
        self.setAccessibleName("secondary")
        self.clicked.connect(self.close_application)

    @QtCore.Slot()
    def close_application(self):
        QtCore.QCoreApplication.instance().quit()
