import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from knnFunction import predict_hours_of_work_knn
from linearRegressionFunction import predict_hours_of_work_lr
from supportVectorFunction import predict_hours_of_work_rfr


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create the label and entry for the employee name
        self.employee_label = tk.Label(self, text="Employee Name:")
        self.employee_label.grid(row=0, column=0)
        self.employee_entry = tk.Entry(self)
        self.employee_entry.grid(row=0, column=1)

        # Create the label and dropdown for the algorithm selection
        self.algorithm_label = tk.Label(self, text="Algorithm:")
        self.algorithm_label.grid(row=1, column=0)
        self.algorithm_var = tk.StringVar(value="Linear Regression")
        self.algorithm_dropdown = ttk.Combobox(self, textvariable=self.algorithm_var, values=[
                                               "Linear Regression", "KNN", "Random Forest Regression"])
        self.algorithm_dropdown.grid(row=1, column=1)

        # Create the labels and entries for the algorithm parameters
        self.param1_label = tk.Label(self, text="Week day:")
        self.param1_label.grid(row=2, column=0)
        self.param1_entry = tk.Entry(self)
        self.param1_entry.grid(row=2, column=1)

        self.param2_label = tk.Label(self, text="Month:")
        self.param2_label.grid(row=3, column=0)
        self.param2_entry = tk.Entry(self)
        self.param2_entry.grid(row=3, column=1)

        # Create the predict button
        self.predict_button = tk.Button(
            self, text="Predict", command=self.predict)
        self.predict_button.grid(row=4, column=1)

        # Create the result label
        self.result_label = tk.Label(self, text="")
        self.result_label.grid(row=5, column=0, columnspan=2)

    def predict(self):
        # Get the input values
        employee_name = int(self.employee_entry.get())
        algorithm = self.algorithm_var.get()
        param1 = float(self.param1_entry.get())
        param2 = float(self.param2_entry.get())

        # Call the appropriate function based on the selected algorithm
        if algorithm == "Linear Regression":
            result = predict_hours_of_work_lr(employee_name, param1, param2)
        elif algorithm == "KNN":
            result = predict_hours_of_work_knn(
                employee_name, param1, param2, n_neighbors=5, weights="uniform")
        else:
            result = predict_hours_of_work_rfr(employee_name, param1, param2)

        # Print the predicted number of hours worked
        self.result_label.config(text=result)


# Create the Tkinter GUI and start the main loop
root = tk.Tk()
app = Application(master=root)
app.mainloop()
