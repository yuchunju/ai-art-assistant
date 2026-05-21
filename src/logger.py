from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_PATH = os.path.join(BASE_DIR, "data/error.log")


def _write(level, message):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().isoformat()}] [{level}] {message}\n")


def log_error(message):
    _write("ERROR", message)


def log_info(message):
    _write("INFO", message)


def log_debug(message):
    _write("DEBUG", message)


def log_api(message):
    _write("API", message)