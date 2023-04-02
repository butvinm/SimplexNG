from typing import Optional

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QAbstractItemView, QGridLayout, QHeaderView,
                               QLabel, QPushButton, QTableWidget,
                               QTableWidgetItem, QWidget)
from utils.math import get_plot_points, get_max_solution, get_min_solution, get_task_data
import context

class BaseTable(QTableWidget):
    def __init__(self, rows: int, columns: int, parent: QWidget):
        super().__init__(rows, columns, parent)

        vertical_header = QHeaderView(Qt.Vertical, self)
        vertical_header.setSectionResizeMode(QHeaderView.Stretch)
        self.setHorizontalHeader(vertical_header)

        horizontal_header = QHeaderView(Qt.Horizontal, self)
        horizontal_header.setSectionResizeMode(QHeaderView.Stretch)
        self.setHorizontalHeader(horizontal_header)

        self.clear_data()

    def clear_data(self):
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                self.setItem(i, j, QTableWidgetItem(''))


class TaskDataTable(BaseTable):
    def __init__(self, parent: QWidget):
        super().__init__(4, 4, parent)
        self.setVerticalHeaderLabels(['A1', 'A2', 'A3', 'B2'])  # type: ignore
        self.setHorizontalHeaderLabels(['A1', 'A2', 'A3', 'B1'])  # type: ignore

    def get_data(self) -> list[list[Optional[float]]]:
        data: list[list[Optional[float]]] = []
        for i in range(self.rowCount()):
            data.append([])
            for j in range(self.columnCount()):
                try:
                    value = float(self.item(i, j).text())
                except ValueError:
                    value = None

                data[-1].append(value)

        return data


class AnswerTable(BaseTable):
    def __init__(self, parent: QWidget):
        super().__init__(4, 4, parent)
        self.setVerticalHeaderLabels(['A1', 'A2', 'A3', 'B2'])  # type: ignore
        self.setHorizontalHeaderLabels(['A1', 'A2', 'A3', 'B1'])  # type: ignore

        # disable data editing
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)


class TaskTab(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.init_widgets()

    def init_widgets(self):
        # create grid layout for tab widgets
        layout = QGridLayout()
        layout.setSpacing(15)
        # set stretching (size of widgets areas)
        layout.setRowStretch(0, 0)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 0)
        layout.setRowStretch(3, 1)

        # set widgets
        self.task_data_title = QLabel('Условие')
        layout.addWidget(self.task_data_title, 0, 0)

        self.clear_table_button = QPushButton('Очистить', self)
        self.clear_table_button.setCursor(Qt.PointingHandCursor)
        self.clear_table_button.clicked.connect(self.clear_tables)  # type: ignore
        layout.addWidget(self.clear_table_button, 0, 2)

        self.task_data_table = TaskDataTable(self)
        self.task_data_table.cellChanged.connect(self.update_answer)  # type: ignore
        layout.addWidget(self.task_data_table, 1, 0, 1, 0)

        self.answer_title = QLabel('Решение')
        layout.addWidget(self.answer_title, 2, 0)

        self.change_solve_mode_button = QPushButton('Максимум', self)
        self.change_solve_mode_button.setCursor(Qt.PointingHandCursor)
        self.change_solve_mode_button.clicked.connect(self.change_solve_mode)  # type: ignore
        layout.addWidget(self.change_solve_mode_button, 2, 2)

        self.answer_table = AnswerTable(self)
        layout.addWidget(self.answer_table, 3, 0, 1, 0)

        self.setLayout(layout)

    def change_solve_mode(self):
        if context.solve_mode == 'Maximum':
            context.solve_mode = 'Minimum'
            self.change_solve_mode_button.setText('Минимум')
        else:
            context.solve_mode = 'Maximum'
            self.change_solve_mode_button.setText('Максимум')

        self.update_answer()

    def clear_tables(self):
        self.task_data_table.clear_data()
        self.answer_table.clear_data()

    def update_answer(self):
        context.input_data = self.task_data_table.get_data()
        a_data, b_data = get_task_data(context.input_data)

        plot_points = get_plot_points(b_data)
        if plot_points:
            if context.solve_mode == 'Minimum':
                answer = get_min_solution(a_data, b_data, plot_points)
            else:
                answer = get_max_solution(a_data, b_data, plot_points)

            print(answer)

        # answer_view(self, b, ans[0], ans[1], ans[2], ans[3], ans[4], ans[5])

    
