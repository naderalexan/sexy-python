"""
Using iterators to check for one and only one truthy in a list
"""


def single_truthy_val(arr):
    my_iter = iter(arr)
    return any(my_iter) and not any(my_iter)


if __name__ == "__main__":
    arr = [0, 1, 0, 0]
    assert single_truthy_val(arr)

    arr = [0, 1, 0, 0, 1]
    assert not single_truthy_val(arr)
