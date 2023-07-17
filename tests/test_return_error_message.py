from plotter_function import Plotter_Function


def test_return_error_message_empty_field():
    obj = Plotter_Function()
    assert obj.return_error_message(1) == "There's an Empty Input Field"


def test_return_error_message_non_numeric_xmin():
    obj = Plotter_Function()
    assert obj.return_error_message(2) == "The Minimum Value of x is Not a Number"


def test_return_error_message_non_numeric_xmax():
    obj = Plotter_Function()
    assert obj.return_error_message(3) == "The Maximum Value of x is Not a Number"


def test_return_error_message_xmin_greater_than_xmax():
    obj = Plotter_Function()
    assert obj.return_error_message(4) == "The Minimum Value of x are greater than or equal Maximum Value of x"


def test_return_error_message_invalid_function():
    obj = Plotter_Function()
    assert obj.return_error_message(5) == "Input Function Must be a Function of x"


def test_return_error_message_invalid_inputs():
    obj = Plotter_Function()
    assert obj.return_error_message(7) == "Invalid Input"


