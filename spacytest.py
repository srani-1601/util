import spacy
import json

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# The given email text
email_text = """
After a few hours of troubleshooting with cust care, no one was able to activate this brand new iPhone 14 we received.

Here is the phone info:

number: 619.993.0929

IMEI: 355241387893747

IMEI2: 355241386551148

eSIM only iPhone 14

Serial: YDC7MKPVGZ

FYI: Due to all our phones being on an MDM, the Settings > Cellular section is completely blank. We can't go in that section to select anything.

619-993-0929
Line Details:
LINE ID: 436904444
"""

# Function to extract the required fields
def extract_fields(email):
    fields = {
        "Mobile Number": "Not Available",
        "Attention Name": "Not Available",
        "Shipping Address Line 1": "Not Available",
        "Shipping Address Line 2": "Not Available",
        "City": "Not Available",
        "State": "Not Available",
        "Shipping Zip Code": "Not Available"
    }

    # Parse the email text with spaCy
    doc = nlp(email)

    # Extract mobile numbers using pattern matching
    phone_numbers = []
    for token in doc:
        if re.match(r'\d{3}[-.]\d{3}[-.]\d{4}', token.text):
            phone_numbers.append(token.text)
    if phone_numbers:
        fields["Mobile Number"] = ', '.join(phone_numbers)

    # Extract other details using named entity recognition
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            fields["Attention Name"] = ent.text
        elif ent.label_ == "GPE":
            fields["City"] = ent.text
        elif ent.label_ == "ZIP":
            fields["Shipping Zip Code"] = ent.text

    return fields

# Extract fields from the email text
extracted_fields = extract_fields(email_text)

# Convert the extracted fields to JSON
json_output = json.dumps(extracted_fields, indent=4)
print(json_output)
