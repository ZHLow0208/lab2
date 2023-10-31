import lab2_1 as lab2

def test_find_min_max():
    numList = [20,25,70,11]
    result = lab2.find_min_max(numList)
    assert (result == [70,11])

def test_calc_average():
    numList = [20,25,70,11]
    result = lab2.calc_average(numList)
    assert (result == 31.5)

def test_calc_median_temperature():
    numList = [20, 25, 70, 11]
    result = lab2.calc_median_temperature(numList)
    assert (result == 22.5)