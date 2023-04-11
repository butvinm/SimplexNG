from PySide2.QtGui import QFont, QIcon, QPixmap
from PySide2.QtWidgets import QGridLayout, QLabel, QWidget
from utils.path import get_path


class InfoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFont(QFont('Arial', 12))
        self.setMaximumSize(640, 480)
        self.setWindowTitle('Формат таблицы для открытия')
        self.setWindowIcon(QIcon(get_path('assets/icon.ico')))

        self.init_widgets()

    def init_widgets(self):
        layout = QGridLayout()

        title = QLabel('Формат таблицы для открытия')
        layout.addWidget(title, 0, 0)

        picture_1 = QLabel()
        picture_1.setPixmap(QPixmap(get_path('assets/pic1.jpg')))
        layout.addWidget(picture_1, 1, 0)

        picture_2 = QLabel()
        picture_2.setPixmap(QPixmap(get_path('assets/pic2.jpg')))
        layout.addWidget(picture_2, 1, 1)

        self.setLayout(layout)
