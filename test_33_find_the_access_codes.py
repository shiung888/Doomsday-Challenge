from c33_find_the_access_codes import solution

def test1():
    assert solution([1, 2, 3, 4, 5, 6]) == 3

def test2():
    assert solution([1, 1, 1]) == 1

def test3():
    assert solution([1, 1, 1, 1]) == 4

def test4():
    assert solution([1, 1, 1, 1, 1]) == 10

