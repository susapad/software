
# import time

# from PySide6 import QtWidgets, QtCore
# from PySide6.QtCore import Qt

# from susapad.controller import exception
# from susapad import base_widgets as base


# class TriggerButton(base.BaseToggleButton):

#     def __init__(self, window, susapad):
#         super().__init__(window, susapad)
#         self.susapad = susapad
#         self.turn_on()

#     def command_on(self) -> bool:
#         return self.susapad.set_trigger(True)

#     def command_off(self) -> bool:
#         return self.susapad.set_trigger(False)


# class RapidTriggerButton(base.BaseToggleButton):

#     def __init__(self, window, susapad):
#         super().__init__(window, susapad)
#         self.susapad = susapad
#         self.turn_on()

#     def command_on(self) -> bool:
#         return self.susapad.set_rapid_trigger(True)

#     def command_off(self) -> bool:
#         return self.susapad.set_rapid_trigger(False)


# class ContinuousRapidTriggerButton(base.BaseToggleButton):

#     def __init__(self, window, susapad):
#         super().__init__(window, susapad)
#         self.susapad = susapad
#         self.turn_on()

#     def command_on(self) -> bool:
#         return self.susapad.set_continuous_rapid_trigger(True)

#     def command_off(self) -> bool:
#         return self.susapad.set_continuous_rapid_trigger(False)



import time

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt

from susapad.window import alert as alert_dialog
from susapad.base_widgets import button


TOGGLERS_STYLE = """
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

    QPushButton[accessibleName="off"] {
        background-color: #b71970;
    }

    QPushButton:hover[accessibleName="off"] {
        background-color: #dd1e87;
    }
"""


class TriggerButton(button.BaseButton):

    def __init__(self, window, susapad):
        super().__init__("Desativar", None)
        self.setFixedSize(100, 30)

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
        if self.susapad.set_trigger(True):
            self.on = True
            self.setAccessibleName("on")
            self.setText("Desligar")
            self.setStyleSheet(TOGGLERS_STYLE)
        else:
            print("Algum problema ocorreu. Certifique-se que seu Susapad está conectado.")
            self.__raise_alert()


    def __turn_off(self):
        if self.susapad.set_trigger(False):
            self.on = False
            self.setAccessibleName("off")
            self.setText("Ligar")
            self.setStyleSheet(TOGGLERS_STYLE)
        else:
            print("Algum problema ocorreu. Certifique-se que seu Susapad está conectado.")
            self.__raise_alert()


    @QtCore.Slot()
    def rapid_trigger(self):
        if self.on:
            self.__turn_off()
        else:
            self.__turn_on()


class RapidTriggerButton(button.BaseButton):

    def __init__(self, window, susapad):
        super().__init__("Desativar", None)
        self.setFixedSize(100, 30)

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
        if self.susapad.set_rapid_trigger(True):
            self.on = True
            self.setAccessibleName("on")
            self.setText("Desligar")
            self.setStyleSheet(TOGGLERS_STYLE)
        else:
            print("Algum problema ocorreu. Certifique-se que seu Susapad está conectado.")
            self.__raise_alert()


    def __turn_off(self):
        if self.susapad.set_rapid_trigger(False):
            self.on = False
            self.setAccessibleName("off")
            self.setText("Ligar")
            self.setStyleSheet(TOGGLERS_STYLE)
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
        self.setFixedSize(100, 30)

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
        if self.susapad.set_continuous_rapid_trigger(True):
            self.on = True
            self.setAccessibleName("on")
            self.setText("Desligar")
            self.setStyleSheet(TOGGLERS_STYLE)
        else:
            print("Algum problema ocorreu. Certifique-se que seu Susapad está conectado.")
            self.__raise_alert()


    def __turn_off(self):
        if self.susapad.set_continuous_rapid_trigger(False):
            self.on = False
            self.setAccessibleName("off")
            self.setText("Ligar")
            self.setStyleSheet(TOGGLERS_STYLE)
        else:
            print("Algum problema ocorreu. Certifique-se que seu Susapad está conectado.")
            self.__raise_alert()


    @QtCore.Slot()
    def rapid_trigger(self):
        if self.on:
            self.__turn_off()
        else:
            self.__turn_on()
