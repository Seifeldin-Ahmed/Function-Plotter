from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout, QLineEdit
import sys
from PySide2.QtGui import QIcon, QFont, QGuiApplication, QColor
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar, FigureCanvasQTAgg as FigureCanvas
from plotter_function import Plotter_Function


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Function Plotter")
        self.setGeometry(550, 350, 800, 500)  # x , y , width , height
        self.set_icon()
        self.center()
        self.create_widgets()
        self.edit_widgets()
        self.create_layout()
        self.connect_signals()

    def set_icon(self):
        app_icon = QIcon("bar.png")
        self.setWindowIcon(app_icon)

    def center(self):
        q_rect = self.frameGeometry()
        center_point = QGuiApplication.primaryScreen().availableGeometry().center()
        q_rect.moveCenter(center_point)
        self.move(q_rect.topLeft())

    def create_widgets(self):

        # creating QlineEdit widgets:
        self.input_function = QLineEdit()
        self.min_x = QLineEdit()
        self.max_x = QLineEdit()

        # creating Label widgets:
        self.label_of_input_function = QLabel("Function of x: ")
        self.label_of_min_x = QLabel("The Minimum Value of x: ")
        self.label_of_max_x = QLabel("The Maximum Value of x: ")
        self.label = QLabel("")  # to add spacing before push buttons in GUI

        # creating Push Buttons:
        self.plot_button = QPushButton("Plot")
        self.edit_title_button = QPushButton("Edit Title")
        self.edit_x_axis_label_button = QPushButton("Edit X-axis Label")
        self.edit_y_axis_label_button = QPushButton("Edit Y-axis Label")
        self.plot_again_button = QPushButton("Plot another Function")
        self.reset_button = QPushButton("Reset")

        # for plotting section:
        self.figure = Figure()                                # creating a figure
        self.canvas = FigureCanvas(self.figure)               # Create a FigureCanvas
        self.toolbar = NavigationToolbar(self.canvas, self)   # create a Navigation Toolbar

    def edit_widgets(self):
        self.edit_QlineEdit()
        self.edit_labels()
        self.edit_push_buttons()

    def edit_QlineEdit(self):
        self.input_function.setPlaceholderText("Enter your function here...")
        self.min_x.setPlaceholderText("Enter The Min Value Of x...")
        self.max_x.setPlaceholderText("Enter The Max Value Of x...")
        self.input_function.setStyleSheet("background-color: #FFFFFF ;")  # make the color: white
        self.min_x.setStyleSheet("background-color: #FFFFFF ;")           # make the color: white
        self.max_x.setStyleSheet("background-color: #FFFFFF ;")           # make the color: white

    def edit_labels(self):

        # set Fixed Size for all labels
        self.label_of_input_function.setFixedSize(250, 30)
        self.label_of_min_x.setFixedSize(250, 30)
        self.label_of_max_x.setFixedSize(250, 30)

        # create object from QFont() Class:
        # Font Name: "Times New Roman"
        # Fone Size: 12
        # make the fond bold
        self.font = QFont("Times New Roman", 12, QFont.Bold)

        # Set the font for all labels
        self.label_of_input_function.setFont(self.font)
        self.label_of_min_x.setFont(self.font)
        self.label_of_max_x.setFont(self.font)

    def edit_push_buttons(self):

        color = QColor.fromRgb(44, 131, 215)   # create object from QColor class with a blue color
        self.font.setPointSize(10)             # edit font size and make it with size = 10

        # Set the font for all push buttons
        self.plot_button.setFont(self.font)
        self.edit_title_button.setFont(self.font)
        self.edit_x_axis_label_button.setFont(self.font)
        self.edit_y_axis_label_button.setFont(self.font)
        self.plot_again_button.setFont(self.font)
        self.reset_button.setFont(self.font)

        # edit style of all push buttons:
        # make the color: blue as specifed with rgb = 44,131,215
        # make the corners of each button rounded with border_radius 10px, border width 5px and solid border style
        # make a hover (when the mouse enter the button area, make the color light gray)
        self.plot_button.setStyleSheet(" QPushButton{ background-color: " + color.name() + " ;"
                                                                                           "border-style: solid;"
                                                                                           "border-width: 5px;"
                                                                                           "border-radius: 10px;}"
                                                                                           "QPushButton:hover{ background-color: lightgray;}"
                                       )
        self.edit_title_button.setStyleSheet(" QPushButton{ background-color: " + color.name() + " ;"
                                                                                                 "border-style: solid;"
                                                                                                 "border-width: 5px;"
                                                                                                 "border-radius: 10px;}"
                                                                                                 "QPushButton:hover{ background-color: lightgray;}"
                                             )
        self.edit_x_axis_label_button.setStyleSheet(" QPushButton{ background-color: " + color.name() + " ;"
                                                                                                        "border-style: solid;"
                                                                                                        "border-width: 5px;"
                                                                                                        "border-radius: 10px;}"
                                                                                                        "QPushButton:hover{ background-color: lightgray;}"
                                                    )
        self.edit_y_axis_label_button.setStyleSheet(" QPushButton{ background-color: " + color.name() + " ;"
                                                                                                        "border-style: solid;"
                                                                                                        "border-width: 5px;"
                                                                                                        "border-radius: 10px;}"
                                                                                                        "QPushButton:hover{ background-color: lightgray;}"
                                                    )

        self.plot_again_button.setStyleSheet(" QPushButton{ background-color: " + color.name() + " ;"
                                                                                                        "border-style: solid;"
                                                                                                        "border-width: 5px;"
                                                                                                        "border-radius: 10px;}"
                                                                                                        "QPushButton:hover{ background-color: lightgray;}"
                                             )

        self.reset_button.setStyleSheet(" QPushButton{ background-color: " + color.name() + " ;"
                                                                                                        "border-style: solid;"
                                                                                                        "border-width: 5px;"
                                                                                                        "border-radius: 10px;}"
                                                                                                        "QPushButton:hover{ background-color: lightgray;}"
                                        )

    def create_layout(self):

        # creating 3 layouts
        page_layout = QHBoxLayout()
        widgets_layout = QVBoxLayout()
        plot_layout = QVBoxLayout()

    ###################################################################################################################
        # adding label and Q lineEdit for input function to the layout
        widgets_layout.addWidget(self.label_of_input_function)
        widgets_layout.addWidget(self.input_function)

        # adding label and Q lineEdit for the minimum value of x to the layout
        widgets_layout.addWidget(self.label_of_min_x)
        widgets_layout.addWidget(self.min_x)

        # adding label and Q lineEdit for the maximum value of x to the layout
        widgets_layout.addWidget(self.label_of_max_x)
        widgets_layout.addWidget(self.max_x)

        widgets_layout.addWidget(self.label)  # label to get some spacing before the Push buttons

        # adding all buttons to the layout
        widgets_layout.addWidget(self.plot_button)
        widgets_layout.addWidget(self.edit_title_button)
        widgets_layout.addWidget(self.edit_x_axis_label_button)
        widgets_layout.addWidget(self.edit_y_axis_label_button)
        widgets_layout.addWidget(self.plot_again_button)
        widgets_layout.addWidget(self.reset_button)

        # set the left and right margins to 0 pixels
        # set the top margin to 35 and the bottom margins to 20 px
        widgets_layout.setContentsMargins(0, 35, 0, 20)

    ###################################################################################################################
        # add the navigation toolbar and plot into the layout vertically
        plot_layout.addWidget(self.toolbar)
        plot_layout.addWidget(self.canvas)

    ###################################################################################################################
        # add the widgets layout, and The Plot_Layout Horizontally
        page_layout.addLayout(widgets_layout, 25)
        page_layout.addLayout(plot_layout, 75)

    ###################################################################################################################
        # create a widget with color : gray
        widget = QWidget()                                   # create a widget
        widget.setLayout(page_layout)                        # set layout on the widget
        widget.setStyleSheet("background-color: #EDEDF4 ;")  # make the widget color: light gray
        self.setCentralWidget(widget)

    def connect_signals(self):
        obj = Plotter_Function()
        self.plot_button.pressed.connect(lambda: obj.plot(self, self.input_function.text(), self.min_x.text(), self.max_x.text()))
        self.edit_title_button.pressed.connect(lambda: obj.edit_title(self))
        self.edit_x_axis_label_button.pressed.connect(lambda: obj.edit_x_axis_label(self))
        self.edit_y_axis_label_button.pressed.connect(lambda: obj.edit_y_axis_label(self))
        self.plot_again_button.pressed.connect(lambda: obj.plot_another_function(self, self.input_function.text(), self.min_x.text(), self.max_x.text()))
        self.reset_button.pressed.connect(lambda: obj.reset(self))


myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)
