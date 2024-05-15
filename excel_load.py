import pandas as pd
import json

def get_request_details(request_type, file_path):
    # Read the Excel file to check sheet names
    xls = pd.ExcelFile(file_path)
    sheet_names = xls.sheet_names
    print("Available sheets:", sheet_names)  # Debugging: Print available sheet names

    # Read the main sheet to verify request type exists
    main_sheet = pd.read_excel(file_path, sheet_name='Request Types')
    print("Columns in 'Request Types' sheet:", main_sheet.columns)  # Debugging: Print columns

    # Search for the sheet containing the request type in its name (partial match)
    matching_sheets = [sheet for sheet in sheet_names if sheet.startswith(request_type)]
    if not matching_sheets:
        return json.dumps({"error": f"No sheet found for request type {request_type}"})


    # Read the first matching sheet
    try:
        request_data = pd.read_excel(file_path, sheet_name=matching_sheets[0])
        print(request_data)
    except Exception as e:
        return json.dumps({"error": str(e)})
    # Filter rows where 'Required' column has 'Y' and extract relevant data
    if 'Required' in request_data.columns:
        required_data = request_data[request_data['Required'] == 'y']
        relevant_data = required_data.iloc[:, 0].tolist()
        print(relevant_data)

    else:
        return json.dumps({"error": "Column 'Required' not found in the sheet"})


# Example usage
file_path = 'data.xlsx'
request_type = 'EUP'  # Example request type
details_json = get_request_details(request_type, file_path)
print(details_json)
