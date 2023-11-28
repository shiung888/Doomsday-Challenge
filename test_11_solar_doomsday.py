from c11_solar_doomsday_solution import solution

def test1():
    assert solution(15324) == [15129, 169, 25, 1]

def test2():
    assert solution(12) == [9, 1, 1, 1]

def test3():
    assert solution(15) == [9, 4, 1, 1]
