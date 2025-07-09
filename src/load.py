import pandas as pd
import requests
import logging

class IngestData():
    def __init__(self, path: str):
        self.path = path

    def load_data(self):
        """
        Load Data
        """
        logging.info(f"Reading data from {self.path}")
        df = pd.read_csv(self.path)
        return df

