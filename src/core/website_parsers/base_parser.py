from abc import ABC, abstractmethod
from typing import Dict, List
import requests
from bs4 import BeautifulSoup

class WebsiteParser(ABC):
    def __init__(self, url: str):
        self.url = url
        self.soup = None
        
    @abstractmethod
    def parse(self) -> Dict:
        pass
        
    def fetch_content(self) -> None:
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.soup = BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch content: {str(e)}")