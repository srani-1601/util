import json


def extract_overall_summary():

    return "overall summary"


def extract_overall_info_required():
    # Dummy implementation, replace with actual extraction logic
    return ["info1", "info2", "info3"]


def create_json():
    case_id = 1#extract_case_id()

    email_level_1 = {
        "summary": 'summary',#extract_email_level_1_summary(),
        "entities": 'Intent',
        "to": "",  # Add extraction logic if needed
        "CC": "",  # Add extraction logic if needed
        "from": "",  # Add extraction logic if needed
        "body": "as is"
    }

    summary = {
        "overall_summary": extract_overall_summary(),
        "overall_info_required": ", ".join(extract_overall_info_required())
    }

    result = {
        "case id": 1,
        "email_level_1": email_level_1,
        "summary": summary
    }

    return json.dumps(result, indent=4)
