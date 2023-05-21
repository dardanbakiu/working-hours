import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data = pd.read_csv('final_preprocessed_employee_working_hours.csv')


def on_model_selection(event):
    selected_model = model_var.get()

    if selected_model == "Select the algorithm":
        return

    # Preprocess the data and split it into training and testing sets
    X = data[['employee_name', 'working_day',
              'work_from_home', 'month', 'department']]
    y = data['hours_of_work']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Fit and predict the selected model
    if selected_model == "KNN":
        model = KNeighborsRegressor()
    elif selected_model == "Linear Regression":
        model = LinearRegression()
    else:
        model = SVR()

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Calculate accuracy
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Fill the table
    table.delete(*table.get_children())  # Clear the table before filling
    rows = []
    for i, (test_index, row) in enumerate(X_test.iterrows()):
        day_month = f"{row['working_day']}/{row['month']}"
        avg_hour = y_pred[i]
        rows.append((row['employee_name'], day_month, avg_hour, r2))

    # Order the rows by the "Co-worker ID" column
    rows.sort(key=lambda x: x[0])

    # Insert the sorted rows into the table
    for row in rows:
        table.insert('', 'end', values=row)

    # Plot the graph
    ax.clear()
    ax.scatter(y_test, y_pred)
    ax.set_title(f'{selected_model} Predictions')
    ax.set_xlabel('Actual Hours')
    ax.set_ylabel('Predicted Hours')
    canvas.draw()


def open_main_window():
    root_pg1.destroy()  # Close the current window
    os.system('python main_window.py')  # Open the main_window.py script


root_pg1 = tk.Tk()
root_pg1.title("Overall work hours average tab")

# Create the dropdown menu
model_var = tk.StringVar()
model_var.set("Select an algorithm here!")
model_dropdown = ttk.Combobox(root_pg1, textvariable=model_var, values=[
                              "KNN", "Linear Regression", "Support Vector Machine"], width=25)
model_dropdown.bind("<<ComboboxSelected>>", on_model_selection)
model_dropdown.grid(row=0, column=0, padx=10, pady=10)

open_main_button = tk.Button(
    root_pg1, text="Go Back", command=open_main_window)
open_main_button.grid(row=1, column=0, padx=10, pady=10)

# Create the table
table = ttk.Treeview(root_pg1, columns=(
    "ID", "Day/Month", "Average Hour", "Accuracy"), show="headings")
table.heading("ID", text="Co-worker ID")
table.heading("Day/Month", text="Day/Month")
table.heading("Average Hour", text="Average Hour Calculated")
table.heading("Accuracy", text="Accuracy")
table.grid(row=2, column=0, padx=10, pady=10)

# Create the matplotlib graph
fig = plt.Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root_pg1)
canvas.draw()
canvas.get_tk_widget().grid(row=3, column=0, padx=10, pady=10)

root_pg1.mainloop()
