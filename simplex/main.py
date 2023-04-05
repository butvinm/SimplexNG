import sys

import context
import style
from PySide2.QtGui import QGuiApplication, QIcon
from PySide2.QtWidgets import (QAction, QApplication, QFileDialog, QGridLayout,
                               QMainWindow, QMessageBox, QTableWidgetItem,
                               QTabWidget, QWidget)
from utils.excel import get_workbook, load_task, write_answer, write_task
from utils.path import get_path
from widgets import InfoWindow, MainWidget, TheoryWindow
from xlrd import open_workbook
from xlwt import Font, Workbook, easyxf


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.theory_window = TheoryWindow()
        self.info_window = InfoWindow()

        ########
        my_menubar = self.menuBar()

        '''Fail'''
        M_Fail = my_menubar.addMenu('Файл')

        Open_Task = QAction('Открыть задачу', self)
        Open_Task.setShortcut('Ctrl+O')
        Open_Task.triggered.connect(self.open_task)

        Task_Save = QAction('Сохранить задачу', self)
        Task_Save.setShortcut('Ctrl+S')
        Task_Save.triggered.connect(self.save_task)

        Answer_Save = QAction('Сохранить решение', self)
        Answer_Save.setShortcut('Ctrl+A')
        Answer_Save.triggered.connect(self.save_answer)

        All_Save = QAction('Сохранить задачу и решение', self)
        All_Save.setShortcut('Ctrl+F')
        All_Save.triggered.connect(self.save_all)

        Graph_Save = QAction('Сохранить график', self)
        Graph_Save.setShortcut('Ctrl+G')
        Graph_Save.triggered.connect(self.GraphSave)

        Programm_Exit = QAction('Выйти', self)
        Programm_Exit.setShortcut('Ctrl+C')
        Programm_Exit.triggered.connect(self.close)

        M_Fail.addAction(Open_Task)
        M_Fail.addAction(Task_Save)
        M_Fail.addAction(Answer_Save)
        M_Fail.addAction(All_Save)
        M_Fail.addAction(Graph_Save)
        M_Fail.addAction(Programm_Exit)
        '''Theory'''
        M_Inf = my_menubar.addMenu('Справка')

        Theory_Open = QAction('Открыть теорию', self)
        Theory_Open.setShortcut('Ctrl+T')
        Theory_Open.triggered.connect(self.open_theory)

        Inf_Open = QAction('Справка', self)
        Inf_Open.setShortcut('Ctrl+I')
        Inf_Open.triggered.connect(self.open_info)

        M_Inf.addAction(Theory_Open)
        M_Inf.addAction(Inf_Open)
        '''Tasks'''
        M_Tasks = my_menubar.addMenu('Задачи')

        Task_1 = QAction('Задача №1', self)
        Task_1.triggered.connect(self.Task1)

        Task_2 = QAction('Задача №2', self)
        Task_2.triggered.connect(self.Task2)

        M_Tasks.addAction(Task_1)
        M_Tasks.addAction(Task_2)

        self.main_widget = MainWidget()
        self.setCentralWidget(self.main_widget)

        self.setMinimumSize(500, 900)
        self.setWindowTitle('Simplex')
        self.setWindowIcon(QIcon(get_path('assets/App.ico')))
        screen_height = QGuiApplication.primaryScreen().geometry().height()
        f = style.Style(screen_height)
        self.setStyleSheet(f.style)
        self.showMaximized()

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

    def GraphSave(self):
        filename = QFileDialog.getSaveFileName(
            None, 'Сохранение графика', 'График.png', '*.png ')

        if filename == ('', ''):
            return

        try:
            self.graph_tab.graph.save(filename[0], 'PNG')
        except AttributeError:
            mb = QMessageBox(QMessageBox.Critical,
                             'Ошибка', 'Пустой график',
                             buttons=QMessageBox.Ok,
                             parent=self)
            mb_view = mb.exec_()

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

    def task_sheet(self, data):

        font0 = Font()
        font0.name = 'Arial'
        font0.colour_index = 0

        style0 = easyxf('font: color black; align: horiz center')

        ws = self.wb.add_sheet('Задача', cell_overwrite_ok=True)

        ws.write_merge(0, 0, 0, 4, 'Условие', style0)
        ws.write(1, 1, 'A')
        ws.write(1, 2, 'B')
        ws.write(1, 3, 'C')
        ws.write(1, 4, 'D')
        ws.write(2, 0, 'I')
        ws.write(3, 0, 'II')
        ws.write(4, 0, 'III')
        ws.write(5, 0, 'IV')

        if data[2] == 0:
            # 'a's
            ws.write(2, 1, data[0][0])
            ws.write(2, 2, data[0][1])
            ws.write(2, 3, data[0][2])
            ws.write(3, 1, data[0][3])
            ws.write(3, 2, data[0][4])
            ws.write(3, 3, data[0][5])
            # 'b's
            ws.write(2, 4, data[1][0])
            ws.write(3, 4, data[1][1])
            ws.write(5, 1, data[1][2])
            ws.write(5, 2, data[1][3])
            ws.write(5, 3, data[1][4])
        else:
            # 'a's
            ws.write(4, 1, data[0][0])
            ws.write(3, 1, data[0][1])
            ws.write(2, 1, data[0][2])
            ws.write(4, 2, data[0][3])
            ws.write(3, 2, data[0][4])
            ws.write(2, 2, data[0][5])
            # 'b's
            ws.write(5, 1, data[1][0])
            ws.write(5, 2, data[1][1])
            ws.write(4, 4, data[1][2])
            ws.write(3, 4, data[1][3])
            ws.write(2, 4, data[1][4])

    def answer_sheet(self, data, ans):

        font0 = Font()
        font0.name = 'Arial'
        font0.colour_index = 0

        style0 = easyxf('font: color black; align: horiz center')

        ws = self.wb.add_sheet('Решение', cell_overwrite_ok=True)

        # Минимум
        ws.write_merge(0, 0, 0, 4, 'Минимум', style0)
        ws.write(1, 1, 'A')
        ws.write(1, 2, 'B')
        ws.write(1, 3, 'C')
        ws.write(1, 4, 'D')
        ws.write(2, 0, 'I')
        ws.write(3, 0, 'II')
        ws.write(4, 0, 'III')
        ws.write(5, 0, 'IV')

        if data[2] == 0:
            # 'a's
            ws.write(2, 1, ans[0][0])
            ws.write(2, 2, ans[0][1])
            ws.write(2, 3, ans[0][2])
            ws.write(3, 1, ans[0][3])
            ws.write(3, 2, ans[0][4])
            ws.write(3, 3, ans[0][5])
            # 'b's
            ws.write(2, 4, data[1][0])
            ws.write(3, 4, data[1][1])
            ws.write(5, 1, data[1][2])
            ws.write(5, 2, data[1][3])
            ws.write(5, 3, data[1][4])
        else:
            # 'a's
            ws.write(4, 1, ans[0][0])
            ws.write(3, 1, ans[0][1])
            ws.write(2, 1, ans[0][2])
            ws.write(4, 2, ans[0][3])
            ws.write(3, 2, ans[0][4])
            ws.write(2, 2, ans[0][5])
            # 'b's
            ws.write(5, 1, data[1][0])
            ws.write(5, 2, data[1][1])
            ws.write(4, 4, data[1][2])
            ws.write(3, 4, data[1][3])
            ws.write(2, 4, data[1][4])

        ws.write(5, 4, 'F= '+str(ans[1]))

        if ans[2]:
            ws.write(4, 3, 'Бесконечное')
        else:
            ws.write(4, 3, 'Конечное')

        # Максимум
        ws.write_merge(7, 7, 0, 4, 'Максимум', style0)
        ws.write(8, 1, 'A')
        ws.write(8, 2, 'B')
        ws.write(8, 3, 'C')
        ws.write(8, 4, 'D')
        ws.write(9, 0, 'I')
        ws.write(10, 0, 'II')
        ws.write(11, 0, 'III')
        ws.write(12, 0, 'IV')

        if data[2] == 0:
            # 'a's
            ws.write(9, 1, ans[3][0])
            ws.write(9, 2, ans[3][1])
            ws.write(9, 3, ans[3][2])
            ws.write(10, 1, ans[3][3])
            ws.write(10, 2, ans[3][4])
            ws.write(10, 3, ans[3][5])
            # 'b's
            ws.write(9, 4, data[1][0])
            ws.write(10, 4, data[1][1])
            ws.write(12, 1, data[1][2])
            ws.write(12, 2, data[1][3])
            ws.write(12, 3, data[1][4])
        else:
            # 'a's
            ws.write(11, 1, ans[3][0])
            ws.write(10, 1, ans[3][1])
            ws.write(9, 1, ans[3][2])
            ws.write(11, 2, ans[3][3])
            ws.write(10, 2, ans[3][4])
            ws.write(9, 2, ans[3][5])
            # 'b's
            ws.write(12, 1, data[1][0])
            ws.write(12, 2, data[1][1])
            ws.write(10, 4, data[1][2])
            ws.write(9, 4, data[1][3])
            ws.write(8, 4, data[1][4])

        ws.write(12, 4, 'F= '+str(ans[4]))

        if ans[5]:
            ws.write(11, 3, 'Бесконечное')
        else:
            ws.write(11, 3, 'Конечное')


if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    sys.exit(app.exec_())
