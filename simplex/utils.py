from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtGui import QPainter, QBrush, QPen, QColor, QFont, QPolygon
from PySide2.QtCore import Qt, QPoint
from math import atan, degrees

'''
Input
'''

# Data


def input_data(my_table_1):
    data = []
    mod = 0

    for row in range(4):
        for col in range(4):
            data.append(my_table_1.item(row, col).text())

    if data[2] == '':
        mod = 1
    else:
        mod = 0

    if mod == 0:
        a_data = [data[0], data[1], data[2],
                  data[4], data[5], data[6]]

        b_data = [data[3], data[7], data[12], data[13], data[14]]
    else:
        a_data = [data[8], data[4], data[0],
                  data[9], data[5], data[1]]

        b_data = [data[12], data[13], data[11], data[7], data[3]]

    try:
        a_data = list(map(float, a_data))
        b_data = list(map(int, b_data))
        able = True
    except ValueError:
        able = False

    return a_data, b_data, mod, able


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


def answer_view(self, b, xs_min, f_min, min_endless, xs_max, f_max, max_endless):
    xmax_items = [QTableWidgetItem(str(i)) for i in xs_max]
    xmin_items = [QTableWidgetItem(str(i)) for i in xs_min]

    for i in range(4):
        for j in range(4):
            item = QTableWidgetItem()
            self.my_table_2.setItem(i, j, item)

    if self.input_mod == 0:
        # b
        self.my_table_2.setItem(0, 3, QTableWidgetItem(str(b[0])))
        self.my_table_2.setItem(1, 3, QTableWidgetItem(str(b[1])))
        self.my_table_2.setItem(3, 0, QTableWidgetItem(str(b[2])))
        self.my_table_2.setItem(3, 1, QTableWidgetItem(str(b[3])))
        self.my_table_2.setItem(3, 2, QTableWidgetItem(str(b[4])))
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
        # b
        self.my_table_2.setItem(3, 0, QTableWidgetItem(str(b[0])))
        self.my_table_2.setItem(3, 1, QTableWidgetItem(str(b[1])))
        self.my_table_2.setItem(0, 3, QTableWidgetItem(str(b[4])))
        self.my_table_2.setItem(1, 3, QTableWidgetItem(str(b[3])))
        self.my_table_2.setItem(2, 3, QTableWidgetItem(str(b[2])))
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

# Points Finding


def find_points(b):
    points = {}
    i = 0
    if b[0] >= 0 and b[2] >= 0 and b[3] >= 0:

        # 1 I--II
        if abs(b[4]-b[0]) == 0:
            if not([0, 0] in points.values()):
                points.update({i: [0, 0]})
                i += 1

        # 2 I--III
        if b[2] >= b[0] and b[4] - b[0] <= b[0]:
            if not([b[0], 0] in points.values()):
                points.update({i: [b[0], 0]})
                i += 1

        # 3 I--IV
        if b[2] >= abs(b[4]-b[0]) and b[0] >= abs(b[4]-b[0]):
            if not([abs(b[4]-b[0]), 0] in points.values()):
                points.update({i: [abs(b[4]-b[0]), 0]})
                i += 1

        # 4 I--VI
        if b[0] >= b[2] and abs(b[4]-b[0]) <= b[2]:
            if not([b[2], 0] in points.values()):
                points.update({i: [b[2], 0]})
                i += 1

        # 5 II--III
        if b[3] >= b[0] and abs(b[4]-b[0]) <= b[0]:
            if not([0, b[0]] in points.values()):
                points.update({i: [0, b[0]]})
                i += 1

        # 6 II--V
        if b[0] >= b[3] and abs(b[4]-b[0]) <= b[3]:
            if not([0, b[3]] in points.values()):
                points.update({i: [0, b[3]]})
                i += 1

        # 7 II--IV
        if b[0] >= abs(b[4]-b[0]) and b[3] >= abs(b[4]-b[0]):
            if not([0, abs(b[4]-b[0])] in points.values()):
                points.update({i: [0, abs(abs(b[4]-b[0]))]})
                i += 1

        # 8 III-V
        if b[3] <= b[0] and b[2] >= b[0]-b[3] and abs(b[4]-b[0]) <= b[0]:
            if not([b[0]-b[3], b[3]] in points.values()):
                points.update({i: [b[0]-b[3], b[3]]})
                i += 1

        # 9 III-VI
        if b[2] <= b[0] and b[3] >= b[0]-b[2] and abs(b[4]-b[0]) <= b[0]:
            if not([b[2], b[0]-b[2]] in points.values()):
                points.update({i: [b[2], b[0]-b[2]]})
                i += 1

        # 10 IV--V
        if b[0] >= abs(b[4]-b[0]) and b[2] >= abs(b[4]-b[0])-b[3] and b[3] <= abs(b[4]-b[0]):
            if not([abs(b[4]-b[0])-b[3], b[3]] in points.values()):
                points.update({i: [abs(b[4]-b[0])-b[3], b[3]]})
                i += 1

        # 11 IV--VI
        if b[0] >= abs(b[4]-b[0]) and b[3] >= abs(b[4]-b[0])-b[2] and b[2] <= abs(b[4]-b[0]):
            if not([b[2], abs(b[4]-b[0])-b[2]] in points.values()):
                points.update({i: [b[2], abs(b[4]-b[0])-b[2]]})
                i += 1

        # 12 V--VI
        if b[0] >= b[2]+b[3] and abs(b[4]-b[0]) <= b[2]+b[3]:
            if not([b[2], b[3]] in points.values()):
                points.update({i: [b[2], b[3]]})
                i += 1

    return points

# Points Sorting


def answer(a, b, points):

    try:
        alfa = round(
            degrees(atan((a[1]-a[2]-a[4]+a[5])/(a[0]-a[2]-a[3]+a[5]))))
        alfa = 90 - alfa
    except ZeroDivisionError:
        alfa = 360

    if alfa < 0:
        alfa += 180

    if points:
        x_min = min(range(len(points)), key=[points[i][0]
                                             for i in range(len(points))].__getitem__)
        y_min = min(range(len(points)), key=[points[i][1]
                                             for i in range(len(points))].__getitem__)
        x_max = max(range(len(points)), key=[points[i][0]
                                             for i in range(len(points))].__getitem__)
        y_max = max(range(len(points)), key=[points[i][1]
                                             for i in range(len(points))].__getitem__)

    if alfa > 45:

        min_endless_able = False

        # Min
        ans_min = points[x_min]
        for i in range(len(points)):
            if points[i][0] == points[x_min][0]:
                min_endless_able = True
                if points[i][1] < points[x_min][1]:
                    ans_min = points[i]

        max_endless_able = False

        # Max
        ans_max = points[x_max]
        for i in range(len(points)):
            if points[i][0] == points[x_max][0]:
                max_endless_able = False
                if points[i][1] > points[x_max][1]:
                    ans_max = points[i]

    else:
        min_endless_able = False

        # Min
        ans_min = points[y_min]
        for i in range(len(points)):
            if points[i][1] == points[y_min][1]:
                min_endless_able = True
                if points[i][0] < points[y_min][0]:
                    ans_min = points[i]

        max_endless_able = False

        # Max
        ans_max = points[y_max]
        for i in range(len(points)):
            if points[i][1] == points[y_max][1]:
                max_endless_able = True
                if points[i][0] > points[y_max][0]:
                    ans_max = points[i]

    xs_min = [ans_min[0],
              ans_min[1],
              b[0]-ans_min[0]-ans_min[1],
              b[2]-ans_min[0],
              b[3]-ans_min[1],
              b[4]-b[0]+ans_min[0]+ans_min[1]]

    f_min = sum(list(map(lambda x, y: x*y, xs_min, a)))

    xs_max = [ans_max[0],
              ans_max[1],
              b[0]-ans_max[0]-ans_max[1],
              b[2]-ans_max[0],
              b[3]-ans_max[1],
              b[4]-b[0]+ans_max[0]+ans_max[1]]

    f_max = sum(list(map(lambda x, y: x*y, xs_max, a)))

    min_endless = False
    max_endless = False

    if min_endless_able == True and alfa in [0, 45, 90]:
        min_endless = True

    if max_endless_able == True and alfa in [0, 45, 90]:
        max_endless = True

    xs_min = [int(i) for i in xs_min]
    xs_max = [int(i) for i in xs_max]
    f_min = round(f_min, 2)
    f_max = round(f_max, 2)

    return xs_min, f_min, min_endless,   xs_max, f_max, max_endless


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


def graph_lines(graph, m, b, w, h):
    x_0 = 150//m*m
    y_0 = h-150//m*m

    qp = QPainter(graph)

    qp.setPen(QPen(Qt.darkGreen, 3))
    # L1
    qp.drawLine(x_0, y_0, x_0, 0)
    # L2
    qp.drawLine(x_0, y_0, w, y_0)
    # L3
    qp.drawLine(x_0+b[2]*m, y_0, x_0+b[2]*m, 0)
    # L4
    qp.drawLine(x_0, y_0-b[3]*m, w, y_0-b[3]*m)
    # L5
    qp.drawLine(x_0+b[0]*m, y_0, x_0, y_0-b[0]*m)
    # L6
    qp.drawLine(x_0+abs(b[0]-b[4])*m, y_0, x_0, y_0-abs(b[0]-b[4])*m)
    # Numbers
    qp.setPen(QPen(Qt.red, 2))
    qp.setFont(QFont('Times', 10))

    qp.drawText(x_0-20, y_0+25, '0')
    qp.drawText(x_0+b[2]*m-10, y_0+25, str(b[2]))
    qp.drawText(x_0-30, y_0-b[3]*m+10, str(b[3]))
    qp.drawText(x_0+b[0]*m-10, y_0+25, str(b[0]))
    qp.drawText(x_0-30, y_0-abs(b[0]-b[4])*m+10, str(abs(b[0]-b[4])))

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
    b = True
    while b:
        point = sorted(points_0, key=lambda p: (-p[1], p[0]))

        for i in range(len(point)-1):
            if point[i][1] == point[i+1][1] and point[i][0] < point[i+1][0]:
                point[i], point[i+1] = point[i+1], point[i]

        b = True
        if point:
            for i in point:
                if i[0] > points_1[-1][0] and i[1] <= points_1[-1][1]:
                    points_0.remove(i)
                    points_1.append(i)
                    b = True
                    break
                else:
                    b = False
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
    b = True
    while b:
        point = sorted(points_0, key=lambda p: (p[1], -p[0]))
        b = True
        if point:
            for i in point:
                if i[0] < points_1[-1][0] and i[1] >= points_1[-1][1]:
                    points_0.remove(i)
                    points_1.append(i)
                    b = True
                    break
                else:
                    b = False
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


