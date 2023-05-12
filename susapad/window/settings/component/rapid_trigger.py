from __feature__ import true_property
from __feature__ import snake_case

import time

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt

from susapad import widget


class TriggerButton(widget.BaseToggleButton):

    def __init__(self, window, susapad):
        super().__init__("Desativar")
        self.susapad = susapad
        self.window = window

        self.text_on = "Desativar"
        self.text_off = "Ativar"

        self.clicked.connect(self.toggle)
        self.turn_on()

    def turn_on(self):
        if self.susapad.set_trigger(True):
            self._turn_on()
        else:
            self.error(self.window)

    def turn_off(self):
        if self.susapad.set_trigger(False):
            self._turn_off()
        else:
            self.error(self.window)

    @QtCore.Slot()
    def toggle(self):
        if self.on:
            self.turn_off()
        else:
            self.turn_on()


class RapidTriggerButton(widget.BaseToggleButton):

    def __init__(self, window, susapad):
        super().__init__()
        self.susapad = susapad
        self.window = window

        self.text_on = "Desativar"
        self.text_off = "Ativar"

        self.clicked.connect(self.toggle)
        self.turn_on()

    def turn_on(self):
        if self.susapad.set_rapid_trigger(True):
            self._turn_on()
        else:
            self.error(self.window)

    def turn_off(self):
        if self.susapad.set_rapid_trigger(False):
            self._turn_off()
        else:
            self.error(self.window)

    @QtCore.Slot()
    def toggle(self):
        if self.on:
            self.turn_off()
        else:
            self.turn_on()


class ContinuousRapidTriggerButton(widget.BaseToggleButton):

    def __init__(self, window, susapad):
        super().__init__()
        self.susapad = susapad
        self.window = window

        self.text_on = "Desativar"
        self.text_off = "Ativar"

        self.clicked.connect(self.toggle)
        self.turn_on()

    def turn_on(self):
        if self.susapad.set_continuous_rapid_trigger(True):
            self._turn_on()
        else:
            self.error(self.window)

    def turn_off(self):
        if self.susapad.set_continuous_rapid_trigger(False):
            self._turn_off()
        else:
            self.error(self.window)

    @QtCore.Slot()
    def toggle(self):
        if self.on:
            self.turn_off()
        else:
            self.turn_on()
