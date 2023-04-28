
import time

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt 

from susapad.controler import exception
from susapad import base_widgets as base


class RapidTriggerButton(base.BaseButton):

    def __init__(self, window, susapad):
        super().__init__("Desativar", None)
        self.setFixedSize(100, 30)

        self.susapad = susapad
        self.window = window
        self.on = True

        self.clicked.connect(self.rapid_trigger)
        self.setCursor(Qt.PointingHandCursor)
        self.__turn_on()


    def __turn_on(self):
        if self.susapad.set_rapid_trigger(True):
            self.on = True
            self.setAccessibleName("on")
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
            exception.susapad_not_found(self.window)
            exception.close_current_window(self.window)


    def __turn_off(self):
        if self.susapad.set_rapid_trigger(False):
            self.on = False
            self.setAccessibleName("off")
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
            exception.susapad_not_found(self.window)
            exception.close_current_window(self.window)
    

    @QtCore.Slot()
    def rapid_trigger(self):
        if self.on:
            self.__turn_off()
        else:
            self.__turn_on()


class ContinuousRapidTriggerButton(base.BaseButton):

    def __init__(self, window, susapad):
        super().__init__("Desativar", None)
        self.setFixedSize(100, 30)

        self.susapad = susapad
        self.window = window
        self.on = True

        self.clicked.connect(self.rapid_trigger)
        self.setCursor(Qt.PointingHandCursor)
        self.__turn_on()

    def __turn_on(self):
        if self.susapad.set_continuous_rapid_trigger(True):
            self.on = True
            self.setAccessibleName("on")
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
            exception.susapad_not_found(self.window)
            exception.close_current_window(self.window)


    def __turn_off(self):
        if self.susapad.set_continuous_rapid_trigger(False):
            self.on = False
            self.setAccessibleName("off")
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
            exception.susapad_not_found(self.window)
            exception.close_current_window(self.window)
    

    @QtCore.Slot()
    def rapid_trigger(self):
        if self.on:
            self.__turn_off()
        else:
            self.__turn_on()
