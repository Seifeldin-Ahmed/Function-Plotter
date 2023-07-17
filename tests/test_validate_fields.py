from plotter_function import Plotter_Function


def test_validate_fields_valid_input():
    obj = Plotter_Function()
    # Test the function with valid inputs
    assert obj.validate_fields("x+2", "1", "10") == (0, 1, 10)

def test_validate_fields_empty_input():
    obj = Plotter_Function()
    # Test the function with empty input fields
    assert obj.validate_fields("", "1", "10") == (1, "1", "10")

def test_validate_fields_non_numeric_min_value():
    obj = Plotter_Function()
    # Test the function with a non-numeric min_value_of_x
    assert obj.validate_fields("x+2", "abc", "10") == (2, "abc", "10")

def test_validate_fields_non_numeric_max_value():
    obj = Plotter_Function()
    # Test the function with a non-numeric max_value_of_x
    assert obj.validate_fields("x+2", "1", "xyz") == (3, 1, "xyz")

def test_validate_fields_min_greater_than_max():
    obj = Plotter_Function()
    # Test the function with min_value_of_x >= max_value_of_x
    assert obj.validate_fields("x+2", "10", "1") == (4, 10, 1)

def test_validate_fields_invalid_function():
    obj = Plotter_Function()
    # Test the function with an invalid function input
    assert obj.validate_fields("x+", "1", "10") == (5, 1, 10)
