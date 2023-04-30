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

    def __init__(self, window, susapad):
        super().__init__()

        # Configure Style
        self.setStyleSheet(self.styleSheet() + _SETTINGS_STYLE)

        # Configure Layout

        self.first_h2 = QtWidgets.QLabel("Rapid Trigger")
        self.first_h2.setObjectName("first-h2")

        self.rt_button = rt.RapidTriggerButton(window, susapad)
        self.crt_button = rt.ContinuousRapidTriggerButton(window, susapad)

        self.sensibility_slider = sensibility.SensiblitySlidersGroup(window, susapad)
        self.actuation_slider = actuation_point.ActuationPointGroup(window, susapad)
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.first_h2)
        self.layout.addWidget(self.rt_button)
        self.layout.addWidget(QtWidgets.QLabel("Rapid Trigger Contínuo"))
        self.layout.addWidget(self.crt_button)
        self.layout.addWidget(self.sensibility_slider)
        self.layout.addWidget(self.actuation_slider)
