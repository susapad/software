
import time

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt 

from susapad.susa.ui import alert_dialog


class RapidTriggerButton(button.BaseButton):

    def __init__(self, window, susapad):
        super().__init__("Desativar", None)
        self.setFixedSize(100, 40)

        self.susapad = susapad
        self.window = window
        self.on = True

        self.clicked.connect(self.rapid_trigger)
        self.setCursor(Qt.PointingHandCursor)
        self.__turn_on()


    def __raise_alert(self):
        alert = alert_dialog.AlertDialog(self.window)
        alert.show()
        self.window.close()


    def __turn_on(self):
        if not self.susapad.set_rapid_trigger(True):
            self.on = True
            self.accessibleName = "on"
            self.setText("Desligar")
            self.setStyleSheet(
                """
                QPushButton {
                    background-color: #0e639e;
                    border-radius: 15px;
                    min-width: 10em;
                    padding: 6px;
                    font: bold;
                    color: white;
                }

                QPushButton:hover {
                    background-color: #127ecb;
                }
                """
            )
        else:
            print("Algum problema ocorreu. Certifique-se que seu Susapad está conectado.")
            self.__raise_alert()


    def __turn_off(self):
        if not self.susapad.set_rapid_trigger(False):
            self.on = False
            self.accessibleName = "off"
            self.setText("Ligar")
            self.setStyleSheet(
                """
                QPushButton {
                    background-color: #b71970;
                    border-radius: 15px;
                    min-width: 10em;
                    padding: 6px;
                    font: bold;
                    color: white;
                }

                QPushButton:hover {
                    background-color: #dd1e87;
                }
                """
            )
        else:
            print("Algum problema ocorreu. Certifique-se que seu Susapad está conectado.")
            self.__raise_alert()
    

    @QtCore.Slot()
    def rapid_trigger(self):
        if self.on:
            self.__turn_off()
        else:
            self.__turn_on()


class ContinuousRapidTriggerButton(button.BaseButton):

    def __init__(self, window, susapad):
        super().__init__("Desativar", None)
        self.setFixedSize(100, 40)

        self.susapad = susapad
        self.window = window
        self.on = True

        self.clicked.connect(self.rapid_trigger)
        self.setCursor(Qt.PointingHandCursor)
        self.__turn_on()


    def __raise_alert(self):
        alert = alert_dialog.AlertDialog(self.window)
        alert.show()
        self.window.close()


    def __turn_on(self):
        if not self.susapad.set_rapid_trigger(True):
            self.on = True
            self.accessibleName = "on"
            self.setText("Desligar")
            self.setStyleSheet(
                """
                QPushButton {
                    background-color: #0e639e;
                }

                QPushButton:hover {
                    background-color: #127ecb;
                }
                """
            )
        else:
            print("Algum problema ocorreu. Certifique-se que seu Susapad está conectado.")
            self.__raise_alert()


    def __turn_off(self):
        if not self.susapad.set_rapid_trigger(False):
            self.on = False
            self.accessibleName = "off"
            self.setText("Ligar")
            self.setStyleSheet(
                """
                QPushButton {
                    background-color: #b71970;
                }

                QPushButton:hover {
                    background-color: #dd1e87;
                }
                """
            )
        else:
            print("Algum problema ocorreu. Certifique-se que seu Susapad está conectado.")
            self.__raise_alert()
    

    @QtCore.Slot()
    def rapid_trigger(self):
        if self.on:
            self.__turn_off()
        else:
            self.__turn_on()
