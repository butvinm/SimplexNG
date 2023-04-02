from math import atan, degrees
from typing import Optional


def get_task_data(data: list[list[Optional[float]]]) -> tuple[list[float], list[float]]:
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


def get_plot_points(b_data: list[float]) -> dict[int, tuple[float, float]]:
    """Some weird math stuff that find points for plot"""

    points: dict[int, tuple[float, float]] = {}
    if b_data[0] < 0 or b_data[2] < 0 or b_data[3] < 0:
        raise ValueError('Incorrect b_data')

    i = 0

    # 1 I--II
    if abs(b_data[4]-b_data[0]) == 0:
        if not ([0, 0] in points.values()):
            points.update({i: (0, 0)})
            i += 1

    # 2 I--III
    if b_data[2] >= b_data[0] and b_data[4] - b_data[0] <= b_data[0]:
        if not ([b_data[0], 0] in points.values()):
            points.update({i: (b_data[0], 0)})
            i += 1

    # 3 I--IV
    if b_data[2] >= abs(b_data[4]-b_data[0]) and b_data[0] >= abs(b_data[4]-b_data[0]):
        if not ([abs(b_data[4]-b_data[0]), 0] in points.values()):
            points.update({i: (abs(b_data[4]-b_data[0]), 0)})
            i += 1

    # 4 I--VI
    if b_data[0] >= b_data[2] and abs(b_data[4]-b_data[0]) <= b_data[2]:
        if not ([b_data[2], 0] in points.values()):
            points.update({i: (b_data[2], 0)})
            i += 1

    # 5 II--III
    if b_data[3] >= b_data[0] and abs(b_data[4]-b_data[0]) <= b_data[0]:
        if not ([0, b_data[0]] in points.values()):
            points.update({i: (0, b_data[0])})
            i += 1

    # 6 II--V
    if b_data[0] >= b_data[3] and abs(b_data[4]-b_data[0]) <= b_data[3]:
        if not ([0, b_data[3]] in points.values()):
            points.update({i: (0, b_data[3])})
            i += 1

    # 7 II--IV
    if b_data[0] >= abs(b_data[4]-b_data[0]) and b_data[3] >= abs(b_data[4]-b_data[0]):
        if not ([0, abs(b_data[4]-b_data[0])] in points.values()):
            points.update({i: (0, abs(abs(b_data[4]-b_data[0])))})
            i += 1

    # 8 III-V
    if b_data[3] <= b_data[0] and b_data[2] >= b_data[0]-b_data[3] and abs(b_data[4]-b_data[0]) <= b_data[0]:
        if not ([b_data[0]-b_data[3], b_data[3]] in points.values()):
            points.update({i: (b_data[0]-b_data[3], b_data[3])})
            i += 1

    # 9 III-VI
    if b_data[2] <= b_data[0] and b_data[3] >= b_data[0]-b_data[2] and abs(b_data[4]-b_data[0]) <= b_data[0]:
        if not ([b_data[2], b_data[0]-b_data[2]] in points.values()):
            points.update({i: (b_data[2], b_data[0]-b_data[2])})
            i += 1

    # 10 IV--V
    if b_data[0] >= abs(b_data[4]-b_data[0]) and b_data[2] >= abs(b_data[4]-b_data[0])-b_data[3] and b_data[3] <= abs(b_data[4]-b_data[0]):
        if not ([abs(b_data[4]-b_data[0])-b_data[3], b_data[3]] in points.values()):
            points.update({i: (abs(b_data[4]-b_data[0])-b_data[3], b_data[3])})
            i += 1

    # 11 IV--VI
    if b_data[0] >= abs(b_data[4]-b_data[0]) and b_data[3] >= abs(b_data[4]-b_data[0])-b_data[2] and b_data[2] <= abs(b_data[4]-b_data[0]):
        if not ([b_data[2], abs(b_data[4]-b_data[0])-b_data[2]] in points.values()):
            points.update({i: (b_data[2], abs(b_data[4]-b_data[0])-b_data[2])})
            i += 1

    # 12 V--VI
    if b_data[0] >= b_data[2]+b_data[3] and abs(b_data[4]-b_data[0]) <= b_data[2]+b_data[3]:
        if not ([b_data[2], b_data[3]] in points.values()):
            points.update({i: (b_data[2], b_data[3])})
            i += 1

    return points


def get_min_solution(
    a_data: list[float],
    b_data: list[float],
    points: dict[int, tuple[float, float]]
) -> tuple[list[float], float, bool]:
    """Some other weird math stuff that calculation minimum solution"""
    try:
        alfa = round(degrees(atan((a_data[1]-a_data[2]-a_data[4]+a_data[5])/(a_data[0]-a_data[2]-a_data[3]+a_data[5]))))
        alfa = 90 - alfa
    except ZeroDivisionError:
        alfa = 360

    if alfa < 0:
        alfa += 180

    with_x_min = min(points.values(), key=lambda point: point[0])
    with_y_min = min(points.values(), key=lambda point: point[1])

    min_endless_able = False
    if alfa > 45:
        ans_min = with_x_min
        for i in range(len(points)):
            if points[i][0] == with_x_min[0]:
                min_endless_able = True
                if points[i][1] < with_x_min[1]:
                    ans_min = points[i]
    else:
        ans_min = with_y_min
        for i in range(len(points)):
            if points[i][1] == with_y_min[1]:
                min_endless_able = True
                if points[i][0] < with_y_min[0]:
                    ans_min = points[i]

    xs_min = [ans_min[0],
              ans_min[1],
              b_data[0]-ans_min[0]-ans_min[1],
              b_data[2]-ans_min[0],
              b_data[3]-ans_min[1],
              b_data[4]-b_data[0]+ans_min[0]+ans_min[1]]

    f_min = sum(list(map(lambda x, y: x*y, xs_min, a_data)))

    min_endless = False
    if min_endless_able == True and alfa in [0, 45, 90]:
        min_endless = True

    return xs_min, f_min, min_endless


def get_max_solution(
    a_data: list[float],
    b_data: list[float],
    points: dict[int, tuple[float, float]]
) -> tuple[list[float], float, bool]:
    """Some other weird math stuff that calculation maximum solution"""
    try:
        alfa = round(degrees(atan((a_data[1]-a_data[2]-a_data[4]+a_data[5])/(a_data[0]-a_data[2]-a_data[3]+a_data[5]))))
        alfa = 90 - alfa
    except ZeroDivisionError:
        alfa = 360

    if alfa < 0:
        alfa += 180

    with_x_max = max(points.values(), key=lambda point: point[0])
    with_y_max = max(points.values(), key=lambda point: point[1])

    max_endless_able = False
    if alfa > 45:
        ans_max = with_x_max
        for i in range(len(points)):
            if points[i][0] == with_x_max[0]:
                max_endless_able = False
                if points[i][1] > with_x_max[1]:
                    ans_max = points[i]
    else:
        ans_max = with_y_max
        for i in range(len(points)):
            if points[i][1] == with_y_max[1]:
                max_endless_able = True
                if points[i][0] > with_y_max[0]:
                    ans_max = points[i]

    xs_max = [ans_max[0],
              ans_max[1],
              b_data[0]-ans_max[0]-ans_max[1],
              b_data[2]-ans_max[0],
              b_data[3]-ans_max[1],
              b_data[4]-b_data[0]+ans_max[0]+ans_max[1]]

    f_max = sum(list(map(lambda x, y: x*y, xs_max, a_data)))

    max_endless = False

    if max_endless_able == True and alfa in [0, 45, 90]:
        max_endless = True

    return xs_max, f_max, max_endless
