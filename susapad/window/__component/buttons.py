from __feature__ import true_property
from __feature__ import snake_case

from PySide6 import QtCore

from susapad import widget


class ActionButton(widget.BaseButton):

    def __init__(self, main_window):
        super().__init__("Conectar", "Enter")

        self.main_window = main_window
        self.found: bool = False
        self.set_found(main_window.susapad.serial)
        self.clicked.connect(self.action)

    def set_found(self, found: bool = True):
        if found:
            self.found = True
            self.text = "Configurar"
        else:
            self.found = False
            self.text = "Tentar novamente!"

    @QtCore.Slot()
    def action(self):
        if self.found:
            self.main_window.open_settings_window()
        else:
            self.main_window.connect_to_susapad()


class CloseButton(widget.BaseButton):

    def __init__(self):
        super().__init__("Fechar", "Escape")

        self.accessible_name = "secondary"
        self.clicked.connect(self.close_application)

    @QtCore.Slot()
    def close_application(self):
        QtCore.QCoreApplication.instance().quit()
