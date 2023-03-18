import pandas as pd

def preprocess_working_days(filename):
    # Read in the CSV file as a Pandas dataframe
    df = pd.read_csv(filename)

    # Define a dictionary to map working days to numbers
    day_dict = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7
    }

    # Replace working days with their corresponding numbers
    df["working_day"] = df["working_day"].map(day_dict)

    # Extract the month from the date
    df["month"] = pd.to_datetime(df["date"]).dt.month
    # Drop the original date column
    df.drop("date", axis=1, inplace=True)

    # Save the preprocessed dataframe to a new CSV file
    output_filename = "preprocessed_" + filename
    df.to_csv(output_filename, index=False)
    
    print(f"Preprocessed data saved to {output_filename}")
