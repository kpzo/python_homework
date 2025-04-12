import pandas as pd
from io import StringIO
import numpy as np
import os

# -----------------------
# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
# -----------------------

# 1.1. Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(data)
print("task1_data_frame:")
print(task1_data_frame)

# 1.2. Add a new column by making a copy of the DataFrame
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print("\ntask1_with_salary:")
print(task1_with_salary)

# 1.3. Modify an existing column by incrementing the Age column
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print("\ntask1_older:")
print(task1_older)

# 1.4. Save the final DataFrame to a CSV file without the index
task1_older.to_csv('employees.csv', index=False)

# Check that the file exists and has the expected shape
print("\nCSV file exists:", os.access("./employees.csv", os.F_OK))
df_csv = pd.read_csv('employees.csv')
print("CSV file shape:", df_csv.shape)



# -----------------------
# Task 2: Loading Data from CSV and JSON
# -----------------------

# 2.1. Read data from CSV file:
task2_employees = pd.read_csv('employees.csv')
print("task2_employees:")
print(task2_employees)

# 2.2. Create a JSON file with additional employees data
additional_employees_data = {
    'Name': ['Eve', 'Frank'],
    'Age': [28, 40],
    'City': ['Miami', 'Seattle'],
    'Salary': [60000, 95000]
}
# Create a DataFrame from the additional employees data
df_additional = pd.DataFrame(additional_employees_data)

# Save the DataFrame to a JSON file using 'records' orientation
# so that it can be read back as a DataFrame with the same structure.
df_additional.to_json('additional_employees.json', orient='records')
print("\nCreated additional_employees.json with the following data:")
print(df_additional)

# Read the JSON file into a DataFrame
json_employees = pd.read_json('additional_employees.json', orient='records')
print("\njson_employees:")
print(json_employees)

# 2.3. Combine the DataFrames from CSV and JSON
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("\nmore_employees:")
print(more_employees)

# Optionally, verify the shape
print("\nCombined DataFrame shape:", more_employees.shape)



# -----------------------
# Task 3: Data Inspection - Using Head, Tail, and Info Methods
# -----------------------

# 3.1 Use the head() method
# Assign the first three rows of the more_employees DataFrame to first_three
first_three = more_employees.head(3)
print("first_three:")
print(first_three)

# 3.2 Use the tail() method
# Assign the last two rows of the more_employees DataFrame to last_two
last_two = more_employees.tail(2)
print("\nlast_two:")
print(last_two)

# 3.3 Get the shae of a DataFrame
# Assign the shape of the more_employees DataFrame to employee_shape
employee_shape = more_employees.shape
print("\nemployee_shape:")
print(employee_shape)

# 3.4 Use the info() method
# to print a concise summary of the DataFrame
print("\nDataFrame info:")
more_employees.info()

# -----------------------
# Task 4: Data Cleaning
# -----------------------


# 4.1. Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data.
dirty_data = pd.read_csv('dirty_data.csv')
print("dirty_data:")
print(dirty_data)

# Create a copy of dirty_data for cleaning
clean_data = dirty_data.copy()

# 4.2. Remove duplicate rows
clean_data.drop_duplicates(inplace=True)

# 4.3. Convert Age to numeric and handle missing values
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')

# 4.4. Convert Salary to numeric:
#   First, replace known placeholders 'unknown' and 'n/a' with pd.NA,
#   then convert to numeric
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')

# 4.5. Fill missing values:
#   Fill missing Age with the mean and Salary with the median
clean_data['Age'].fillna(clean_data['Age'].mean(), inplace=True)
clean_data['Salary'].fillna(clean_data['Salary'].median(), inplace=True)

# 4.6. Convert Hire Date to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')

# 4.7. Strip extra whitespace and standardize Name and Department as uppercase
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()

print("\nclean_data:")
print(clean_data)
