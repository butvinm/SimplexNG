from PySide2.QtGui import QFont, QIcon
from PySide2.QtWidgets import QFrame, QGridLayout, QTextEdit, QWidget

from utils.path import get_path


class TheoryWindow(QWidget):
    """A window to display text of a theory file.

    Attributes:
        None

    Methods:
        __init__(): Initializes the window with the necessary settings.
        init_widgets(): Initializes the window's widgets and their layout.
    """

    def __init__(self):
        """Initializes the window with the necessary settings."""
        super().__init__()
        # Set the font for the text in the window.
        self.setFont(QFont('Arial', 12))
        # Set the icon for the window.
        self.setWindowIcon(QIcon(get_path('assets/icon.ico')))
        # Set the title for the window.
        self.setWindowTitle('Теория')
        # Initialize the widgets for the window.
        self.init_widgets()

    def init_widgets(self):
        """Initializes the window's widgets and their layout."""
        # Open the theory file and read its contents.
        with open(get_path('assets/theory.txt'), 'r', encoding='utf-8') as f:
            theory = f.read()

        # Create a grid layout to place the text widget.
        layout = QGridLayout()

        # Create a text widget to display the theory text.
        text = QTextEdit()
        # Set the frame style of the text widget.
        text.setFrameStyle(QFrame.Box)
        # Set the text to display in the widget.
        text.setText(theory)
        # Set the text widget to read-only.
        text.setReadOnly(True)

        # Add the text widget to the grid layout.
        layout.addWidget(text, 0, 0)

        # Set the layout for the window.
        self.setLayout(layout)
