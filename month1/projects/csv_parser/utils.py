import csv

def read_csv(filename):
    """
    Reads a CSV file and returns list of dictionaries
    """
    data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def remove_duplicates(data):
    """
    Removes duplicate rows from data
    """
    unique_data = []
    seen_rows = set()
    
    for row in data:
        # We turn the dictionary items into a sorted tuple so the set can track it
        row_tuple = tuple(sorted(row.items()))
        
        if row_tuple not in seen_rows:
            unique_data.append(row)
            seen_rows.add(row_tuple)
            
    return unique_data

def clean_whitespace(data):
    """
    Strips extra whitespace from all fields
    """
    for row in data:
        for key, value in row.items():
            # We ensure we are only stripping if the value is actually text
            if isinstance(value, str):
                row[key] = value.strip()
    return data

def handle_missing_values(data, strategy='remove'):
    """
    Handles missing values - either remove row or fill with default
    """
    if strategy == 'remove':
        # We only keep rows where ALL values are truthy (not empty strings)
        return [row for row in data if all(row.values())]
    
    elif strategy == 'fill':
        for row in data:
            for key, value in row.items():
                if not value:  # Checks for empty strings or None
                    row[key] = "N/A"
        return data
    
def standardize_case(data, case='title'):
    """
    Standardizes capitalization
    case: 'lower', 'upper', or 'title'
    """
    for row in data:
        for key, value in row.items():
            if isinstance(value, str):
                if case == 'lower':
                    row[key] = value.lower()
                elif case == 'upper':
                    row[key] = value.upper()
                elif case == 'title':
                    row[key] = value.title()
    return data

def validate_data(data, required_columns):
    """
    Checks if all required columns are present
    Returns True/False and list of missing columns
    """
    if not data:
        return False, required_columns
    
    # Get the columns that actually exist in the first row
    existing_columns = data[0].keys()
    
    # Find which required ones are missing
    missing_columns = [col for col in required_columns if col not in existing_columns]
    
    # If missing_columns is empty, is_valid will be True
    is_valid = len(missing_columns) == 0
    return is_valid, missing_columns
import csv

def write_csv(filename, data):
    """
    Writes cleaned data to new CSV file
    """
    if not data:
        return
    
    # Get the column names from the first row's keys
    headers = data[0].keys()
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        
        # Write the header row first
        writer.writeheader()
        
        # Write all the rows of data
        writer.writerows(data)
