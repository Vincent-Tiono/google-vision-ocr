# Google Vision OCR

This project demonstrates the use of Google Cloud Vision API for image analysis and processing.

## Prerequisites

- Python 3.x
- Google Cloud Platform account with Vision API enabled

## Setup

1. Clone this repository:
```bash
git clone (https://github.com/Vincent-Tiono/google-vision-ocr.git)
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your Google Cloud credentials:
   - Create a service account key from Google Cloud Console
   - Download the JSON key file
   - Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to point to your key file:
     ```bash
     # On Windows
     set GOOGLE_APPLICATION_CREDENTIALS=path/to/your/credentials.json
     # On Unix or MacOS
     export GOOGLE_APPLICATION_CREDENTIALS=path/to/your/credentials.json
     ```

## Usage

The project includes sample code for image analysis using Google Cloud Vision API. You can run the sample script:

```bash
python sample.py
```

## Project Structure

- `sample.py`: Main script demonstrating Google Vision API usage
- `requirements.txt`: Project dependencies
- `test.png` and `ibon.png`: Sample images for testing

## Dependencies

- google-cloud-vision: Google Cloud Vision API client library
- python-dotenv: Environment variable management
- requests: HTTP library for Python

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
