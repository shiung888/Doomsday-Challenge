from c22_ion_flux_relabeling import solution

def test_1():
    assert solution(3, [7, 3, 5, 1]) == [-1, 7, 6, 3]

def test_2():
    assert solution(5, [19, 14, 28]) == [21, 15, 29]

def test_3():
    h = 30
    q = [14, 17, 2, 15, 963778942, 928893203, 985399664, 631052492]
    p = [15, 18, 3, 31, 963778946, 928893204, 985399665, 631052493]
    assert solution(h, q) == p
