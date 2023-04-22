import pandas as pd
from sklearn.neighbors import KNeighborsRegressor


def predict_hours_of_work_knn(employee_name, working_day, month, n_neighbors, weights):
    # Read the dataset into a Pandas DataFrame
    df = pd.read_csv("your_dataset.csv")

    # Extract the features (working_day and month) and the target (hours_of_work)
    X = df[["working_day", "month"]]
    y = df["hours_of_work"]

    # Create a KNN regression model
    model = KNeighborsRegressor(n_neighbors=n_neighbors, weights=weights)

    # Train the model on the entire dataset
    model.fit(X, y)

    # Create a DataFrame with the user input
    user_input = pd.DataFrame({"working_day": [working_day], "month": [month]})

    # Use the model to make a prediction for the user input
    prediction = model.predict(user_input)

    # Return the predicted number of hours worked
    return f"Employee {employee_name} is predicted to work {prediction[0]:.2f} hours using KNN."
