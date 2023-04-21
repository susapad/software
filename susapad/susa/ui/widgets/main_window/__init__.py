from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt

from susapad.susa.ui.widgets.main_window import buttons, header


class WindowLayout(QtWidgets.QFrame):

    def __init__(self, parent):
        super().__init__()

        # Configuration
        self.setObjectName("background-frame")
        self._init_style()

        # Elements
        self.logo            = header.SusaPadLogo()
        self.title           = header.SusaPadTitle()
        self.connect_button  = buttons.ConnectButton(self)
        self.settings_button = buttons.SettingsButton(self)
        self.close_button    = buttons.CloseButton(self)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.logo, 
                alignment = Qt.AlignCenter | Qt.AlignTop)
        self.layout.addWidget(self.title, 
                alignment = Qt.AlignCenter | Qt.AlignTop)
        self.layout.addWidget(self.connect_button, 
                alignment = Qt.AlignCenter | Qt.AlignBottom)
        self.layout.addWidget(self.settings_button, 
                alignment = Qt.AlignCenter | Qt.AlignBottom)
        self.layout.addWidget(self.close_button, 
                alignment = Qt.AlignCenter | Qt.AlignBottom)

    def _init_style(self):
        self.setStyleSheet(
            """
                border-radius: 20px;
                background-color: #121212;
            """
        )
        self.setContentsMargins(20, 20, 20, 20)
