from math import atan, degrees
from typing import Optional


from typing import Optional, List, Tuple


def get_data_align(data: List[List[Optional[float]]]) -> str:
    """Determine the alignment of the input data table.

    Args:
        data (List[List[Optional[float]]]): A 2D list of float values.

    Returns:
        str: The alignment of the table. Either 'Horizontal' or 'Vertical'.
    """

    # Check if the second row of the table contains any non-None values.
    # If it does, then the table is aligned horizontally, otherwise vertically.
    align = 'Horizontal' if data[1][2] is not None else 'Vertical'

    return align


def get_task_data(data: List[List[Optional[float]]]) -> Tuple[List[float], List[float]]:
    """Extract the task data (A and B values) from the input data table.

    Args:
        data (List[List[Optional[float]]]): A 2D list of float values.

    Returns:
        Tuple[List[float], List[float]]: A tuple of two 1D lists.
            The first list contains the A values, and the second list contains the B values.
    """

    # Determine the alignment of the input data table.
    align = get_data_align(data)

    # Extract the A and B values from the input data table based on the alignment.
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

    # Check if any item in the A or B data lists is None.
    # If any item is None, then raise a ValueError.
    if any(value is None for value in a_data + b_data):
        raise ValueError('Incorrect input data: empty items')

    # Return the A and B data lists as a tuple.
    return a_data, b_data  # pyright: reportGeneralTypeIssues=none


def get_plot_points(b_data: list[float]) -> dict[int, tuple[float, float]]:
    """Some weird math stuff that find points for plot.

    The function takes a list of five float values as input, representing the constrains for a simplex optimization problem. 
    The function uses a series of 12 mathematical formulas to determine the points on the graph that are relevant for the given optimization problem. 
    Each formula checks for a specific condition that must be met for a point to be included in the dictionary of plot points. 
    The formulas are numbered from 1 to 12 in the code, and each formula corresponds to a specific pair of vertices on the simplex.

    Args:
        b_data: A list of five float values representing the data for a simplex optimization problem.

    Returns:
        A dictionary with integer keys and tuple values, where each key represents a point on a graph and the value is a tuple containing its x and y coordinates.

    Raises:
        ValueError: If any of the first three values in the input list are negative.

    """

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
    """ Given input data describing a linear programming problem in standard form, this function returns the minimum solution
    using the simplex method. The input data consists of:
    - a_data: a list of coefficients for the objective function
    - b_data: a list of constraints (i.e., the right-hand side of the equations)
    - points: a dictionary mapping variable indices to (x, y) coordinates for plotting purposes

    The simplex method involves iteratively improving a basic feasible solution until an optimal solution is reached.
    To apply the simplex method, we first convert the problem into standard form by introducing slack variables.
    The resulting tableau is then iteratively pivoted until the optimal solution is found.

    The function returns a tuple containing:
    - xs_min: a list of the optimal values of the decision variables
    - f_min: the minimum value of the objective function
    - min_endless: a boolean indicating whether the solution is unbounded

    Note that the function assumes that the problem is feasible and bounded. If the problem is infeasible or unbounded,
    the function may raise an exception or return incorrect results.
    """

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
    """ Given input data describing a linear programming problem in standard form, this function returns the maximum solution
    using the simplex method. The input data consists of:
    - a_data: a list of coefficients for the objective function
    - b_data: a list of constraints (i.e., the right-hand side of the equations)
    - points: a dictionary mapping variable indices to (x, y) coordinates for plotting purposes

    The simplex method involves iteratively improving a basic feasible solution until an optimal solution is reached.
    To apply the simplex method, we first convert the problem into standard form by introducing slack variables.
    The resulting tableau is then iteratively pivoted until the optimal solution is found.

    The function returns a tuple containing:
    - xs_max: a list of the optimal values of the decision variables
    - f_max: the maximum value of the objective function
    - max_endless: a boolean indicating whether the solution is unbounded

    Note that the function assumes that the problem is feasible and bounded. If the problem is infeasible or unbounded,
    the function may raise an exception or return incorrect results.
    """

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
