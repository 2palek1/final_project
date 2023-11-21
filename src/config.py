from dotenv import load_dotenv
import os


# Load environment variables from the .env file
load_dotenv()

# Retrieve database configuration from environment variables
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

# Retrieve the secret for authentication from environment variables
SECRET_AUTH = os.environ.get("SECRET_AUTH")
