from string import Template

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

from susapad import base_widgets as base
from susapad.controller import exception

class HysteresisGroup(base.BaseSliderGroup):

    def __init__(self, window, susapad):
        super().__init__(window, susapad, vertical = True)
        self.set_range((8, 380))
        self.set_template(Template("Hysteresis: (${value})"))
        self._update_label()

    def update_susapad(self, value: int) -> bool:
        return self.susapad.set_insider_hysteresis(self.reverse(value))

    @staticmethod
    def reverse(value: int) -> int:
        if 194 == value:
            return 194
        else:
            return 400 - value
