from PySide2.QtWidgets import QMessageBox, QInputDialog


class Plotter_Function:

    def __init__(self):
        self.ax = None

    def evaluate_function(self, func_str, x_min, x_max):
        y_list = []      # create a list for y values
        x_list = []      # create a list for x values
        x_values = range(x_min, x_max + 1)   # range from x_min to x_max+1 to ensure that x_max are included
        for x in x_values:
            # the eval function takes a string in a form of mathematical expression and evaluate it then return the value of the equation
            # example:  eval("x+2") if x =3, the return is 5
            # so here for each value of x, it will be substituted in func_str and the eval function will return the value of the equation for that x.
            # i used func_str.lower() because if the user entered a function X+2 instead of x+2
            y_list.append(eval(func_str))
            x_list.append(x)
        return x_list, y_list

    def validate_fields(self, function, min_value_of_x, max_value_of_x):

        if function == "" or min_value_of_x == "" or max_value_of_x == "":
            return 1, min_value_of_x, max_value_of_x    # return 1 is error type (to indicate that this error because there's empty input field)

        ################################################################################################################

        try:
            min_value_of_x = int(min_value_of_x)        # if min_value_of_x can't be converted to int, this means it's not a number
        except:
            return 2, min_value_of_x, max_value_of_x    # return 2 is error type (to indicate that this error because min_value_of_x is not a number)

        ################################################################################################################

        try:
            max_value_of_x = int(max_value_of_x)        # if max_value_of_x can't be converted to int, this means it's not a number
        except:
            return 3, min_value_of_x, max_value_of_x    # return 3 is error type (to indicate that this error because max_value_of_x is not a number)

        ################################################################################################################

        if min_value_of_x >= max_value_of_x:
            return 4, min_value_of_x, max_value_of_x    # return 4 is error type (to indicate that this error because min_value_of_x >= max_value_of_x)

        ################################################################################################################

        try:
            x = 0  # make x with any value to evaluate function
            y = eval(function)  # if function is not a mathematical expression, exception will be raised
        except (SyntaxError, TypeError, NameError):
            return 5, min_value_of_x, max_value_of_x    # return 5 is error type (to indicate that this error because function(input function) is not a mathematical expression)

        ################################################################################################################
        return 0, min_value_of_x, max_value_of_x        # if the return was 0 , it means everything is okay
        # note: the reason i returned min_value_of_x, max_value_of_x because i have converted it to int

    def plot(self, self_of_gui_object, function, min_value_of_x, max_value_of_x):

        function = function.replace('^', '**')  # Replace ^ with ** for exponentiation, because eval function treat ^ as bitwise operator not as power
        function = function.lower()             # because if the user entered a function X+2 instead of x+2
        error_status, min_value_of_x, max_value_of_x = self.validate_fields(function, min_value_of_x, max_value_of_x)

        if error_status == 0:  # means everything is okay
            x, y = self.evaluate_function(function, min_value_of_x, max_value_of_x)
            self_of_gui_object.figure.clear()
            # add a plot, First argument: The number of rows of subplots in the grid, Second argument: The number of columns of subplots in the grid, Third argument: The index of the subplot
            self.ax = self_of_gui_object.figure.add_subplot(111)   # the argument 111 indicates that the figure should have one row, one column, and the current subplot should be the first (and only) subplot.
            self.ax.plot(x, y)
            self_of_gui_object.canvas.draw()  # Redrawing the canvas is necessary when you want to update the plot with new data or changes to the plot properties

        else:
            error_message = self.return_error_message(error_status)
            QMessageBox.warning(self_of_gui_object, "Invalid Input", error_message, QMessageBox.Ok)

    def return_error_message(self, error_status):
        if error_status == 1:  # indicate that there's empty input field
            return "There's an Empty Input Field"

        elif error_status == 2:  # indicate that min_value_of_x is not a number
            return "The Minimum Value of x is Not a Number"

        elif error_status == 3:  # indicate that max_value_of_x is not a number
            return "The Maximum Value of x is Not a Number"

        elif error_status == 4:  # indicate that min_value_of_x >= max_value_of_x
            return "The Minimum Value of x are greater than or equal Maximum Value of x"

        elif error_status == 5:  # indicate that function(input function) is not a mathematical expression
            return "Input Function Must be a Function of x"

        else:
            return "Invalid Input"

    def edit_title(self, self_of_gui_object):
        if self.ax is None:   # check first the there's a plot before you change the title
            QMessageBox.warning(self_of_gui_object, "Warning", "Please plot the function first before changing the title", QMessageBox.Ok)
        else:
            text, ok = QInputDialog.getText(self_of_gui_object, "Input", "Enter a title:")
            if ok:
                # The user clicked OK, and the input is stored in the `text` variable
                self.ax.set_title(text)
                self_of_gui_object.canvas.draw()     # Redrawing the canvas is necessary when you want to update the plot with new data or changes to the plot properties
            else:
                # The user clicked Cancel
                pass

    def edit_x_axis_label(self, self_of_gui_object):
        if self.ax is None:   # check first the there's a plot before you change the x label
            QMessageBox.warning(self_of_gui_object, "Warning", "Please plot the function first before changing the x label", QMessageBox.Ok)
        else:
            text, ok = QInputDialog.getText(self_of_gui_object, "Input", "Enter x label:")
            if ok:
                # The user clicked OK, and the input is stored in the `text` variable
                self.ax.set_xlabel(text)
                self_of_gui_object.canvas.draw()      # Redrawing the canvas is necessary when you want to update the plot with new data or changes to the plot properties
            else:
                # The user clicked Cancel
                pass

    def edit_y_axis_label(self, self_of_gui_object):
        if self.ax is None:       # check first the there's a plot before you change the y label
            QMessageBox.warning(self_of_gui_object, "Warning",
                                "Please plot the function first before changing the y label", QMessageBox.Ok)
        else:
            text, ok = QInputDialog.getText(self_of_gui_object, "Input", "Enter y label:")
            if ok:
                # The user clicked OK, and the input is stored in the `text` variable
                self.ax.set_ylabel(text)
                self_of_gui_object.canvas.draw()       # Redrawing the canvas is necessary when you want to update the plot with new data or changes to the plot properties
            else:
                # The user clicked Cancel
                pass

    def reset(self, self_of_gui_object):        # check first the there's a plot before you reset
        if self.ax is None:
            QMessageBox.warning(self_of_gui_object, "Warning", "there is no plot to reset it", QMessageBox.Ok)
        else:
            self_of_gui_object.figure.clear()
            self_of_gui_object.canvas.draw()    # Redrawing the canvas is necessary when you want to update the plot with new data or changes to the plot properties
            self.ax = None          # make ax = None, because there's no longer any plot on the figure

    def plot_another_function(self,self_of_gui_object, function, min_value_of_x, max_value_of_x):

        if self.ax is None:     # check first the there's a plot before you plot another function
            QMessageBox.warning(self_of_gui_object, "Warning", "there is no plot", QMessageBox.Ok)
        else:
            function = function.replace('^', '**')   # Replace ^ with ** for exponentiation, because eval function treat ^ as bitwise operation not as power
            function = function.lower()              # because if the user entered a function X+2 instead of x+2
            error_status, min_value_of_x, max_value_of_x = self.validate_fields(function, min_value_of_x, max_value_of_x)

            if error_status == 0:  # means everything is okay
                x, y = self.evaluate_function(function, min_value_of_x, max_value_of_x)
                self.ax.plot(x, y)
                self_of_gui_object.canvas.draw()  # Redrawing the canvas is necessary when you want to update the plot with new data or changes to the plot properties

            else:
                error_message = self.return_error_message(error_status)
                QMessageBox.warning(self_of_gui_object, "Invalid Input", error_message, QMessageBox.Ok)

