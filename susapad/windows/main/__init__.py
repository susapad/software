
import dataclasses as ds
import time

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from susapad.controler import susapad
from susapad.ui import alert_dialog
from susapad.windows import settings
from susapad.windows.main import widgets
from susapad.base_widgets import window


class MainWindow(window.BaseWindow):

    def __init__(self, susapad):

        ## Configuration
        super().__init__(susapad)

        self.settings_window = None
        self.susapad = susapad

        ## Configure Layout
        self.main_widget = widgets.WindowLayout(self)
        self.layout.addWidget(self.main_widget)

        ## Startup
        self.connect_to_susapad()

    
    @QtCore.Slot()
    def connect_to_susapad(self):
        port = "COM5" if self.susapad.debug else self.susapad.find() 
        if "" == port:
            self.main_widget.group_button.main.set_found(False)
            self.main_widget.group_header.status.setText("SusaPad não encontrado!")
            
            alert = alert_dialog.AlertDialog(self)
            alert.show()
        else:
            if not self.susapad.debug:
                self.susapad.connect(port)
            self.main_widget.group_button.main.set_found(True)
            self.main_widget.group_header.status.setText(f"SusaPad encontrado na porta {port}")

    @QtCore.Slot()
    def open_settings_window(self):
        if not self.settings_window:
            self.settings_window = settings.SettingsWindow(self)
            self.settings_window.show()

    @QtCore.Slot()
    def close_settings_window(self):
        self.settings_window.close()
        self.settings_window = None
