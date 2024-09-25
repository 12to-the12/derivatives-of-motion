from src.vector import Vector


def test_mag():
    assert Vector([1]).mag == 1
    assert round(Vector([1, 1]).mag, 2) == 1.41


def test_dot():
    assert round(Vector([1, 1]) @ Vector([1, 1]), 2) == 2


def test_mult():

    assert (Vector([1, 1]) * Vector([1, 1])).vector == Vector([1, 1]).vector
    assert (Vector([2]) * 5).vector == Vector([10]).vector

    assert (Vector([5]) * 5.0).vector == Vector([25]).vector

    assert (Vector([1, 2]) * 4).vector == Vector([4, 8]).vector
    assert (Vector([2, 1]) * 3.3).vector == Vector([6.6, 3.3]).vector


def test_add():
    assert (Vector([1]) + Vector([2])).vector == Vector([3]).vector

    assert (Vector([1, 1]) + Vector([1, 2])).vector == Vector([2, 3]).vector

    assert (Vector([5, 7, 9]) + Vector([3, 2, 1])).vector == Vector([8, 9, 10]).vector
