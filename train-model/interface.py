import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from knnFunction import predict_hours_of_work_knn
from linearRegressionFunction import predict_hours_of_work_lr

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
        self.algorithm_dropdown = ttk.Combobox(self, textvariable=self.algorithm_var, values=["Linear Regression", "KNN"])
        self.algorithm_dropdown.grid(row=1, column=1)

        # Create the labels and entries for the algorithm parameters
        self.param1_label = tk.Label(self, text="Parameter 1:")
        self.param1_label.grid(row=2, column=0)
        self.param1_entry = tk.Entry(self)
        self.param1_entry.grid(row=2, column=1)

