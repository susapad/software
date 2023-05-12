from __feature__ import true_property
from __feature__ import snake_case

from string import Template

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

from susapad import widget
from susapad.controller import exception

class ActuationPointGroup(widget.BaseSliderGroup):

    def __init__(self, susapad):
        super().__init__(vertical = True)

        self.susapad = susapad

        self.set_range((10, 390))
        self.template = Template("Ponto de atuação: (${value})")
        self._update_label()

    def update_susapad(self, value: int) -> bool:
        return self.susapad.set_actuation_point(self.reverse(value))

    @staticmethod
    def reverse(value: int) -> int:
        if 190 == value:
            return 190
        else:
            return 400 - value
