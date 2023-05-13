from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from susapad import base_widgets as base

from .rapid_trigger import RapidTriggerButton
from .hysteresis    import HysteresisGroup
from .sensibility   import SensiblitySlidersGroup
from .buttons       import CloseButton, SaveButton

_SETTINGS_STYLE = """
    QLabel {
        color: white;
        font: 16px;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    QLabel#first-h2 {
        margin-top: 0px;
    }

    QPushButton {
        margin-left: 20px;
    }
"""


class WindowLayout(base.BaseFrame):

    def __init__(self, window, main_window, susapad, language: dict):
        super().__init__()

        # Configure Style
        self.setStyleSheet(self.styleSheet() + _SETTINGS_STYLE)

        # Configure Layout

        self.rt_label = QtWidgets.QLabel(language["default-config"]["rapid-trigger"])
        self.rt_label.setObjectName("first-h2")
        self.rt_button = RapidTriggerButton(window, susapad, language)

        self.sensibility_slider = SensiblitySlidersGroup(window, susapad, language)
        self.hysteresis_slider = HysteresisGroup(window, susapad, language)
        self.save_button = SaveButton(window, main_window, susapad, language)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.rt_label)
        self.layout.addWidget(self.rt_button)
        self.layout.addWidget(self.sensibility_slider)
        self.layout.addWidget(self.hysteresis_slider)
        self.layout.addWidget(self.save_button)
