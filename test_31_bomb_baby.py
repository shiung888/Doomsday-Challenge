from c31_bomb_baby import solution

def test_1():
    assert solution('4', '7') == '4'

def test_2():
    assert solution('2', '1') == '1'

def test_3():
    assert solution('2', '4') == 'impossible'

def test_4():
    assert solution('2', '6') == 'impossible'

def test_5():
    assert solution('3', '6') == 'impossible'

def test_6():
    assert solution('3', '5') == '3'

def test_7():
    assert solution('5', '8') == '4'

def test_8():
    assert solution('5', '9') == '5'

def test_9():
    assert solution('5', '3') == '3'

def test_10():
    assert solution('8', '5') == '4'

def test_11():
    assert solution('8', '21') == '6'

def test_12():
    x = '99999999999999999999999999999999999999999999684225'
    y = '99999999999999999999999999999999999999999999600827'
    assert solution(x, y) == '1199069522050888510515839708386292237223914395'
