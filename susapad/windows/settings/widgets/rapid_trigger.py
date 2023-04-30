
import time

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt 

from susapad.controller import exception
from susapad import base_widgets as base


class RapidTriggerButton(base.BaseToggleButton):

    def __init__(self, window, susapad):
        super().__init__(window, susapad)

    def command_on(self):
        return self.susapad.set_rapid_trigger(True)

    def command_off(self):
        return self.susapad.set_rapid_trigger(False)


class ContinuousRapidTriggerButton(base.BaseToggleButton):

    def __init__(self, window, susapad):
        super().__init__(window, susapad)

    def command_on(self):
        return self.susapad.set_continuous_rapid_trigger(True)

    def command_off(self):
        return self.susapad.set_continuous_rapid_trigger(False)
