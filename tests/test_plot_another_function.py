import pytest
from plotter_function import Plotter_Function
from PySide2.QtWidgets import QMainWindow, QMessageBox
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.figure = Figure()  # creating a figure
        self.canvas = FigureCanvas(self.figure)  # Create a FigureCanvas

@pytest.fixture
def gui(qtbot):
    """Create and return a GUI instance."""
    gui = GUI()
    qtbot.addWidget(gui)
    return gui


# The mocker fixture is used to create mock objects that can replace dependencies in the code during testing.

def test_plot_another_function_with_no_plot(gui, mocker):

    plotter = Plotter_Function()
    message_box_mock = mocker.patch.object(QMessageBox, 'warning')

    # Call the function we want to test
    plotter.plot_another_function(self_of_gui_object=gui, function='x**2', min_value_of_x='0', max_value_of_x='10')

    assert not gui.figure.axes
    message_box_mock.assert_called_once()
    # extracts the arguments and keyword arguments passed to a message_box_mock object when it was called.
    args, kwargs = message_box_mock.call_args
    # args[2] refers to the third element of the args tuple, which is the message text
    assert args[2] == "there is no plot"


def test_plot_another_function_with_plot_exist_and_valid_inputs(gui, mocker):

    plotter = Plotter_Function()
    plotter.ax = gui.figure.add_subplot(111)  # add a plot first to make ax not None

    # Mock the validate_fields method to return 0 (no errors)
    # Mock the evaluate_function method to return the desired x,y
    mocker.patch.object(plotter, 'validate_fields', return_value=(0, 0, 10))
    mocker.patch.object(plotter, 'evaluate_function', return_value=([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]))

    # Call the function we want to test
    plotter.plot_another_function(self_of_gui_object=gui, function='x+1', min_value_of_x='0', max_value_of_x='10')

    # Note: plotter.ax.lines is a list of line objects that represent the plotted lines in a Matplotlib plot.
    assert plotter.ax.lines[0].get_xydata().tolist() == [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81], [10, 100]]



def test_plot_another_function_with_plot_exist_and_invalid_inputs(gui, mocker):

    plotter = Plotter_Function()
    plotter.ax = gui.figure.add_subplot(111)  # add a plot first to make ax not None

    # Mock the validate_fields method to return 1 (empty fields)
    # Mock the return_error_message method to return the desired massage
    mocker.patch.object(plotter, 'validate_fields', return_value=(1, '', ''))
    mocker.patch.object(plotter, 'return_error_message', return_value="There's an Empty Input Field")
    message_box_mock = mocker.patch.object(QMessageBox, 'warning')

    # Call the function we want to test
    plotter.plot_another_function(self_of_gui_object=gui, function='', min_value_of_x='', max_value_of_x='')

    message_box_mock.assert_called_once()
    # extracts the arguments and keyword arguments passed to a message_box_mock object when it was called.
    args, kwargs = message_box_mock.call_args
    # args[2] refers to the third element of the args tuple, which is the message text
    assert args[2] == "There's an Empty Input Field"




