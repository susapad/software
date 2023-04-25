
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt 

from susapad.susa.ui import alert_dialog


class RapidTriggerButton(QtWidgets.QPushButton):

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
        try:
            # TODO: enable this for production
            self.susapad.serial.write('rt 1'.encode())
            self.susapad.serial.flush()
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
        except:
            print("Algum problema ocorreu. Certifique-se que seu Susapad está conectado.")
            self.__raise_alert()


    def __turn_off(self):
        try:
            # TODO: enable this for production
            self.susapad.serial.write('rt 0'.encode())
            self.susapad.serial.flush()
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
        except:
            print("Algum problema ocorreu. Certifique-se que seu Susapad está conectado.")
            self.__raise_alert()
    

    @QtCore.Slot()
    def rapid_trigger(self):
        if self.on:
            self.__turn_off()
        else:
            self.__turn_on()
