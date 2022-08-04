
import matplotlib.pyplot as plt
from scipy import stats
from spotlight import solver

def func(p):
    """ Executed for each set of drawn parameters in the optimization search.
    """

    # get the x and y values from Mystic
    x, y = p[0], p[1]

    # get value at 2-D Gaussian function x and y
    var = stats.multivariate_normal(mean=[0, 0], cov=[[0.5, 0],[0, 0.5]])
    stat = -50.0 * var.pdf([x, y])

    # set sign of function
    # a positive lets you search for minimum
    # a negative lets you search for maximum
    stat *= 1.0

    return stat

s = solver.Solver([-9.5, -9.5], [9.5, 9.5],
                  local_solver="powell",
                  sampling_method="uniform")

s.solve(func)

print(s.solution)
