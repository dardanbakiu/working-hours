import csv

# Define a dictionary that maps employee IDs to their respective departments
employee_department_mapping = {
    1: 1,
    2: 1,
    3: 2,
    4: 2,
    5: 3,
    6: 3,
    7: 3,
    8: 3,
    9: 3,
    10: 3,
    11: 3,
    12: 4,
    13: 4,
    14: 4,
    15: 4,
    16: 4,
    17: 4,
    18: 4
}

# Open the CSV file for reading
with open('preprocessed_employee_working_hours.csv', 'r') as f:
    reader = csv.reader(f)

    # Skip the first row (column headers)
    next(reader)

    # Create a list to store the modified rows
    modified_rows = []

    # Loop through the remaining rows in the CSV file
    for row in reader:

        # Get the employee ID from the first column of the row
        employee_id = int(row[0])

        # Look up the employee's department based on the ID
        department = employee_department_mapping[employee_id]

        # Append the department to the end of the row
        row.append(str(department))

        # Add the modified row to the list
        modified_rows.append(row)

# Open the CSV file for writing
with open('preprocessed_employee_working_hours_with_department.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the modified rows to the new CSV file
    for row in modified_rows:
        writer.writerow(row)
