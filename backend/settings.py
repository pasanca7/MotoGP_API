from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='settings.env')

POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DATABASE_URL = os.getenv('DATABASE_URL')

DEBUG = os.getenv('DEBUG') == 'True'
DATASET_PATH = os.getenv('DATASET_PATH')