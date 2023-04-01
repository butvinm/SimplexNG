from typing import Optional
from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtGui import QPainter, QBrush, QPen, QColor, QFont, QPolygon
from PySide2.QtCore import Qt, QPoint
from math import atan, degrees

'''
Input
'''

# Data





# Clear

def table_clear(self):
    for i in range(4):
        for j in range(4):
            item = QTableWidgetItem()
            self.my_table_1.setItem(i, j, item)

    for i in range(4):
        for j in range(4):
            item = QTableWidgetItem()
            self.my_table_2.setItem(i, j, item)


'''
Output
'''

# Mod


def mod_change(self):
    if self.mod == 0:
        self.mod = 1
        self.output_mod_button.setText('Минимум')
    else:
        self.mod = 0
        self.output_mod_button.setText('Максимум')

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


'''
Math
'''





'''
Graph
'''

# Marks


def graph_marks(graph, m, w, h):
    qp = QPainter(graph)

    qp.setPen(QPen(Qt.lightGray, m//40+1))
    for i in range(0, w, m):
        qp.drawLine(i, 0, i, h)
    for i in range(0, h, m):
        qp.drawLine(0, h-i, w, h-i)

    qp.setPen(QPen(Qt.black, 3))
    qp.drawLine(150//m*m, 0, 150//m*m, h)
    qp.drawLine(0, h-150//m*m, w, h-150//m*m)

    qp.end()

    return graph

# Vector


def graph_vector(graph, m, a, w, h):
    x_1 = a[0]-a[2]-a[3]+a[5]
    x_2 = a[1]-a[2]-a[4]+a[5]

    qp = QPainter(graph)
    qp.setPen(QPen(Qt.red, 3))
    qp.drawLine(150//m*m, h-150//m*m, 150//m*m+x_1*m*5, h-150//m*m-x_2*m*5)
    qp.drawLine(150//m*m+x_2*5, h-150//m*m+x_1*5,
                150//m*m-x_2*5, h-150//m*m-x_1*5)
    qp.end()

    return graph

# Points


def graph_points(graph, m, a, points, p_min, p_max, w, h):
    x_0 = 150//m*m
    y_0 = h-150//m*m

    x_1 = a[0]-a[2]-a[3]+a[5]
    x_2 = a[1]-a[2]-a[4]+a[5]

    qp = QPainter(graph)
    for i in points.values():
        if i == p_min or i == p_max:
            qp.setPen(QPen(Qt.red, 3))
            qp.drawLine(150//m*m+x_2*m+i[0]*m, h-150//m*m+x_1*m-i[1]*m,
                        150//m*m-x_2*m+i[0]*m, h-150//m*m-x_1*m-i[1]*m)
        else:
            qp.setPen(QPen(Qt.black, 3))

        qp.setBrush(QBrush(Qt.white))
        qp.drawEllipse(x_0+i[0]*m-7, y_0-i[1]*m-7, 14, 14)
    qp.end()

    return graph

# Lines


def graph_lines(graph, m, b_data, w, h):
    x_0 = 150//m*m
    y_0 = h-150//m*m

    qp = QPainter(graph)

    qp.setPen(QPen(Qt.darkGreen, 3))
    # L1
    qp.drawLine(x_0, y_0, x_0, 0)
    # L2
    qp.drawLine(x_0, y_0, w, y_0)
    # L3
    qp.drawLine(x_0+b_data[2]*m, y_0, x_0+b_data[2]*m, 0)
    # L4
    qp.drawLine(x_0, y_0-b_data[3]*m, w, y_0-b_data[3]*m)
    # L5
    qp.drawLine(x_0+b_data[0]*m, y_0, x_0, y_0-b_data[0]*m)
    # L6
    qp.drawLine(x_0+abs(b_data[0]-b_data[4])*m, y_0, x_0, y_0-abs(b_data[0]-b_data[4])*m)
    # Numbers
    qp.setPen(QPen(Qt.red, 2))
    qp.setFont(QFont('Times', 10))

    qp.drawText(x_0-20, y_0+25, '0')
    qp.drawText(x_0+b_data[2]*m-10, y_0+25, str(b_data[2]))
    qp.drawText(x_0-30, y_0-b_data[3]*m+10, str(b_data[3]))
    qp.drawText(x_0+b_data[0]*m-10, y_0+25, str(b_data[0]))
    qp.drawText(x_0-30, y_0-abs(b_data[0]-b_data[4])*m+10, str(abs(b_data[0]-b_data[4])))

    qp.end()

    return graph


# Polygon
def graph_polygon(graph, points_0, m, w, h):

    x_0 = 150//m*m
    y_0 = h-150//m*m

    points_0 = list(points_0.values())
    points_1 = []

    p = points_0

    p.sort(key=lambda p: (p[0], -p[1]))

    points_1.append(p[0])
    points_0.remove(p[0])

    # Смотрим справа
    b_data = True
    while b_data:
        point = sorted(points_0, key=lambda p: (-p[1], p[0]))

        for i in range(len(point)-1):
            if point[i][1] == point[i+1][1] and point[i][0] < point[i+1][0]:
                point[i], point[i+1] = point[i+1], point[i]

        b_data = True
        if point:
            for i in point:
                if i[0] > points_1[-1][0] and i[1] <= points_1[-1][1]:
                    points_0.remove(i)
                    points_1.append(i)
                    b_data = True
                    break
                else:
                    b_data = False
        else:
            break

    # Под собой
    point = sorted(points_0, key=lambda p: (-p[1], p[0]))

    for i in point:
        if i[0] == points_1[-1][0] and i[1] <= points_1[-1][1]:
            points_0.remove(i)
            points_1.append(i)
            break

    # Смотрим слева
    b_data = True
    while b_data:
        point = sorted(points_0, key=lambda p: (p[1], -p[0]))
        b_data = True
        if point:
            for i in point:
                if i[0] < points_1[-1][0] and i[1] >= points_1[-1][1]:
                    points_0.remove(i)
                    points_1.append(i)
                    b_data = True
                    break
                else:
                    b_data = False
        else:
            break

    # Под собой
    point = sorted(points_0, key=lambda p: (p[1], -p[0]))

    for i in point:
        if i[0] == points_1[-1][0] and i[1] >= points_1[-1][1]:
            points_0.remove(i)
            points_1.append(i)
            break

    polygon = QPolygon([QPoint(x_0+i[0]*m, y_0-i[1]*m) for i in points_1])

    qp = QPainter(graph)
    qp.setBrush(QBrush(Qt.blue, Qt.Dense6Pattern))
    qp.drawPolygon(polygon)
    qp.end()

    return graph
