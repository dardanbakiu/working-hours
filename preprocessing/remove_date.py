import pandas as pd

def remove_date_attribute(filename):
    # Read in the CSV file as a Pandas dataframe
    df = pd.read_csv(filename)

    # Drop the "date" attribute from the dataframe
    df = df.drop("date", axis=1)

    # Save the preprocessed dataframe to a new CSV file
    output_filename = "date_removed_" + filename
    df.to_csv(output_filename, index=False)
    
    print(f"Preprocessed data saved to {output_filename}")
