
import pandas as pd
import json

def get_request_details(request_type, file_path):

    """
    Retrieve details for a given request type from an Excel file.

    This function reads an Excel file containing various request types and their corresponding details
    in separate sheets. It validates if the given request type exists in the main sheet ('Request Types')
    and then fetches details from the sheet whose name starts with the request type. The function 
    specifically filters rows where the 'Required' column has 'Y' and the 'where info can be found' 
    column is 'customer provided'.

    Parameters:
    request_type (str): The request type to search for (e.g., 'EUP').
    file_path (str): The path to the Excel file containing the request types and details.

    Returns:
    str: A JSON string containing the relevant details if found, or an error message.


    """
    
    # Read the Excel file to check sheet names
    xls = pd.ExcelFile(file_path)
    sheet_names = xls.sheet_names

    # Read the main sheet to verify request type exists
    main_sheet = pd.read_excel(file_path, sheet_name='Request Types')

    # Check if request type exists in the main sheet
    if 'Request Type' not in main_sheet.columns:
        return json.dumps({"error": "Column 'Request Type' not found in the main sheet"})

    if request_type not in main_sheet['Request Type'].values:
        return json.dumps({"error": f"{request_type} not found in the main sheet"})

    # Search for the sheet containing the request type in its name (partial match)
    matching_sheets = [sheet for sheet in sheet_names if sheet.startswith(request_type)]
    if not matching_sheets:
        return json.dumps({"error": f"No sheet found for request type {request_type}"})

    # Read the first matching sheet
    try:
        request_data = pd.read_excel(file_path, sheet_name=matching_sheets[0])
    except Exception as e:
        return json.dumps({"error": str(e)})

    # Ensure columns are correctly named
    request_data.columns = [col.strip() for col in request_data.columns]

    # Print the columns for debugging
    print("Columns in matching sheet:", request_data.columns)

    # Filter rows where 'Required' column has 'Y' and 'where info can be found' column is 'customer provided'
    if 'Required' in request_data.columns and 'where info can be found' in request_data.columns:
        print(request_data)
        required_data = request_data[
            (request_data['Required'].str.strip().str.upper() == 'Y') &
            (request_data['where info can be found'].str.strip().str.lower() == 'customer provided')
        ]

        relevant_data = required_data.iloc[:, 0].tolist()
        print('ppp', relevant_data)
    else:
        return json.dumps({"error": "Required columns not found in the sheet"})

    return json.dumps(relevant_data, indent=4)

# Example usage
file_path = '/mnt/data/data.xlsx'
request_type = 'EUP'  # Example request type
details_json = get_request_details(request_type, file_path)
print(details_json)
