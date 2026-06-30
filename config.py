# config.py
import os
from dotenv import load_dotenv

load_dotenv()

USER = os.environ["QA_USER"]
PASSWORD = os.environ["QA_PASSWORD"]

if not USER or not PASSWORD:
    raise EnvironmentError("Eviorenment variables not configured!")