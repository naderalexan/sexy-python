"""
Fastest way to flatten list of lists (probably)

Source: https://stackoverflow.com/a/45323085/1223945
"""

import functools
import operator


def flatten(arr):
    return functools.reduce(operator.iconcat, arr, [])


if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6]]
    arr = flatten(arr)
    print(arr)
