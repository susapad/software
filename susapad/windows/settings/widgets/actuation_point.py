from string import Template

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

from susapad import base_widgets as base
from susapad.controller import exception

class ActuationPointGroup(base.BaseSliderGroup):

    def __init__(self, window, susapad):
        super().__init__(window, susapad)
        self.set_range((10, 390))
        self.set_template(Template("Ponto de atuação: (${value})"))
        self._update_label()

    def update_susapad(self, value: int) -> bool:
        return self.susapad.set_actuation_point(self.reverse(value))

    @staticmethod
    def reverse(value: int) -> int:
        if 190 == value:
            return 190
        else:
            return 400 - value
