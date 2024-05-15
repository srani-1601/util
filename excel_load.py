import pandas as pd
import json

def get_request_details(request_type, file_path):
    # Read the main sheet to verify request type exists
    main_sheet = pd.read_excel(file_path, sheet_name='Request Types')

    # Verify request type exists in the main sheet
    if request_type not in main_sheet['Request Type'].values:
        return json.dumps({"error": "Request type not found"})

    # Read the sheet corresponding to the request type
    try:
        request_data = pd.read_excel(file_path, sheet_name=request_type)
    except Exception as e:
        return json.dumps({"error": str(e)})

    # Convert the dataframe to JSON
    request_data_json = request_data.to_json(orient='records')
    return request_data_json

# Example usage
file_path = 'path_to_your_excel_file.xlsx'
request_type = 'EUP'  # Example request type
details_json = get_request_details(request_type, file_path)
print(details_json)
