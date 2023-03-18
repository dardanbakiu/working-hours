import csv
from datetime import datetime, timedelta
import random

# Define list of employee names
# employee_names = ["John Smith", "Jane Doe", "Bob Johnson", "Samantha Lee"]
employee_names = ["Diellëza Galica", "Synim Selimi", "Agon Ramizi", "Egzona Lipovica", "Ariana Grajçevci", "Era Ibrahimi", "Dardan Bakiu", "Diellza Bajrami", "Elira Hasangjekaj", "Artira Ferati", "Arbenita Maloku", "Arbena Musa", "Bled Kastrati", "Tarik Sadiku", "Fatbardh Kadriu", "Rron Lamoja", "Laurat Hajrullaaga", "Fatbardh Emini"]

# Define start date
start_date = datetime.strptime("2023-03-17", "%Y-%m-%d")

# Define number of days to generate data for
num_days = 30 * 19

# Open CSV file for writing
with open("employee_working_hours.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["employee_name", "working_day", "date", "hours_of_work", "work_from_home"])

    # Generate data for each day
    for i in range(num_days):
        # Calculate date for current day
        current_date = start_date - timedelta(days=i)

        # Get weekday name for current day
        weekday_name = current_date.strftime("%A")

        # Generate data for each employee
        for employee in employee_names:
            # Set working hours based on weekday
            if weekday_name in ["Saturday", "Sunday"]:
                hours_of_work = 0
            else:
                if random.random() <= 0.7:
                    hours_of_work = round(random.uniform(5.3, 7), 2)
                else:
                    hours_of_work = round(random.uniform(4.5, 5.3), 2)

            # Set work from home based on probability
            if(weekday_name != "Saturday" and weekday_name != "Sunday"):
                if (weekday_name == "Friday" and random.random() < 0.6) or (weekday_name != "Friday" and random.random() < 0.2):
                    work_from_home = 1
                else:
                    work_from_home = 0
            else:
                work_from_home = 0

            # Write data to CSV file
            writer.writerow([employee, weekday_name, current_date.strftime("%Y-%m-%d"), hours_of_work, work_from_home])