from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

APP_NAME = os.getenv("APP_NAME")

DATABASE_NAME = os.getenv("DATABASE_NAME")

DATA_FOLDER = os.getenv("DATA_FOLDER")

DEBUG = os.getenv("DEBUG") == "True"