from PySide6 import QtWidgets

_FRAME_STYLE = """
    QFrame {
        border-radius: 20px;
        background-color: #121212;
        font-size: 15px;
        color: white;
    }
"""


class BaseFrame(QtWidgets.QFrame):

    def __init__(self):
        super().__init__()

        # Configuration
        self.setObjectName("background-frame")
        self.setStyleSheet(_FRAME_STYLE)
        self.setContentsMargins(20, 20, 20, 20)
