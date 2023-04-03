import sys

import style
from PySide2.QtGui import QGuiApplication, QIcon
from PySide2.QtWidgets import (QAction, QApplication, QFileDialog, QGridLayout,
                               QMainWindow, QMessageBox, QTableWidgetItem,
                               QTabWidget, QWidget)
from utils.path import get_path
from widgets import GraphTab, InfoWindow, TaskTab, TheoryWindow
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
        Open_Task.triggered.connect(self.OpenTask)

        Task_Save = QAction('Сохранить задачу', self)
        Task_Save.setShortcut('Ctrl+T')
        Task_Save.triggered.connect(self.TaskSave)

        Answer_Save = QAction('Сохранить решение', self)
        Answer_Save.setShortcut('Ctrl+A')
        Answer_Save.triggered.connect(self.AnswerSave)

        All_Save = QAction('Сохранить задачу и решение', self)
        All_Save.setShortcut('Ctrl+F')
        All_Save.triggered.connect(self.AllSave)

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
        ########

        my_tab = QTabWidget(self)

        self.task_tab = TaskTab(self)

        self.graph_tab = GraphTab()

        my_tab.addTab(self.task_tab, 'Решение')
        my_tab.addTab(self.graph_tab, 'График')

        main_layout = QGridLayout()

        main_layout.addWidget(my_tab, 0, 0)

        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)
        self.setMinimumSize(500, 900)
        self.setWindowTitle('Simplex')
        self.setWindowIcon(QIcon(get_path('assets/App.ico')))
        screen_height = QGuiApplication.primaryScreen().geometry().height()
        f = style.Style(screen_height)
        self.setStyleSheet(f.style)
        self.showMaximized()

    def OpenTask(self):
        filename = QFileDialog.getOpenFileName(
            self, "Выбирете файл", None, "*.xlsx, *.xls")
        if filename == ('', ''):
            return

        book = open_workbook(filename[0])
        sheet = book.sheets()[0]
        data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)]
                for r in range(sheet.nrows)]

        for i in range(len(data)):
            for j in range(len(data[i])):
                try:
                    data[i][j] = int(data[i][j])
                except ValueError:
                    continue

        data = [list(map(str, i)) for i in data]

        k = self.task_tab.my_table_1

        k.setItem(0, 0, QTableWidgetItem(data[2][1]))
        k.setItem(0, 1, QTableWidgetItem(data[2][2]))
        k.setItem(0, 2, QTableWidgetItem(data[2][3]))
        k.setItem(1, 0, QTableWidgetItem(data[3][1]))
        k.setItem(1, 1, QTableWidgetItem(data[3][2]))
        k.setItem(1, 2, QTableWidgetItem(data[3][3]))
        k.setItem(2, 0, QTableWidgetItem(data[4][1]))
        k.setItem(2, 1, QTableWidgetItem(data[4][2]))
        k.setItem(2, 2, QTableWidgetItem(data[4][3]))

        k.setItem(0, 3, QTableWidgetItem(data[2][4]))
        k.setItem(1, 3, QTableWidgetItem(data[3][4]))
        k.setItem(2, 3, QTableWidgetItem(data[4][4]))
        k.setItem(3, 0, QTableWidgetItem(data[5][1]))
        k.setItem(3, 1, QTableWidgetItem(data[5][2]))
        k.setItem(3, 2, QTableWidgetItem(data[5][3]))

    def TaskSave(self):
        data = input_data(self.task_tab.my_table_1)

        filename = QFileDialog.getSaveFileName(
            None, 'Сохранение графика', 'Моя Задача.xls', '*.xls')
        if filename == ('', ''):
            return

        self.wb = Workbook()

        self.task_sheet(data)

        try:
            self.wb.save(filename[0])
        except PermissionError:
            mb = QMessageBox(QMessageBox.Critical,
                             "Ошибка", "Закройте файл",
                             buttons=QMessageBox.Ok,
                             parent=self)
            mb_view = mb.exec_()

    def AnswerSave(self):
        data = input_data(self.task_tab.my_table_1)

        try:
            ans = answer(data[0], data[1], find_points(data[1]))
            filename = QFileDialog.getSaveFileName(
                None, 'Сохранение графика', 'Мое Решение.xls', '*.xls')
            if filename == ('', ''):
                return

            self.wb = Workbook()

            self.answer_sheet(data, ans)

            try:
                self.wb.save(filename[0])
            except PermissionError:
                mb = QMessageBox(QMessageBox.Critical,
                                 "Ошибка", "Закройте файл",
                                 buttons=QMessageBox.Ok,
                                 parent=self)
                mb_view = mb.exec_()
        except TypeError:
            mb = QMessageBox(QMessageBox.Critical,
                             "Ошибка", "Недостаточно данных",
                             buttons=QMessageBox.Ok,
                             parent=self)
            mb_view = mb.exec_()

    def AllSave(self):
        data = input_data(self.task_tab.my_table_1)

        try:
            ans = answer(data[0], data[1], find_points(data[1]))

            filename = QFileDialog.getSaveFileName(
                None, 'Сохранение графика', 'Задача и Решение.xls', '*.xls')
            if filename == ('', ''):
                return

            self.wb = Workbook()

            self.task_sheet(data)
            self.answer_sheet(data, ans)

            try:
                self.wb.save(filename[0])
            except PermissionError:
                mb = QMessageBox(QMessageBox.Critical,
                                 "Ошибка", "Закройте файл",
                                 buttons=QMessageBox.Ok,
                                 parent=self)
                mb_view = mb.exec_()

        except TypeError:
            mb = QMessageBox(QMessageBox.Critical,
                             "Ошибка", "Недостаточно данных",
                             buttons=QMessageBox.Ok,
                             parent=self)
            mb_view = mb.exec_()

    def GraphSave(self):
        filename = QFileDialog.getSaveFileName(
            None, 'Сохранение графика', 'График.png', '*.png ')

        if filename == ('', ''):
            return

        try:
            self.graph_tab.graph.save(filename[0], 'PNG')
        except AttributeError:
            mb = QMessageBox(QMessageBox.Critical,
                             "Ошибка", "Пустой график",
                             buttons=QMessageBox.Ok,
                             parent=self)
            mb_view = mb.exec_()

    def open_theory(self):
        self.theory_window.showMaximized()

    def open_info(self):
        self.info_window.show()

    def Task1(self):
        k = self.task_tab.my_table_1

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
        k = self.task_tab.my_table_1

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

        style0 = easyxf("font: color black; align: horiz center")

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

        style0 = easyxf("font: color black; align: horiz center")

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


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    sys.exit(app.exec_())
