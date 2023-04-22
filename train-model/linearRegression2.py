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

