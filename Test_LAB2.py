import LAB2 as lab2

print ("Test_Lab2.lab2")

def test_find_min_max():
    input_arr = [1,2,3]
    test_arr = [1,3]

    result = lab2.find_min_max(input_arr)

    assert (result == test_arr)

def test_calc_average():
    #result = ""
    input_arr = [1,2,3]

    result = lab2.calc_average(input_arr)

    assert (result == '2.0')

def test_calc_median_temperature():
    #result = ""
    input_arr = [1,2,3]

    result = lab2.calc_median(input_arr)

    assert (result == '2')