import os
import requests
from dotenv import load_dotenv
import base64

load_dotenv()
api_key = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    
def detect_text(path):
    """Detects text in the file using REST API."""
    # Read the image file
    with open(path, 'rb') as image_file:
        content = base64.b64encode(image_file.read()).decode('utf-8')
    
    # Prepare the request
    url = f'https://vision.googleapis.com/v1/images:annotate?key={api_key}'
    
    request_data = {
        'requests': [{
            'image': {
                'content': content
            },
            'features': [{
                'type': 'TEXT_DETECTION',
                'maxResults': 1
            }]
        }]
    }
    
    # Make the API request
    response = requests.post(url, json=request_data)
    response.raise_for_status()  # Raise an exception for bad status codes
    
    # Process the response
    result = response.json()
    
    if 'responses' in result and result['responses']:
        texts = result['responses'][0].get('textAnnotations', [])
        
        if texts:
            # Get only the first text annotation which contains the complete text
            complete_text = texts[0].get('description', '')
            print("Detected Text:")
            print(complete_text)
            return complete_text
        else:
            print("No text found in the response")
            return None
    else:
        print("No text found in the response")
        return None
    
if __name__ == "__main__":
    detect_text("ibon.png")

