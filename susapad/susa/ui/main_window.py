
import dataclasses as ds
import time

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt

from susapad.susa.controler import susapad
from . import settings_window, alert_dialog
from .widgets.common import window
from .widgets import main_window


class MainWindow(window.BaseWindow):

    def __init__(self, susapad):

        ## Configuration
        super().__init__(susapad)

        ## Configure Layout
        self.main_widget = main_window.WindowLayout(self)
        self.layout.addWidget(self.main_widget)

        ## Startup
        self.connect_to_susapad()

    
    @QtCore.Slot()
    def connect_to_susapad(self):
        port = self.susapad.find()
        if "" == port:
            # Todo: set it as false for production
            self.main_widget.group_button.main.set_found(True)
            self.main_widget.group_header.status.setText("SusaPad não encontrado!")
            
            alert = alert_dialog.AlertDialog(self)
            alert.show()

        else:
            self.main_widget.group_button.main.set_found(True)
            self.main_widget.group_header.status.setText(f"SusaPad encontrado na porta {port}")

    @QtCore.Slot()
    def open_settings_window(self):
        self.settings_window = settings_window.SettingsWindow(self)
        self.settings_window.show()
