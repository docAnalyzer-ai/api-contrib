For those who would like to use Python:
def chat_document(doc_id, chat_string):
    url = "https://api.docanalyzer.ai/api/v1/doc/"+doc_id+"/chat"

    payload = { "prompt" : chat_string }
    headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.request("POST", url, headers=headers, json=payload)
    
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

