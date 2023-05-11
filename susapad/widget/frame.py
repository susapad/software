from __feature__ import true_property
from __feature__ import snake_case

from PySide6 import QtWidgets, QtCore

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
        self.object_name = "background-frame"
        self.style_sheet = _FRAME_STYLE
        self.set_contents_margins(QtCore.QMargins(20, 20, 20, 20))
