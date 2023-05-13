
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt

from susapad.windows import alert as alert_dialog
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

    def __init__(self, window, susapad, language: dict):
        super().__init__(language["buttons"]["turn-off"], None)
        self.setFixedSize(100, 30)
        self.language = language

        self.susapad = susapad
        self.window = window
        self.on = True

        self.clicked.connect(self.rapid_trigger)
        self.setCursor(Qt.PointingHandCursor)
        self.__turn_on()


    def __raise_alert(self):
        alert = alert_dialog.AlertDialog(self.window, self.language["error"]["not-found"])
        alert.show()
        self.window.close()


    def __turn_on(self):
        if self.susapad.set_trigger(True):
            self.on = True
            self.setAccessibleName("on")
            self.setText(self.language["buttons"]["turn-off"])
            self.setStyleSheet(TOGGLERS_STYLE)
        else:
            self.__raise_alert()


    def __turn_off(self):
        if self.susapad.set_trigger(False):
            self.on = False
            self.setAccessibleName("off")
            self.setText(self.language["buttons"]["turn-on"])
            self.setStyleSheet(TOGGLERS_STYLE)
        else:
            self.__raise_alert()


    @QtCore.Slot()
    def rapid_trigger(self):
        if self.on:
            self.__turn_off()
        else:
            self.__turn_on()


class RapidTriggerButton(button.BaseButton):

    def __init__(self, window, susapad, language: dict):
        super().__init__(language["buttons"]["turn-off"], None)
        self.setFixedSize(100, 30)
        self.language = language

        self.susapad = susapad
        self.window = window
        self.on = True

        self.clicked.connect(self.rapid_trigger)
        self.setCursor(Qt.PointingHandCursor)
        self.__turn_on()


    def __raise_alert(self):
        alert = alert_dialog.AlertDialog(self.window, self.language["error"]["not-found"])
        alert.show()
        self.window.close()


    def __turn_on(self):
        if self.susapad.set_rapid_trigger(True):
            self.on = True
            self.setAccessibleName("on")
            self.setText(self.language["buttons"]["turn-off"])
            self.setStyleSheet(TOGGLERS_STYLE)
        else:
            self.__raise_alert()


    def __turn_off(self):
        if self.susapad.set_rapid_trigger(False):
            self.on = False
            self.setAccessibleName("off")
            self.setText(self.language["buttons"]["turn-on"])
            self.setStyleSheet(TOGGLERS_STYLE)
        else:
            self.__raise_alert()


    @QtCore.Slot()
    def rapid_trigger(self):
        if self.on:
            self.__turn_off()
        else:
            self.__turn_on()


class ContinuousRapidTriggerButton(button.BaseButton):

    def __init__(self, window, susapad, language: dict):
        super().__init__(language["buttons"]["turn-off"], None)
        self.setFixedSize(100, 30)
        self.language = language

        self.susapad = susapad
        self.window = window
        self.on = True

        self.clicked.connect(self.rapid_trigger)
        self.setCursor(Qt.PointingHandCursor)
        self.__turn_on()


    def __raise_alert(self):
        alert = alert_dialog.AlertDialog(self.window, self.language["error"]["not-found"])
        alert.show()
        self.window.close()


    def __turn_on(self):
        if self.susapad.set_continuous_rapid_trigger(True):
            self.on = True
            self.setAccessibleName("on")
            self.setText(self.language["buttons"]["turn-off"])
            self.setStyleSheet(TOGGLERS_STYLE)
        else:
            self.__raise_alert()


    def __turn_off(self):
        if self.susapad.set_continuous_rapid_trigger(False):
            self.on = False
            self.setAccessibleName("off")
            self.setText(self.language["buttons"]["turn-on"])
            self.setStyleSheet(TOGGLERS_STYLE)
        else:
            self.__raise_alert()


    @QtCore.Slot()
    def rapid_trigger(self):
        if self.on:
            self.__turn_off()
        else:
            self.__turn_on()
