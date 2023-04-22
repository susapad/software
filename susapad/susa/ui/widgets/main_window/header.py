"""Common Widgets used by `MainWindow`"""

from PySide6 import QtWidgets, QtGui, QtCore


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


class StatusLabel(QtWidgets.QLabel):

    def __init__(self, window):
        super().__init__()
        self.__init_style()
        
        self.set_found(window.susapad.serial)


    def set_found(self, found: bool = True):
        if found:
            self.setText("SusaPad encontrado!")
        else:
            self.setText("SusaPad não encontrado!")

    def __init_style(self):
        self.setStyleSheet("font: 12px; color: white;")
