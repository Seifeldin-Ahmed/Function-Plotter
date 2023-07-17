from plotter_function import Plotter_Function

def test_evaluate_function_linear():
    obj = Plotter_Function()
    func_str = "x+2"
    x_min = 1
    x_max = 5
    x_list, y_list = obj.evaluate_function(func_str, x_min, x_max)
    assert x_list == [1, 2, 3, 4, 5]
    assert y_list == [3, 4, 5, 6, 7]

def test_evaluate_function_quadratic():
    obj = Plotter_Function()
    func_str = "x**2"
    x_min = -2
    x_max = 2
    x_list, y_list = obj.evaluate_function(func_str, x_min, x_max)
    assert x_list == [-2, -1, 0, 1, 2]
    assert y_list == [4, 1, 0, 1, 4]
