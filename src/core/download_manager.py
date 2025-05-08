from PyQt5.QtCore import QThread, pyqtSignal
import requests
from pytube import YouTube

class DownloadManager(QThread):
    progress_signal = pyqtSignal(int, str)
    completed_signal = pyqtSignal(str)
    error_signal = pyqtSignal(str, str)
    
    def __init__(self):
        super().__init__()
        self.download_queue = []
        self.max_concurrent_downloads = 5