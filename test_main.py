import pytest
from main import SparseArray


def test_sparse_array_getitem():
    arr = SparseArray(default_value=0, values=[1, 0, 3, 0, 5])
    assert arr[0] == 1
    assert arr[1] == 0
    assert arr[2] == 3
    assert arr[3] == 0
    assert arr[4] == 5
    assert arr[5] == 0


def test_sparse_array_setitem():
    arr = SparseArray(default_value=0)
    arr[2] = 7
    arr[5] = 9
    assert arr[2] == 7
    assert arr[5] == 9
    assert len(arr) == 6


def test_sparse_array_delitem():
    arr = SparseArray(default_value=0, values=[1, 2, 3])
    del arr[1]
    assert arr[0] == 1
    assert arr[1] == 0
    assert len(arr) == 2


def test_sparse_array_len():
    arr = SparseArray(default_value=0, values=[1, 0, 3, 0, 5])
    assert len(arr) == 5


def test_sparse_array_str():
    arr = SparseArray(default_value=0, values=[1, 0, 3, 0, 5])
    assert str(arr) == "[1, 0, 3, 0, 5]"


def test_sparse_array_contains():
    arr = SparseArray(default_value=0, values=[1, 0, 3, 0, 5])
    assert 3 in arr
    assert 2 not in arr


def test_sparse_array_check_index_range():
    arr = SparseArray(default_value=0, values=[1, 0, 3, 0, 5])
    with pytest.raises(IndexError):
        arr.check_index_range(5)
    with pytest.raises(IndexError):
        arr.check_index_range(10)


def test_sparse_array_add_value():
    arr = SparseArray(default_value=0, values=[1, 0, 3])
    arr.add_value(7)
    assert arr[3] == 7
    assert len(arr) == 4


pytest.main()
