from c32_the_grandest_staircase_of_them_all import solution

def test1():
    assert solution(3) == 1

def test2():
    assert solution(4) == 1

def test3():
    assert solution(5) == 2

def test4():
    assert solution(6) == 3

def test5():
    assert solution(7) == 4

def test6():
    assert solution(8) == 5

def test7():
    assert solution(9) == 7

def test8():
    assert solution(10) == 9

def test9():
    assert solution(200) == 487067745
