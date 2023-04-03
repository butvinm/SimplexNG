from PySide2.QtWidgets import QGridLayout, QTabWidget, QWidget
from widgets.graph_tab import GraphTab
from widgets.task_tab import TaskTab


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_widgets()

    def init_widgets(self):
        layout = QGridLayout()

        tab = QTabWidget(self)

        self.task_tab = TaskTab(self)
        tab.addTab(self.task_tab, 'Решение')

        self.graph_tab = GraphTab()
        tab.addTab(self.graph_tab, 'График')

        layout.addWidget(tab, 0, 0)

        self.setLayout(layout)
