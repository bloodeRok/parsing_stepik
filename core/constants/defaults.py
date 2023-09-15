import os
from .secret_dicts import GOOGLE_SHEET_CREDENTIALS

from dotenv import load_dotenv

load_dotenv()

STEPIK_CLIENT_ID = os.environ.get("STEPIK_CLIENT_ID", "")
STEPIK_CLIENT_SECRET = os.environ.get("STEPIK_CLIENT_SECRET", "")
AUTH_DATA = {"grant_type": "client_credentials"}
GOOGLE_SHEET_CREDENTIALS = GOOGLE_SHEET_CREDENTIALS
GOOGLE_SHEET_ID = os.environ.get("GOOGLE_SHEET_ID", "")