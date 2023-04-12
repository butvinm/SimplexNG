from typing import Optional

from xlrd import open_workbook
from xlrd.book import Book
from xlrd.sheet import Sheet
from xlwt import Workbook


def get_workbook() -> Workbook:
    """Creates a new instance of Workbook.

    Returns:
        Workbook: A new instance of Workbook.
    """
    return Workbook()


def load_task(file: str) -> list[list[str]]:
    """Loads a task from an Excel file.

    Args:
        file (str): The path to the Excel file.

    Returns:
        list[list[str]]: A list of lists of strings representing the task data.
    """
    # Open the workbook
    book: Book = open_workbook(file)
    # Get the sheet named 'Условие'
    sheet: Sheet = book.sheet_by_name('Условие')

    # Extract the data from the sheet
    data: list[list[str]] = [
        [
            sheet.cell_value(r, c) for c in range(1, sheet.ncols)
        ]
        for r in range(1, sheet.nrows)
    ]

    return data


def write_task(wb: Workbook, data: list[list[Optional[float]]]):
    """Writes a task to a Workbook.

    Args:
        wb (Workbook): The Workbook to write to.
        data (list[list[Optional[float]]]): A list of lists of optional floats representing the task data.
    """
    # Create a new sheet in the workbook named 'Условие'
    ws = wb.add_sheet('Условие', cell_overwrite_ok=True)

    # Write the column headers
    ws.write(0, 1, 'A')
    ws.write(0, 2, 'B')
    ws.write(0, 3, 'C')
    ws.write(0, 4, 'D')
    ws.write(1, 0, 'I')
    ws.write(2, 0, 'II')
    ws.write(3, 0, 'III')
    ws.write(4, 0, 'IV')

    # Write the data to the sheet
    for i in range(len(data)):
        for j in range(len(data[i])):
            value = f'{data[i][j]:.2f}' if data[i][j] is not None else ''
            ws.write(i + 1, j + 1, value)


def write_answer(wb: Workbook, data_align: str, b_data: list[float], xs: list[float], f: float, endless: bool):
    """
    Writes the results of the optimization task to a new sheet in the specified workbook.

    Args:
        wb (Workbook): The workbook to write the results to.
        data_align (str): The alignment of the input data in the resulting table. Valid options are "Horizontal" and "Vertical".
        b_data (list[float]): The array of the constant terms from the optimization task constraints.
        xs (list[float]): The array of the decision variables of the optimization task.
        f (float): The optimal objective function value.
        endless (bool): Whether the optimization task has an infinite optimal objective function value.

    Returns:
        None
    """
    ws = wb.add_sheet('Решение', cell_overwrite_ok=True)

    # Write the column and row headers for the table
    ws.write(0, 1, 'A')
    ws.write(0, 2, 'B')
    ws.write(0, 3, 'C')
    ws.write(0, 4, 'D')
    ws.write(1, 0, 'I')
    ws.write(2, 0, 'II')
    ws.write(3, 0, 'III')
    ws.write(4, 0, 'IV')

    # Determine the mapping of the constant terms and decision variables to table positions based on the input data alignment
    if data_align == 'Vertical':
        b_items = {
            (3, 0): b_data[0],
            (3, 1): b_data[1],
            (2, 3): b_data[2],
            (1, 3): b_data[3],
            (0, 3): b_data[4],
        }
        xs_items = {
            (0, 0): xs[0],
            (0, 1): xs[1],
            (1, 0): xs[2],
            (1, 1): xs[3],
            (2, 0): xs[4],
            (2, 1): xs[5],
        }
    else:
        b_items = {
            (0, 3): b_data[0],
            (1, 3): b_data[1],
            (3, 0): b_data[2],
            (3, 1): b_data[3],
            (3, 2): b_data[4],
        }
        xs_items = {
            (0, 0): xs[0],
            (0, 1): xs[1],
            (0, 2): xs[2],
            (1, 0): xs[3],
            (1, 1): xs[4],
            (1, 2): xs[5],
        }

    # Write the constant terms to the table
    for pos, b in b_items.items():
        ws.write(pos[0] + 1, pos[1] + 1, str(b))

    # Write the decision variables to the table
    for pos, x in xs_items.items():
        ws.write(pos[0] + 1, pos[1] + 1, str(x))

    # Write the optimal objective function value to the table
    ws.write(4, 4, 'F=' + str(f))

    # Write whether the optimization task has an infinite optimal objective function value to the table
    if endless:
        ws.write(3, 3, 'Бесконечное')
    else:
        ws.write(3, 3, 'Конечное')
