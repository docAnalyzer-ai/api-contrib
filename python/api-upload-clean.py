#!/usr/bin/env python3

import os
import requests
import json
import logging
from pprint import pformat

logging.basicConfig(level=logging.DEBUG)  # Adjust the level as necessary
API_KEY = "xxxxxxxxxxxxx"

def upload_document(file_path):
    url = "https://api.docanalyzer.ai/api/v1/doc/upload"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    # Debugging: Log the API Key and File Path
    logging.debug(f"Using API Key: {API_KEY}")
    logging.debug(f"Uploading File: {file_path}")

    # Get the file name from the full path
    file_name = os.path.basename(file_path)
    
    # Open the file in binary mode
    with open(file_path, 'rb') as f:
        # Create the files object with the file name and the open file
        files = {'mydoc': (file_name, f, 'application/pdf')}
        
        # Make the POST request with headers and files
        response = requests.post(url, headers=headers, files=files)
    
    logging.debug(f"Response Status: {response.status_code}")
    logging.debug(f"Response Headers: {response.headers}")
    logging.debug(f"Response Body: {response.text}")

    logging.debug("Overall structure of the JSON response:")
    logging.debug(pformat(json.loads(response.text)))
    
    if response.status_code == 200:
        try:
            response_json = json.loads(response.text)
            # Fetch docid from the nested 'data' property
            return response_json.get('data', {})
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON: {e}")
            return None
    else:
        logging.error(f"API call error: {response.status_code}")
        logging.error(f"API Response: {response.text}")
        return None

# Example usage:
#document_path = "../../data/Mutual-NDA.pdf"
document_path = "./pdf/1-s2.0-S0169433210016612-mainext.pdf"
doc_ids = upload_document(document_path)
print(f"Document IDs: {doc_ids}")
