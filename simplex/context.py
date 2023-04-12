"""This script declares global variables that are used in a mathematical optimization problem."""

from typing import Optional


# solve_mode specifies the type of solution being sought (in this case, 'Minimum'). 
solve_mode = 'Minimum'

# input_data is a list of lists of optional floats that represents the input data to be optimized. 
input_data: list[list[Optional[float]]] = []

# data_align is a string that specifies how the data is to be aligned. 
data_align: str = 'Vertical'

# answer_xs is a list of floats that represents the optimized variables. 
answer_xs: list[float] = []

# answer_b_data is a list of floats that represents the constraints on the variables. 
answer_b_data: list[float] = []

# answer_endless is a boolean that indicates whether the optimization problem has no feasible solution. 
answer_endless: bool = False

# answer_f is a float that represents the optimized objective function value.
answer_f: float = 0
