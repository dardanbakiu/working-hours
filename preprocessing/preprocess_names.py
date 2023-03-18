import pandas as pd

def preprocess_employee_names(filename):
    # Read in the CSV file as a Pandas dataframe
    df = pd.read_csv(filename)

    # Get a list of unique employee names
    employee_names = df["employee_name"].unique()

    # Create a dictionary to map employee names to numbers
    employee_dict = {name: i+1 for i, name in enumerate(employee_names)}

    # Replace employee names with their corresponding numbers
    df["employee_name"] = df["employee_name"].map(employee_dict)

    # Save the preprocessed dataframe to a new CSV file
    output_filename = "preprocessed_" + filename
    df.to_csv(output_filename, index=False)
    
    print(f"Preprocessed data saved to {output_filename}")