import tkinter as tk
from knnFunction import predict_hours_of_work_knn
from linearRegressionFunction import predict_hours_of_work_lr
from supportVectorFunction import predict_hours_of_work_rfr
import re
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import subprocess


def format_result(result):
    hours = re.search(r"work (\d+\.\d+)", result)
    accuracy = re.search(r"accuracy score is (\d+\.\d+)", result)
    if hours and accuracy:
        hours = hours.group(1)
        accuracy = accuracy.group(1)
        return f"Predicted work {hours} hours with accuracy {accuracy}"
    else:
        return "Invalid input"


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Employee Averages")
        self.state('zoomed')
        # Create labels, input fields, and output fields
        self.create_widgets()

        # Update button
        self.update_button = tk.Button(
            self, text="Update values", command=self.update_values, state='disabled')
        self.update_button.grid(row=15, column=1, pady=20)

        # Go back button
        self.go_back_button = tk.Button(
            self, text="Go Back", command=self.go_back)
        self.go_back_button.grid(row=16, column=1, pady=20)

        # Center items in the grid
        self.center_items()

        # Destroy on close the window
        self.protocol('WM_DELETE_WINDOW', self.on_exit)

    def create_widgets(self):
        headers = ["First employee ID:", "Second employee ID:"]
        labels = ["Enter ID data:", "Enter week day number:", "Enter month number:",
                  "Average according to K-Nearest Neighbour:", "Average according to Linear Regression:", "Average according to Support Vector Machine:"]

        for i, header in enumerate(headers):
            tk.Label(self, text=header).grid(row=0, column=i+1)

        for i, label in enumerate(labels):
            tk.Label(self, text=label).grid(row=i+1, column=0)

        self.input_vars = [[tk.StringVar() for _ in range(2)]
                           for _ in range(3)]
        self.input_fields = [[tk.Entry(
            self, textvariable=self.input_vars[i][j]) for j in range(2)] for i in range(3)]
        for i, row in enumerate(self.input_fields):
            for j, entry in enumerate(row):
                entry.grid(row=i+1, column=j+1)

        for i in range(3):
            for j in range(2):
                self.input_vars[i][j].trace("w", self.validate_inputs)

        self.output_fields = [
            [tk.Entry(self, state='readonly', width=40) for _ in range(2)] for _ in range(3)]
        for i, row in enumerate(self.output_fields):
            for j, entry in enumerate(row):
                entry.grid(row=i+4, column=j+1)

    def center_items(self):
        for i in range(3):
            self.columnconfigure(i, weight=1)

        for i in range(8):
            self.rowconfigure(i, weight=1)

    def validate_inputs(self, *args):
        for row in self.input_vars:
            for var in row:
                if not var.get():
                    self.update_button.config(state='disabled')
                    return
        self.update_button.config(state='normal')

    def update_values(self):

        employee1 = self.input_vars[0][0].get()
        employee2 = self.input_vars[0][1].get()
        self.plot_graph(employee1, employee2)

        # Update the output field for KNN
        # Left fields
        result = predict_hours_of_work_knn(
            self.input_vars[0][0].get(), self.input_vars[1][0].get(), self.input_vars[2][0].get(), n_neighbors=9, weights="uniform")
        formatted_result = format_result(result)
        self.output_fields[0][0].config(state='normal')
        self.output_fields[0][0].delete(0, 'end')
        self.output_fields[0][0].insert(0, formatted_result)
        self.output_fields[0][0].config(state='readonly')
        # Right fields
        result = predict_hours_of_work_knn(
            self.input_vars[0][1].get(), self.input_vars[1][1].get(), self.input_vars[2][1].get(), n_neighbors=9, weights="uniform")
        formatted_result = format_result(result)
        self.output_fields[0][1].config(state='normal')
        self.output_fields[0][1].delete(0, 'end')
        self.output_fields[0][1].insert(0, formatted_result)
        self.output_fields[0][1].config(state='readonly')

        # Update the output field for LR
        # Left fields
        result = predict_hours_of_work_lr(
            self.input_vars[0][0].get(), self.input_vars[1][0].get(), self.input_vars[2][0].get())
        formatted_result = format_result(result)
        self.output_fields[1][0].config(state='normal')
        self.output_fields[1][0].delete(0, 'end')
        self.output_fields[1][0].insert(0, formatted_result)
        self.output_fields[1][0].config(state='readonly')
        # Right fields
        result = predict_hours_of_work_lr(
            self.input_vars[0][1].get(), self.input_vars[1][1].get(), self.input_vars[2][1].get())
        formatted_result = format_result(result)
        self.output_fields[1][1].config(state='normal')
        self.output_fields[1][1].delete(0, 'end')
        self.output_fields[1][1].insert(0, formatted_result)
        self.output_fields[1][1].config(state='readonly')

        # Update the output field for SVG
        # Left fields
        result = predict_hours_of_work_rfr(
            self.input_vars[0][0].get(), self.input_vars[1][0].get(), self.input_vars[2][0].get())
        formatted_result = format_result(result)
        self.output_fields[2][0].config(state='normal')
        self.output_fields[2][0].delete(0, 'end')
        self.output_fields[2][0].insert(0, formatted_result)
        self.output_fields[2][0].config(state='readonly')
        # Right fields
        result = predict_hours_of_work_rfr(
            self.input_vars[0][1].get(), self.input_vars[1][1].get(), self.input_vars[2][1].get())
        formatted_result = format_result(result)
        self.output_fields[2][1].config(state='normal')
        self.output_fields[2][1].delete(0, 'end')
        self.output_fields[2][1].insert(0, formatted_result)
        self.output_fields[2][1].config(state='readonly')
        pass

    def go_back(self):
        self.withdraw()
        subprocess.run(['python', 'main_window.py'])  # Open the MainWindow
        self.on_exit()  # Close the current window

    def on_exit(self):
        """When you click to exit, this function is called"""
        self.destroy()  # Close the window
        exit()  # Stop the Python script

    def plot_graph(self, employee1, employee2):
        # Read the dataset
        df = pd.read_csv("final_preprocessed_employee_working_hours.csv")

        # Filter the data for the two employees
        employee1_data = df[df["employee_name"] == int(employee1)]
        employee2_data = df[df["employee_name"] == int(employee2)]

        # Group data by month and calculate the average working hours
        employee1_monthly_data = employee1_data.groupby(
            'month')['hours_of_work'].mean()
        employee2_monthly_data = employee2_data.groupby(
            'month')['hours_of_work'].mean()

        # Create a figure and axis for the plot
        fig, ax = plt.subplots()

        # Plot the average working hours per month for both employees
        ax.plot(employee1_monthly_data.index, employee1_monthly_data,
                color='red', label=f"Employee {employee1}")
        ax.plot(employee2_monthly_data.index, employee2_monthly_data,
                color='blue', label=f"Employee {employee2}")

        # Set labels and title
        ax.set_xlabel("Month")
        ax.set_ylabel("Average Hours of Work")
        ax.set_title("Average Working Hours per Month")
        ax.legend()

        # Create a canvas for the figure and add it to the app
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=8, columnspan=3, pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
