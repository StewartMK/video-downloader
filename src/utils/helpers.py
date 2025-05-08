import os
from pathlib import Path

def create_directory(path: str) -> None:
    """Create directory if it doesn't exist"""
    Path(path).mkdir(parents=True, exist_ok=True)

def get_downloads_path() -> str:
    """Get downloads directory path"""
    return os.path.join(os.path.expanduser("~"), "Downloads", "video_downloader")