import logging
import os
import sys
from datetime import datetime
from src.exception import CustomException

# Project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create run-specific log folder
RUN_ID = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
logs_dir = os.path.join(PROJECT_ROOT, "logs", RUN_ID)
os.makedirs(logs_dir, exist_ok=True)

# Log file inside the run folder
LOG_FILE_PATH = os.path.join(logs_dir, f"{RUN_ID}.log")

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.exception("Divide by zero error")
        raise CustomException(e, sys)
