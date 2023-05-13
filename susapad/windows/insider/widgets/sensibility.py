from string import Template

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

from susapad.controller import exception
from susapad import base_widgets as base


class SensiblitySlidersGroup(base.BaseSliderGroup):

    def __init__(self, window, susapad, language: dict):
        super().__init__(window, susapad)

        self.set_template(Template(language["insider-config"]["sensibility"]))
        self.set_range((10, 400))
        self._update_label()

    @QtCore.Slot() # press
    def update_susapad(self, value: int) -> bool:
        return self.susapad.set_insider_sensibility(value)
