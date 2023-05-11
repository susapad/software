from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from susapad import widget
from .component import actuation_point, rapid_trigger as rt, sensibility

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


class SettingsUI(widget.BaseFrame):

    def __init__(self, window, susapad):
        super().__init__()

        # Configure Style
        self.setStyleSheet(self.styleSheet() + _SETTINGS_STYLE)
        self.init_widgets()
        self.init_layout()

    def init_widgets(self):
        self.input_label = QtWidgets.QLabel("Habilitar Input")
        self.input_label.setObjectName("first-h2")
        self.input_button = rt.TriggerButton(window, susapad)

        self.rt_label = QtWidgets.QLabel("Rapid Trigger")
        self.rt_button = rt.RapidTriggerButton(window, susapad)

        self.crt_label = QtWidgets.QLabel("Rapid Trigger Contínuo")
        self.crt_button = rt.ContinuousRapidTriggerButton(window, susapad)

        self.actuation_slider = actuation_point.ActuationPointGroup(window, susapad)

        self.sensibility_slider = sensibility.SensiblitySlidersGroup(window, susapad)

    def init_layout(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.addLayout(self.__init_upper_layout())
        layout.addWidget(self.sensibility_slider)

    def __init_upper_layout(self):

        left_layout = QtWidgets.QVBoxLayout()
        left_layout.addWidget(self.input_label)
        left_layout.addWidget(self.input_button)
        left_layout.addWidget(self.rt_label)
        left_layout.addWidget(self.rt_button)
        left_layout.addWidget(self.crt_label)
        left_layout.addWidget(self.crt_button)

        right_layout = QtWidgets.QBoxLayout()
        right_layout.addWidget(self.actuation_slider)

        upper_layout = QtWidgets.QHBoxLayout()
        upper_layout.addLayout(self.left_layout, 1)
        upper_layout.addLayout(self.right_layout, 1)

        return upper_layout
