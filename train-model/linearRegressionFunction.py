import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def predict_hours_of_work_lr(employee_name, working_day, month):
    # Read the dataset into a Pandas DataFrame
    df = pd.read_csv("final_preprocessed_employee_working_hours.csv")

    # Extract the features (employee_name, working_day and month) and the target (hours_of_work)
    X = df[["employee_name", "working_day", "month"]]
    y = df["hours_of_work"]

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Create a linear regression model
    model = LinearRegression()

    # Train the model on the training set
    model.fit(X_train, y_train)

    # Predict the target values for the test set
    y_pred = model.predict(X_test)

    # Calculate the mean squared error
    mse = mean_squared_error(y_test, y_pred)

    # Create a DataFrame with the user input
    user_input = pd.DataFrame({"employee_name": [employee_name], "working_day": [
                              working_day], "month": [month]})

    # Use the model to make a prediction for the user input
    prediction = model.predict(user_input)

    # Return the predicted number of hours worked and the mean squared error
    r2 = r2_score(y_test, y_pred)
    return f"Employee {employee_name} is predicted to work {prediction[0]:.2f} hours using Linear Regression.\n\nThe mean squared error of this model is {mse:.2f}.\n\nThe accuracy score is {r2:.2f}."
