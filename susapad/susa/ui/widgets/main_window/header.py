
from PySide6 import QtWidgets, QtGui

class SusaPadLogo(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()
        self.setPixmap(QtGui.QPixmap("susapad/media/logo.png"))



class SusaPadTitle(QtWidgets.QLabel):

    def __init__(self):
        super().__init__("SusaPad")
        self.setStyleSheet(
            """
                color: white;
                font: 24px;
            """
        )
