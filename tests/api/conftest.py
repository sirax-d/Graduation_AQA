import os

from dotenv import load_dotenv

load_dotenv()
email = os.getenv("EMAIL")
base_url_api = os.getenv("BASE_URL_API")
