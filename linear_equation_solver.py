"""
3-liner for solving linear equations

Source: https://code.activestate.com/recipes/365013/
"""


def solve(eq, var="x"):
    eq1 = eq.replace("=", "-(") + ")"
    c = eval(eq1, {var: 1j})
    return -c.real / c.imag


if __name__ == "__main__":
    equation = "x - 2*x + 5*x - 46*(235-24) = x + 2"
    print(solve(equation))
