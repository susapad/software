from __feature__ import true_property
from __feature__ import snake_case

from string import Template

from PySide6 import QtWidgets, QtCore

from . import _base_labeled, _group_qss


class DoubleSlider(QtWidgets.QWidget):

    def __init__(self,
            template: str = "${value1}, ${value2}",
            range: tuple[int, int] = (0, 100)):

        super().__init__()
        self.vertical = False
        self.template = Template(template)
        self._init_widgets()
        self.set_range(range)
        self._init_layout()
        self._init_configuration()

    def _init_widgets(self):
        self.title = QtWidgets.QLabel()
        self.group1 = _base_labeled.BaseLabeledSlider(self.vertical)
        self.group2 = _base_labeled.BaseLabeledSlider(self.vertical)
        self.group1.slider.valueChanged.connect(self.update_label)
        self.group2.slider.valueChanged.connect(self.update_label)

    def _init_layout(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.add_widget(self.title)
        layout.add_widget(self.group1)
        layout.add_widget(self.group2)
        layout.contents_margins = QtCore.QMargins(0, 0, 0, 0)
        self.layout = layout

    def _init_configuration(self):
        self.accessible_name  = "group"
        self.style_sheet = _group_qss.GROUP_STYLE

    def set_range(self, value: tuple[int, int]):
        assert value[0] < value[1]
        self.group1.slider.minimum = value[0]
        self.group2.slider.minimum = value[0]
        self.group1.slider.maximum = value[1]
        self.group2.slider.maximum = value[1]
        self.group1.min.text = self.__in_mm(value[0])
        self.group2.min.text = self.__in_mm(value[0])
        self.group1.max.text = self.__in_mm(value[1])
        self.group2.max.text = self.__in_mm(value[1])

    # Internal functions
    @staticmethod
    def __in_mm(value: int) -> str:
        return f"{value/100}mm"

    @QtCore.Slot()
    def update_label(self):
        template = self.template.substitute(
            value1 = self.__in_mm(self.group1.slider.value),
            value2 = self.__in_mm(self.group2.slider.value))
        self.title.text = template

    def error():
        exception.susapad_not_found(self.window)
        exception.close_current_window(self.window)
