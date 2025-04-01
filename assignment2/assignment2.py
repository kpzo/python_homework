# Task 2: Read a CSV File ---------------------------------
import csv
import traceback
import sys

def read_employees():
    employee_data = {}
    rows = []

    try:
        with open('../csv/employees.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)

            for index, row in enumerate(reader):
                if index == 0:
                    employee_data["fields"] = row
                else:
                    rows.append(row)

            employee_data["rows"] = rows
            return employee_data

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)

# global variable
employees = read_employees()



# Task 3: Find the Column Index ---------------------------------

# Function to find index of a column
def column_index(column_name):
    return employees["fields"].index(column_name)

# Global variable
employee_id_column = column_index("employee_id")




# Task 4: Find the Employee First Name ---------------------------------
def first_name(row_num):
    index = column_index("first_name")
    return employees["rows"][row_num][index]



# Task 5: Find the Employee: a Function in a Function ---------------------------------
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches


# Task 6: Find the Employee with a Lambda ---------------------------------
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches



# Task 7: Sort the Rows by last_name Using a Lambda ---------------------------------
def sort_by_last_name():
    index = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[index])
    return employees["rows"]



# Task 8: Create a dict for an Employee ---------------------------------
def employee_dict(row):
    headers = employees["fields"]
    result = {}

    for i in range(len(headers)):
        if headers[i] != "employee_id":
            result[headers[i]] = row[i]

    return result



# Task 9: A dict of dicts, for All Employees ---------------------------------
def all_employees_dict():
    result = {}

    for row in employees["rows"]:
        emp_id = row[employee_id_column]  # employee_id is still a string
        result[emp_id] = employee_dict(row)

    return result



# Task 10: Use the os Module ---------------------------------
import os
def get_this_value():
    return os.getenv("THISVALUE")



# Task 11: Creating Your Own Module ---------------------------------
import custom_module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)



# Task 12: Read minutes1.csv and minutes2.csv ---------------------------------
def read_csv_as_dict(path):
    result = {"fields": [], "rows": []}
    try:
        with open(path, newline='') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    result["fields"] = row
                else:
                    result["rows"].append(tuple(row))  # convert each row to a tuple
    except Exception as e:
        print(f"Error reading {path}: {e}")
        raise
    return result

def read_minutes():
    minutes1 = read_csv_as_dict("../csv/minutes1.csv")
    minutes2 = read_csv_as_dict("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()



# Task 13: Create minutes_set ---------------------------------
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    combined = set1.union(set2)
    return combined

minutes_set = create_minutes_set()


# Task 14: Convert to datetime ---------------------------------
from datetime import datetime

def create_minutes_list():
    raw_list = list(minutes_set)
    converted = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), raw_list))
    return converted

minutes_list = create_minutes_list()

# Task 15: Write Out Sorted List ---------------------------------
def write_sorted_list():
    # Sort by datetime (2nd item in each tuple)
    sorted_minutes = sorted(minutes_list, key=lambda x: x[1])

    # Convert datetime back to formatted string
    formatted = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_minutes))

    # Write to CSV
    with open("./minutes.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(minutes1["fields"])  # Write header
        writer.writerows(formatted)          # Write rows

    return formatted

sorted_minutes_list = write_sorted_list()