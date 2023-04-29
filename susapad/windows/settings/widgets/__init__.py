from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from . import actuation_point, togglers, sensibility
from .close import CloseButton


class FormsGroup(QtWidgets.QWidget):

    def __init__(self, window, susapad):
        super().__init__()

        self.first_h2 = QtWidgets.QLabel("Rapid Trigger")
        self.first_h2.setObjectName("first-h2")

        self.rt_button = togglers.RapidTriggerButton(window, susapad)
        self.crt_button = togglers.ContinuousRapidTriggerButton(window, susapad)

        self.sensibility_slider = sensibility.SensiblitySlidersGroup(window, susapad)
        self.actuation_slider = actuation_point.ActuationPointGroup(window, susapad)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.first_h2)
        self.layout.addWidget(self.rt_button)
        self.layout.addWidget(QtWidgets.QLabel("Rapid Trigger Contínuo"))
        self.layout.addWidget(self.crt_button)
        self.layout.addWidget(self.sensibility_slider)
        self.layout.addWidget(self.actuation_slider)



class WindowLayout(QtWidgets.QFrame):

    def __init__(self, window, susapad):
        super().__init__()

        self.setObjectName("background-frame")
        self.__init_style()

        self.forms = FormsGroup(window, susapad)
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.forms)


    def __init_style(self):
        self.setStyleSheet(
            """

            QFrame {
                border-radius: 20px;
                background-color: #121212;
            }

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
        )
        self.setContentsMargins(20, 20, 20, 20)
