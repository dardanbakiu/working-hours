import pandas as pd
from sklearn.neighbors import KNeighborsRegressor

# Read the dataset into a Pandas DataFrame
df = pd.read_csv("your_dataset.csv")

# Extract the features (working_day and month) and the target (hours_of_work)
X = df[["working_day", "month"]]
y = df["hours_of_work"]

# Create a KNN regression model
model = KNeighborsRegressor()

# Train the model on the entire dataset
model.fit(X, y)

