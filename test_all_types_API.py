import requests
import json

def load_config(file_path):
    """
    Load the configuration from a JSON file.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

def test_api(config_path):
    """
    Perform API testing based on the configuration file.
    """
    config = load_config(config_path)
    
    base_url = config.get("base_url")
    endpoint = config.get("endpoint", "")
    url = base_url + endpoint
    method = config.get("method", "GET").upper()
    headers = config.get("headers", {})
    params = config.get("params", {})
    payload = config.get("payload", {})
    
    # Remove optional headers or payload keys if not provided
    notes = config.get("notes", {})
    optional_headers = notes.get("headers", {})
    optional_payload_keys = notes.get("payload", {})
    
    # Remove non-mandatory headers if not set
    headers = {k: v for k, v in headers.items() if v or k not in optional_headers}
    # Remove optional payload keys if not set
    payload = {k: v for k, v in payload.items() if v or k not in optional_payload_keys}

    # Execute the request
    try:
        response = None
        if method == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method == "POST":
            response = requests.post(url, headers=headers, params=params, json=payload)
        elif method == "PUT":
            response = requests.put(url, headers=headers, params=params, json=payload)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, params=params, json=payload)
        else:
            print(f"Unsupported HTTP method: {method}")
            return
        
        # Print response details
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Body: {response.json()}")
    
    except Exception as e:
        print(f"Error during API call: {e}")

if __name__ == "__main__":
    # Replace with the path to your configuration file
    config_file_path = "config.json"
    test_api(config_file_path)
