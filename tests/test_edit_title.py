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

def test_edit_title_with_no_plot(gui, mocker):

    plotter = Plotter_Function()
    message_box_mock = mocker.patch.object(QMessageBox, 'warning')

    # Call the function we want to test
    plotter.edit_title(self_of_gui_object=gui)

    assert not gui.figure.axes
    message_box_mock.assert_called_once()
    # extracts the arguments and keyword arguments passed to a message_box_mock object when it was called.
    args, kwargs = message_box_mock.call_args
    # args[2] refers to the third element of the args tuple, which is the message text
    assert args[2] == "Please plot the function first before changing the title"


# ( the user entered title = "my plot" and then pressed ok )
def test_edit_title_with_plot_exist_and_Data_Entered(gui, mocker):

    plotter = Plotter_Function()
    plotter.ax = gui.figure.add_subplot(111)  # add a plot first to make ax not None

    # Call the function we want to test
    plotter.edit_title(self_of_gui_object=gui)

    # Assert that the title has been changed to the desired title
    assert plotter.ax.get_title() == "my plot"


# ( the user pressed cancel )
def test_edit_title_with_plot_exist_and_No_Data_Entered(gui, mocker):

    plotter = Plotter_Function()
    plotter.ax = gui.figure.add_subplot(111)  # add a plot first to make ax not None

    # Call the function we want to test
    plotter.edit_title(self_of_gui_object=gui)

    # Assert that the title doesn't change
    assert plotter.ax.get_title() == ""
