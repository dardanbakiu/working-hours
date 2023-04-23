import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def predict_hours_of_work_rfr(employee_name, working_day, month):
    # Read the dataset into a Pandas DataFrame
    df = pd.read_csv("final_preprocessed_employee_working_hours.csv")

    # Extract the features (working_day and month) and the target (hours_of_work)
    X = df[["working_day", "month"]]
    y = df["hours_of_work"]

