from typing import Optional

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QAbstractItemView, QGridLayout, QHeaderView,
                               QLabel, QPushButton, QTableWidget,
                               QTableWidgetItem, QWidget)
from utils.math import get_plot_points, get_max_solution, get_min_solution


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
        self.solve_mode = 'Minimum'
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
        if self.solve_mode == 'Maximum':
            self.solve_mode = 'Minimum'
            self.change_solve_mode_button.setText('Минимум')
        else:
            self.solve_mode = 'Maximum'
            self.change_solve_mode_button.setText('Максимум')

        self.update_answer()

    def clear_tables(self):
        self.task_data_table.clear_data()
        self.answer_table.clear_data()

    def update_answer(self):
        table_data = self.task_data_table.get_data()

        a_data, b_data = self.get_task_data(table_data)

        plot_points = get_plot_points(b_data)
        if plot_points:
            if self.solve_mode == 'Minimum':
                answer = get_min_solution(a_data, b_data, plot_points)
            else:
                answer = get_max_solution(a_data, b_data, plot_points)

            print(answer)

        # answer_view(self, b, ans[0], ans[1], ans[2], ans[3], ans[4], ans[5])

    def get_task_data(self, data: list[list[Optional[float]]]) -> tuple[list[float], list[float]]:
        """Get task data from table depends on data alignment and return A's and B's values"""

        align = 'Horizontal' if data[1][2] is not None else 'Vertical'

        if align == 'Horizontal':
            a_data = [
                data[0][0], data[0][1], data[0][2],
                data[1][0], data[1][1], data[1][2]
            ]
            b_data = [
                data[0][3], data[1][3],
                data[3][0], data[3][1], data[3][2]
            ]
        else:
            a_data = [
                data[2][0], data[1][0], data[0][0],
                data[2][1], data[1][1], data[0][1]
            ]

            b_data = [
                data[3][0], data[3][1],
                data[2][3], data[1][3], data[0][3]
            ]

        if any(value is None for value in a_data + b_data):
            raise ValueError('Incorrect input data: empty items')

        return a_data, b_data  # pyright: reportGeneralTypeIssues=none
