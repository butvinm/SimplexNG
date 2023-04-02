from PySide2.QtWidgets import QTableWidgetItem


'''
Output
'''

# View
def answer_view(self, b_data, xs_min, f_min, min_endless, xs_max, f_max, max_endless):
    xmax_items = [QTableWidgetItem(str(i)) for i in xs_max]
    xmin_items = [QTableWidgetItem(str(i)) for i in xs_min]

    for i in range(4):
        for j in range(4):
            item = QTableWidgetItem()
            self.my_table_2.setItem(i, j, item)

    if self.input_mod == 0:
        # b_data
        self.my_table_2.setItem(0, 3, QTableWidgetItem(str(b_data[0])))
        self.my_table_2.setItem(1, 3, QTableWidgetItem(str(b_data[1])))
        self.my_table_2.setItem(3, 0, QTableWidgetItem(str(b_data[2])))
        self.my_table_2.setItem(3, 1, QTableWidgetItem(str(b_data[3])))
        self.my_table_2.setItem(3, 2, QTableWidgetItem(str(b_data[4])))
        # xs

        if self.mod == 0:
            self.my_table_2.setItem(0, 0, xmax_items[0])
            self.my_table_2.setItem(0, 1, xmax_items[1])
            self.my_table_2.setItem(0, 2, xmax_items[2])
            self.my_table_2.setItem(1, 0, xmax_items[3])
            self.my_table_2.setItem(1, 1, xmax_items[4])
            self.my_table_2.setItem(1, 2, xmax_items[5])
            self.my_table_2.setItem(3, 3, QTableWidgetItem('F='+str(f_max)))
            if max_endless:
                self.my_table_2.setItem(2, 2, QTableWidgetItem('Бесконечное'))
            else:
                self.my_table_2.setItem(2, 2, QTableWidgetItem('Конечное'))
        else:
            self.my_table_2.setItem(0, 0, xmin_items[0])
            self.my_table_2.setItem(0, 1, xmin_items[1])
            self.my_table_2.setItem(0, 2, xmin_items[2])
            self.my_table_2.setItem(1, 0, xmin_items[3])
            self.my_table_2.setItem(1, 1, xmin_items[4])
            self.my_table_2.setItem(1, 2, xmin_items[5])
            self.my_table_2.setItem(3, 3, QTableWidgetItem('F='+str(f_min)))
            if max_endless:
                self.my_table_2.setItem(2, 2, QTableWidgetItem('Бесконечное'))
            else:
                self.my_table_2.setItem(2, 2, QTableWidgetItem('Конечное'))

    else:
        # b_data
        self.my_table_2.setItem(3, 0, QTableWidgetItem(str(b_data[0])))
        self.my_table_2.setItem(3, 1, QTableWidgetItem(str(b_data[1])))
        self.my_table_2.setItem(0, 3, QTableWidgetItem(str(b_data[4])))
        self.my_table_2.setItem(1, 3, QTableWidgetItem(str(b_data[3])))
        self.my_table_2.setItem(2, 3, QTableWidgetItem(str(b_data[2])))
        # xs

        if self.mod == 0:
            self.my_table_2.setItem(2, 0, xmax_items[0])
            self.my_table_2.setItem(2, 1, xmax_items[3])
            self.my_table_2.setItem(1, 0, xmax_items[1])
            self.my_table_2.setItem(1, 1, xmax_items[4])
            self.my_table_2.setItem(0, 0, xmax_items[2])
            self.my_table_2.setItem(0, 1, xmax_items[5])
            self.my_table_2.setItem(3, 3, QTableWidgetItem('F='+str(f_max)))
            if min_endless:
                self.my_table_2.setItem(2, 2, QTableWidgetItem('Бесконечное'))
            else:
                self.my_table_2.setItem(2, 2, QTableWidgetItem('Конечное'))
        else:
            self.my_table_2.setItem(2, 0, xmin_items[0])
            self.my_table_2.setItem(2, 1, xmin_items[3])
            self.my_table_2.setItem(1, 0, xmin_items[1])
            self.my_table_2.setItem(1, 1, xmin_items[4])
            self.my_table_2.setItem(0, 0, xmin_items[2])
            self.my_table_2.setItem(0, 1, xmin_items[5])
            self.my_table_2.setItem(3, 3, QTableWidgetItem('F='+str(f_min)))
            if min_endless:
                self.my_table_2.setItem(2, 2, QTableWidgetItem('Бесконечное'))
            else:
                self.my_table_2.setItem(2, 2, QTableWidgetItem('Конечное'))

