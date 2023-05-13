from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from susapad import base_widgets as base
from . import actuation_point, rapid_trigger as rt, sensibility
from .close import CloseButton

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

    def __init__(self, window, susapad, language: dict):
        super().__init__()

        # Configure Style
        self.setStyleSheet(self.styleSheet() + _SETTINGS_STYLE)

        # Configure Layout

        self.input_label = QtWidgets.QLabel(language["default-config"]["input"])
        self.input_label.setObjectName("first-h2")
        self.input_button = rt.TriggerButton(window, susapad, language)

        self.rt_label = QtWidgets.QLabel(language["default-config"]["rapid-trigger"])
        self.rt_button = rt.RapidTriggerButton(window, susapad, language)

        self.crt_label = QtWidgets.QLabel(language["default-config"]["continuous-rapid-trigger"])
        self.crt_button = rt.ContinuousRapidTriggerButton(window, susapad, language)

        self.actuation_slider = actuation_point.ActuationPointGroup(window, susapad, language)

        self.sensibility_slider = sensibility.SensiblitySlidersGroup(window, susapad, language)

        self.trigger_layout = QtWidgets.QVBoxLayout()
        self.trigger_layout.addWidget(self.input_label)
        self.trigger_layout.addWidget(self.input_button)
        self.trigger_layout.addWidget(self.rt_label)
        self.trigger_layout.addWidget(self.rt_button)
        self.trigger_layout.addWidget(self.crt_label)
        self.trigger_layout.addWidget(self.crt_button)

        self.upper_layout = QtWidgets.QHBoxLayout()
        self.upper_layout.addLayout(self.trigger_layout, 1)
        self.upper_layout.addWidget(self.actuation_slider, 1)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addLayout(self.upper_layout)
        self.layout.addWidget(self.sensibility_slider)
