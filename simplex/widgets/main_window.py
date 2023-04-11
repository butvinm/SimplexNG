import context
from PySide2.QtGui import QGuiApplication, QIcon, QKeySequence
from PySide2.QtWidgets import (QAction, QFileDialog, QMainWindow,
                               QTableWidgetItem)
from utils.excel import get_workbook, load_task, write_answer, write_task
from utils.path import get_path
from utils.style import get_adjusted_style
from widgets.info_window import InfoWindow
from widgets.main_widget import MainWidget
from widgets.theory_window import TheoryWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.theory_window = TheoryWindow()
        self.info_window = InfoWindow()

        self.init_menu_bar()
        self.init_widgets()

        self.setMinimumSize(500, 900)
        self.setWindowTitle('Simplex')
        self.setWindowIcon(QIcon(get_path('assets/icon.ico')))

        height = QGuiApplication.primaryScreen().geometry().height()
        self.setStyleSheet(get_adjusted_style(height))
        self.showNormal()

    def init_menu_bar(self):
        file_menu = self.menuBar().addMenu('Файл')

        open_task_action = QAction('Открыть задачу', self)
        open_task_action.setShortcut(QKeySequence('Ctrl+O'))
        open_task_action.triggered.connect(self.open_task)  # type: ignore
        file_menu.addAction(open_task_action)

        save_task_action = QAction('Сохранить задачу', self)
        save_task_action.setShortcut(QKeySequence('Ctrl+S'))
        save_task_action.triggered.connect(self.save_task)  # type: ignore
        file_menu.addAction(save_task_action)

        save_answer_action = QAction('Сохранить решение', self)
        save_answer_action.setShortcut(QKeySequence('Ctrl+A'))
        save_answer_action.triggered.connect(self.save_answer)  # type: ignore
        file_menu.addAction(save_answer_action)

        save_all_action = QAction('Сохранить задачу и решение', self)
        save_all_action.setShortcut(QKeySequence('Ctrl+F'))
        save_all_action.triggered.connect(self.save_all)  # type: ignore
        file_menu.addAction(save_all_action)

        save_graph_action = QAction('Сохранить график', self)
        save_graph_action.setShortcut(QKeySequence('Ctrl+G'))
        save_graph_action.triggered.connect(self.save_graph)  # type: ignore
        file_menu.addAction(save_graph_action)

        exit_action = QAction('Выйти', self)
        exit_action.setShortcut(QKeySequence('Ctrl+C'))
        exit_action.triggered.connect(self.close)  # type: ignore
        file_menu.addAction(exit_action)

        info_menu = self.menuBar().addMenu('Справка')

        open_theory_action = QAction('Открыть теорию', self)
        open_theory_action.setShortcut(QKeySequence('Ctrl+T'))
        open_theory_action.triggered.connect(self.open_theory)  # type: ignore
        info_menu.addAction(open_theory_action)

        open_info_action = QAction('Справка', self)
        open_info_action.setShortcut(QKeySequence('Ctrl+I'))
        open_info_action.triggered.connect(self.open_info)  # type: ignore
        info_menu.addAction(open_info_action)

        tasks_menu = self.menuBar().addMenu('Задачи')

        task_1_action = QAction('Задача №1', self)
        task_1_action.triggered.connect(self.Task1)  # type: ignore
        tasks_menu.addAction(task_1_action)

        task_2_action = QAction('Задача №2', self)
        task_2_action.triggered.connect(self.Task2)  # type: ignore
        tasks_menu.addAction(task_2_action)

    def init_widgets(self):
        self.main_widget = MainWidget()
        self.setCentralWidget(self.main_widget)

    def open_task(self):
        filepath, _ = QFileDialog.getOpenFileName(None, 'Загрузить задачу', '.', '*.xls')
        if not filepath:
            return

        data = load_task(filepath)

        task_data_table = self.main_widget.task_tab.task_data_table
        task_data_table.clear_data()

        for i in range(len(data)):
            for j in range(len(data[i])):
                task_data_table.setItem(i, j, QTableWidgetItem(str(data[i][j])))

    def save_task(self):
        filepath, _ = QFileDialog.getSaveFileName(None, 'Сохранение условия', 'Моя Задача.xls', '*.xls')
        if not filepath:
            return

        wb = get_workbook()
        write_task(wb, context.input_data)
        wb.save(filepath)

    def save_answer(self):
        filepath, _ = QFileDialog.getSaveFileName(None, 'Сохранение решения', 'Моя Задача.xls', '*.xls')
        if not filepath:
            return

        wb = get_workbook()
        write_answer(wb, context.data_align, context.answer_b_data,
                     context.answer_xs, context.answer_f, context.answer_endless)
        wb.save(filepath)

    def save_all(self):
        filepath, _ = QFileDialog.getSaveFileName(None, 'Сохранение задачи', 'Моя Задача.xls', '*.xls')
        if not filepath:
            return

        wb = get_workbook()
        write_task(wb, context.input_data)
        write_answer(wb, context.data_align, context.answer_b_data,
                     context.answer_xs, context.answer_f, context.answer_endless)
        wb.save(filepath)

    def save_graph(self):
        filepath, _ = QFileDialog.getSaveFileName(None, 'Сохранение графика', 'График.png', '*.png ')
        if not filepath:
            return

        self.main_widget.graph_tab.graph.save(filepath)

    def open_theory(self):
        self.theory_window.showMaximized()

    def open_info(self):
        self.info_window.show()

    def Task1(self):
        k = self.main_widget.task_tab.task_data_table

        k.setItem(0, 0, QTableWidgetItem('5'))
        k.setItem(0, 1, QTableWidgetItem('6'))
        k.setItem(0, 2, QTableWidgetItem('8'))
        k.setItem(1, 0, QTableWidgetItem('7'))
        k.setItem(1, 1, QTableWidgetItem('3'))
        k.setItem(1, 2, QTableWidgetItem('11'))

        k.setItem(0, 3, QTableWidgetItem('40'))
        k.setItem(1, 3, QTableWidgetItem('30'))
        k.setItem(3, 0, QTableWidgetItem('20'))
        k.setItem(3, 1, QTableWidgetItem('35'))
        k.setItem(3, 2, QTableWidgetItem('15'))

    def Task2(self):
        k = self.main_widget.task_tab.task_data_table

        k.setItem(0, 0, QTableWidgetItem('0.7'))
        k.setItem(0, 1, QTableWidgetItem('0.9'))
        k.setItem(0, 2, QTableWidgetItem('0.8'))
        k.setItem(1, 0, QTableWidgetItem('0.3'))
        k.setItem(1, 1, QTableWidgetItem('0.4'))
        k.setItem(1, 2, QTableWidgetItem('0.6'))

        k.setItem(0, 3, QTableWidgetItem('3'))
        k.setItem(1, 3, QTableWidgetItem('5'))
        k.setItem(3, 0, QTableWidgetItem('5'))
        k.setItem(3, 1, QTableWidgetItem('2'))
        k.setItem(3, 2, QTableWidgetItem('1'))
