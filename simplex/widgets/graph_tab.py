from math import atan2

import context
from PySide2.QtCore import QPoint, Qt
from PySide2.QtGui import (QBrush, QFont, QImage, QPainter, QPaintEvent, QPen,
                           QPolygon)
from PySide2.QtWidgets import QCheckBox, QFrame, QGridLayout, QSlider, QWidget
from utils.math import (get_max_solution, get_min_solution, get_plot_points,
                        get_task_data)


class GraphTab(QWidget):
    def __init__(self):
        super().__init__()
        self.graph_scale = 10
        self.init_widgets()

    def init_widgets(self):
        # create layout for tab widgets
        layout = QGridLayout()
        layout.setHorizontalSpacing(60)
        layout.setVerticalSpacing(150)

        # set widgets
        self.scale_slider = QSlider(Qt.Vertical, self)
        self.scale_slider.valueChanged[int].connect(self.on_slider_change)  # type: ignore
        self.scale_slider.setRange(10, 100)
        self.scale_slider.setSliderPosition(10)
        self.scale_slider.setTickInterval(10)
        self.scale_slider.setSingleStep(10)
        layout.addWidget(self.scale_slider, 0, 1, 0, 1)

        self.polygon_checkbox = QCheckBox('Область решений', self)
        self.polygon_checkbox.stateChanged.connect(self.update)  # type: ignore
        self.polygon_checkbox.toggle()
        layout.addWidget(self.polygon_checkbox, 0, 0)

        self.vector_checkbox = QCheckBox('Вектор', self)
        self.vector_checkbox.stateChanged.connect(self.update)  # type: ignore
        self.vector_checkbox.toggle()
        layout.addWidget(self.vector_checkbox, 1, 0)

        self.points_checkbox = QCheckBox('Точки входа и выхода', self)
        self.points_checkbox.stateChanged.connect(self.update)  # type: ignore
        self.points_checkbox.toggle()
        layout.addWidget(self.points_checkbox, 2, 0)

        self.marks_checkbox = QCheckBox('Разметка', self)
        self.marks_checkbox.stateChanged.connect(self.update)  # type: ignore
        self.marks_checkbox.toggle()
        layout.addWidget(self.marks_checkbox, 3, 0)

        self.paint_box = QFrame()
        self.paint_box.setFrameStyle(QFrame.Box)
        self.graph = QImage(self.paint_box.size(), QImage.Format_ARGB32)
        layout.addWidget(self.paint_box, 0, 2, 0, 1)

        self.setLayout(layout)

    def on_slider_change(self, value: int):
        self.graph_scale = value
        self.update()

    def paintEvent(self, event: QPaintEvent):
        a_data, b_data = get_task_data(context.input_data)
        plot_points = get_plot_points(b_data)
        if not plot_points:
            return

        xs_min, _, _ = get_min_solution(a_data, b_data, plot_points)
        min_point = (xs_min[0], xs_min[1])

        xs_max, _, _ = get_max_solution(a_data, b_data, plot_points)
        max_point = (xs_max[0], xs_max[1])

        self.graph = QImage(self.paint_box.size(), QImage.Format_ARGB32)
        self.graph.fill(Qt.white)

        if self.marks_checkbox.isChecked():
            self.draw_ticks(self.graph)

        if self.polygon_checkbox.isChecked():
            self.draw_polygon(self.graph, list(plot_points.values()))

        self.draw_lines(self.graph, b_data)

        if self.vector_checkbox.isChecked():
            self.draw_vector(self.graph, a_data)

        if self.points_checkbox.isChecked():
            self.draw_points(self.graph, a_data, list(plot_points.values()), min_point, max_point)

        p = QPainter(self)
        p.drawImage(self.paint_box.pos(), self.graph)
        p.end()

    def draw_ticks(self, graph: QImage):
        width = self.paint_box.width()
        height = self.paint_box.height()

        k = 150 // self.graph_scale

        qp = QPainter(graph)
        qp.setPen(QPen(Qt.lightGray, self.graph_scale // 40 + 1))

        for i in range(0, width, self.graph_scale):
            qp.drawLine(i, 0, i, height)

        for i in range(0, height, self.graph_scale):
            qp.drawLine(0, height-i, width, height-i)

        qp.setPen(QPen(Qt.black, 3))
        qp.drawLine(
            k * self.graph_scale, 0,
            k * self.graph_scale, height
        )
        qp.drawLine(
            0, height - k * self.graph_scale,
            width, height - k * self.graph_scale
        )
        qp.end()

    def draw_lines(self, graph: QImage, b_data: list[float]):
        width = self.paint_box.width()
        height = self.paint_box.height()

        k = 150 // self.graph_scale
        x_0 = k * self.graph_scale
        y_0 = height - k * self.graph_scale

        qp = QPainter(graph)

        qp.setPen(QPen(Qt.darkGreen, 3))
        # L1
        qp.drawLine(x_0, y_0, x_0, 0)
        # L2
        qp.drawLine(x_0, y_0, width, y_0)
        # L3
        qp.drawLine(
            round(x_0 + b_data[2] * self.graph_scale), y_0,
            round(x_0 + b_data[2] * self.graph_scale), 0
        )
        # L4
        qp.drawLine(
            x_0, round(y_0 - b_data[3] * self.graph_scale),
            width, round(y_0 - b_data[3] * self.graph_scale)
        )
        # L5
        qp.drawLine(
            round(x_0 + b_data[0] * self.graph_scale), y_0,
            x_0, round(y_0 - b_data[0] * self.graph_scale)
        )
        # L6
        qp.drawLine(
            round(x_0 + abs(b_data[0] - b_data[4]) * self.graph_scale), y_0,
            x_0, round(y_0 - abs(b_data[0] - b_data[4]) * self.graph_scale)
        )
        # Numbers
        qp.setPen(QPen(Qt.red, 2))
        qp.setFont(QFont('Times', 10))

        qp.drawText(x_0 - 20, y_0 + 25, '0')
        qp.drawText(round(x_0 + b_data[2] * self.graph_scale - 10), y_0 + 25, str(b_data[2]))
        qp.drawText(x_0 - 30, round(y_0 - b_data[3] * self.graph_scale + 10), str(b_data[3]))
        qp.drawText(round(x_0 + b_data[0] * self.graph_scale - 10), y_0 + 25, str(b_data[0]))
        qp.drawText(x_0 - 30, round(y_0 - abs(b_data[0] - b_data[4])
                    * self.graph_scale + 10), str(abs(b_data[0] - b_data[4])))

        qp.end()

    def draw_points(
        self,
        graph: QImage,
        a_data: list[float],
        points: list[tuple[float, float]],
        min_point: tuple[float, float],
        max_point: tuple[float, float]
    ):
        height = self.paint_box.height()

        k = 150 // self.graph_scale
        x_0 = k * self.graph_scale
        y_0 = height - k * self.graph_scale

        x_1 = a_data[0] - a_data[2] - a_data[3] + a_data[5]
        x_2 = a_data[1] - a_data[2] - a_data[4] + a_data[5]

        qp = QPainter(graph)
        for point in points:
            if point == min_point or point == max_point:
                qp.setPen(QPen(Qt.red, 3))
                qp.drawLine(
                    round(k * self.graph_scale + x_2 * self.graph_scale + point[0] * self.graph_scale),
                    round(height - k * self.graph_scale + x_1 * self.graph_scale - point[1] * self.graph_scale),
                    round(k * self.graph_scale - x_2 * self.graph_scale + point[0] * self.graph_scale),
                    round(height - k * self.graph_scale - x_1 * self.graph_scale - point[1] * self.graph_scale)
                )
            else:
                qp.setPen(QPen(Qt.black, 3))

            qp.setBrush(QBrush(Qt.white))
            qp.drawEllipse(
                round(x_0 + point[0] * self.graph_scale - 7), round(y_0 - point[1] * self.graph_scale - 7),
                14, 14
            )
        qp.end()

    def draw_polygon(self, graph: QImage, points: list[tuple[float, float]]):
        height = self.paint_box.height()

        centroid = tuple(map(lambda l: sum(l) / len(l), zip(*points)))
        points_with_angles = [(point, atan2(point[1]-centroid[1], point[0]-centroid[0])) for point in points]
        sorted_points = [point[0] for point in sorted(points_with_angles, key=lambda point: point[1])]

        k = 150 // self.graph_scale
        x_0 = k * self.graph_scale
        y_0 = height - k * self.graph_scale

        polygon = QPolygon(
            [
                QPoint(
                    round(x_0 + (i[0] * self.graph_scale)),
                    round(y_0 - (i[1] * self.graph_scale))
                ) for i in sorted_points
            ]
        )

        qp = QPainter(graph)
        qp.setBrush(QBrush(Qt.blue, Qt.Dense6Pattern))
        qp.drawPolygon(polygon)  # type: ignore
        qp.end()

    def draw_vector(self, graph: QImage, a_data: list[float]):
        height = self.paint_box.height()

        k = 150 // self.graph_scale
        x_1 = a_data[0]-a_data[2]-a_data[3]+a_data[5]
        x_2 = a_data[1]-a_data[2]-a_data[4]+a_data[5]

        qp = QPainter(graph)
        qp.setPen(QPen(Qt.red, 3))
        qp.drawLine(
            round(k * self.graph_scale),
            round(height - k * self.graph_scale),
            round(k * self.graph_scale + x_1 * self.graph_scale * 5),
            round(height - k * self.graph_scale - x_2 * self.graph_scale * 5)
        )
        qp.drawLine(
            round(k * self.graph_scale+x_2*5), round(height-k * self.graph_scale+x_1*5),
            round(k * self.graph_scale-x_2*5), round(height-k * self.graph_scale-x_1*5)
        )
        qp.end()
