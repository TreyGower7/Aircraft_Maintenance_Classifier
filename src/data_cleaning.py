import logging 
from abc import ABC, abstractmethod
import pandas as pd
from sklearn.model_selection import train_test_split
from typing import Tuple, Any

class DataStrategy(ABC):
    """
    Abstract class for defining strategy for handling data
    """
    @abstractmethod
    def handle_data(self, data: pd.DataFrame) -> Any:
        pass

class DataPreProcess(DataStrategy):
    def handle_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Eliminates null values, organizes data, and normalizes data
        """
        
    
class DataDivide(DataStrategy):
    def handle_data(self, data: pd.DataFrame) -> Tuple[
        pd.DataFrame, pd.DataFrame, 
        pd.DataFrame, pd.DataFrame
        ]:
        """
        Divides data using train, test, split
        """
        try:
            Y = data[""]
            X = data.drop("", axis=1)
    
            X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
            return  X_train, X_test, y_train, y_test
        except Exception as e:
            logging.error(f"Cannot split data: {e}")

class DataCleaning:
    def __init__(self, data: pd.DataFrame, strategy: DataStrategy):
        self.strategy = strategy
        self.data = data
    
    def handle_data(self) -> Any:
        try:
            self.strategy.handle_data(self.data)
            return self.data
        except Exception as e:
            logging.error(f"Error in cleaning data: {e}")
            raise e