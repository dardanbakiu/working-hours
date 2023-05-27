import pandas as pd
from sklearn.linear_model import LinearRegression

# Read the dataset into a Pandas DataFrame
df = pd.read_csv("final_preprocessed_employee_working_hours.csv")

# Extract the features (working_day and month) and the target (hours_of_work)
X = df[["working_day", "month"]]
y = df["hours_of_work"]

# Create a linear regression model
model = LinearRegression()

# Train the model on the entire dataset
model.fit(X, y)

# Get user input for the employee name, working day, and month
employee_name = int(input("Enter employee name: "))
working_day = int(input("Enter working day: "))
month = int(input("Enter month: "))

# Create a DataFrame with the user input
user_input = pd.DataFrame({"working_day": [working_day], "month": [month]})

# Use the model to make a prediction for the user input
prediction = model.predict(user_input)

# Print the predicted number of hours worked
print(
    f"Employee {employee_name} is predicted to work {prediction[0]:.2f} hours.")
