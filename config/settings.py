from pathlib import Path
import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# App settings
APP_NAME = os.getenv("APP_NAME", "FinanceOS")

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Database
DATABASE_NAME = os.getenv("DATABASE_NAME", "finance.db")

DATA_FOLDER = os.getenv("DATA_FOLDER", "data")

DATA_DIR = BASE_DIR / DATA_FOLDER

DB_PATH = DATA_DIR / DATABASE_NAME