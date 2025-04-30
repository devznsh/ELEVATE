import os
from pathlib import Path

DATA_DIR = Path(__file__).parent  # Points to `app/data/`

def get_data_path(filename):
    """Helper to get absolute paths to data files."""
    return str(DATA_DIR / filename)