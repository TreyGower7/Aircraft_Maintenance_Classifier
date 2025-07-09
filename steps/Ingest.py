import logging
import pandas as pd
from zenml import step
from typing_extensions import Annotated
from src.load import IngestData


@step
def Ingest(path: str) -> pd.DataFrame:
    try:
        logging.info(f"Loading Data from path {path}")
        Ingestor = IngestData()
        df = Ingestor.load_data(path)
        logging.info("Data Loaded Succesfully")
        return df
    except Exception as e:
        logging.error(f"Data Not Loaded Due To: {e}")
