from PySide2.QtGui import QFont, QIcon
from PySide2.QtWidgets import QFrame, QGridLayout, QTextEdit, QWidget

from utils.path import get_path


class TheoryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFont(QFont('Arial', 12))
        self.setWindowIcon(QIcon(get_path('assets/App.ico')))
        self.setWindowTitle('Теория')
        self.init_widgets()

    def init_widgets(self):
        with open(get_path('assets/theory.txt'), 'r', encoding='utf-8') as f:
            theory = f.read()

        layout = QGridLayout()

        text = QTextEdit()
        text.setFrameStyle(QFrame.Box)
        text.setText(theory)
        text.setReadOnly(True)

        layout.addWidget(text, 0, 0)

        self.setLayout(layout)
