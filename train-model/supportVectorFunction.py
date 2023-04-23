import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


def predict_hours_of_work_rfr(employee_name, working_day, month):
    # Read the dataset into a Pandas DataFrame
    df = pd.read_csv("final_preprocessed_employee_working_hours.csv")

    # Extract the features (working_day and month) and the target (hours_of_work)
    X = df[["working_day", "month"]]
    y = df["hours_of_work"]
# Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42)

    # Create a Random Forest regression model
    model = RandomForestRegressor(n_estimators=100, random_state=42)

    # Train the model on the training set
    model.fit(X_train, y_train)

    # Use the model to make a prediction for the user input
    prediction = model.predict([[working_day, month]])

    # Return the predicted number of hours worked
    return f"Employee {employee_name} is predicted to work {prediction[0]:.2f} hours using Random Forest Regression."
