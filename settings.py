from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
API_AUDIENCE = os.getenv("API_AUDIENCE")

DATABASE_PATH = os.getenv("DATABASE_PATH")
