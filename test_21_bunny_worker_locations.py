from c21_bunny_worker_locations_solution import solution

def test_1():
    assert solution(5, 10) == '96'

def test_2():
    assert solution(3, 2) == '9'

def test_3():
    assert solution(100000, 100000) == '19999800001'
