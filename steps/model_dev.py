import pandas as pd
from zenml import step
from typing_extensions import Annotated
from typing import Tuple

@step
def train_model(df: pd.DataFrame) -> None:
    pass